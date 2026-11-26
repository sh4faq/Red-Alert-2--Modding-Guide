#!/usr/bin/env python3
"""mo_tool.py - helper for adding units to Mental Omega 3.3.6 (see ../10-Adding-Units.md).

Never changes the game's archives. It only writes:
  - files you ask it to extract, into the folder you name;
  - with 'init-art', a NEW loose artmo.ini in the game folder (it refuses to overwrite one);
  - with 'set-normals' / 'rotate-hva', the model files you name (after saving a .bak copy).

Run it from the project folder (the folder that contains "Mental Omega"):

  python "MentalOmega-Modding-Guide\\scripts\\mo_tool.py" section ETNK
        print the stock RULES section [ETNK]            (add --art or --sound for the other files)
  python "MentalOmega-Modding-Guide\\scripts\\mo_tool.py" stock "stock-reference"
        extract rulesmo.ini, artmo.ini and soundmo.ini so you can read and search them
  python "MentalOmega-Modding-Guide\\scripts\\mo_tool.py" extract "stock-reference" etnkicon.pcx etnk.vxl
        copy any stock file out of the archives by name
  python "MentalOmega-Modding-Guide\\scripts\\mo_tool.py" init-art
        create the loose "Mental Omega\\artmo.ini" from the stock art file (first time only)
  python "MentalOmega-Modding-Guide\\scripts\\mo_tool.py" check ARBL
        preflight a NEW unit (ID ARBL) before you start the game; a weapon of your own that the unit
        uses (a block in Standard.ini) is checked too, with the projectile and warhead it names
  python "MentalOmega-Modding-Guide\\scripts\\mo_tool.py" lint-weapon TankieGun
        the same weapon checks for ONE weapon block of yours in Standard.ini, without a unit
        (for the weapon of a take-over block such as [ETNK], where 'check' stops)
  python "MentalOmega-Modding-Guide\\scripts\\mo_tool.py" set-normals "Mental Omega\\NEW.vxl" "Mental Omega\\NEWTUR.vxl"
        set the normals-mode byte to 4 (what every stock tank has); keeps a .bak copy
  python "MentalOmega-Modding-Guide\\scripts\\mo_tool.py" rotate-hva "Mental Omega\\NEW.hva" "Mental Omega\\NEWTUR.hva"
        turn a model 90 degrees through its HVA file (add --cw for the other direction); keeps a .bak copy

Option for all commands:  --game "path\\to\\Mental Omega"   (default: the folder next to this guide)
Needs only Python 3; no extra packages.
"""
import argparse
import os
import re
import struct
import sys
import zlib

RULES, ART, SOUND = "rulesmo.ini", "artmo.ini", "soundmo.ini"
MODE_FILE = os.path.join("INI", "Map Code", "Standard.ini")
BUILTIN_PREREQ = {"POWER", "FACTORY", "BARRACKS", "RADAR", "TECH", "PROC"}
ART_KEYS = {"voxel", "remapable", "cameo", "altcameo", "cameopcx", "altcameopcx", "primaryfireflh",
            "secondaryfireflh", "turretoffset", "usebuffer"}
MARKER = [
    "",
    ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;",
    "; USER ADDITIONS - everything above this line is the stock Mental Omega art file.",
    "; Add your own art sections BELOW this line. Never edit or delete anything above it.",
    "",
]
# --- weapons of your own (blocks in the mode file) ---
# Unit keys that name a weapon. These are all such keys in the stock unit sections (the four old ones,
# DeathWeapon, Weapon1..56 and EliteWeapon1..56, OccupyWeapon, PrismForwarding.SupportWeapon).
WEAPON_KEY = re.compile(r"(elite)?(primary|secondary|occupyweapon|weapon\d+)|deathweapon"
                        r"|prismforwarding\.(elite)?supportweapon", re.I)
OLD_WEAPON_KEYS = ("Primary", "Secondary", "ElitePrimary", "EliteSecondary")
# Keys of a weapon / projectile / warhead block whose value is the NAME of something else, and the kind
# of thing it names. Found by reading every stock weapon, projectile and warhead section of Mental
# Omega 3.3.6: these are all the keys there that hold names, except Projectile=, Warhead=,
# IvanBomb.Warhead=, Image=, AirburstWeapon= and ShrapnelWeapon= (handled in the code below) and
# IvanBomb.Image= (a picture file of the base game, which this tool cannot look for).
WEAPON_REFS = (("Report", "sound"), ("IvanBomb.AttachSound", "sound"), ("IvanBomb.TickingSound", "sound"),
               ("Anim", "anim"), ("OpenToppedAnim", "anim"), ("OccupantAnim", "anim"), ("AssaultAnim", "anim"),
               ("Abductor.Anim", "anim"), ("AttachedParticleSystem", "psys"),
               ("Cursor.Attack", "cursor"), ("Cursor.AttackOutOfRange", "cursor"))
PROJECTILE_REFS = (("AttachedSystem", "psys"),)
WARHEAD_REFS = (("AnimList", "anim"), ("Anim", "anim"), ("PreImpactAnim", "anim"), ("InfDeathAnim", "anim"),
                ("AttachEffect.Animation", "anim"), ("EMP.Sparkles", "anim"), ("Particle", "psys"),
                ("DieSound.Override", "sound"))
NOTHING = ("none", "<none>")  # the stock rules write these where a line names nothing on purpose


# ----------------------------------------------------------------------------- archives
def ra2_id(name):
    """File id used by Red Alert 2 / Yuri's Revenge archives (CRC32 of the padded upper-case name)."""
    s = name.upper().encode("latin-1")
    n = len(s)
    if n & 3:
        a = n >> 2
        s = s + bytes([n - (a << 2)])
        s = s + bytes([s[a << 2]]) * (3 - (n & 3))
    return zlib.crc32(s) & 0xFFFFFFFF


def default_game():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(os.path.dirname(os.path.dirname(here)), "Mental Omega")


def archives(game):
    found = []
    for fn in os.listdir(game):
        m = re.fullmatch(r"expandmo(\d\d)\.mix", fn, re.I)
        if m:
            found.append((int(m.group(1)), os.path.join(game, fn)))
    return [p for _, p in sorted(found, reverse=True)]


def read_index(path):
    with open(path, "rb") as f:
        head = f.read(10)
        if len(head) < 10:
            return None
        flags = struct.unpack_from("<I", head, 0)[0]
        if flags & 0xFFFF or flags & 0x00020000:
            return None  # old-style or encrypted header: cannot be read here
        count = struct.unpack_from("<H", head, 4)[0]
        raw = f.read(count * 12)
    base = 10 + count * 12
    idx = {}
    for i in range(count):
        fid, off, size = struct.unpack_from("<III", raw, i * 12)
        if off != 0xFFFFFFFF and fid not in idx:
            idx[fid] = (base + off, size)
    return idx


class Stock:
    def __init__(self, game):
        self.game = game
        self.mixes = []
        for p in archives(game):
            idx = read_index(p)
            if idx is not None:
                self.mixes.append((p, idx))
        if not self.mixes:
            sys.exit('ERROR: no readable expandmo##.mix archives in "%s". Use --game to point at the game folder.' % game)
        self._cache = {}

    def find(self, name):
        fid = ra2_id(name)
        for p, idx in self.mixes:
            if fid in idx:
                return p, idx[fid][0], idx[fid][1]
        return None

    def read(self, name):
        if name not in self._cache:
            hit = self.find(name)
            if hit is None:
                self._cache[name] = None
            else:
                with open(hit[0], "rb") as f:
                    f.seek(hit[1])
                    self._cache[name] = f.read(hit[2])
        return self._cache[name]


# ----------------------------------------------------------------------------- ini helpers
def parse_ini(text):
    """Return (sections, header_counts). sections: {lower id: {'name': id, 'keys': [(key, value)]}}."""
    sections, counts, cur = {}, {}, None
    for raw in text.splitlines():
        line = raw.split(";", 1)[0].strip()
        if not line:
            continue
        m = re.match(r"^\[([^\]]+)\]", line)
        if m:
            name = m.group(1).strip()
            cur = name.lower()
            counts[cur] = counts.get(cur, 0) + 1
            sections.setdefault(cur, {"name": name, "keys": []})
            continue
        if cur is not None and "=" in line:
            k, v = line.split("=", 1)
            sections[cur]["keys"].append((k.strip(), v.strip()))
    return sections, counts


def get(section, key, default=None):
    val = default
    for k, v in section["keys"]:
        if k.lower() == key.lower():
            val = v  # last one wins, like the game
    return val


def section_text(text, name):
    """All raw text blocks of [name] (case-insensitive), as a list of strings."""
    out, cur = [], None
    for raw in text.splitlines():
        m = re.match(r"^\s*\[([^\]]+)\]", raw)
        if m:
            if cur is not None:
                out.append("\n".join(cur).rstrip())
            cur = [raw] if m.group(1).strip().lower() == name.lower() else None
            continue
        if cur is not None:
            cur.append(raw)
    if cur is not None:
        out.append("\n".join(cur).rstrip())
    return out


def yes(v):
    return str(v).strip().lower() in ("yes", "true", "1")


# ----------------------------------------------------------------------------- commands
def cmd_section(args):
    stock = Stock(args.game)
    fname = ART if args.art else SOUND if args.sound else RULES
    data = stock.read(fname)
    if data is None:
        sys.exit("ERROR: %s was not found in the archives." % fname)
    blocks = section_text(data.decode("latin-1"), args.id)
    if not blocks:
        print("[%s] does not exist in the stock %s  (so this ID is free there)." % (args.id, fname))
        return 1
    for b in blocks:
        print(b)
        print()
    if len(blocks) > 1:
        print("; note: [%s] appears %d times in the stock %s" % (args.id, len(blocks), fname))
    return 0


def extract(stock, outdir, names, force):
    os.makedirs(outdir, exist_ok=True)
    rc = 0
    for n in names:
        hit = stock.find(n)
        if hit is None:
            print("MISSING  %s  (not in any expandmo archive)" % n)
            rc = 1
            continue
        out = os.path.join(outdir, n.lower())
        if os.path.exists(out) and not force:
            print("SKIPPED  %s  (already exists in the folder; add --force to replace it)" % n)
            continue
        with open(out, "wb") as f:
            f.write(stock.read(n))
        print("OK       %-20s %9d bytes  from %s  ->  %s" % (n, hit[2], os.path.basename(hit[0]), out))
    return rc


def cmd_extract(args):
    return extract(Stock(args.game), args.outdir, args.names, args.force)


def cmd_stock(args):
    return extract(Stock(args.game), args.outdir, [RULES, ART, SOUND], args.force)


def cmd_init_art(args):
    target = os.path.join(args.game, ART)
    if os.path.exists(target):
        print('NOTHING DONE: "%s" already exists. This command never overwrites it.' % target)
        print("If you really need a fresh one, move the existing file away first (keep it: it holds your own sections).")
        return 1
    data = Stock(args.game).read(ART)
    if data is None:
        sys.exit("ERROR: artmo.ini was not found in the archives.")
    with open(target, "wb") as f:
        f.write(data + b"\r\n" + b"\r\n".join(s.encode("ascii") for s in MARKER))
    print('Created "%s": %d stock bytes plus the "USER ADDITIONS" marker.' % (target, len(data)))
    print("Add your own art sections at the very end of that file.")
    return 0


class Report:
    def __init__(self):
        self.fails = 0
        self.warns = 0

    def ok(self, msg):
        print("  PASS  " + msg)

    def fail(self, msg):
        self.fails += 1
        print("  FAIL  " + msg)

    def warn(self, msg):
        self.warns += 1
        print("  WARN  " + msg)


def check_pcx(rep, path, label):
    d = open(path, "rb").read()
    if len(d) < 128 + 769:
        rep.fail("%s: too small to be an 8-bit PCX with a palette" % label)
        return
    man, ver, enc, bpp, x0, y0, x1, y1 = struct.unpack_from("<BBBBHHHH", d, 0)
    planes, w, h = d[65], x1 - x0 + 1, y1 - y0 + 1
    problems = []
    if man != 10:
        problems.append("not a PCX file")
    if ver != 5 or enc != 1:
        problems.append("version %d / encoding %d (stock icons: version 5, RLE)" % (ver, enc))
    if bpp != 8 or planes != 1:
        problems.append("%d bits x %d planes (stock icons: 8-bit, 1 plane, 256-colour palette)" % (bpp, planes))
    if (w, h) != (60, 48):
        problems.append("%dx%d pixels (stock icons: 60x48)" % (w, h))
    if d[-769] != 12:
        problems.append("no 256-colour palette at the end of the file")
    if problems:
        rep.fail("%s: %s" % (label, "; ".join(problems)))
    else:
        rep.ok("%s: 60x48, 8-bit paletted PCX like the stock icons" % label)


def check_vxl_pair(rep, game, base, flies=False):
    vxl, hva = os.path.join(game, base + ".vxl"), os.path.join(game, base + ".hva")
    missing = [os.path.basename(p) for p in (vxl, hva) if not os.path.isfile(p)]
    if missing:
        rep.fail("model file(s) missing from the game folder: " + ", ".join(missing))
        return
    d = open(vxl, "rb").read()
    h = open(hva, "rb").read()
    if not d.startswith(b"Voxel Animation") or len(d) < 802 + 28 + 92:
        rep.fail("%s.vxl is not a voxel file (bad header)" % base)
        return
    limbs = struct.unpack_from("<I", d, 20)[0]
    body = struct.unpack_from("<I", d, 28)[0]
    tail = 802 + limbs * 28 + body
    if limbs < 1 or tail + limbs * 92 != len(d):
        rep.fail("%s.vxl: header sizes do not add up to the file size (file is damaged)" % base)
        return
    x, y, z, mode = d[tail + 88], d[tail + 89], d[tail + 90], d[tail + 91]
    if 0 in (x, y, z):
        rep.fail("%s.vxl: model size is %dx%dx%d" % (base, x, y, z))
    else:
        rep.ok("%s.vxl: %d section(s), size %dx%dx%d" % (base, limbs, x, y, z))
    if mode != 4:
        rep.warn("%s.vxl: normals mode is %d; every stock tank and every working custom model uses 4" % (base, mode))
    if (d[32], d[33]) != (16, 31):
        rep.warn("%s.vxl: team-colour range is %d-%d; stock files use 16-31" % (base, d[32], d[33]))
    if len(h) < 24:
        rep.fail("%s.hva is too small" % base)
        return
    frames, sections = struct.unpack_from("<II", h, 16)
    if frames < 1 or sections < 1 or len(h) != 24 + 16 * sections + 48 * frames * sections:
        rep.fail("%s.hva: frame/section counts do not match the file size (file is damaged)" % base)
        return
    if sections != limbs:
        rep.warn("%s: the VXL has %d section(s) but the HVA has %d" % (base, limbs, sections))
    m = struct.unpack_from("<12f", h, 24 + 16 * sections)
    identity = all(abs(a - b) < 1e-4 for a, b in zip((m[0], m[1], m[4], m[5]), (1, 0, 0, 1)))
    if y > x and identity and flies:
        rep.ok("%s.hva: %d frame(s), %d section(s); the model is wider (%d) than long (%d), as some of the game's own "
               "flyers are" % (base, frames, sections, y, x))
    elif y > x and identity:
        rep.warn("%s: the model is longer along Y (%d) than along X (%d) and its HVA has no rotation; "
                 "a tank like that drove sideways in April 2026 (see the guide, model files section)" % (base, y, x))
    else:
        rep.ok("%s.hva: %d frame(s), %d section(s)" % (base, frames, sections))


# ----------------------------------------------------------------------------- weapons of your own
def list_values(sections, name):
    sec = sections.get(name.lower())
    return [v for _, v in sec["keys"]] if sec else []


def names_in(value, keep_nothing=False):
    """The names in a comma-separated value. Empty parts are dropped; so are none / <none> unless asked for."""
    out = [t.strip() for t in (value or "").split(",") if t.strip()]
    return out if keep_nothing else [t for t in out if t.lower() not in NOTHING]


def overlay(srules, mrules, name):
    """What the game ends up with for a block: the stock section of that name, if any, with your lines on top."""
    mode, stock = mrules.get(name.lower()), srules.get(name.lower())
    if mode and stock:
        return {"name": mode["name"], "keys": stock["keys"] + mode["keys"]}
    return mode or stock


def user_art_sections(game, sart):
    """The art sections of the loose artmo.ini that the stock art file does not have: the ones you added."""
    path = os.path.join(game, ART)
    if not os.path.isfile(path):
        return {}
    lart, _ = parse_ini(open(path, "rb").read().decode("latin-1"))
    return {n: s for n, s in lart.items() if n not in sart}


def mode_file_format(rep, mraw):
    """Format checks for the mode file: byte-order mark, line endings, lines below ';END OF FILE'."""
    if mraw[:3] == b"\xef\xbb\xbf":
        rep.fail("the file starts with a UTF-8 byte-order mark; save it as plain ANSI text")
    if mraw.count(b"\n") != mraw.count(b"\r\n"):
        rep.warn("the file has lines without Windows (CRLF) endings; the original is pure CRLF")
    end = mraw.find(b";END OF FILE")
    if end >= 0:
        below = [l for l in mraw[end:].decode("latin-1").splitlines()[1:] if l.split(";", 1)[0].strip()]
        if below:
            rep.warn("there are %d line(s) below ';END OF FILE'; keep everything you add above that line" % len(below))


def print_result(rep):
    print("\nResult: %d FAIL, %d WARN" % (rep.fails, rep.warns))
    if rep.fails == 0 and rep.warns == 0:
        print("Nothing blocking was found. Test in a Standard-mode skirmish.")
    elif rep.fails == 0:
        print("No FAIL, but read every WARN line above before you test.")
    else:
        print("Fix every FAIL line above before you start the game.")


class StockFacts:
    """What the stock files say about weapons, projectiles and warheads. Everything in here is read from them."""

    def __init__(self, srules, sart, ssound):
        self.rules, self.art, self.sound = srules, sart, ssound
        self._index = None

        def low(name):
            return {v.lower() for v in list_values(srules, name)}

        def has(sec, key):
            return get(sec, key) is not None

        # a weapon: registered under [WeaponTypes], or a section with both Projectile= and Warhead=
        # a projectile: registered under [Projectiles], or named by a stock weapon's Projectile=
        # a warhead: registered under [Warheads], or with a Verses= line, or named by a stock weapon
        self.weapons = low("WeaponTypes") | {n for n, s in srules.items() if has(s, "Projectile") and has(s, "Warhead")}
        self.projectiles = low("Projectiles")
        self.warheads = low("Warheads") | {n for n, s in srules.items() if has(s, "Verses")}
        for n in self.weapons:
            if n in srules:
                self.projectiles.update(t.lower() for t in names_in(get(srules[n], "Projectile")))
                for key in ("Warhead", "IvanBomb.Warhead"):
                    self.warheads.update(t.lower() for t in names_in(get(srules[n], key)))
        self.units = low("InfantryTypes") | low("VehicleTypes") | low("AircraftTypes") | low("BuildingTypes")
        self.anims = low("Animations")
        self.psys = low("ParticleSystems")
        self.cursors = {k.lower() for k, _ in srules.get("mousecursors", {"keys": []})["keys"]}

        # every key the stock blocks of each kind use (lower case -> the stock spelling). A stock name that is
        # also a unit or a country is left out here: the warhead "Special" shares its block with a country.
        foreign = self.units | low("Countries")
        self.keys, self.total = {}, {}
        for kind, members in (("weapon", self.weapons), ("projectile", self.projectiles), ("warhead", self.warheads)):
            own = sorted(m for m in members if m in srules and m not in foreign)
            spell = {}
            for m in own:
                for k, _ in srules[m]["keys"]:
                    spell.setdefault(k.lower(), k)
            self.keys[kind], self.total[kind] = spell, len(own)

        # armour names: the [ArmorTypes] list (its keys, and the basic armours it points at) and every Armor= line
        arm = srules.get("armortypes", {"keys": []})["keys"]
        self.armors = {k.lower() for k, _ in arm} | {v.lower() for _, v in arm if not re.fullmatch(r"-?\d+%", v)}
        self.armors |= {(get(s, "Armor") or "").lower() for s in srules.values()} - {""}
        self.versus_tails = {k.split(".")[2] for k in self.keys["warhead"] if k.startswith("versus.") and k.count(".") == 2}

        counts = {}
        for w in self.warheads:
            v = get(srules[w], "Verses") if w in srules else None
            if v is not None:
                counts[len(v.split(","))] = counts.get(len(v.split(",")), 0) + 1
        self.verses_n = max(counts, key=counts.get) if counts else 11
        self.with_verses = sum(counts.values())
        self.anim_counts = sorted({len(names_in(get(srules[w], "Anim"))) for w in self.weapons
                                   if w in srules and names_in(get(srules[w], "Anim"))})
        projs = [srules[p] for p in self.projectiles if p in srules]
        self.proj_total = len(projs)
        self.proj_with_image = sum(1 for s in projs if get(s, "Image"))
        self.proj_none = [s for s in projs if (get(s, "Image") or "").lower() in NOTHING]
        self.proj_none_inviso = sum(1 for s in self.proj_none if yes(get(s, "Inviso", "no")))

    def kind_of(self, low):
        for kind, members in (("weapon", self.weapons), ("projectile", self.projectiles), ("warhead", self.warheads)):
            if low in members:
                return kind
        return None

    def members(self, kind):
        return {"weapon": self.weapons, "projectile": self.projectiles, "warhead": self.warheads}[kind]

    def describe(self, low):
        kind = self.kind_of(low)
        if kind:
            return "a stock " + kind
        if low in self.units:
            return "a stock unit or building"
        if low in self.psys:
            return "a stock particle system"
        return "a stock section of another kind"

    def named_by(self, low):
        """How many stock rules sections name this one in one of their lines (the three ID lists not counted)."""
        if self._index is None:
            self._index = {}
            for n, s in self.rules.items():
                if n in ("weapontypes", "projectiles", "warheads"):
                    continue
                for _, v in s["keys"]:
                    for t in v.split(","):
                        self._index.setdefault(t.strip().lower(), set()).add(n)
        return len(self._index.get(low, set()) - {low})

    def versus_ok(self, key):
        """Versus.<armour> and Versus.<armour>.<tail>: fine for every armour name of the stock rules."""
        parts = key.lower().split(".")
        return (len(parts) in (2, 3) and parts[0] == "versus" and parts[1] in self.armors
                and (len(parts) == 2 or parts[2] in self.versus_tails))


class WeaponLint:
    """Checks for the weapon blocks you wrote in the mode file, and for the projectile and warhead blocks they name.

    FAIL is kept for one thing: a name that points at nothing (the tool's rule is that every name that is used
    must exist) - a missing Projectile=/Warhead= block, animation, particle system, projectile image or
    fragment weapon. Everything else is a WARN: a sound that is not in the stock sound file (the old Report=
    line was a WARN already), a Verses= line unlike the stock ones, a block named like a stock section (the
    tool cannot know whether that is meant), a key that no stock block uses, and things that are merely unlike
    anything in the stock files.
    """

    def __init__(self, rep, game, stock, facts, mrules, mcounts, user_art, old_reported=()):
        self.rep, self.game, self.stock, self.f = rep, game, stock, facts
        self.mrules, self.mcounts, self.user_art = mrules, mcounts, user_art
        self.old = {n.lower() for n in old_reported}  # weapons whose three old lines 'check' has already printed
        self.kind = {}       # lower-case name -> the kind that block is used as
        self.printed = set()  # blocks that have been checked
        self.queue = []      # weapons named by a projectile (AirburstWeapon=, ShrapnelWeapon=), checked afterwards
        self.own_done = set()

    def run(self, name, used=""):
        """Check the weapon block [name] and every block of yours that it leads to."""
        self.weapon(name, used)
        while self.queue:
            nxt, why = self.queue.pop(0)
            self.weapon(nxt, why)

    def has_file(self, name):
        return os.path.isfile(os.path.join(self.game, name)) or self.stock.find(name) is not None

    def registered(self, list_name):
        reg = self.mrules.get(list_name)
        return {v.lower() for v in dict(reg["keys"]).values()} if reg else set()  # same number twice: the later line counts

    # ---- one block of each kind
    def weapon(self, name, used):
        low = name.lower()
        if low in self.printed:
            return
        sec, eff = self.mrules[low], overlay(self.f.rules, self.mrules, low)
        tag = "[%s]" % sec["name"]
        print("\nCustom weapon %s%s" % (tag, "   (%s)" % used if used else ""))
        self.block(low, "weapon", tag)
        later = []
        for key, kind in (("Projectile", "projectile"), ("Warhead", "warhead")):
            val = get(eff, key)
            if not val or (val.lower() not in self.mrules and val.lower() not in self.f.rules):
                if low not in self.old:  # 'check' has printed this as "Primary=...: its Warhead=... is not defined anywhere"
                    self.rep.fail("%s: its %s=%s is not defined anywhere" % (tag, key, val))
            else:
                self.block_ref(tag, key, val, kind, later)
        self.refs(tag, eff, WEAPON_REFS, low in self.old)
        n = len(names_in(get(eff, "Anim")))
        if n and n not in self.f.anim_counts:
            usual = [str(c) for c in self.f.anim_counts]
            self.rep.warn("%s Anim= has %d names; the stock weapons have %s (one for all directions, or one for each direction)"
                          % (tag, n, " or ".join([", ".join(usual[:-1])] * (len(usual) > 1) + usual[-1:])))
        for val in names_in(get(eff, "IvanBomb.Warhead")):
            if val.lower() not in self.mrules and val.lower() not in self.f.rules:
                self.rep.fail("%s IvanBomb.Warhead=%s is not defined anywhere" % (tag, val))
            else:
                self.block_ref(tag, "IvanBomb.Warhead", val, "warhead", later)
        for kind, val, why in later:
            (self.projectile if kind == "projectile" else self.warhead)(val, why)

    def projectile(self, name, used):
        low = name.lower()
        sec, eff = self.mrules[low], overlay(self.f.rules, self.mrules, low)
        tag = "[%s]" % sec["name"]
        print("\nCustom projectile %s   (%s)" % (tag, used))
        self.block(low, "projectile", tag)
        self.image(tag, eff)
        for key in ("AirburstWeapon", "ShrapnelWeapon"):
            for val in names_in(get(eff, key)):
                vlow = val.lower()
                if vlow in self.mrules:
                    if self.kind.get(vlow, "weapon") != "weapon":
                        self.two_kinds(tag, key, val, "weapon")
                    else:
                        self.rep.ok("%s %s=%s (defined in the mode file%s)"
                                    % (tag, key, val, ", checked above" if vlow in self.printed else ""))
                        self.kind[vlow] = "weapon"
                        self.queue.append((val, "%s= of %s" % (key, tag)))
                        # The game reads every weapon block first and the projectile blocks after them (gamemd.exe
                        # 0x679B10 and 0x679B33). A weapon that only a projectile names is created while the
                        # projectiles are read, too late for that pass; the list [WeaponTypes] creates it in time.
                        # All 110 stock weapons named this way (24 by ShrapnelWeapon=, 86 by AirburstWeapon=) have
                        # their list line; 108 of them are named by no unit at all.
                        if vlow in self.registered("weapontypes"):
                            self.rep.ok("%s %s=%s has its line under [WeaponTypes]" % (tag, key, val))
                        else:
                            self.rep.warn("%s %s=%s: this weapon has no line under [WeaponTypes] in the mode file. A weapon "
                                          "that only a projectile names may be created too late to be read; all 110 stock "
                                          "weapons used this way are listed" % (tag, key, val))
                elif vlow in self.f.weapons:
                    self.rep.ok("%s %s=%s (stock weapon)" % (tag, key, val))
                elif vlow in self.f.rules:
                    self.rep.warn("%s %s=%s names %s, which is not a weapon" % (tag, key, val, self.f.describe(vlow)))
                else:
                    self.rep.fail("%s %s=%s is not defined in the stock rules or in the mode file" % (tag, key, val))
        self.refs(tag, eff, PROJECTILE_REFS)

    def warhead(self, name, used):
        low = name.lower()
        sec, eff, f = self.mrules[low], overlay(self.f.rules, self.mrules, low), self.f
        tag = "[%s]" % sec["name"]
        print("\nCustom warhead %s   (%s)" % (tag, used))
        self.block(low, "warhead", tag)
        verses = get(eff, "Verses")
        if verses is None:
            self.rep.warn("%s has no Verses= line; %d of the %d stock warheads have one, with %d values "
                          "(what the game does without it is not tested)" % (tag, f.with_verses, f.total["warhead"], f.verses_n))
        else:
            vals = [t.strip() for t in verses.split(",")]
            odd = [t or "(empty)" for t in vals if not re.fullmatch(r"-?\d+%", t)]
            if len(vals) != f.verses_n:
                self.rep.warn("%s Verses= has %d value(s); every stock warhead has %d, one for each basic armour "
                              "(what the game does with another number is not tested)" % (tag, len(vals), f.verses_n))
            if odd:
                self.rep.warn("%s Verses= has value(s) that are not written like the stock ones, a whole number "
                              "followed by %%: %s" % (tag, ", ".join(odd)))
            if len(vals) == f.verses_n and not odd:
                self.rep.ok("%s Verses= has %d values, like every stock warhead" % (tag, f.verses_n))
        # A warhead that spares a side does nothing when the owner forces an attack (Ctrl) on a unit of that side.
        # The owner of this install tests every weapon that way (report of 25 Nov 2026).
        spares = [(k, get(eff, k)) for k in ("AffectsAllies", "AffectsEnemies", "AffectsOwner")
                  if (get(eff, k) or "yes").strip().lower() in ("no", "false", "0")]
        for k, v in spares:
            self.rep.warn("%s has %s=%s: a forced attack (Ctrl) on a unit of that side does NO damage. Take the line out "
                          "unless that is meant" % (tag, k, v))
        if not spares:
            self.rep.ok("%s spares no side: a forced attack hurts whatever it is aimed at" % tag)
        self.refs(tag, eff, WARHEAD_REFS)

    # ---- checks shared by the three kinds
    def block(self, low, kind, tag):
        """The name of a block and its keys."""
        f, rep, sec = self.f, self.rep, self.mrules[low]
        self.kind[low] = kind
        self.printed.add(low)
        repeated = self.mcounts.get(low, 1) > 1
        if repeated:
            rep.warn("%s appears %d times in the mode file; keep ONE block of that name (what the game does with "
                     "a repeated header is not tested)" % (tag, self.mcounts[low]))
        if low not in f.rules and not f.kind_of(low):
            rep.ok("%s the name is not used by the stock rules" % tag)
        elif f.kind_of(low) == kind:
            rep.warn("%s is also the name of a stock %s: your block CHANGES that stock %s for everything that uses it "
                     "(%d stock section(s) name it), and a key you leave out keeps its stock value. Pick another "
                     "name unless that is what you want" % (tag, kind, kind, f.named_by(low)))
        else:
            rep.warn("%s is also the name of %s, and you use it as a %s: the game would read two different things "
                     "from one block. Pick another name" % (tag, f.describe(low), kind))
        known, unknown, respelled, twice, seen = f.keys[kind], [], [], [], set()
        for k, _ in sec["keys"]:
            kl = k.lower()
            if kl in seen:
                if k not in twice:
                    twice.append(k)
                continue
            seen.add(kl)
            if kl in known:
                if known[kl] != k:
                    respelled.append("%s (stock: %s)" % (k, known[kl]))
            elif not (kind == "warhead" and f.versus_ok(kl)):
                unknown.append(k)
        if repeated:
            twice = []  # every key of a repeated block shows up twice; the line above says why
        if unknown:
            rep.warn("%s has %d key(s) that none of the %d stock %ss uses (a typing mistake, or a key this game "
                     "does not have): %s" % (tag, len(unknown), f.total[kind], kind, ", ".join(unknown)))
        if respelled:
            rep.warn("%s writes %d key(s) with other capital letters than the stock rules, which always write a key "
                     "one way (whether the game minds is not tested): %s" % (tag, len(respelled), ", ".join(respelled)))
        if twice:
            rep.warn("%s has %d key(s) written more than once; keep one line of each (which line the game uses is "
                     "not tested): %s" % (tag, len(twice), ", ".join(twice)))
        if not (unknown or respelled or twice):
            rep.ok("%s %d key(s), all of them used by stock %ss" % (tag, len(seen), kind))

    def block_ref(self, tag, key, val, kind, later):
        """A line that names a block that exists: one of yours (checked afterwards, once) or a stock one."""
        low = val.lower()
        if low in self.mrules:
            if self.kind.get(low, kind) != kind:
                self.two_kinds(tag, key, val, kind)
                return
            self.rep.ok("%s %s=%s (defined in the mode file%s)" % (tag, key, val, ", checked above" if low in self.printed else ""))
            if low not in self.kind:
                self.kind[low] = kind
                later.append((kind, val, "%s= of %s" % (key, tag)))
        elif low in self.f.members(kind):
            self.rep.ok("%s %s=%s (stock %s)" % (tag, key, val, kind))
        else:
            self.rep.warn("%s %s=%s names %s; no stock weapon uses that as a %s"
                          % (tag, key, val, self.f.describe(low), kind))

    def two_kinds(self, tag, key, val, kind):
        self.rep.warn("%s %s=%s: the block [%s] is already used as a %s, and here as a %s; no stock block is two "
                      "kinds of thing at once. Give each its own block"
                      % (tag, key, val, self.mrules[val.lower()]["name"], self.kind[val.lower()], kind))

    def refs(self, tag, eff, table, report_printed=False):
        for key, what in table:
            if what == "sound":
                self.sound(tag, eff, key, report_printed)
            elif what == "anim":
                self.anim(tag, eff, key)
            elif what == "psys":
                self.particles(tag, eff, key)
            else:
                self.cursor(tag, eff, key)

    def sound(self, tag, eff, key, report_printed):
        val = get(eff, key)
        names = names_in(val, keep_nothing=(key == "Report"))
        if not names or not self.f.sound:
            return
        bad = [t for t in names if t.lower() not in self.f.sound]
        for t in bad:
            if key != "Report":
                self.rep.warn("%s %s=%s does not exist in the stock sound file (no sound)" % (tag, key, t))
            elif not report_printed:  # 'check' has printed this one as "Primary=...: firing sound Report=..."
                self.rep.warn("%s: firing sound Report=%s does not exist in the stock sound file (silent shot)" % (tag, t))
        if not bad:
            self.rep.ok("%s %s=%s (stock sound)" % (tag, key, val))

    def anim(self, tag, eff, key):
        names = names_in(get(eff, key))
        if not names:
            return
        f, bad, own = self.f, [], []
        for t in names:
            low = t.lower()
            if low in f.anims and low in f.art:
                continue
            if low in self.user_art:
                own.append(t)
            elif low in f.anims:
                bad.append("%s (it is in the stock [Animations] list, but the stock art has no [%s])" % (t, t))
            elif low in f.art:
                bad.append("%s (a stock art section, but not an animation: it is not in the stock [Animations] list)" % t)
            elif low in self.registered("animations"):
                bad.append("%s (registered under [Animations] in the mode file, but artmo.ini has no [%s] of yours)" % (t, t))
            else:
                bad.append(t)
        if bad:
            self.rep.fail("%s %s= names %d animation(s) that do not exist: %s   (not a stock animation, and no art "
                          "section of yours in artmo.ini)" % (tag, key, len(bad), ", ".join(bad)))
        else:
            self.rep.ok("%s %s=: %d animation name(s), %s" % (tag, key, len(names), "all stock" if not own
                        else "%d of them yours (%s)" % (len(own), ", ".join(own))))
        for t in own:
            self.own_anim(t)

    def own_anim(self, name):
        """An animation that is not stock but has an art section of yours. New animations are untested ground."""
        low = name.lower()
        if low in self.own_done:
            return
        self.own_done.add(low)
        if low not in self.registered("animations") and low not in self.f.anims:
            self.rep.warn("animation %s is yours (art section in artmo.ini), but it is not registered under [Animations] "
                          "in the mode file; all %d stock animations are registered in the stock rules (whether the game "
                          "shows an unregistered one is not tested)" % (name, len(self.f.anims)))
        if low in self.registered("animations") and low not in self.mrules:
            # read in gamemd.exe on 23 Nov 2026: an animation that the mode file adds is loaded from a section in the
            # mode file itself; its art section alone gives it neither settings nor picture (guide, 14.1)
            self.rep.warn("animation %s is registered under [Animations] in the mode file, but the mode file has no "
                          "section [%s]. The game loads an added animation only from a section in the mode file itself, "
                          "so this one will most likely not be drawn. Put a copy of its art section into the mode file "
                          "(guide, 14.1)" % (name, name))
        img = get(self.user_art[low], "Image") or self.user_art[low]["name"]
        if img.lower() not in self.f.art and not self.has_file(img + ".shp"):
            self.rep.warn("animation %s is yours, but there is no %s.shp in the game folder or in the archives "
                          "(nothing to draw)" % (name, img))

    def particles(self, tag, eff, key):
        for t in names_in(get(eff, key)):
            low = t.lower()
            if low in self.f.psys and low in self.f.rules:
                self.rep.ok("%s %s=%s (stock particle system)" % (tag, key, t))
            elif low in self.mrules:
                self.rep.ok("%s %s=%s (defined in the mode file)" % (tag, key, t))
                if low not in self.registered("particlesystems") and low not in self.own_done:
                    self.own_done.add(low)
                    self.rep.warn("particle system %s is yours, but it is not registered under [ParticleSystems] in the "
                                  "mode file; all %d stock particle systems are registered in the stock rules (whether "
                                  "the game needs that is not tested)" % (t, len(self.f.psys)))
            else:
                why = ("it is %s, not a particle system" % self.f.describe(low) if low in self.f.rules else
                       "it is not in the stock [ParticleSystems] list, and the mode file has no [%s]" % t)
                self.rep.fail("%s %s=%s: no such particle system (%s)" % (tag, key, t, why))

    def cursor(self, tag, eff, key):
        own = {k.lower() for k, _ in self.mrules.get("mousecursors", {"keys": []})["keys"]}
        for t in names_in(get(eff, key)):
            if t.lower() in self.f.cursors:
                self.rep.ok("%s %s=%s (stock mouse cursor)" % (tag, key, t))
            elif t.lower() in own:
                self.rep.ok("%s %s=%s (defined in the mode file)" % (tag, key, t))
            else:
                self.rep.warn("%s %s=%s is not in the stock [MouseCursors] list" % (tag, key, t))

    def image(self, tag, eff):
        """The picture of a projectile. Stock practice: an art section of that name, or Inviso=yes with Image=none."""
        f, img = self.f, (get(eff, "Image") or "").strip()
        if yes(get(eff, "Inviso", "no")):
            self.rep.ok("%s Inviso=yes: an invisible projectile, its image is not looked at" % tag)
        elif not img:
            self.rep.warn("%s has no Image= line and no Inviso=yes; %d of the %d stock projectiles have an Image= line"
                          % (tag, f.proj_with_image, f.proj_total))
        elif img.lower() in NOTHING:
            self.rep.warn("%s Image=%s without Inviso=yes; %d of the %d stock projectiles with Image=none have Inviso=yes"
                          % (tag, img, f.proj_none_inviso, len(f.proj_none)))
        elif img.lower() in f.art:
            self.rep.ok("%s Image=%s (stock art section)" % (tag, img))
        elif img.lower() in self.user_art:
            self.rep.ok("%s Image=%s (your art section in artmo.ini)" % (tag, img))
            exts = (".vxl", ".hva") if yes(get(self.user_art[img.lower()], "Voxel", "no")) else (".shp",)
            gone = [img + ext for ext in exts if not self.has_file(img + ext)]
            if gone:
                self.rep.warn("%s Image=%s: there is no %s in the game folder or in the archives (nothing to draw)"
                              % (tag, img, " / ".join(gone)))
        else:
            files = [img + ext for ext in (".shp", ".vxl") if self.has_file(img + ext)]
            if files:
                self.rep.warn("%s Image=%s: %s exists, but there is no art section [%s]; the image of every visible "
                              "stock projectile has one" % (tag, img, files[0], img))
            else:
                self.rep.fail("%s Image=%s does not exist: no art section [%s] in the stock art or among your own in "
                              "artmo.ini, and no %s.shp or %s.vxl in the game folder or in the archives"
                              % (tag, img, img, img, img))


def cmd_check(args):
    game, uid = args.game, args.id
    rep = Report()
    stock = Stock(game)
    rules_b, art_b, sound_b = stock.read(RULES), stock.read(ART), stock.read(SOUND)
    if rules_b is None or art_b is None:
        sys.exit("ERROR: stock rulesmo.ini / artmo.ini not found in the archives.")
    srules, _ = parse_ini(rules_b.decode("latin-1"))
    sart, _ = parse_ini(art_b.decode("latin-1"))
    ssound, _ = parse_ini(sound_b.decode("latin-1")) if sound_b else ({}, {})
    countries = [v for _, v in srules["countries"]["keys"]][:14]
    generic = {k.upper() for k, _ in srules.get("genericprerequisites", {"keys": []})["keys"]} | BUILTIN_PREREQ

    print('Preflight for NEW unit "%s"   game folder: %s' % (uid, game))
    print("\nRules (%s)" % MODE_FILE)
    mode_path = os.path.join(game, MODE_FILE)
    if not os.path.isfile(mode_path):
        rep.fail("file not found: " + mode_path)
        mrules, mcounts, mraw = {}, {}, b""
    else:
        mraw = open(mode_path, "rb").read()
        mrules, mcounts = parse_ini(mraw.decode("latin-1"))
        mode_file_format(rep, mraw)
    stock_vehicles = {v.lower() for _, v in srules["vehicletypes"]["keys"]}
    if uid.lower() in srules or uid.lower() in stock_vehicles:
        rep.fail('"%s" already exists in the stock rules. A block with that name CHANGES that stock unit '
                 "(that is the take-over route); pick another ID for a new unit" % uid)
        print("\nThis check is only for brand-new unit IDs, so it stops here.")
        print("\nResult: %d FAIL, %d WARN" % (rep.fails, rep.warns))
        return 1
    rep.ok("the ID is not used by the stock rules")
    unit = mrules.get(uid.lower())
    vt = mrules.get("vehicletypes")
    if mcounts.get("vehicletypes", 0) > 1:
        rep.fail("[VehicleTypes] appears %d times; keep ONE header and put every entry under it"
                 % mcounts["vehicletypes"])
    if not vt:
        rep.fail("no [VehicleTypes] section: the unit is not registered")
    else:
        keys = [k for k, _ in vt["keys"]]
        vals = [v.lower() for _, v in vt["keys"]]
        dup = sorted({k for k in keys if keys.count(k) > 1})
        if dup:
            rep.fail("[VehicleTypes] uses the same key twice: " + ", ".join(dup))
        n = vals.count(uid.lower())
        if n == 1:
            rep.ok("registered once under [VehicleTypes]")
        elif n == 0:
            rep.fail("not listed under [VehicleTypes] (add a line like 7412=%s with an unused key)" % uid)
        else:
            rep.fail("listed %d times under [VehicleTypes]" % n)
    art_name = uid
    turret = False
    flies = False
    own_weapons = {}  # lower-case name of a weapon block of yours -> the unit keys that name it
    if not unit:
        rep.fail("no [%s] section" % uid)
    else:
        if mcounts.get(uid.lower(), 0) > 1:
            rep.fail("[%s] appears %d times" % (uid, mcounts[uid.lower()]))
        else:
            rep.ok("[%s] section found (%d keys)" % (uid, len(unit["keys"])))
        art_name = get(unit, "Image", uid)
        turret = yes(get(unit, "Turret", "no"))
        flies = (get(unit, "MovementZone", "") or "").strip().lower() == "fly"      # a wing may be wider than long
        owners = [o.strip() for o in (get(unit, "Owner", "") or "").split(",") if o.strip()]
        bad = [o for o in owners if o.lower() not in [c.lower() for c in countries]]
        if not owners:
            rep.fail("no Owner= line: nobody can build it")
        elif bad:
            rep.fail("Owner= has names that are not Mental Omega countries: %s   (valid: %s)"
                     % (", ".join(bad), ", ".join(countries[:12])))
        else:
            rep.ok("Owner= lists %d valid countries" % len(owners))
        for req_key in ("RequiredHouses", "ForbiddenHouses"):
            req = get(unit, req_key)
            if req:
                bad = [o.strip() for o in req.split(",") if o.strip()
                       and o.strip().lower() not in [c.lower() for c in countries] + ["none"]]
                if bad:
                    rep.fail("%s= has names that are not Mental Omega countries: %s" % (req_key, ", ".join(bad)))
        tl = get(unit, "TechLevel")
        if tl is None or not re.fullmatch(r"-?\d+", tl) or not 1 <= int(tl) <= 10:
            rep.warn("TechLevel=%s; keep it between 1 and 10 (a value outside that range on a new unit is untested)" % tl)
        else:
            rep.ok("TechLevel=%s" % tl)
        pre = [p.strip() for p in (get(unit, "Prerequisite", "") or "").split(",") if p.strip()]
        bad = [p for p in pre if p.upper() not in generic and p.lower() not in srules and p.lower() not in mrules]
        if bad:
            rep.fail("Prerequisite= names something that does not exist: " + ", ".join(bad))
        else:
            rep.ok("Prerequisite=%s" % (",".join(pre) if pre else "(none)"))
        for wkey in OLD_WEAPON_KEYS:
            w = get(unit, wkey)
            if not w:
                continue
            if w.lower() in mrules:
                # a block of yours with a stock weapon's name is laid over that stock weapon (WeaponLint warns about it)
                wsec = overlay(srules, mrules, w)
                for sub in ("Warhead", "Projectile"):
                    sv = get(wsec, sub)
                    if not sv or (sv.lower() not in mrules and sv.lower() not in srules):
                        rep.fail("%s=%s: its %s=%s is not defined anywhere" % (wkey, w, sub, sv))
                for snd in names_in(get(wsec, "Report"), keep_nothing=True):
                    if ssound and snd.lower() not in ssound:
                        rep.warn("%s=%s: firing sound Report=%s does not exist in the stock sound file (silent shot)"
                                 % (wkey, w, snd))
                rep.ok("%s=%s (defined in the mode file)" % (wkey, w))
            elif w.lower() in srules:
                rep.ok("%s=%s (stock weapon)" % (wkey, w))
            else:
                rep.fail("%s=%s is not defined in the stock rules or in the mode file" % (wkey, w))
        for key in unit["keys"]:
            w = get(unit, key[0])
            if WEAPON_KEY.fullmatch(key[0]) and w and w.lower() in mrules:
                keys = own_weapons.setdefault(w.lower(), [])
                if key[0].lower() not in [k.lower() for k in keys]:
                    keys.append(key[0])
        stray = sorted({k for k, _ in unit["keys"] if k.lower() in ART_KEYS})
        if stray:
            rep.warn("art keys in the rules section do nothing here; they belong in artmo.ini: " + ", ".join(stray))
        if get(unit, "TurretAnim"):
            rep.warn("TurretAnim= is a building key; a vehicle's turret is found by file name (%sTUR.vxl)" % art_name)

    if own_weapons:  # nothing is printed here for a unit whose weapons are all stock
        old = [n for n, keys in own_weapons.items() if any(k.lower() in [o.lower() for o in OLD_WEAPON_KEYS] for k in keys)]
        lint = WeaponLint(rep, game, stock, StockFacts(srules, sart, ssound), mrules, mcounts,
                          user_art_sections(game, sart), old)
        for n, keys in own_weapons.items():
            lint.run(n, "%s of [%s]" % (", ".join(k + "=" for k in keys), unit["name"]))

    print("\nArt (loose artmo.ini, section [%s])" % art_name)
    art_path = os.path.join(game, ART)
    art_sec = None
    if not os.path.isfile(art_path):
        rep.fail('"%s" does not exist; create it with the init-art command, then add the section' % art_path)
    else:
        loose = open(art_path, "rb").read()
        if loose[:3] == b"\xef\xbb\xbf":
            rep.fail("artmo.ini starts with a UTF-8 byte-order mark; save it as plain ANSI text")
        if loose[:len(art_b)] != art_b:
            rep.fail("the first %d bytes are not the stock art file (edited, or the mod was updated); "
                     "re-create it with init-art and re-add your own sections" % len(art_b))
        else:
            rep.ok("the stock part of artmo.ini is intact (%d bytes)" % len(art_b))
        if loose.count(b"\n") != loose.count(b"\r\n"):
            rep.warn("artmo.ini has lines without Windows (CRLF) endings")
        lart, lcounts = parse_ini(loose.decode("latin-1"))
        n = lcounts.get(art_name.lower(), 0)
        if n == 0:
            rep.fail("no [%s] section in artmo.ini: the unit would be invisible and have no icon" % art_name)
        elif n > 1 or art_name.lower() in sart:
            rep.fail("[%s] is defined more than once (it already exists in the stock art, or you added it twice)"
                     % art_name)
        else:
            art_sec = lart[art_name.lower()]
            rep.ok("[%s] section found" % art_name)
    if art_sec:
        if yes(get(art_sec, "Voxel", "no")):
            rep.ok("Voxel=yes")
        else:
            rep.fail("Voxel=yes is missing: the game would look for a sprite, not your voxel model")
        for ck in ("CameoPCX", "AltCameoPCX"):
            cv = get(art_sec, ck)
            if not cv:
                (rep.warn if ck == "CameoPCX" else rep.ok)("%s not set%s" % (ck, " (no sidebar icon)" if ck == "CameoPCX" else ""))
                continue
            p = os.path.join(game, cv)
            if os.path.isfile(p):
                check_pcx(rep, p, "%s=%s" % (ck, cv))
            elif stock.find(cv):
                rep.ok("%s=%s (stock icon inside the archives)" % (ck, cv))
            else:
                rep.fail("%s=%s: no such file in the game folder or in the archives" % (ck, cv))
        if get(art_sec, "Cameo") or get(art_sec, "AltCameo"):
            rep.warn("Cameo=/AltCameo= are not what Mental Omega uses; its icons are set with CameoPCX=/AltCameoPCX=")

    print("\nModel files (game folder)")
    check_vxl_pair(rep, game, art_name, flies)
    if turret:
        check_vxl_pair(rep, game, art_name + "TUR", flies)
    else:
        print("  note  Turret=yes is not set, so no %sTUR files are expected" % art_name)
    if unit and turret and yes(get(unit, "IsChargeTurret", "no")):
        # a charge turret: the game draws one of TurretCount turret files, chosen by the time left until the weapon may
        # fire again (gamemd.exe 0x6FA505). Stage 0 is <ID>TUR, the others <ID>TUR1, <ID>TUR2 ... (0x5F7A90; the
        # game's table has 18 places). The stock Tesla Cruiser has 5 files, the Prism Tank 4.
        tc = (get(unit, "TurretCount", "") or "").strip()
        if not re.fullmatch(r"\d+", tc) or not 2 <= int(tc) <= 18:
            rep.fail("IsChargeTurret=yes needs TurretCount= between 2 and 18 (it is %r); the stock charge turrets have 4 or 5"
                     % tc)
        else:
            for k in range(1, int(tc)):
                check_vxl_pair(rep, game, "%sTUR%d" % (art_name, k), flies)
            rep.ok("IsChargeTurret=yes, TurretCount=%s: %sTUR and %sTUR1 to %sTUR%d are looked at above"
                   % (tc, art_name, art_name, art_name, int(tc) - 1))
        if (get(unit, "WeaponCount", "") or "").strip() in ("", "0") or not get(unit, "Weapon1"):
            rep.warn("IsChargeTurret=yes without WeaponCount= and Weapon1=; all three stock charge-turret units have both")
        if art_sec and not get(art_sec, "Weapon1FLH"):
            rep.warn("no Weapon1FLH= in the art section; all three stock charge-turret units set their fire point with it")

    print_result(rep)
    print("Not checked: section names inside model files, and rules lines such as Locomotor=, Armor= and sounds.")
    return 1 if rep.fails else 0


def cmd_lint_weapon(args):
    """The weapon checks of 'check' for one weapon block of the mode file, without a unit."""
    game, wid = args.game, args.id
    rep = Report()
    stock = Stock(game)
    rules_b, art_b, sound_b = stock.read(RULES), stock.read(ART), stock.read(SOUND)
    if rules_b is None or art_b is None:
        sys.exit("ERROR: stock rulesmo.ini / artmo.ini not found in the archives.")
    srules, _ = parse_ini(rules_b.decode("latin-1"))
    sart, _ = parse_ini(art_b.decode("latin-1"))
    ssound, _ = parse_ini(sound_b.decode("latin-1")) if sound_b else ({}, {})

    print('Lint for weapon "%s"   game folder: %s' % (wid, game))
    print("\nMode file (%s)" % MODE_FILE)
    mode_path = os.path.join(game, MODE_FILE)
    if not os.path.isfile(mode_path):
        rep.fail("file not found: " + mode_path)
        print_result(rep)
        return 1
    mraw = open(mode_path, "rb").read()
    mrules, mcounts = parse_ini(mraw.decode("latin-1"))
    mode_file_format(rep, mraw)
    sec = mrules.get(wid.lower())
    eff = overlay(srules, mrules, wid)
    if not sec:
        rep.fail("no [%s] section in the mode file%s" % (wid, "" if wid.lower() not in srules else
                 " (the stock rules have a section of that name; this command only checks blocks of your own)"))
    elif get(eff, "Projectile") is None and get(eff, "Warhead") is None:
        rep.fail("[%s] has neither Projectile= nor Warhead=, so it is not a weapon block%s" % (sec["name"],
                 "; it has a Verses= line like a warhead (give the name of the weapon that uses it)"
                 if get(eff, "Verses") is not None else ""))
    else:
        rep.ok("[%s] section found (%d keys)" % (sec["name"], len(sec["keys"])))
        WeaponLint(rep, game, stock, StockFacts(srules, sart, ssound), mrules, mcounts,
                   user_art_sections(game, sart)).run(wid)

    print_result(rep)
    print("Not checked: the numbers and the yes/no switches of the blocks, IvanBomb.Image=, what is inside a "
          "particle system or an animation of your own, and whether the game accepts the weapon.")
    return 1 if rep.fails else 0


def backup(path):
    """Copy path to path.bak (or .bak2, .bak3 ...) without ever overwriting an existing backup."""
    n = 1
    while True:
        bak = path + (".bak" if n == 1 else ".bak%d" % n)
        if not os.path.exists(bak):
            break
        n += 1
    with open(path, "rb") as src, open(bak, "wb") as dst:
        dst.write(src.read())
    return bak


def cmd_set_normals(args):
    """Set the normals-mode byte of every section to 4 (the value all stock tanks use)."""
    rc = 0
    for path in args.files:
        d = bytearray(open(path, "rb").read())
        if not d.startswith(b"Voxel Animation") or len(d) < 802 + 28 + 92:
            print("SKIPPED  %s: not a voxel (.vxl) file" % path)
            rc = 1
            continue
        limbs = struct.unpack_from("<I", d, 20)[0]
        body = struct.unpack_from("<I", d, 28)[0]
        tail = 802 + limbs * 28 + body
        if limbs < 1 or tail + limbs * 92 != len(d):
            print("SKIPPED  %s: header sizes do not add up to the file size; not touching it" % path)
            rc = 1
            continue
        old = [d[tail + i * 92 + 91] for i in range(limbs)]
        if all(o == 4 for o in old):
            print("OK       %s: normals mode is already 4, nothing changed" % path)
            continue
        bak = backup(path)
        for i in range(limbs):
            d[tail + i * 92 + 91] = 4
        with open(path, "wb") as f:
            f.write(d)
        print("CHANGED  %s: normals mode %s -> 4   (backup: %s)" % (path, ",".join(map(str, old)), os.path.basename(bak)))
    return rc


def cmd_rotate_hva(args):
    """Write a 90-degree turn about the vertical axis into every matrix of an HVA file.

    This is the April 2026 orientation fix. It REPLACES all twelve numbers of each matrix,
    so any offsets stored there are set to zero (as they were in April).
    """
    ccw = (0.0, -1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    cw = (0.0, 1.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    new = cw if args.cw else ccw
    rc = 0
    for path in args.files:
        h = bytearray(open(path, "rb").read())
        if len(h) < 24:
            print("SKIPPED  %s: too small to be an HVA file" % path)
            rc = 1
            continue
        frames, sections = struct.unpack_from("<II", h, 16)
        if frames < 1 or sections < 1 or len(h) != 24 + 16 * sections + 48 * frames * sections:
            print("SKIPPED  %s: frame/section counts do not match the file size; not touching it" % path)
            rc = 1
            continue
        start = 24 + 16 * sections
        old = struct.unpack_from("<12f", h, start)
        bak = backup(path)
        for i in range(frames * sections):
            struct.pack_into("<12f", h, start + i * 48, *new)
        with open(path, "wb") as f:
            f.write(h)
        print("CHANGED  %s: %d matrix(es) set to a 90-degree %s turn   (backup: %s)"
              % (path, frames * sections, "clockwise" if args.cw else "counter-clockwise", os.path.basename(bak)))
        print("         first matrix before: " + " ".join("%g" % v for v in old))
    return rc


def main():
    ap = argparse.ArgumentParser(description="Helper for adding units to Mental Omega 3.3.6 (never changes the archives).")
    ap.add_argument("--game", default=default_game(), help='the "Mental Omega" folder (default: next to this guide)')
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("section", help="print a stock section")
    p.add_argument("id")
    p.add_argument("--art", action="store_true", help="look in the stock art file instead of the rules")
    p.add_argument("--sound", action="store_true", help="look in the stock sound file instead of the rules")
    p.set_defaults(fn=cmd_section)
    p = sub.add_parser("extract", help="copy stock files out of the archives")
    p.add_argument("outdir")
    p.add_argument("names", nargs="+")
    p.add_argument("--force", action="store_true")
    p.set_defaults(fn=cmd_extract)
    p = sub.add_parser("stock", help="extract rulesmo.ini, artmo.ini and soundmo.ini for reading")
    p.add_argument("outdir")
    p.add_argument("--force", action="store_true")
    p.set_defaults(fn=cmd_stock)
    p = sub.add_parser("init-art", help="create the loose artmo.ini from the stock art file (never overwrites)")
    p.set_defaults(fn=cmd_init_art)
    p = sub.add_parser("check", help="preflight a NEW unit before starting the game")
    p.add_argument("id")
    p.set_defaults(fn=cmd_check)
    p = sub.add_parser("lint-weapon", help="check ONE weapon block of your own in the mode file, without a unit")
    p.add_argument("id")
    p.set_defaults(fn=cmd_lint_weapon)
    p = sub.add_parser("set-normals", help="set the normals-mode byte of .vxl files to 4 (keeps a .bak copy)")
    p.add_argument("files", nargs="+")
    p.set_defaults(fn=cmd_set_normals)
    p = sub.add_parser("rotate-hva", help="turn a model 90 degrees through its .hva file (keeps a .bak copy)")
    p.add_argument("files", nargs="+")
    p.add_argument("--cw", action="store_true", help="turn the other way (use if the model ends up facing backwards)")
    p.set_defaults(fn=cmd_rotate_hva)
    args = ap.parse_args()
    if not os.path.isdir(args.game):
        sys.exit('ERROR: game folder not found: "%s"  (use --game)' % args.game)
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
