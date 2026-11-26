# Modding Mental Omega 3.3.6: the one guide

Last checked against the game folder: 25 November 2026.

This is the single guide for modding this install: units, weapons, effects, buildings and maps. It replaces the older documents that stood beside it until 25 Nov 2026: the first `README.md`, `QUICK-REFERENCE.md`, docs `01` to `09` and the old scripts in `scripts`. That day, at the owner's wish, they were taken out of this folder, and the published repository, which had held docs `01` to `06`, the quick reference and the old scripts, was started anew with this guide alone (12, "Publishing the guide"). They are kept in `backups\2026-11-25-before-github-replace` (11). Where they disagree with this guide, this guide is right. Section 9 lists their known errors and the old scripts that are not safe.

Since 24 Nov 2026 the guide also says how the things themselves are made: a weapon with its hit effect, its damage and its reach (13), an animation (14), an infantry unit (15), a building on a map (16), a building that moves (17), a tank's model and icon (18), the mistakes made on the way (19), a hovering craft with a part that turns (20), how the first model here, the Nexus tank, became a unit of its own (21), ranks (22), and what to check before anything counts as finished (23). Since 25 Nov 2026 section 1 is the playbook: the one way to make each kind of thing, step by step, with the commands. If you are new to this work, or an assistant picking it up in a new session, read section 0 first, then section 1. The older docs `05`, `08` and `09` (now only in the backup named above) described a Blender route for models and for infantry sprites; the Arbalest's own model and everything made after it, the Doomsayer included, were made by script instead (15, 18).

Not covered: sound files and voices of your own. None has been made here; every new unit uses stock ones (13.7).

## How to read the labels

Every claim that matters carries a label, so you know how far to trust it.

- **[CONFIRMED]** Seen working in the game. The date is given.
- **[FILES]** Read directly from the game's files or logs. True of the files, but nobody watched the effect in game.
- **[UNTESTED]** Reasoned from the above. Nobody has tried it. When you try one, change its label (section 12).

What a command prints was taken from real runs of that command on a copy of the game folder on 22 Nov 2026. That tells you what the command does. It tells you nothing about the game.

## Words used in this guide

- **Stock**: as Mental Omega was delivered, before any change of yours.
- **Archive**: one of the game's big `expandmo` files in the `Mental Omega` folder. There are four: `expandmo95.mix`, `expandmo96.mix`, `expandmo97.mix`, `expandmo99.mix`. Many files are packed inside. You never change them.
- **Loose file**: a normal file in the `Mental Omega` folder, not packed in an archive.
- **Section** (also called block): a line in square brackets, such as `[ARBL]`, and the `Key=value` lines under it. The line in brackets is the **header**.
- **Rules**: what a unit is (price, strength, weapon). The stock rules are one text file, `rulesmo.ini`, inside an archive.
- **Art**: how a unit is drawn (model, icon). The stock art is one text file, `artmo.ini`, inside an archive.
- **Game mode**: what you choose in the skirmish screen, for example Standard.
- **Map code** (mode file): a file in `Mental Omega\INI\Map Code`, one per game mode. The client adds its text to every game of that mode.
- **Register**: add the unit's ID to the list `[VehicleTypes]`.
- **Model files**: a `.vxl` file (the shape) and a `.hva` file (its direction and position) with the same name. A tank has two pairs: one for the hull, one for the turret.
- **Icon** (the old docs say cameo): the unit's picture in the sidebar. It is a `.pcx` file.
- **Take over** (Route A; the old docs say reskin): change a stock unit instead of adding a new one.
- **The check**: the helper tool's test of a new unit before you start the game (section 4, step 6).
- **Sprite file**: a `.shp` file. It holds the pictures of a building, of a soldier or of an animation, one after the other. This guide calls each of them a picture; the tools and other guides say frame.
- **Palette**: the table of 256 colours that the pixels of a sprite point into. Units and buildings use the unit palette; in it the colours 16 to 31 are shown in the owner's colour (the house colour). Animations use the animation palette.
- **Animation**: a sprite that plays by itself: an explosion, a marker, a moving part of a building (sections 14 and 17).
- **Bundle**, **pack**: a folder with everything one new thing needs (rules, art, files), made for one of the two installers. A bundle holds one vehicle (10.7). A pack holds an infantry unit, a fix, or buildings on a map (10.8).
- **Cell**, **lot**, **height level**: a cell is one square of the map. A building's lot is the cells it stands on, for example 3x3. The ground lies on height levels; the plaza of (6) Kalifornia Crisis is four levels above its streets.
- **Rehearsal copy** (the tools say sandbox): a copy of the game files that an installer writes, in a folder outside the game, for trying an install without risk (16.10, 18.3).
- **Range ring**: the circle that a selected defence draws round itself (13.5).
- **Forced attack**: an attack ordered while you hold Ctrl. The unit attacks whatever you click, your own units and neutral buildings included (13.10).
- **Rank**: rookie, veteran or elite. A unit rises by killing enemies (22). The owner calls them tiers.

Two stand-in names are used. They are explained here, once:

- **`NEWID`** stands for the ID of your new unit (Route B, section 4). **`NEWID` is not a real name. Never type the letters N-E-W-I-D.** Wherever this guide shows `NEWID`, type your own unit ID in capital letters. Wherever it shows `newid`, type the same ID in small letters. This is true for commands, for file names and for text you put into the INI files. Example: if your ID is `MYTK`, then `NEWIDTUR.vxl` means `MYTKTUR.vxl`, `newidicon.pcx` means `mytkicon.pcx`, and a command that ends with `check NEWID` ends with `check MYTK`.
- **`NAME`** stands for the word you write after `Image=` when a stock unit gets your model (Route A, section 5). Your model files are named after it. Example: the working block has `Image=FTNKNEXUS`, so there `NAMETUR.vxl` means `FTNKNEXUSTUR.vxl`. For a new unit (Route B), `NAME` is the same as `NEWID`.

`ARBL` (the Arbalest Tank) is not a stand-in. It is the real, finished example of a new unit. It is taken.

## Contents

0. Start here if you are picking this work up
1. The playbook: what to do when the owner asks for something
2. How the game loads things
3. One-time setup
4. Route B: add a brand-new unit, step by step
5. Route A: give a stock unit your model, step by step
6. Reference tables
7. Model files: what a working model has
8. Troubleshooting
9. Things that do not work, and errors in the old docs
10. Backups, undo, updates, playing online
11. What is installed right now
12. Keeping this guide correct
13. A weapon of your own: the shot, the hit and the damage
14. An animation of your own: explosion, marker, flying picture
15. An infantry unit with a body of its own
16. A building on a map
17. A building that moves
18. A vehicle's model and icon, made by script
19. Mistakes made on the way
20. Flyers: what the game does, and the three craft that were built
21. The Nexus tank as a unit of its own
22. Ranks: veteran and elite
23. Before it counts as finished: a list by kind

---

## 0. Start here if you are picking this work up

This section is for whoever continues the work: you, or an assistant in a new session that has seen none of the earlier work. It says what exists, where it is, what must never be done, and in which order work is done here. **When the owner asks you to make or change something, section 1 says how, step by step.**

**What can be put into the game, and where to read about it.** Section 11 lists what is installed.

| Kind of thing | How it gets into the game | Worked example | Read |
|---|---|---|---|
| A vehicle with a model and an icon of its own | Rules in the mode file `Standard.ini`, art in the loose `artmo.ini`, loose model and icon files | Arbalest (by hand); Reaver, Cerberus, Moloch (with the installer); the Nexus tank, an older model that was given a unit of its own | 4, 10.7, 18, 21 |
| A weapon of its own, with its hit effect and its damage | Blocks next to the unit, each copied from a stock weapon | The three vehicle weapons, the Doomsayer's flare, the Stormspire's bolt, the Nexus's starburst (an orb that hits and throws rays from there) | 6.6, 13, 21.3 |
| A shot that throws pieces from where it hits | `ShrapnelWeapon=` and `ShrapnelCount=` on the projectile; the piece weapon needs a line under `[WeaponTypes]` | The Nexus's five rays | 13.8, 21.3 |
| An animation of its own (explosion, marker, flying picture) | A sprite file, a line under `[Animations]` and a section of its own in the same file. A flying picture needs only an art section | `REAVZAP`, `DOOMMARK`, `DOOMBLST`; the flying picture `DOOMFLR` | 14 |
| An infantry unit with a body of its own | A "mode pack": `Standard.ini`, `artmo.ini`, sprite and icon files | Doomsayer | 10.8, 15 |
| Buildings that stand on one map | A "map pack": lines and sections in the map file, `artmo.ini`, sprite files | The five buildings of the Black Site | 10.8, 16 |
| A landmark that soldiers can garrison | The same pack; the rules of the game's own garrisonable landmarks and ten firing points | The Vessel | 16.12 |
| Buildings that move | Two animation files per building | The same four buildings | 17 |
| A flyer (a hovering craft with a part that turns) | Like a vehicle, with the vehicle installer. Its rules are a copy of a stock flyer's, its turning part is the turret file | Seraph, Tempest, Nova | 20 |
| A turret that glows as its weapon charges | One turret file per stage, `IsChargeTurret=true` in the rules | The Nexus tank (eight stages) | 21.3 |
| A salvo of homing missiles with a model, a smoke trail and an explosion of their own | A weapon with `Burst=`; a projectile whose picture is a small model; a trail animation named in that picture's art section | The Tempest's swarm of eight | 13.9, 20.5 |
| Ranks (veteran, elite): what a unit gains, an elite weapon, a look of its own for a rank | Lines in the unit's block. A look of its own is a second unit that the game turns it into | All nine new units have the game's ranks; none has an elite look yet | 22 |
| The two preview pictures of a map: in the skirmish screen and on the loading screen | Both are part of the map pack: a PNG file beside the map, and the section `[PreviewPack]` inside it | The Black Site, since 25 Nov 2026, 15:04 | 16.13 |

**Where things are.** Every path in this guide starts at the project folder (3.1).

| Folder | What it holds |
|---|---|
| `Mental Omega` | The game. Only the installers write into it, and only while the game and the client are closed. |
| `MentalOmega-Modding-Guide` | This guide, `README.md`, `.gitignore` and the helper tool `scripts\mo_tool.py` (3.2), and since 25 Nov 2026 nothing else (Python's `__pycache__` folder beside the tool is ignored). It is a git repository, published as the public GitHub repository `sh4faq/Red-Alert-2--Modding-Guide`. Anyone can read what is in it: nothing in it may contain a personal folder path, a name or an e-mail address. Commit and push only when the owner asks (12, "Publishing the guide"). The other folders of this table are not published. |
| `arbalest-tank\kit` | The tools: the two installers (`unit_bundle.py`, `packs.py`), the model tools (`forge.py`, `forge_build.py`, `forge_stock.py`, `vxlkit.py`, `voxrender.py`, `pcxkit.py`, `validate_model.py`), the sprite tools in `sprites` (`shpkit.py`, `fxkit.py`, `figkit.py`, `structkit.py`), the map reader `mapkit.py`, the two tools for a map's preview pictures (`previewkit.py`, `lzo_pack.ps1`, 16.13), the read-only `weapon_audit.py` (what every weapon of ours can and cannot hurt, 13.10) and `find_unit.py` (a unit by the name the player sees, whether a name is taken, units by a key, 1.13), `pick_sheet.py` (candidates in one picture, 1.1), the tests in `tests`, and what was measured and read in `research`. Each tool named in this guide starts with a description of itself; read that before you use it. |
| `arbalest-tank` | The four designs of the Arbalest and the script that puts one in (`install_arbalest_option.py`). |
| `new-units` | Reaver, Cerberus, Moloch: build scripts, finished bundles, preview. |
| `new-infantry` | Doomsayer and `REAVFIX`: build scripts, finished packs, preview. |
| `new-buildings` | The five buildings: build scripts, the animation tool `anim.py`, the finished pack `SITE`, the range check, the script that makes the map's two preview pictures (`site_preview.py`, its output in `SITE-preview`, a picture to look at in `PREVIEW-CHECK.png`, 16.13), previews, and the earlier versions as packs (`round1` to `round5`; `round5` is the pack of 25 Nov 2026, 01:16 to 15:04: the five buildings without the preview pictures). Since 25 Nov 2026 also a second model of the Vessel made from photographs, which is NOT installed: `build_vessel2.py`, the photographs in `vessel-photos`, the built candidates in `vessel-v2`, and the picture the owner picks from, `VESSEL-PICK.png` (16.12). |
| `new-aircraft` | Seraph, Tempest, Nova: the three build scripts, the finished bundles, the Seraph's other weapon (`SRPH-laser`), the preview, in `candidates` what the owner picked from, and in `round1` the Tempest as it was until 25 Nov 2026 (lightning), with the four scripts of that day; in `round2` the swarm as it was from 12:57 to 14:41 that day, when its warhead spared its own side (13.10), with its scripts. |
| `nexus-tank` | The Nexus tank as a unit of its own: its four original model files (`original`), the build scripts, the paint rules `paint.py`, the finished bundle `NEXS`, the other paint `paint-B`, the version of 24 Nov 2026 in `round1`, the second version (25 Nov 2026, 00:05 to 11:34, the shot that burst in the air) in `round2`, the third as it was from 11:34 to 14:41 that day, when its warheads spared its own side (13.10), in `round3`, the owner's screenshot of 25 Nov 2026 in `evidence-2026-11-25`, the script that retired the Bulldog take-over, and the preview. |
| `stock-reference` | The game's own `rulesmo.ini`, `artmo.ini` and `soundmo.ini` as text, to read and search. |
| `backups` | A copy of everything that was changed, by date and time. The installers fill it by themselves. |

**Never do these.**

- Never change or rebuild an `expandmo` archive, and never run the old scripts listed in section 9.
- Never write into `Mental Omega` while the game or the client runs. The installers refuse; do not work round them.
- Never leave a loose `.pal` file in `Mental Omega`. The game uses it in place of its own palette and draws buildings and units in wrong colours (seen in 2026, before this guide). The palettes the tools need are in `arbalest-tank\kit\sprites\base\palettes`.
- Never run the client's map renderer on the game's own files, and never with its options that change a map (`-k`, `-K`, `-l`, `-L`, `--fixup-tiles`, `--fix-overlays`, `--cmprs-tiles`). The scripts of 16.7 run it on copies.
- Never change a label in this guide without the owner's own report or screenshot (section 12).
- Do not play online with this install (10.6).
- An assistant does not start the game on the owner's desktop. The owner plays and reports.

**What the owner of this install asked for, in the order it was said.** These are standing wishes, not one-time remarks.

- New art must look at home beside the game's own. Measure the closest stock thing first and build the way it is built (16.6 for buildings, 18.2 for tanks).
- A new unit is an original model. A stock sprite in other colours does not count as new (15).
- A building is not finished until something on it clearly moves: a part that turns, swings or flies, and lamps that switch (17).
- Where several designs are possible, show finished candidates in one picture and let the owner pick. When the owner says "go ahead", or when something already installed is being corrected, install directly, with a backup and a way back.
- Say plainly what gap to the game's art remains. Do not claim that something matches when it has not been seen in the game.
- Every weapon must hurt whatever it is forced on. The owner tests a weapon by holding Ctrl and attacking their own soldiers, tanks and flyers and neutral buildings, and asked for that to be minded "in all of the builds" (25 Nov 2026). Never give a warhead a line that spares a side (13.10). A 0% against an armour stays only where the stock template has it, and the owner is told (1.2, rule 4).
- What a pack adds to a map must show in the map's two preview pictures too: in the skirmish screen and on the loading screen (16.13).
- The owner asked whether the new units get ranks, change their look and repair themselves (25 Nov 2026). Decide a new unit's ranks with the unit (22).

**The order of work for anything new.**

1. Find the closest stock thing and read its rules and art with `mo_tool.py section` (3.2). Copy whole blocks and change values; do not write keys from memory. Copy from a stock unit that does the same job: a tank's gun from a tank's gun, not from an artillery piece (21.1).
2. Check every new name against the stock rules and the stock art. `CAHELI` looked free and was a stock helipad.
3. Build the files with the kit into a folder of their own (`new-units`, `new-infantry`, `new-buildings`), never in the game folder.
4. Look at the result beside stock art: a preview picture for units, the map renderer for buildings (16.7), a moving picture for animations.
5. Make the bundle or the pack (10.7, 10.8).
6. Rehearse on a copy of the game files: `arbalest-tank\kit\tests\make_sandbox.py`, then the installer with `--root` (16.10 for a pack, 18.3 for a vehicle).
7. Install with the installer. It checks that the game is closed, keeps a backup, runs its checks and puts everything back if one fails.
8. Run the check that fits the kind of thing (the table below), and go through the list for its kind in section 23.
9. Ask the owner to look at named things in one game. Record the answer in sections 10 to 12 with a label and the date. Then read `Mental Omega\debug\debug.log` of that game: it must have no line with `Failed to parse INI file content`.

**Which check fits which kind.**

| Kind of thing | The check | Not this one |
|---|---|---|
| A vehicle (section 4, or a bundle), a hovering craft included | `mo_tool.py check ID`. The vehicle installer runs it by itself. | |
| A weapon block in `Standard.ini` | `mo_tool.py lint-weapon NAME`. `check ID` also checks the weapon of that vehicle. | `lint-weapon` on a weapon that stands in a map file: it reads `Standard.ini` only |
| An infantry unit, a fix, anything else in a pack | `packs.py verify NAME` | `mo_tool.py check` on an infantry unit: it is made for vehicles and prints three false FAILs (no `[VehicleTypes]` line, no `Voxel=yes`, no model file) |
| Buildings on a map | `packs.py verify SITE`, and for a building with a weapon `check_range.py` (13.5) | |
| Every weapon of ours, before a game | `weapon_audit.py` (1.2) must end with `Result: 0 WARN`; `mo_tool.py check ID` warns as well for a vehicle (13.10) | |
| Every weapon, in a game | Hold Ctrl and attack one of your own soldiers, tanks and flyers and a neutral building: each must lose health (13.10, 23) | |
| A map pack's two preview pictures | `packs.py verify NAME` checks both (16.13) | |
| Any of them, after a game | No line with `Failed to parse INI file content` in `Mental Omega\debug\debug.log` | |

**Numbers for list lines.** A list line is a number, `=` and a name. The number only has to be unused in that list of that file. The stock lists count up from 0: `[InfantryTypes]` to 150, `[VehicleTypes]` to 363, `[AircraftTypes]` to 50, `[BuildingTypes]` to 1155, `[WeaponTypes]` to 1072, `[Projectiles]` to 666, `[Warheads]` to 733, `[Animations]` to 2261. **[FILES]** In use by this work, in `Standard.ini`: 7411 to 7415, 7417, 7420 and 7421 under `[VehicleTypes]` (7416, 7418 and 7419 are free again), 9421 under `[InfantryTypes]`, 9421 to 9423 under `[WeaponTypes]`, 9421 under `[Projectiles]` and under `[Warheads]`, 9001, 9011 to 9015, 9018, 9019 and 9029 to 9037 under `[Animations]` (9020 to 9028 are free again). In the map file: 86001 to 86005 and 86101 to 86113. The vehicle installer takes, by itself, one above the highest number in use in that list. A pack names its numbers itself, when its `make_pack.py` runs: take the next ones above those in use, and make the pack right before you install it, because a vehicle installed in between can take a number. The pack installer refuses a number that is taken.

**Notes for an assistant.**

- Run every command exactly as this guide prints it. Start your own scripts as `python -I -B`; the installers and `mo_tool.py` are printed with plain `python` where that is how they were run. Only numpy and Pillow are needed, and both are installed. Do not install anything.
- Write a helper script to a file and run the file. Text typed straight into the shell loses backslashes and quotes.
- Run every command from the project folder, with paths that start there.
- Some builds take minutes: the Doomsayer's 301 pictures about three minutes, a 3x3 building about six seconds per picture.
- This guide has Windows line endings. The blocks marked "exactly as it is in the file" must stay equal to the game's files, character for character. Two small read-only checks help with that: `python -I "arbalest-tank\kit\research\guide\guide_lint.py" "MentalOmega-Modding-Guide\10-Adding-Units.md"` (tables, code blocks, line endings, personal paths) and `python -I "arbalest-tank\kit\research\guide\guide_blocks.py" "MentalOmega-Modding-Guide\10-Adding-Units.md" "Mental Omega"` (which quoted INI blocks stand in the game's files; four blocks are expected to be missing: the three with `NEWID` or example lines, and the Bulldog take-over of section 5, which was retired on 24 Nov 2026).
- Tools changed after a version was installed no longer reproduce that version's files. That is why every finished pack and bundle folder is kept: the folder installs, whatever the scripts do today.
- A build writes over its folder: `new-buildings\make_pack.py` over `new-buildings\SITE`, `new-units\make_bundles.py` over all three unit folders. Before you change something that is installed, copy its folder to a new `round` folder, the way `round1` to `round3` were made (for a vehicle too: `nexus-tank\round1` and `round2`). What is installed is also kept in `backups\packs\<NAME>\pack` and `backups\unit-bundles\<ID>`.

---

## 1. The playbook: what to do when the owner asks for something

This is the one way to do each kind of work in this install, in the order it is done, with the exact commands and what they must answer. Everything in it was done here between 22 and 25 Nov 2026, and every mistake the owner found on the way is built into it (section 19). Each step names the section that explains it. Where a step has been done only once, or only on a rehearsal copy, it says so.

An assistant in a new session: read section 0 first (what exists, what must never be done, the owner's standing wishes), then 1.1 and 1.2, then the recipe that fits the request. Do its steps in their order. Never skip the rehearsal or the check.

### 1.1 First, for every request

1. See what is installed now:

```powershell
python "arbalest-tank\kit\unit_bundle.py" status
python -I "arbalest-tank\kit\packs.py" status
```

   The first prints every list of `Standard.ini` with the numbers in use (`[VehicleTypes]`, `[Animations]`, `[WeaponTypes]`, `[InfantryTypes]`, `[Projectiles]`, `[Warheads]`) and one line for each vehicle it installed; the second prints one line for each installed pack. Section 11 says what each thing is.

2. Find the recipe:

| The owner asks for | It is | Recipe |
|---|---|---|
| a new tank, a new vehicle | a vehicle with a model, an icon and a weapon of its own | 1.3 |
| an aircraft, a plane, a flyer | a hovering vehicle with a part that turns. A true jet under `[AircraftTypes]` was never tried (20.1) | 1.4 |
| a soldier, an infantry unit | an infantry unit with a body of its own | 1.5 |
| a building, a landmark, something on a map | buildings that stand on one map | 1.6 |
| a new attack or weapon for a unit | a weapon, its shot and its hit | 1.7 |
| an explosion, an effect, a glow | an animation | 1.8 |
| "it does not hit", "it does no damage", anything wrong in a game | a fault | 1.9 |
| a new look, the old version back, a unit out | a change to something installed | 1.10 |
| ranks ("tiers"): veteran and elite | every unit has them already; what can be added | 22 |

3. Decide how to show it (the owner's standing wishes, section 0):
   - Something new to look at (a model, an icon, a building, an effect): build two or three finished candidates and show them in one picture. The owner picks; then the picked one is finished and installed. Examples: `new-aircraft\candidates\PREVIEW.png`, and `new-buildings\VESSEL-PICK.png`, made by `new-buildings\vessel_pick.py`. Any finished pictures (the sheets of model candidates, sheets of effects, renders of buildings) go side by side, labelled A, B, C, with:

```powershell
python -I "arbalest-tank\kit\pick_sheet.py" "$env:TEMP\pick.png" "new-units\REAV\REAV_sheet.png" "new-units\CERB\CERB_sheet.png" "new-units\MLCH\MLCH_sheet.png"
```

     It answers `wrote` with the file and `3 pictures, 2989 x 1046`. Write the picture for the owner into the unit's folder in the project, not into the temporary folder.
   - When a request can mean more than one thing (a building that "shows the map": its surroundings, the radar map or the whole map), or a report does not say which unit or which game, ask one short question with the choices found in the stock files before you build.
   - The owner says "go ahead", "build" or "surprise me", or something installed is being put right: build and install directly, with a backup and a way back, and tell the owner the way back.
   - The owner names a real thing (a landmark, a kind of craft) or asks you to look something up: look it up first, keep what you found and its sources in the project folder (`new-buildings\vessel-photos` with the photographers and licences; `arbalest-tank\kit\research\aircraft\scifi_attack_craft.md`), and build from it.
4. Before anything installed is changed, copy its folder to a new `round` folder (section 0). The installers keep their own copies in `backups` as well.
5. Every install, swap and removal needs the game and the client closed; the installers refuse otherwise. Never start the game yourself: the owner plays and reports.

### 1.2 The eight rules every recipe follows

They come from section 19. Each one cost a round with the owner.

1. **Copy, do not invent.** Find the stock thing that does the same job, print its blocks (`mo_tool.py section NAME`, with `--art` for its art), copy them whole and change values. A tank's gun from a tank's gun, a flyer from a flyer, a soldier from a soldier. A gun copied from an artillery piece behaved like artillery and burst in the air (21.1). The bundle scripts copy with a function that stops when a key you want to change is not in the stock block (13.2).
2. **Check every name.** A new ID and every new section name must be free in the stock rules, the stock art and our own files (1.3, step 2). `CAHELI` looked free and was a stock helipad.
3. **List what must be listed.** A vehicle under `[VehicleTypes]`, a soldier under `[InfantryTypes]`, an animation under `[Animations]` with a section of its own in the same file (14.1), a weapon that only a projectile names under `[WeaponTypes]` (13.8). The installers write these lines from the bundle's `register` or the pack's `lists`.
4. **A weapon hurts whatever it is forced on.** No `AffectsAllies=no`, `AffectsEnemies=no` or `AffectsOwner=no`, also none kept from a copied stock warhead. Decide whether it may aim at flyers (`AA=yes`). A 0% against an armour stays only where the stock template has it (a sniper's rifle does nothing to tanks), and the owner is told before it is built. One read-only line shows all of it for every weapon of ours (13.10):

```powershell
python -I "arbalest-tank\kit\weapon_audit.py"
```

   It prints one line per weapon (its shot with `AA=` and `AG=`, its warhead, a `WARN` for a line that spares a side, under `shot:` the lines that make the shot do more than fly to its target, and under `does nothing to:` the armours it does not hurt that an ordinary tank gun does) and ends with `Result: 0 WARN`. `0 WARN` does not mean that it hurts everything: read the two columns.
5. **Look like the game.** Measure the closest stock thing first and build to its numbers: tanks 18.2, buildings 16.6, soldiers 15.4. Look at every picture of a stock sprite of the same kind: a garrisonable building's third picture is its occupied look (16.12). A real landmark is modelled from photographs (16.12). A building is not finished until something on it moves (17). A new unit is an original model, never a stock one in other colours (15).
6. **Build by script, into a folder of its own.** Nothing is drawn or typed into the game folder by hand. The scripts give the same files every time; the folder is what the installer reads.
7. **Rehearse, install, check.** First a copy of the game files (`make_sandbox.py`), then the installer on the real folder, then the check that fits (section 0's table) and `weapon_audit.py`.
8. **Ask, then record.** Named questions for the owner's next game (section 12). The answers go into sections 10 to 12 with a label and the date, and the game's log is read (1.11).

### 1.3 A new tank

The worked examples are the Reaver, the Cerberus and the Moloch (`new-units`, 23 Nov 2026). These steps were followed to the end once more on 25 Nov 2026 with a throw-away ID on a rehearsal copy: the install ended with `installed` and `Result: 0 FAIL, 0 WARN`. **[FILES]** Commands and code with `NEWID` or `newid` are templates: put your ID in first (3.1).

1. **The job and the template.** Decide what the tank does (a gun, a flamer, lightning, a siege gun) and find the stock vehicle that does it: 6.4 has a table, `stock-reference\rulesmo.ini` has them all, and `find_unit.py` finds one by the name the player sees:

```powershell
python -I "arbalest-tank\kit\find_unit.py" Cavalier
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" section MTNK
```

   The first answers `[MTNK]  stock        VehicleTypes   Name=Cavalier Medium Tank   Primary=105mmR`; the second prints its whole block. Print its weapon the same way (`section 105mmR`), then the `Projectile=` and the `Warhead=` that the weapon names. To find a stock unit by what it fires, search the weapons' names or any key:

```powershell
python -I "arbalest-tank\kit\find_unit.py" --key Primary=Rail
```

   It lists the five stock units whose weapon has `Rail` in its name, among them `[MARA]  stock        Primary=MarauderRailgun` (the Marauder). The kinds of shot the game draws (bolts, lasers, railgun beams with particles, waves) are in the table of 20.4. Look at the weapon's projectile too: `Airburst=`, `Ranged=` with a short `ProjectileRange=` on the weapon, `Splits=`, `Inaccurate=` or `FlakScatter=` make a shot do more than fly to what it is aimed at, which is right for artillery and wrong for a tank's gun (21.1).

2. **The ID.** Capital letters, four like all of ours. It must be free in both stock files and in ours:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" section NEWID
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" section NEWID --art
python -I "arbalest-tank\kit\find_unit.py" --exact NEWID
```

   The first two must answer `[NEWID] does not exist in the stock rulesmo.ini  (so this ID is free there).` and the same for `artmo.ini`; the third `0 found`. Check every other new name with the third line: the weapon, the warhead, the hit effect. It looks in the rules and the art, stock and ours, for every kind of section.

3. **The model and the icon.** Copy `new-units\build_reaver.py` to `new-units\build_newid.py`. In the copy:
   - change the shapes in `make()`: the front is +X, the unit's left +Y, up +Z (18.3), built to the measured look of the game's tanks (18.2);
   - the fire point is worked out by the validator, from the barrel it finds among the turret's voxels; `t.muzzle` in the script is not read by the build;
   - in the `return dict(...)` at its end change `name='REAV'` to `name='NEWID'`, `title='REAVER'` to the name for the icon in capitals, and `out=os.path.join(HERE, 'REAV')` to `out=os.path.join(HERE, 'NEWID')`.

```powershell
python -I -B "new-units\build_newid.py"
```

   It takes about ten seconds and must print a line that starts with `RESULT: PASS` and one that starts with `PrimaryFireFLH`. It writes the folder `new-units\NEWID`: the four model files, the two icons, `NEWID_sheet.png` (eight directions, at real size and enlarged), two enlarged icons (`NEWID_icon_4x.png`, `NEWID_icon_art_4x.png`), `NEWID_validator.txt` and `NEWID_report.json`. Look at the sheet, and at the lines `barrel tip` and `suggested PrimaryFireFLH` in `NEWID_validator.txt`: the tip must be the weapon's tip. If it is not (rails, fins or an aerial reach further forward), give the value by hand in step 4: `unit_art('NEWID', 'x,y,z')` in place of `unit_art('NEWID', flh_of('NEWID'))`. A later `swap` of the look takes the report's value unless its line ends with `--flh x,y,z` (10.7): give the same value there. To let the owner pick, make two or three such scripts with other shapes and other folders and put their sheets into one picture with `pick_sheet.py` (1.1).

4. **The weapon, the hit and the unit's block.** At the end of `new-units\make_bundles.py`, add a part like this one. The Reaver's part in that file is the same with other numbers.

```python
# ------------------------------------------------------------------------------------------- NEWID
newid_gun = change(stock('WormqueenBolt'), set={'Damage': '85', 'Warhead': 'NEWIDGunWH'},
                   remove=('MinimumRange', 'FireWhileMoving', 'Ammo'))
newid_wh = change(stock('WormqueenBoltWH'), set={'AnimList': 'NEWIDHIT'})
shutil.copyfile(os.path.join(SPRITES, 'tslaexpe.shp'), os.path.join(HERE, 'NEWID', 'newidhit.shp'))
newid_hit = text('NEWIDHIT', stock('TSLAEXPE', art=True))
write_bundle('NEWID', 'Shown Name',
             unit_rules('NEWID', 'Shown Name', 'NEWIDGun', Cost='900', Strength='500')
             + '\n' + text('NEWIDGun', newid_gun) + '\n' + text('NEWIDGunWH', newid_wh) + '\n' + newid_hit,
             unit_art('NEWID', flh_of('NEWID')) + '\n' + newid_hit,
             extra_files=['newidhit.shp'], register={'Animations': ['NEWIDHIT']})
```

   - `change(stock(...))` copies a stock block: `set=` changes values, `remove=` drops lines, `add=[(key, value)]` adds lines, and it stops if a key in `set=` is not in the stock block (13.2). Put in the stock weapon and warhead of step 1 and your numbers. If the stock warhead has `AffectsAllies=no` or the like, put that key into `remove=` (13.10).
   - The hit effect here is a stock picture under a new name (14.3). For a painted one (14.4), write the sprite file into the unit's folder with your own script and leave out the `shutil.copyfile` line; take the section's keys from the stock animation that behaves the same (14.5). The section goes into BOTH texts: the rules text is what the game loads it from (14.1).
   - The light at the hit: `Bright=yes` and `CombatLightSize=` on the warhead; `CLDisableRed=yes`, `CLDisableGreen=yes` and `CLDisableBlue=yes` switch a colour off. For a blue light switch red and green off (50 stock warheads have `CLDisableGreen`, 32 `CLDisableRed`), and take a `CLDisableBlue=yes` of a copied block out (13.3).
   - The colours of a painted effect: `fxkit.py` paints glowing parts along a colour ramp, `glow_stops`. It has `RED` (the default) and `VIOLET`; `nexus-tank\build_effects.py` has a blue-white one, `STAR`, to copy (14.4).
   - A particle system of its own (a trail of sparks along a beam, 20.4) cannot be added by the vehicle installer; use a stock one.
   - `unit_rules` takes the proven unit block `[ARBL]` from the installed `Standard.ini` and changes the name, the weapon and the numbers you give: `Cost`, `Strength`, `Speed`, `Armor`, `ROT`, `TurretROT`, `Soylent`, `Points`, `ThreatPosed` and the like (6.5). `Shown Name` is the name the player sees (1.13). The ranks come with the block (22): `VeteranAbilities=STRONGER`, `EliteAbilities=SELF_HEAL,FIREPOWER,FASTER`, and the same weapon as elite. For an elite weapon of its own, add a second weapon block and give `ElitePrimary=` its name (22.4).

```powershell
python -I -B "new-units\make_bundles.py"
```

   It prints one line per unit, for yours `NEWID: 4 rules sections, 2 art sections, 7 files, registers {"Animations": ["NEWIDHIT"]}`, and writes `rules.ini`, `art.ini` and `bundle.json` into `new-units\NEWID`. It writes the folders of the three installed units again too; they come out the same, byte for byte (checked 25 Nov 2026).

5. **Rehearse** on a copy. The folder in the first line must not exist yet:

```powershell
python -I "arbalest-tank\kit\tests\make_sandbox.py" . "$env:TEMP\mo-sandbox-newtank" --units
python "arbalest-tank\kit\unit_bundle.py" --root "$env:TEMP\mo-sandbox-newtank" --sandbox install "new-units\NEWID"
python -I "arbalest-tank\kit\weapon_audit.py" --game "$env:TEMP\mo-sandbox-newtank\Mental Omega"
```

   The install must end with `Result: 0 FAIL, 0 WARN` and `installed NEWID`. It picks the list numbers itself. The audit must end with `Result: 0 WARN`. If a FAIL or a WARN shows: read it, change the script, run step 4 again, delete the copy and run step 5 again. Delete the copy at the end:

```powershell
Remove-Item -Recurse -Force "$env:TEMP\mo-sandbox-newtank"
```

6. **Install**, with the game and the client closed:

```powershell
python "arbalest-tank\kit\unit_bundle.py" install "new-units\NEWID"
python -I "arbalest-tank\kit\weapon_audit.py"
```

   The same answers as on the copy. If the check fails, the installer puts everything back and says `NOT INSTALLED`.

7. **Tell the owner** what was made, the way back (`remove NEWID`, 1.10) and the questions for the next game (1.11). Record it in sections 11 and 12 and in the change log.

### 1.4 A new flyer

The worked examples are the Seraph, the Tempest and the Nova (`new-aircraft`, 24 Nov 2026): hovering vehicles copied from the stock Invader `[DISK]`, each with a part that turns. They were made together; a fourth has not been made, so the steps that add to the scripts are **[UNTESTED]**. The rest was done (20.6).

1. The job, the template, the ID and the names as in 1.3, steps 1 and 2. A flyer's block is copied from a stock flyer of the same kind (20.1, 20.5).
2. **The shape**: in `new-aircraft\build_flyers.py` add a shape and its name to `MAKERS`. Everything that turns is built on the turning axis; `seat` is the height of the turning part's underside (20.6).
3. **The effects**: in `new-aircraft\build_effects.py` add its animations to `SETS` (14.4). A light on the craft is painted above the middle of its canvas (20.6).
4. **The bundle**: in `new-aircraft\make_bundles.py` add a `unit(...)` block like the three there. Its weapon is made with `made(...)`, which writes every changed line into `departures.txt`. Decide `AA=yes` if it should fight flyers (13.10).
5. Run the three lines of 20.6 (`build_flyers.py`, `build_effects.py`, `make_bundles.py`) and look at the sheets. Then rehearse, install and check as in 1.3, steps 5 and 6, with the folder `new-aircraft\NEWID`. The craft's validator says FAIL because it compares with a tank; that does not count (20.6).
6. The picture for the owner: `new-aircraft\make_preview.py` (20.6, step 7).

### 1.5 A new soldier

The worked example is the Doomsayer (`new-infantry`, 23 Nov 2026): an original jointed figure drawn by script and installed as a pack. A second soldier has not been made, so the copying steps are **[UNTESTED]** (15.7).

1. The job, the template, the ID and the names as in 1.3, steps 1 and 2. The Doomsayer's rules are the Flak Trooper's `[FLAKT]`. A copied stock soldier block keeps two lines that must go: `Image=` (the game would draw the STOCK soldier's sprite, the mistake the owner refused in 15) and `UIName=NAME:...` (the stock name). Take `Image=` out, so that the game draws the unit's own `newid.shp`, and write the name as `UIName=NOSTR:` and `Name=` (1.13). Since 25 Nov 2026 `packs.py verify` fails on an `Image=` that names a stock unit's art. If the template does nothing to some armour (the stock Sniper's warhead has 0% against every vehicle and building), ask the owner before building it whether that stays (1.2, rule 4).
2. **The figure**: copy `new-infantry\doomsayer.py` and `build_figure.py` and change them (15.7, steps 1 and 2). Keep the plan of 301 pictures, so that `Sequence=FlakSequence` fits. The build stops on an empty picture, a picture that touches the edge, a body that moves after death, and too little or too much house colour. The scripts make soldiers of that layout only. A template with another one cannot be drawn yet: the stock Sniper's `SnipedSequence` has 383 pictures, with deploying behind sandbags. Then keep `FlakSequence` and leave out the template's lines for deploying (in the stock Sniper `Deployer=`, `DeployFire=`, `Cursor.Deploy=`, `DeploySound=`, `UndeploySound=`, `VoiceDeploy=`, and `Secondary=` and `EliteSecondary=`, the weapon of the deployed state), and tell the owner that it cannot deploy. **[UNTESTED]**
3. **The icon and the effects**: copy `build_icon.py`, and `build_effects.py` if it has effects of its own (15.7, step 3).
4. **The pack**: copy `new-infantry\make_pack.py`, take out its `REAVFIX` part and change every name (15.7, step 4). Its list numbers: one above the highest of each list that `unit_bundle.py status` prints (1.1). The installer refuses a number that is taken. The rules text in that script goes through Python's `%` formatting (`""" % OWNERS`): write every `%` in it as `%%`, as its `Verses=95%%,...` line does.
5. `FireUp=` and the fire point from `figure_report.json` go into the art text (15.6).
6. **Rehearse** on a copy, with the pack's folder and name:

```powershell
python -I "arbalest-tank\kit\tests\make_sandbox.py" . "$env:TEMP\mo-sandbox-soldier"
python -I "arbalest-tank\kit\packs.py" --root "$env:TEMP\mo-sandbox-soldier" install "new-infantry\NEWID" --dry-run
python -I "arbalest-tank\kit\packs.py" --root "$env:TEMP\mo-sandbox-soldier" install "new-infantry\NEWID"
python -I "arbalest-tank\kit\packs.py" --root "$env:TEMP\mo-sandbox-soldier" verify NEWID
python -I "arbalest-tank\kit\weapon_audit.py" --game "$env:TEMP\mo-sandbox-soldier\Mental Omega"
```

   Run on 25 Nov 2026 with the Doomsayer in place of `NEWID` (after `remove DOOM` on the copy, because it is installed): the dry run printed `pack DOOM "Doomsayer" (mode): 7 list line(s), 7 rules section(s), 4 art section(s), 6 file(s)`, the install and `verify` ended with `checks: 49 passed, 0 FAILED`, the audit with `Result: 0 WARN`. The same day a copy of the pack with `Image=FLAKT` planted in its unit block was refused: `FAIL  [doom] is drawn with its own art (no Image= naming a stock art section)` and `NOT INSTALLED: everything was put back`. **[FILES]** Delete the copy afterwards.
7. **Install**, with the game and the client closed: the second, third and fourth line without `--root "$env:TEMP\mo-sandbox-soldier"`, then `weapon_audit.py` without `--game`. `mo_tool.py check` is made for vehicles and gives false FAILs on a soldier (section 0).

### 1.6 A new building on a map

The worked example is the Black Site on (6) Kalifornia Crisis (`new-buildings`): four buildings on 23 Nov 2026, and a fifth, the Vessel, on 25 Nov 2026 by the steps below. Section 16 has the details, 17 the moving parts.

1. The job and the template: the stock building that does the same (a power plant, a bank, a defence, a landmark that soldiers can garrison; 16.3, 16.12). ID and names as in 1.3, step 2. Buildings that let their owner see: the stock Sensor Tower `[NASCOM]` (`Sight=15`, it sees 15 cells round itself; with `SensorArray=yes` and `SensorsSight=9`), `[CADOME]`, "Radar Dome Large" (`Radar=yes`: its owner gets the radar map), and `[CACOMN]`, the "Tech Satellite Hack Center" (`SpySat=yes`: the whole map; the Skywatch Array is a copy of it). **[FILES]** Ask the owner which is meant (1.1, step 3).
2. A free, level lot (16.11, step 1).
3. **The build script**: copy `build_spire.py` (2x2) or one of the 3x3 scripts and change it (17.3), measured against the game's own buildings (16.6).
4. **`blacksite.py`**: its line in `BUILDINGS`, its rules, its art numbers, its weapon (16.11, step 3). **`make_preview.py`**: its lines in `ROLE` and `MOVES`, and the number of buildings in its title line.
5. Copy `new-buildings\SITE` to the next free `round` folder: the next number that no folder in `new-buildings` has. 16.12 keeps `round6` for the Vessel's new model if that comes first; whichever change comes second takes the number after it.
6. Build it (its script, 16.10), then make the map's two preview pictures again, then the pack:

```powershell
python -I -B "new-buildings\site_preview.py" "$env:TEMP\mo-site-preview"
python -I -B "new-buildings\make_pack.py"
```

   The first ends with `wrote SITE-preview and PREVIEW-CHECK.png (left stock, right with the buildings: lobby, lobby x4, loading x4)`; look at `new-buildings\PREVIEW-CHECK.png` (16.13). The second refuses pictures that were made from other sprites or places.
7. Rehearse and check the reach as in 16.10: the install on the copy ends with `0 FAILED`, `check_range.py` with `Result: 0 FAIL`. Then look at it on its lot, on the copy, before the real install:

```powershell
python -I -B "new-buildings\render_site.py" "$env:TEMP\mo-site-check" --installed --game "$env:TEMP\mo-sandbox\Mental Omega"
```

   It draws the map of the copy, with the new building, and writes `new-buildings\SITE.png` (16.7). Then install for real (16.10), and run `packs.py verify SITE` and `weapon_audit.py`.
8. A landmark that soldiers can garrison: the rules of a stock one (`[CASEAT01]`, the Space Needle), ten firing points, and a third picture that shows it occupied (16.12).

### 1.7 A new attack for a unit that is installed

Done three times: the Nexus's second and third shot (21.3) and the Tempest's missile swarm (20.5).

1. If the owner wants something "like" a real or a science-fiction thing, look it up first and save what you found (1.1, step 3).
2. Choose the stock weapon that does the same job, and its projectile and warhead, or those of other stock weapons that each do their part well (13.2). The Nexus's orb has the Piranha's weapon, the Salamander's flight and the Ballista fragment's warhead.
3. In the unit's bundle script (the table in 1.10 says which), copy each block from its stock template. `new-units\make_bundles.py` does it with `change(...)`; `nexus-tank\make_bundle.py` and `new-aircraft\make_bundles.py` with `made(...)`, which also records every changed line in `departures.txt`. Both stop on a key the stock block lacks. The last two also stop on what must never get in, a line that spares a side and a key that bursts the shot in the air (21.4, 20.5); for a tank of `new-units` look for those with `weapon_audit.py` (a `WARN`, and its `shot:` column).
4. Paint its effects (14.4), and look at the attack in the moving picture that the unit's `make_preview.py` writes (`attack.gif`).
5. Copy the installed folder to a `round` folder; run the build lines; rehearse `remove` and `install` on a copy; then do it for real with the game closed. The lines for the Nexus are in 21.4, those for the Tempest in 20.7; for another unit put in its ID and folder. The Arbalest is not handled by the installer (1.10).
6. Run `weapon_audit.py` and the check. Tell the owner the way back (the `round` folder) and that saved games from before may not load.

### 1.8 A new effect

1. Where it plays decides where it is named (14.2): at the muzzle, on the flying shot, behind the shot, where the shot lands, on a building.
2. Its picture: a stock picture under a new name (14.3) or a painted one (`fxkit.py`, 14.4).
3. Its section's keys come from the stock animation that behaves the same (14.5).
4. It is listed, and gets its section in the same file as what uses it; in a vehicle bundle that means `register` and both texts (14.1, 1.3 step 4).
5. Look at it as a sheet or a moving picture (`shpkit.py sheet` or `gif`, 14.4).
6. It goes in with the unit or the pack that uses it.

### 1.9 Putting right a fault the owner reports

1. Ask what the files cannot tell: which unit, a forced attack or not, which game (its time), and a screenshot if there is none. The game's log does not name units. Keep the owner's words and screenshots: quote them, and save the screenshot in the project (`nexus-tank\evidence-2026-11-25`).
2. Measure what the screenshot shows, in pixels (16.8: a bolt 30 pixels too high; 13.5: a hit 10.12 cells out with a ring of 8.47).
3. Read the files: the unit's blocks beside its stock template, key by key. Run `weapon_audit.py`, the check and `packs.py verify`; their `0 WARN` and `0 FAILED` do not rule out a 0% against the victims' armour or a shot that bursts early: read the audit's `does nothing to:` and `shot:` columns. Section 8 has a table of symptoms and where to look.
4. Narrow it down: give the hit a stock picture under the same name (14.3) and rebuild. If the stock picture shows, the painted sprite is at fault; if not, the way it is named or listed.
5. If the files cannot explain it, read the game's program (1.12).
6. Name the cause before anything is changed; then change one thing.
7. Copy the installed folder to a `round` folder (for a tank of `new-units`: `new-units\round2\NEWID`, because `round1` there holds the first looks of the three units; elsewhere the next number that folder has not used), rebuild, rehearse, reinstall, check.
8. Add a row to section 19, and a check to a tool where one can catch it the next time. The check warns since 24 Nov 2026 about an animation without its section, and since 25 Nov 2026 about an unlisted piece weapon and a line that spares a side.
9. Tell the owner plainly what it was, whose mistake it was, what changed, how to test it, and the way back.

The faults found so far:

| What was seen | The cause | Read |
|---|---|---|
| The Nexus's shot burst in the air, far from the target | its gun was copied from an artillery piece | 21.1 |
| A forced attack did no damage to the owner's own units | `AffectsAllies=no` in the warheads | 13.10 |
| The Stormspire hit beyond its ring | its projectile had the high-ground bonus | 13.5 |
| Its bolt started above the ball | a building's fire point counts from the middle of the canvas | 16.8 |
| The buildings did not move | only their lamps were animated | 17 |
| The map's pictures lacked the buildings | the pack left them as they were | 16.13 |
| The Vessel was not like the real one | it was modelled without photographs | 16.12 |
| The Doomsayer was a stock soldier in other colours | a recoloured stock sprite | 15 |
| (found by reading, not by the owner) the Reaver's burst was most likely never drawn | an animation without its section in the mode file | 14.1 |

### 1.10 Changing what is installed

| What | How | Read |
|---|---|---|
| A new look for a vehicle (model, icon, fire point) | `unit_bundle.py swap ID folder`; going back is the same line with the folder it kept in `backups` | 10.7, 18.3 |
| Other rules or another weapon for a vehicle | rebuild its folder, then `unit_bundle.py remove ID` and `install` with the folder | 21.5 |
| A pack: a soldier, the buildings | rebuild, then `packs.py remove NAME` and `install` with the folder | 16.10 |
| An older version back | install its `round` folder the same way | 21.5, 16.12, 16.13 |
| Out altogether | `unit_bundle.py remove ID` or `packs.py remove NAME` | 10.7, 10.8 |

Which script makes each unit, and which way it goes in and out:

| Unit | Made by | In, out, a new look |
|---|---|---|
| Arbalest `ARBL` | by hand (section 4); its designs in `arbalest-tank` | Its rules by hand in `Standard.ini` (section 4). A new look with `arbalest-tank\install_arbalest_option.py`, which changes its six files and its fire point. Out only by hand (10.3); the vehicle installer cannot remove it |
| Reaver `REAV`, Cerberus `CERB`, Moloch `MLCH` | `new-units\build_*.py` and `new-units\make_bundles.py` | `unit_bundle.py` (`swap` for a look) |
| Seraph `SRPH`, Tempest `TMPS`, Nova `NOVA` | `new-aircraft\build_flyers.py`, `build_effects.py`, `make_bundles.py` | `unit_bundle.py` |
| Nexus `NEXS` | `nexus-tank\build_nexus.py`, `build_effects.py`, `make_bundle.py` | `unit_bundle.py` |
| Doomsayer `DOOM`, and `REAVFIX` | the scripts in `new-infantry`, then `make_pack.py` | `packs.py` |
| The five buildings, `SITE` | the scripts in `new-buildings`, `site_preview.py`, `make_pack.py` | `packs.py` |

`new-units\make_bundles.py` reads the installed `[ARBL]` block as the template for every tank's rules, on every run. If the Arbalest's block is ever changed by hand, the next run gives the three tanks, and a new one, the changed lines as well. Before installing anything from such a run, check that the `rules.ini` of the three installed tanks did not change (`Get-FileHash` before and after), or write the old values into their `unit_rules(...)` lines.

After a reinstall the list numbers change, so saved games from before may not load. A changed map file is one more reason not to play online (10.6).

### 1.11 After the owner's game

1. Read the report. Record as **[CONFIRMED]** only what the owner said or showed, with the date. "Perfect" or "everything works" is one answer for everything: it confirms nothing that was not named, and it does not answer an open question (a pick, a yes or no).
2. Read the game's log, and see which map and mode it was. The newest game's log is `Mental Omega\debug\debug.log`; older ones carry their date and time in the name.

```powershell
Select-String -Path "Mental Omega\debug\debug.log" -Pattern "Failed to parse","Game loop finished"
Select-String -Path "Mental Omega\spawn.ini" -Pattern "UIMapName","UIGameMode"
```

   A good game prints `Game loop finished. Average FPS = ...` and no line with `Failed to parse`; the second line prints the map and the mode. Every game here also logs about 400 developer warnings (`Pointer 00000000 declared change ...`); they were there before anything of ours and mean nothing.
3. Record: section 11 (the state, with labels), section 12 (answered questions, new ones), the change log, and the assistant's own notes if it keeps any.
4. The questions for a new unit's first game, to adapt:
   - Is its icon in the tab, and can it be built where it should be?
   - Does it look right among the game's own units: the turret on the hull, the shot leaving from the weapon's tip?
   - Does the weapon hit what it is aimed at? Do its hit effect and its sound show?
   - With Ctrl held, on one of your own soldiers, tanks and flyers and on a neutral building: does each take damage (13.10)?
   - After enough kills (22.3): the rank badge, the flash, the sound?

### 1.12 How things were found out, and how to find out the next thing

Every fact in this guide came from one of these. Try them in this order.

1. **The stock files**: `stock-reference\rulesmo.ini`, `artmo.ini` and `soundmo.ini` (3.3), and `mo_tool.py section`. To learn how the game's own units do a thing, count them with a short Python script: "how many stock vehicles fire another weapon as elite" (22.4), "which stock warheads spare a side" (13.10).
2. **The stock pictures and models**: `mo_tool.py extract` takes a file out of the archives (3.2); `shpkit.py` draws a sprite (14.4); `effects_sheet.py` draws stock animations side by side (14.3); the survey of all stock tank models is in `arbalest-tank\kit\research\forge-notes` (18.2).
3. **The game's program**, when the files cannot tell what the game does with a key. The tools are in `arbalest-tank\kit\research\probe` and need only Python:

```powershell
python -I "arbalest-tank\kit\research\probe\b3_xref.py" "Mental Omega\Ares.dll" str:Promote.EliteType
python -I "arbalest-tank\kit\research\probe\b2_dis.py" "Mental Omega\Ares.dll" 1003F14E 4
```

   The first finds the code that reads a key: `"Promote.EliteType" at file 0x9D0B4 = VA 0x1009DCB4: 1 code refs: 0x1003F14F(0068)`. The second prints the instructions at an address. Follow where the value read is stored, then search the code for that place to find the routine that uses it; 22.6 was found that way. `funcstart.py` finds where a routine starts, and `pelib.py` reads the program files. Save what you read as a `dis_*.txt` file in that folder and name its addresses in this guide. `gamemd.exe` is the game; `Ares.dll` is the extension that adds most keys with a dot in their name.
   A key that the stock rules use proves only that the game accepts the name. Before you tell the owner that an effect exists, find the code that does it, or a stock unit that visibly does it (20.4: `IsBigLaser=` is read and never used).
4. **The client's map renderer**, for anything on a map, on copies only (16.7).
5. **The game's log** after each game (1.11).
6. **The owner's screenshots**, measured in pixels.
7. **The web**, when the owner asks for something real or asks to look something up. Save the sources in the project folder.

### 1.13 Names, numbers and files: how each thing is known

| What | How it is named | Example |
|---|---|---|
| A unit's ID | capital letters and digits, free in the stock rules, the stock art and our files (1.3, step 2); all of ours have four | `NEXS` |
| The name the player sees | `UIName=NOSTR:` followed by the text, and `Name=` with the same text, in the rules block. The extension shows the text after `NOSTR:` as it is; no stock unit uses it, and whether the name shows in the game was not reported. **[UNTESTED]** The icon has the name drawn into it as well (18.4) | `UIName=NOSTR:Nexus Tank` |
| A vehicle's files | `NEWID.vxl`, `NEWID.hva`, `NEWIDTUR.vxl`, `NEWIDTUR.hva` (charge stages `NEWIDTUR1` and on, 21.3); the icons `newidicon.pcx` and `newiduico.pcx` | `nexsicon.pcx` |
| An animation | its name in capitals; its sprite file the same name in small letters with `.shp` | `NEXSSPL`, `nexsspl.shp` |
| A building | its ID in the map; its sprite files `cg` and three letters, with `_a` for the main animation and `_l` for the lights (16.4) | `CAVESL`, `cgvesl.shp` |
| A soldier | its ID; one sprite file with all its pictures (15.2) | `DOOM`, `doom.shp` |
| A weapon, a projectile, a warhead | a name with capitals inside, free in the stock rules | `NexusStarburst`, `NexusStarburstP`, `NexusStarburstWH` |
| A list line | a number, `=` and the name. The numbers in use: `unit_bundle.py status` (1.1). The vehicle installer picks them; a pack names its own | `7420=NEXS` |
| Where it stands | the rules of a vehicle and a soldier in `INI\Map Code\Standard.ini`, those of a building in the map file; all art at the end of `Mental Omega\artmo.ini`; the files loose in `Mental Omega` | |
| What an installer wrote | the lines between `; >>> UNIT ID` and `; <<< UNIT ID`, or `; >>> PACK NAME` and `; <<< PACK NAME`. Never edit inside them by hand; use the installers | |
| Its record | `backups\unit-bundles\ID`, `backups\packs\NAME` | |

To find a stock unit by the name the player sees, use `find_unit.py` (1.3, step 1); to see whether a name is taken anywhere, `find_unit.py --exact NAME`; to find units by a key of their weapon, `find_unit.py --key Primary=Rail` (1.3, step 1).

### 1.14 The first way, by hand (22 Nov 2026)

This is how the Arbalest went in, before the installers existed. The recipes above replace it for new work. Sections 4 and 5 are kept because they explain every file and every line.

There are two ways to get a unit in. Each was seen working once.

| | Route B: brand-new unit | Route A: take over a stock unit |
|---|---|---|
| What you get | A new unit with its own ID, model and icon, next to the stock ones | A stock unit is shown with your model and gets your stats and weapon |
| Name and icon | Your own icon: **[CONFIRMED]** 22 Nov 2026. Your own name: **[UNTESTED]** | Stay the stock unit's. **[FILES]** Not reported from the game. |
| Who can build it | The countries you list. Seen only with all twelve listed, playing United States. | Whoever could build the stock unit. **[FILES]** Only United States was played. |
| Files you touch | `INI\Map Code\Standard.ini`, `artmo.ini`, four model files, two icon files | `INI\Map Code\Standard.ini`, four model files |
| Status | **[CONFIRMED]** 22 Nov 2026: Arbalest Tank, "icon and model works" | **[CONFIRMED]** 2 April 2026: the Nexus model on the Bulldog loaded and moved, and the laser was reported as good |
| Where | Section 4 | Section 5 |

Route B is section 4. Route A is section 5.

Route B in short. The numbers and titles are the same as the steps in section 4:

0. Back up.
1. Pick an ID that is not used yet.
2. Model files: put `NEWID.vxl`, `NEWID.hva`, `NEWIDTUR.vxl`, `NEWIDTUR.hva` in the `Mental Omega` folder.
3. Icon files: put two icon files (60x48 PCX) in the `Mental Omega` folder.
4. The art section: add `[NEWID]` at the very end of `Mental Omega\artmo.ini`.
5. The rules: in `Mental Omega\INI\Map Code\Standard.ini`, add one line under `[VehicleTypes]` and a rules section `[NEWID]`.
6. Check before you start the game.
7. Test in the game: a **Standard** skirmish.
8. Remove one unit again. Only if you want it gone.

After it works, change one thing at a time. The part "After it works" at the end of section 4 gives the order.

---

## 2. How the game loads things

Most of the wasted time in 2025 came from editing files the game does not use. This is what it does use.

```
expandmo99.mix ──► rulesmo.ini  (all stock rules)        you never edit the archive
               └─► artmo.ini    (all stock art)

Mental Omega\artmo.ini  (loose) ──► read by the game (seen 22 Nov 2026)
                                    keep the full stock text in it + your sections

INI\Map Code\Standard.ini ──► the client merges it into spawnmap.ini
                              when you start a game in Standard mode
                              (this is where rules for your units go)

Mental Omega\*.vxl *.hva *.pcx  (loose) ──► found by name when a unit asks for them
```

- The game's rules and art are plain text inside `expandmo99.mix`, as `rulesmo.ini` and `artmo.ini`. **[FILES]**
- `cncnet5mo.dll` contains the file names `RULESMO.INI`, `ARTMO.INI`, `SOUNDMO.INI` and `EXPANDMO%02d.MIX`. The loose `Mental Omega\rulesmd.ini` is a vanilla rules file with the vanilla country names, while every engine log lists Mental Omega's countries. So the game does not take its rules from that file. **[FILES]** That the game does not read the loose `Mental Omega\artmd.ini` either is reasoned from the file name `ARTMO.INI`. It was not tested on its own. **[UNTESTED]** Do not edit `Mental Omega\rulesmd.ini` or `Mental Omega\artmd.ini`: the old "Nexus Devastator" blocks in them are not expected to do anything.
- Rules reach the game through "map code". When you start a game, the client merges the mode file of the selected game mode into the scenario file it writes (`Mental Omega\spawnmap.ini`). For a Standard game that is `INI\Map Code\Standard.ini`. Of the 25 mode files, only the selected mode's is used. The client also adds code from the game-option files in `INI\Game Options`, so `spawnmap.ini` holds more sections than the map and the mode file together. **[FILES]**
- Put art keys in the art file, not in a rules block. The stock files never do otherwise: `rulesmo.ini` has no `Voxel=`, `Remapable=`, `CameoPCX=`, `PrimaryFireFLH=` or `TurretOffset=` line at all, and `artmo.ini` has more than 2,000 of them. **[FILES]** That an art key in a rules block does nothing, and that art cannot be supplied through map code, fits the 22 Nov result but was not tested on its own. **[UNTESTED]** The November 2025 new-unit attempts had their art keys in the rules block. Their model files also had normals mode 0 (read on 2 April 2026), so which fault stopped them is **[UNTESTED]**.
- A loose `artmo.ini` in the game folder is read by the game. The proof: the Arbalest's icon and model showed (**[CONFIRMED]** 22 Nov 2026), and its art section exists nowhere else (**[FILES]**). That it is read *instead of* the copy in the archive, and not in addition to it, was not tested, because the loose file contains the whole stock text. **[UNTESTED]** So never cut the stock text out of it.
- Loose model files (`.vxl`, `.hva`) and loose icon files (`.pcx`) are found by name. The proof: the Nexus model showed (**[CONFIRMED]** 2 April 2026), the Arbalest's icon and model showed (**[CONFIRMED]** 22 Nov 2026), and the `FTNKNEXUS` and `ARBL` files are in no archive (**[FILES]**).
- No archive needs to be built or changed for any of this. See section 9 before you touch one.

---

## 3. One-time setup

### 3.1 Where to run commands

1. Open the project folder in File Explorer. It is the folder that contains both `Mental Omega` and `MentalOmega-Modding-Guide`.
2. Click the address bar at the top of the window, type `powershell` and press Enter. A PowerShell window opens.
3. Type this line in the PowerShell window and press Enter:

```powershell
Test-Path "Mental Omega", "MentalOmega-Modding-Guide"
```

It must print `True` twice. If it prints `False`, the window is in the wrong folder: close it and start again at 1.

4. Check that Python is there:

```powershell
python --version
```

It must print a line that starts with `Python 3`. On 22 Nov 2026 it printed `Python 3.14.0`. Nothing else has to be installed.

Rules for every command in this guide:

- Type it in a PowerShell window that was opened this way. For every new window, do 1 to 3 again.
- You may copy a command from this guide and paste it into the window (right mouse button, or Ctrl+V). Then press Enter.
- Some commands are a block of several lines. Paste the whole block into the same window and press Enter after the last line. If Windows warns that you are pasting several lines, choose to paste anyway.
- A command that shows `NEWID` or `newid` must never run the way it is printed. A pasted block can start to run at once, before you can change it. So do this with every such command: paste it into an empty Notepad window first. There, change every `NEWID` to your ID in capital letters and every `newid` to your ID in small letters, by hand. Then copy the lines from Notepad and paste them into the PowerShell window. If a command ran with the letters `NEWID` still in it, its answer says nothing about your unit: run it again with your ID. If it made files named `NEWID...` or `newid...` in `Mental Omega`, delete those files in File Explorer. In section 7, a Route A reader changes `NEWID` to the `NAME` of the model in the same way.
- If a command answers `can't open file` together with `mo_tool.py`, or `Cannot find path`, the window may be in the wrong folder. Type the `Test-Path` line again. If it does not print `True` twice, do 1 to 3 again.

### 3.2 The helper tool

`MentalOmega-Modding-Guide\scripts\mo_tool.py` does the jobs that are awkward by hand. It never changes the game's archives.

Every tool command starts with `python "MentalOmega-Modding-Guide\scripts\mo_tool.py"`, then a space, then one of these endings:

| The end of the command | What it does |
|---|---|
| `section ETNK` | Prints the stock rules section `[ETNK]`. Any stock section name works in place of `ETNK`. Add `--art` at the end for the art file, `--sound` for the sound file. |
| `stock "stock-reference"` | Copies `rulesmo.ini`, `artmo.ini` and `soundmo.ini` out of the archives into the folder `stock-reference`, so you can read and search them. |
| `extract "stock-reference" htnkicon.pcx` | Copies a file out of the four `expandmo` archives by name. The 529 icon files named in the stock art file, and the hull and turret models of every stock voxel vehicle, are in them (checked 22 Nov 2026). A file that is not in those four archives, such as a base-game file, is answered with `MISSING`. |
| `init-art` | Creates the loose `Mental Omega\artmo.ini` from the stock art file. Refuses if one exists. |
| `check NEWID` | The check before you start the game. Only for a brand-new unit (Route B): registration, rules, art section, icons, model files. If the unit has a weapon of your own, that weapon block and its warhead are checked too. It stops when the ID is a stock unit's. It is made for vehicles: for an infantry unit or a building it reports false FAILs (section 0 says which check fits). Since 24 Nov 2026 it warns when an animation that `Standard.ini` lists has no section of its own there (14.1). Since 25 Nov 2026 it also checks every turret file of a charge turret (21.3), and it warns when a weapon that only a projectile names (`ShrapnelWeapon=`, `AirburstWeapon=`) has no line under `[WeaponTypes]` (13.8). |
| `lint-weapon NexusStarburst` | Checks one weapon block of your own in `Standard.ini` without a unit: its projectile, its warhead, its sounds and its animations must exist. Use it for a take-over block (Route A), where `check` stops. Added 23 Nov 2026. It reads `Standard.ini` only: a weapon that stands in a map file is checked by `packs.py verify`. |
| `set-normals "Mental Omega\NEWID.vxl"` | Sets the normals-mode byte of a model file to 4. Saves a backup next to the file first: `.bak`, or `.bak2`, `.bak3` ... if one already exists. Plain `.bak` is the oldest. |
| `rotate-hva "Mental Omega\NEWID.hva"` | Overwrites the direction stored in an HVA file with one fixed quarter turn (90 degrees). With `--cw` at the end it writes the opposite quarter turn. Saves a backup first, named the same way. |

The left column is only the end of the command. Typed alone it fails. So `section ETNK` means this full line:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" section ETNK
```

It prints the stock section of the Bulldog: the header `[ETNK]` and 68 lines under it.

And `check ARBL` means this full line:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" check ARBL
```

It checks the Arbalest. Its output must end with these three lines:

```
Result: 0 FAIL, 0 WARN
Nothing blocking was found. Test in a Standard-mode skirmish.
Not checked: section names inside model files, and rules lines such as Locomotor=, Armor= and sounds.
```

From here on this guide prints every command as the full line.

The older scripts in `scripts\` are not safe to use. Section 9 says which and why.

### 3.3 Stock files to read

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" stock "stock-reference"
```

This writes the three stock text files into the folder `stock-reference` in the project folder. It prints one line per file:

- `OK ...` means the file was written.
- `SKIPPED ... (already exists in the folder; add --force to replace it)` means the file was already there. That is fine. In your project folder the three files are there since 22 Nov 2026, so you will see three `SKIPPED` lines.

Open `stock-reference\rulesmo.ini` in an editor to look up any stock unit, weapon or building. The game does not use this folder: changing these copies changes nothing in the game.

Only if the mod is ever updated, write the files again. That is the same command with `--force` at the end:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" stock "stock-reference" --force
```

It prints three `OK` lines.

The command puts `stock-reference` next to the guide folder, not inside it. Leave it there and never move it into `MentalOmega-Modding-Guide`. Those are the mod's own files; do not share them.

### 3.4 The loose art file

`Mental Omega\artmo.ini` already exists (created 22 Nov 2026). Leave it, and go on to 3.5.

Do the four steps below only in one of these two cases:

- the file `Mental Omega\artmo.ini` is missing;
- the check (section 4, step 6) says `the first 898681 bytes are not the stock art file`.

1. If the file is still there, move it out of the game folder. Do not delete it: it holds your own sections.

```powershell
New-Item -ItemType Directory -Force "backups" | Out-Null
Move-Item "Mental Omega\artmo.ini" "backups\artmo-moved-away-$(Get-Date -Format 'yyyy-MM-dd_HHmmss').ini"
```

The two lines print nothing. The file is now in `backups`, with the date and time in its name.

2. Create a fresh file:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" init-art
```

It prints two lines. The first must start with `Created` and end with `898681 stock bytes plus the "USER ADDITIONS" marker.` If it prints `NOTHING DONE` instead, the old file is still in the game folder: do 1 first.

3. The fresh file ends with a row of `;` signs and two comment lines. The first comment line starts with `; USER ADDITIONS`. Your own art sections are not in the fresh file. Put them back at its very end, below those lines:
   - Open the moved file in your editor, or the newest `artmo.ini` in a `backups` folder that still held all your units.
   - Go to its end (Ctrl+End). Go up to the comment line that contains `USER ADDITION`. One more comment line follows it. Select everything from the first line that starts with `[` below these two lines down to the end of the file. Copy it.
   - Open the fresh `Mental Omega\artmo.ini`, press Ctrl+End, paste, and save.
   - If you have no such file, type the sections again. The Arbalest's section is printed in section 4, step 4.
4. Run the check for every unit you have. For the Arbalest:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" check ARBL
```

Its last three lines must be the ones shown in 3.2, starting with `Result: 0 FAIL, 0 WARN`. A line `FAIL  no [ARBL] section in artmo.ini` means that 3 is not done yet.

### 3.5 Back up before every change

When to back up:

- at the start of a route. That is step 0 in section 4 and in section 5;
- later, before every single change to a unit that works ("After it works" in section 4).

Do not back up in the middle of a route. Step 8 of section 4 and step 7 of section 5 need the step 0 backup to be the last one.

These six lines copy the two INI files into a new folder inside `backups`. Run them once now, as part of the setup. That gives you the first backup that the restore lines below can read.

```powershell
$stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
New-Item -ItemType Directory -Force "backups\$stamp" | Out-Null
Copy-Item "Mental Omega\INI\Map Code\Standard.ini" "backups\$stamp\"
Copy-Item "Mental Omega\artmo.ini" "backups\$stamp\"
Set-Content "backups\last-backup.txt" $stamp
Get-ChildItem "backups\$stamp"
```

- Paste all six lines into the same PowerShell window.
- Only the last line prints something. It must list two files: `artmo.ini` and `Standard.ini`.
- The folder is named after the date and the time, with seconds, for example `2026-11-22_203315`.
- The fifth line writes that folder name into the small text file `backups\last-backup.txt`. The restore lines below read it there, so you never have to type a folder name.

To see which backup is the last one:

```powershell
Get-Content "backups\last-backup.txt"
```

It prints the folder name of the last backup, that is, its date and time.

To go back to the last backup, close the game and the client. Close both INI files in your editor too, and open them again only after the restore: an editor that still shows the old text would write it back when you save. Then type these three lines:

```powershell
$stamp = Get-Content "backups\last-backup.txt"
Copy-Item "backups\$stamp\Standard.ini" "Mental Omega\INI\Map Code\Standard.ini"
Copy-Item "backups\$stamp\artmo.ini" "Mental Omega\artmo.ini"
```

- They print nothing.
- If the first line prints a red `Cannot find path` error, there is no backup yet that was made with the six lines. Then nothing is copied.
- Both files are then as they were when that backup was made. Everything you changed in the two files after it is gone.
- A backup holds only the two INI files. Model files and icon files are not in it.

To go back to an older backup, use File Explorer, not a command: open `backups`, open the folder with the date and time you want, and copy its `Standard.ini` into `Mental Omega\INI\Map Code` and its `artmo.ini` into `Mental Omega`. Let Windows replace the files there.

The folder `backups\2026-11-22-arbalest` is different. It was not made with these six lines. It holds `Standard.ini.before-arbalest` and no `artmo.ini` (10.3). The folder `backups\2026-11-22-old-writeups` is different too. It holds the old guide documents as they were before they got their notes, and no INI file. So is `backups\2026-11-22_224520-arbalest-before-new-model`. It holds the Arbalest's files as they were before it got its own model, and no `Standard.ini` (10.2).

### 3.6 Editing the two INI files

The two files are `Mental Omega\INI\Map Code\Standard.ini` and `Mental Omega\artmo.ini`.

- Close the game and the client before you edit. Start the client again afterwards. The working test of 22 Nov 2026 was done in that order. Whether the client notices an edit that is made while it is open is **[UNTESTED]**.
- Use VS Code or Notepad. Nobody has yet compared a file saved by either editor with the original byte for byte. **[UNTESTED]** The check (section 4, step 6) reports wrong line endings and a byte-order mark. So after every save, run the check before you start the game.
- Both files use Windows line endings (CRLF) and contain only plain English characters. **[FILES]** Do not convert them. In VS Code the status bar at the bottom must keep showing `CRLF`.
- Type only English letters, digits and ordinary punctuation, also after `UIName=NOSTR:`. The stock rules file and your two files contain no other characters. **[FILES]** Names in other alphabets are **[UNTESTED]**.
- In `artmo.ini`, never change or delete anything above the comment line that contains `USER ADDITION`, near the end of the file. That part must stay identical to the stock file.
- A line that starts with `;` is a comment.
- Empty lines between sections are optional. The working files have both forms, and the check passes either way. Press Enter after the last line you add.
- Find a place in a file by searching for its header (Ctrl+F, for example `[VehicleTypes]`), not by its line number. The line numbers in this guide are those of 22 Nov 2026. They shift as soon as a line is added or removed.
- Never add a section whose header is already in the file. Change the section that is there.

---

## 4. Route B: add a brand-new unit, step by step

**To make a new unit now, follow the playbook: 1.3 for a tank, 1.4 for a flyer, 1.5 for a soldier.** This section is the first way, by hand, as the Arbalest went in on 22 Nov 2026. It is kept because it explains every file and every line that the installers write.

The worked example is the Arbalest Tank (ID `ARBL`), added on 22 Nov 2026. Its icon and its model were seen in the game that day. **[CONFIRMED]**

In this section `NEWID` and `newid` stand for your own unit ID. They are explained in "Words used in this guide" at the top. Never type the letters N-E-W-I-D.

Do the steps in order. Close the game and the client before you begin.

The steps use the Arbalest's two INI sections and the Nexus model files as the known-good starting point. They assume that the Arbalest is still installed, as it is on 22 Nov 2026 (section 11). If you have removed it, read 10.3 first.

### Step 0: back up

```powershell
$stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
New-Item -ItemType Directory -Force "backups\$stamp" | Out-Null
Copy-Item "Mental Omega\INI\Map Code\Standard.ini" "backups\$stamp\"
Copy-Item "Mental Omega\artmo.ini" "backups\$stamp\"
Set-Content "backups\last-backup.txt" $stamp
Get-ChildItem "backups\$stamp"
```

Paste all six lines into the same PowerShell window. The last line must list two files: `artmo.ini` and `Standard.ini`. What the lines do is explained in 3.5.

Do not run these six lines again until the unit works. Step 8 can then take both files back to this moment.

### Step 1: pick an ID

Use exactly 4 characters: capital letters A to Z and digits 0 to 9, no spaces. Example: `MYTK`. The stock IDs `ETNK` and `HTNK` look like that, and so does your own `ARBL`. 4 is the most common length of a stock vehicle ID (163 of 364), and then all your file names are as long as the Arbalest's, which work. **[FILES]** Another length is **[UNTESTED]** for a new unit.

Check that the stock game does not use the ID:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" section NEWID
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" section NEWID --art
```

Each line must print one line that starts with your own ID in square brackets, contains `does not exist` and ends with `(so this ID is free there).` If the line starts with `[NEWID]`, the command ran with the stand-in name: run it again with your ID (3.1). If one of them prints a section instead, the stock game uses the ID. Choose another one.

These two commands read only the stock files. They say `does not exist` for `ARBL` too, although `ARBL` is taken by you. So also search your own two files:

```powershell
Select-String -Path "Mental Omega\INI\Map Code\Standard.ini","Mental Omega\artmo.ini" -Pattern "NEWID" -SimpleMatch
```

It must print nothing. If it prints any line, the ID, or a longer word that contains it, is already in one of the two files. Choose another ID and do step 1 again.

Capital and small letters: the check (step 6) accepts any mix of them. That was tried with the tool, not in the game. Whether the game minds is **[UNTESTED]**. So keep the spelling of the Arbalest's files, which work: the ID in capitals inside the INI files, the model files in capitals (`NEWID.vxl`), the icon files in small letters (`newidicon.pcx`).

### Step 2: model files

Four files go in the `Mental Omega` folder:

| File | Part |
|---|---|
| `NEWID.vxl` + `NEWID.hva` | Hull |
| `NEWIDTUR.vxl` + `NEWIDTUR.hva` | Turret |

For a first test, use a model that is known to work, so that a failure can only be the configuration. These four lines copy the Nexus model files. That was the model on the Bulldog until 24 Nov 2026 (section 5), and it is the shape of the Nexus tank now (section 21; its colours differ since 25 Nov 2026); the four files are still in the game folder. It was seen in the game on 2 April 2026, and again on 22 Nov 2026, when the Arbalest wore a copy of it. **[CONFIRMED]**

```powershell
Copy-Item "Mental Omega\FTNKNEXUS.vxl" "Mental Omega\NEWID.vxl"
Copy-Item "Mental Omega\FTNKNEXUS.hva" "Mental Omega\NEWID.hva"
Copy-Item "Mental Omega\FTNKNEXUSTUR.vxl" "Mental Omega\NEWIDTUR.vxl"
Copy-Item "Mental Omega\FTNKNEXUSTUR.hva" "Mental Omega\NEWIDTUR.hva"
```

They print nothing. Keep to these four files for a first test. The Arbalest has a model of its own (section 11), but it goes with another `PrimaryFireFLH=` value than the one in step 4. Put in your real model later, once the unit shows up (see "After it works"). What a model file must look like is in section 7.

### Step 3: icon files

Two files go in the `Mental Omega` folder: the icon and the alternate icon. Stock icons are 60x48 pixels, 8-bit paletted PCX (version 5, RLE, one plane). **[FILES]**

For a first test, copy a stock icon. This line takes the Rhino's two icons out of the archives:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" extract "stock-reference" htnkicon.pcx htnkuico.pcx
```

It prints one line per file. `OK ...` means the file was written into `stock-reference`. `SKIPPED ... (already exists in the folder; add --force to replace it)` means it was already there. That is fine; in your project folder both files are there since 22 Nov 2026. Go on with the two copy lines:

```powershell
Copy-Item "stock-reference\htnkicon.pcx" "Mental Omega\newidicon.pcx"
Copy-Item "stock-reference\htnkuico.pcx" "Mental Omega\newiduico.pcx"
```

They print nothing.

Any stock icon name works in the first command. To find a unit's icon names, print its art section and read the `CameoPCX=` and `AltCameoPCX=` lines. For the Rhino:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" section HTNK --art
```

It prints the section `[HTNK]` with the lines `CameoPCX=htnkicon.pcx` and `AltCameoPCX=htnkuico.pcx`.

### Step 4: the art section

1. Open `Mental Omega\artmo.ini` in your editor. Take the file in the game folder, not the copy in `stock-reference`.
2. Press Ctrl+End. The cursor jumps to the very end of the file. Since 23 Nov 2026 the file ends with three blocks that the installer wrote for the units Reaver, Cerberus and Moloch (10.7). Each of them stands between a comment line that starts with `; >>> UNIT` and one that starts with `; <<< UNIT`. Leave those blocks alone. Above them is the Arbalest's section. This is it, exactly as it is in the file:

```ini
[ARBL]
Voxel=yes
Remapable=yes
PrimaryFireFLH=335,0,117
CameoPCX=arblicon.pcx
AltCameoPCX=arbluico.pcx
```

3. Do not change these lines, and do not add a second `[ARBL]`. The section for your unit has another `PrimaryFireFLH=` value than the Arbalest's: `240,0,120` goes with the first-test model of step 2 (the table below says more). Below the last line of the file, type the section for your unit:

```ini
[NEWID]
Voxel=yes
Remapable=yes
PrimaryFireFLH=240,0,120
CameoPCX=newidicon.pcx
AltCameoPCX=newiduico.pcx
```

4. Press Enter after the last line.
5. Save the file.

Where exactly:

- "The very end" means: below the `END OF ART FILE` banner, below the comment line that contains `USER ADDITION` and the comment line under it, after the last line of the file. Today that last line is the comment line `; <<< UNIT MLCH`.
- `[NEWID]` must start on a line of its own. If the cursor stands at the end of a line with text, press Enter first.
- An empty line above `[NEWID]` is optional.
- In `Standard.ini` (step 5) it is the other way round: there you stay above the last line, `;END OF FILE`.

| Key | Meaning |
|---|---|
| `Voxel=yes` | The usual meaning: the unit is drawn from a voxel model (`NEWID.vxl`). All 13 stock tanks in 6.4 have it. **[FILES]** The Arbalest has it, and its model showed. **[CONFIRMED]** 22 Nov 2026. A new unit without it was not tried. |
| `Remapable=yes` | The usual meaning: the model takes the player's team colour. All 13 stock tanks in 6.4 have it. **[FILES]** Whether the Arbalest showed team colour was not reported. |
| `PrimaryFireFLH=` | Where the shot leaves the model. `240,0,120` is the Bulldog's value. **[FILES]** The Arbalest had it on 22 Nov 2026, while it wore the Nexus model; where the shot left was not reported. The three numbers are usually read as forward, sideways, height; that was not measured here. From late on 22 Nov to 23 Nov 2026 the Arbalest had `298,0,123`, worked out from the shape of its first own model. Asked whether the shot leaves from the tips of the rails, you answered yes. **[CONFIRMED]** 22 Nov 2026. Since 23 Nov 2026 it has `335,0,117`, worked out the same way from its rebuilt model. After a game with it, the question whether each shot leaves from the weapon's tip was asked together with two others, and your answer was "everything was perfect". **[CONFIRMED]** 23 Nov 2026, as one answer for everything. A value for another model is **[UNTESTED]** until it is seen. |
| `CameoPCX=` | The sidebar icon file. The Arbalest's line names `arblicon.pcx`, and its icon showed. **[CONFIRMED]** 22 Nov 2026 |
| `AltCameoPCX=` | A second icon. All 13 stock tanks in 6.4 have one. **[FILES]** When the game shows it was not looked into. |
| `TurretOffset=` | Optional, not in the Arbalest's section. Stock: Rhino `0`, Catastrophe `-30`. **[FILES]** It is meant to move the turret forward or back on the hull. What the number does was not tested. **[UNTESTED]** |

Rules for this file:

- Add at the very end, below everything else.
- One section per unit. Never add a second section with the same header.
- Mental Omega's icon keys are `CameoPCX` and `AltCameoPCX`. The stock art file never uses the keys `Cameo` and `AltCameo` that the 2025 attempts used. **[FILES]**

### Step 5: the rules

Open `Mental Omega\INI\Map Code\Standard.ini` in your editor. Everything you add goes above the last line, `;END OF FILE`.

**5a. Register the unit.** Press Ctrl+F and search for `[VehicleTypes]`. The file already has this block (at line 102 on 22 Nov 2026):

```ini
[VehicleTypes]
7411=ARBL
7412=REAV
7413=CERB
7414=MLCH
```

Type one new line directly under the last line of that block. Today the last line is `7414=MLCH`. Afterwards the block looks like this:

```ini
[VehicleTypes]
7411=ARBL
7412=REAV
7413=CERB
7414=MLCH
7415=NEWID
```

Do not paste this block into the file. Type only the one new line.

- Stock vehicles already use the numbers 0 to 363 (the `[VehicleTypes]` list in `stock-reference\rulesmo.ini`). **[FILES]** Never use a number from 0 to 363. A number that a stock unit already has is **[UNTESTED]**.
- The Arbalest has 7411. The three units that were installed on 23 Nov 2026 have 7412, 7413 and 7414. Use 7415 for your next unit, then 7416 and so on: always the highest number in your block plus one. Mental Omega's own `Assault.ini` does the same for a building (`1999=CAFLAG`; stock buildings use 0 to 1155). **[FILES]**
- Never type the `[VehicleTypes]` header a second time, and never use a number twice. What the client does with either is unknown. The check reports both as `FAIL`.
- The comment lines above the header start with `;` and talk about the Arbalest. Leave them. The `[VehicleTypes]` list under them is shared by all your units.
- Since 23 Nov 2026 four lines stand under the one header. That is the expected way, and it is what the check asks for. The engine logs of that day list five unit types for the starting units (the stock one and the four new ones, 10.7), and after the last game your report was "everything was perfect". **[CONFIRMED]** 23 Nov 2026, as one answer for everything; whether each of the four was also built from the sidebar was not said.

If the file has no `[VehicleTypes]` line at all (after the Arbalest was removed, see 10.3, or after a mod update), type the header yourself, once, above `;END OF FILE`, with your line under it:

```ini
[VehicleTypes]
7412=NEWID
```

**5b. Add the rules section.** This is the Arbalest's rules section, exactly as it is in the file:

```ini
[ARBL]
UIName=NOSTR:Arbalest Tank
Name=Arbalest Tank
Primary=105mm
ElitePrimary=105mmE
Locomotor={4A582741-9839-11d1-B709-00A024DDAFD1}
MovementZone=Normal
Cost=700
Soylent=350
Bounty.Value=140
Bounty=yes
Bounty.Display=yes
Speed=7
MoveSound=RottweilerMoveStart
Prerequisite=FACTORY
Strength=395
Category=AFV
Armor=medium
Crewed=no
Turret=yes
IsTilter=yes
Crusher=yes
TooBigToFitUnderBridge=true
TechLevel=2
Sight=6
CrateGoodie=no
Owner=UnitedStates,Europeans,Pacific,USSR,Latin,Chinese,PsiCorps,ScorpionCell,Headquaters,Guild1,Guild2,Guild3
Points=25
ROT=9
TurretROT=10
IsSelectableCombatant=yes
DeathWeapon=UnitDeathWeapon
Explodes=yes
VoiceSelect=GenAllVehicleSelect
VoiceMove=GenAllVehicleMove
VoiceAttack=GenAllVehicleAttackCommand
DieSound=GenVehicleDie
CrushSound=TankCrush
MinDebris=1
MaxDebris=3
AllowedToStartInMultiplayer=yes
ThreatPosed=15
DamageParticleSystems=SparkSys,SmallGreySSys
DamageSmokeOffset=100,100,275
VeteranAbilities=STRONGER
EliteAbilities=SELF_HEAL,FIREPOWER,FASTER
Accelerates=true
SlowdownDistance=1
AccelerationFactor=1
DeaccelerationFactor=0
ImmuneToVeins=yes
Size=3
OpportunityFire=yes
DamageSound=VehicleDamagedHeavy
Weight=4
CanBeReversed=no
EMP.Threshold=no
```

It was made from the stock Bulldog section (the command in 3.2 prints that section) with these changes: **[FILES]**

- New `UIName=` and `Name=`.
- `Owner=` lists all twelve countries, and the Bulldog's `RequiredHouses=UnitedStates` line is left out.
- `Prerequisite=ALLWEAP` became `Prerequisite=FACTORY`.
- `AllowedToStartInMultiplayer=no` became `yes`.
- The ammo keys (`Ammo`, `PipWrap`, `Reload`, `ReloadAmount`, `EmptyReload`, `PipScale`), the deploy keys (`IsSimpleDeployer`, `Convert.Deploy`, `Cursor.Deploy`, `DeploySound`) and `IFVMode` are left out.

Make your own section like this:

1. Copy the whole block, all 57 lines from `[ARBL]` to `EMP.Threshold=no`. Copy it inside `Standard.ini` itself: select the `[ARBL]` section there. The text is the same as above, and it already has the file's own line endings.
2. Still in `Standard.ini`, click directly in front of the `;` of the line `;END OF FILE`. That is the last line with text.
3. Paste.
4. Press Enter twice.
5. Never change the original `[ARBL]` section in the file. In the pasted copy you MUST change three lines:
   - the header `[ARBL]` to `[NEWID]`;
   - the text after `UIName=NOSTR:` to the name of your unit;
   - the text after `Name=` to the same name.
6. Look at the end of the file. It must now be: what was the end before (today the comment line `; <<< UNIT MLCH`), an empty line, your section from `[NEWID]` down to `EMP.Threshold=no`, an empty line, and `;END OF FILE` as the last line with text. One empty line more or less does no harm (3.6).
7. Save the file.

Then change only what you mean to change:

| Key | What it is | Notes |
|---|---|---|
| `UIName=NOSTR:` | The name shown to the player. `NOSTR:` is meant to make the game show the text after it as it is. No stock unit uses it; the text `NOSTR:` is present inside `Ares.dll`. **[FILES]** | How it displays was not reported. **[UNTESTED]** |
| `Name=` | Internal name. | The engine log printed the Bulldog's `Name=` once (section 5). **[FILES]** The Arbalest's name has not appeared in any log. |
| `Primary=`, `ElitePrimary=` | Weapon, and weapon at elite rank. | `105mm` and `105mmE` are the Bulldog's. See 6.6. |
| `Secondary=`, `EliteSecondary=` | Optional second weapon, and its elite version. | Not in the Arbalest block. Stock: the Rhino has `Secondary=Super120mm`. Its fire position is `SecondaryFireFLH=` in the art section. The check tests these weapons too. **[FILES]** On a new unit **[UNTESTED]**. |
| `Cost=`, `Soylent=` | Price, and its recycle value. | The stock Bulldog uses half the cost for `Soylent`, as do 333 of the 348 stock vehicles that have the key. **[FILES]** |
| `Strength=`, `Armor=` | Hit points, armour type. | See 6.5. |
| `Speed=`, `ROT=`, `TurretROT=` | Speed, hull turn rate, turret turn rate. | |
| `Prerequisite=` | Buildings you must own. | `FACTORY` = any War Factory. See 6.3. |
| `TechLevel=` | Keep it between 1 and 10. | The 22 Nov game ran at tech level 10 (`spawn.ini`). The stock tanks in 6.4 use 2 or 9; 208 of the 364 stock vehicles use 11. **[FILES]** A value outside 1 to 10 on a new unit is **[UNTESTED]**. |
| `Owner=` | Countries that can build it. | Use the IDs in 6.1, nothing else. |
| `Turret=yes` | Has a turret. | The turret is then taken from `NEWIDTUR.vxl` and `NEWIDTUR.hva`: stock turret files are named this way. **[FILES]** The Arbalest's turret is loaded this way, and it was reported to sit on the hull (section 11). **[CONFIRMED]** 22 Nov 2026 |
| `Image=` | Art name. Not in the block and not needed: without it the game uses the unit's ID (art section `[NEWID]`, files `NEWID.vxl` and so on). The Arbalest has no `Image=` line, and its icon and model showed. **[CONFIRMED]** 22 Nov 2026 | If you write an `Image=` line, the art section and the model files must carry that name instead of the ID. Stock: `[MTNK]` has `Image=GTNK`. **[FILES]** On a new unit **[UNTESTED]**. If you copy a stock section that has an `Image=` line, delete that line. |
| `AllowedToStartInMultiplayer=yes` | The unit may be given to players at the start of a game. This is NOT the Bulldog's value. The stock Bulldog has `no`, and no stock vehicle has `yes`. Mental Omega's own mode file `No Bases.ini` has this line with `yes` 102 times, for example for the Kappa tank. **[FILES]** | In the 22 Nov test the engine log's starting-unit line reads "Unit cost of 410 derived from 2 units totalling 820 credits". In the two games before the Arbalest it read "1 units totalling 120 credits". The difference, 700, is the Arbalest's cost. **[FILES]** So the line took effect: the Arbalest was counted among the starting units. Whether one was seen at the start was not reported. Changing the line to `no`, the stock value, is **[UNTESTED]**. |

Leave the other lines as they are. Apart from the changes listed above, they are the stock Bulldog's lines.

Do not put art keys (`Voxel`, `Remapable`, `PrimaryFireFLH`, `CameoPCX`, `TurretOffset`) in this section. They belong in `artmo.ini` (section 2).

`TurretAnim` is not needed. In the stock rules it appears only on buildings (27 of 27 uses), and none of the 103 stock vehicles with `Turret=yes` has it; their turret files are simply named after the art name plus `TUR`. **[FILES]** The Arbalest has no such line, and its turret was reported to sit on the hull (section 11). **[CONFIRMED]** 22 Nov 2026

**A unit without a turret.** Change `Turret=yes` to `Turret=no`. Then only `NEWID.vxl` and `NEWID.hva` are needed, and the check does not ask for the `TUR` files. Stock example: the Mirage Tank `[MGTK]` has `Turret=no`, and there is no `mgtktur.vxl` in the archives. **[FILES]** On a new unit **[UNTESTED]**.

**Starting from another stock tank.** Open `stock-reference\rulesmo.ini` and search for the tank's header (for the Rhino: `[HTNK]`). Copy its section instead of the Arbalest's: the header and every line under it, down to the next line that starts with `[`. Paste it the same way. Then, in the pasted copy:

- change the header to `[NEWID]`;
- delete the `RequiredHouses=` line (or only the countries in it get the unit);
- delete the `ForbiddenHouses=` line (or the countries in it never get the unit);
- delete the `Image=` line (or the unit uses the stock model and icon);
- delete the deploy lines (`IsSimpleDeployer`, `Convert.Deploy`, `Cursor.Deploy`, `DeploySound`, `DeploysInto`);
- change `UIName=` to `UIName=NOSTR:` followed by your unit's name, and the text after `Name=` to the same name;
- change `Owner=` to the countries that shall get the unit (6.1) and `Prerequisite=` to the building it shall need (6.3). The Arbalest has the twelve-country line of 6.1 and `Prerequisite=FACTORY`.

The Arbalest was made from the Bulldog section in this way. Any other base is **[UNTESTED]**.

### Step 6: check before you start the game

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" check NEWID
```

It checks the registration, the rules section, owner names, prerequisite, weapons, the art section, the icons and the model files. If the unit has a weapon of your own (a block in `Standard.ini`), it also checks that block and its warhead: every name they use (projectile, warhead, sound, animation) must exist, and their keys must be ones the stock rules use. It also checks the format of both INI files: the line endings, and a byte-order mark at the start. In `Standard.ini` it also looks for lines below `;END OF FILE`.

The first line of the output starts with `Preflight for NEW unit`. Preflight is the tool's own word for this check. After that it prints one line for each thing it looked at. The lines that matter start with `PASS`, `WARN` or `FAIL`. With the first-test files of steps 2 and 3, the output must end with these three lines:

```
Result: 0 FAIL, 0 WARN
Nothing blocking was found. Test in a Standard-mode skirmish.
Not checked: section names inside model files, and rules lines such as Locomotor=, Armor= and sounds.
```

The line after `Result:` is one of three:

| Line | When |
|---|---|
| `Nothing blocking was found. Test in a Standard-mode skirmish.` | Only with 0 FAIL and 0 WARN. Go on to step 7. |
| `No FAIL, but read every WARN line above before you test.` | 0 FAIL, but one or more WARN. |
| `Fix every FAIL line above before you start the game.` | One or more FAIL. |

The last line, `Not checked: ...`, is printed every time the check runs to its end. There is one case in which it does not: if the ID is a stock unit's, the check stops early, and its last line is the `Result:` line.

- `FAIL` means something is missing, damaged, or breaks one of this guide's rules. Fix it before you start the game. Not every FAIL has been seen to break a unit: for example, any change above the marker in `artmo.ini` is a FAIL because the tool can then no longer vouch for the file.
- `WARN` means the tool found something unusual. Read every WARN line. Some did no harm where they were seen: the Bulldog block that worked until 24 Nov 2026 had `Voxel=yes` and `TurretAnim=` in its rules, and in a new unit's section the tool warns about both. Others are open: a `TechLevel` outside 1 to 10 is only a WARN, and what the game does with such a new unit is **[UNTESTED]**.
- The few words of reason that the tool prints in a `FAIL` or `WARN` line are sometimes reasoned and not tested. Examples: `do nothing here`, `would be invisible`, `would look for a sprite`, `(silent shot)`, `nobody can build it`. Where this guide marks the same thing **[UNTESTED]**, the guide is right.
- For a first test, aim for `0 FAIL, 0 WARN`.

What to do with some of the lines:

| The line contains | What to do |
|---|---|
| `lines without Windows (CRLF) endings` | Your editor, or a text that you pasted, brought in other line endings. Do not simply make the same edit again: it can give the same result. Run the two repair lines below this table, and then the check again. |
| `starts with a UTF-8 byte-order mark` | Your editor saved the file in another format. Same cure: the two repair lines below this table. |
| `below ';END OF FILE'` | Something was pasted below the last line of `Standard.ini`. Move it above `;END OF FILE`. |
| `the first 898681 bytes are not the stock art file` | The stock part of `artmo.ini` was changed. See 3.4. |
| `normals mode is` | See 7.3. |
| `longer along Y` | See 7.4. |

The two repair lines write each of the two INI files again, with Windows line endings and without a byte-order mark. Close both files in your editor first.

```powershell
(Get-Content "Mental Omega\INI\Map Code\Standard.ini") | Set-Content "Mental Omega\INI\Map Code\Standard.ini"
(Get-Content "Mental Omega\artmo.ini") | Set-Content "Mental Omega\artmo.ini"
```

They print nothing. A file that is already right is not changed by them. This was tried on copies of your two files on 22 Nov 2026. If the check shows the same line again afterwards, put both files back from the last backup (the three lines in 3.5).

What the check does not do:

- It does not check the other lines of the rules section. A mistyped `Locomotor=`, `Armor=` or sound name passes. A missing `Turret=yes` passes too; the turret files are then not looked at. Copy those lines from a stock unit; do not retype them.
- It reads a few numbers in each model file (size, normals mode, team-colour range, number of sections). It does not judge the model, and it does not read section names inside model files.
- It says that the files fit together. It does not prove that the game accepts them.

The check was proven on the live Arbalest (it passes) and on 28 deliberately broken sandbox copies. Each of the 28 was reported: 21 as FAIL, 7 as WARN only.

### Step 7: test in the game

1. Start the Mental Omega client the way you always do. The game folder holds `MentalOmegaClient.exe`. **[FILES]** It is the client that merges your rules into the game (section 2), so start the client, not `gamemd.exe`.
2. The client has an "Interfering Files Detected" message for `artmo.ini`. Its text ends "The mod won't work correctly without those files removed." Do not remove the file because of it. Whether the message appeared on 22 Nov was not reported. **[UNTESTED]** The client log of that day shows that, with `artmo.ini` in place, the client started and launched the game about 15 seconds later, so the file did not stop the game from starting. **[FILES]**
3. Choose Skirmish, game mode **Standard**, and a country that is in your `Owner=` line.
4. Build a War Factory and look in the vehicle tab for your unit. With the first-test files its picture is the one you copied in step 3 (the Rhino's), and its model is a copy of the Nexus model.
5. Look whether the Arbalest is still in the tab too. A second line under `[VehicleTypes]` has never been tested.
6. Build one of your units. Let it move and shoot.

With the first-test files of step 2, your new unit has the shape of the Nexus tank (`NEXS`, section 21) in the old black paint; the Nexus tank itself is gunmetal with coloured decks since 25 Nov 2026. **[FILES]** Tell them apart by the picture in the sidebar. The Arbalest (`Cost=700`) has had a model and an icon of its own since late on 22 Nov 2026, and a rebuilt one since 23 Nov 2026 (section 11).

When you report a test, say three things separately: the picture is in the vehicle tab; you built one at a War Factory; the built tank shows and shoots. The 22 Nov report said only "icon and model works".

The 22 Nov 2026 test was a Standard skirmish as United States on (6) Sedona Pass. **[FILES]** The report was "icon and model works". **[CONFIRMED]** In that test the Arbalest wore placeholder parts: a copy of the Nexus model and a copy of the Catastrophe's icon. **[FILES]** The engine log of that game has no warning that the earlier games did not have. **[FILES]**

Only the last row of this table has been seen. The meanings in the other rows are reasoned. **[UNTESTED]**

| What you see | Meaning | Look at |
|---|---|---|
| Client refuses to start, or `artmo.ini` is gone | The client blocks the file | 10.6 |
| Unit not in the vehicle tab | Rules or registration | Step 5, then section 8 |
| The new unit shows but an earlier unit is gone, or neither shows | The second `[VehicleTypes]` line | Remove the new unit (step 8), test again, write the result into section 12 |
| Unit listed, icon blank, unit invisible | The art section is not being read | Step 4 |
| Icon fine, unit invisible | Model files | Step 2, section 7 |
| Icon and model both show | It works | "After it works" below |

### Step 8: remove one unit again

Close the game and the client first. There are two ways.

**Way 1: by hand.** This always works.

1. Open `Mental Omega\INI\Map Code\Standard.ini`.
2. Under `[VehicleTypes]`, delete the unit's line (for example `7412=NEWID`). Keep the header and the other lines. If no line is left under the header, delete the header too: the file had no `[VehicleTypes]` header before the Arbalest. What an empty list does is **[UNTESTED]**.
3. In the same file, delete the whole `[NEWID]` section: from its header down to its last line (`EMP.Threshold=no`), and the one empty line below it.
4. Save the file.
5. Open `Mental Omega\artmo.ini`.
6. Search for `[NEWID]` (Ctrl+F). The section is near the end of the file. Delete its header and the lines under it, down to the next header or to the end of the file. Delete nothing else.
7. Save the file.
8. Delete the unit's files:

```powershell
Remove-Item "Mental Omega\NEWID.vxl"
Remove-Item "Mental Omega\NEWID.hva"
Remove-Item "Mental Omega\NEWIDTUR.vxl"
Remove-Item "Mental Omega\NEWIDTUR.hva"
Remove-Item "Mental Omega\newidicon.pcx"
Remove-Item "Mental Omega\newiduico.pcx"
Remove-Item "Mental Omega\NEWID.vxl.bak*"
Remove-Item "Mental Omega\NEWID.hva.bak*"
Remove-Item "Mental Omega\NEWIDTUR.vxl.bak*"
Remove-Item "Mental Omega\NEWIDTUR.hva.bak*"
```

They print nothing. The last four lines remove the backups that the fixes of section 7 leave behind; if there are none, they do nothing. One of the first six lines prints a red `Cannot find path` error if that file was never there (for example the `TUR` files of a unit without a turret). That is harmless. If all six print that error, the lines did not hold your ID: correct them and run them again (3.1).

9. Run the check for every unit of yours that stays. If the Arbalest stays, that is this line:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" check ARBL
```

Its last three lines must be the ones shown in 3.2, starting with `Result: 0 FAIL, 0 WARN`. For another unit that stays, type its ID in place of `ARBL`. For the unit you have just removed, the check now prints `FAIL` lines. That is correct: the unit is gone.

**Way 2: put the last backup back.** This replaces 1 to 7 of way 1. It works only if the last backup is the one from step 0 of this unit, that is, if you made no backup after it.

1. See which backup is the last one:

```powershell
Get-Content "backups\last-backup.txt"
```

It prints the folder name of the last backup: its date and time. A red error means there is no backup that was made with the six lines. Use way 1.

2. Make sure that this backup does not contain the unit:

```powershell
$stamp = Get-Content "backups\last-backup.txt"
Select-String -Path "backups\$stamp\Standard.ini","backups\$stamp\artmo.ini" -Pattern "NEWID" -SimpleMatch
```

It must print nothing. If it prints any line, the backup was made after the unit was added. Stop here and use way 1.

3. Put both files back:

```powershell
$stamp = Get-Content "backups\last-backup.txt"
Copy-Item "backups\$stamp\Standard.ini" "Mental Omega\INI\Map Code\Standard.ini"
Copy-Item "backups\$stamp\artmo.ini" "Mental Omega\artmo.ini"
```

They print nothing. Both files are now as they were at step 0. Everything else you changed in them since then is gone too.

4. Do 8 and 9 of way 1: delete the unit's files and run the check for every unit that stays.

### After it works

Change one thing at a time. For every change, do these five things in this order.

1. Close the game and the client. Back up:

```powershell
$stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
New-Item -ItemType Directory -Force "backups\$stamp" | Out-Null
Copy-Item "Mental Omega\INI\Map Code\Standard.ini" "backups\$stamp\"
Copy-Item "Mental Omega\artmo.ini" "backups\$stamp\"
Set-Content "backups\last-backup.txt" $stamp
Get-ChildItem "backups\$stamp"
```

2. Change one thing. Suggested order:
   1. The name: `UIName=NOSTR:` and `Name=`.
   2. The numbers: `Cost=`, `Strength=`, `Speed=`.
   3. The weapon: `Primary=` (6.6).
   4. Your own icons: replace the two `.pcx` files. Keep the file names.
   5. Your own model: replace the four model files. Keep the file names (section 7).
   6. `PrimaryFireFLH=`, if the shot leaves from the wrong place.
3. Run the check:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" check NEWID
```

4. Test in the game (step 7).
5. Write the result into section 12. Each of these changes is **[UNTESTED]** until you have tried it.

If a test fails, undo only that last change, then test again:

- A change in an INI file: put the last backup back.

```powershell
$stamp = Get-Content "backups\last-backup.txt"
Copy-Item "backups\$stamp\Standard.ini" "Mental Omega\INI\Map Code\Standard.ini"
Copy-Item "backups\$stamp\artmo.ini" "Mental Omega\artmo.ini"
```

- New icon files or new model files: a backup does not hold them. Run the copy lines of step 3 (icons) or step 2 (model) again. They put the first-test files back.

### Other kinds of unit

Ships and true aircraft (the list `[AircraftTypes]`) have not been tried. **[UNTESTED]** Three hovering craft, which are vehicles to the game, were installed on 24 Nov 2026 (section 20). The expected pattern is the same: rules in the mode file under the matching list, art in `artmo.ini`. One infantry unit and four buildings were put in on 23 Nov 2026 with a second installer; what that took, and what is still unproven about it, is in 10.8. How an infantry unit, a building and its animations are made is in sections 15 to 17.

The other lists are `[InfantryTypes]` (stock numbers 0 to 150), `[AircraftTypes]` (0 to 50) and `[BuildingTypes]` (0 to 1155). Stock ships are in `[VehicleTypes]`, like tanks. **[FILES]**

Mental Omega itself adds a new building this way: its mode file `Assault.ini` has `[BuildingTypes]`, `1999=CAFLAG` and a `[CAFLAG]` rules section, and the art section `[CAFLAG]` is in the stock `artmo.ini`. **[FILES]** That is the same split this guide uses.

---

## 5. Route A: give a stock unit your model, step by step

**For new work, follow the playbook (section 1).** A take-over is not used any more (below).

**Since 24 Nov 2026, 22:07, no take-over of the Bulldog is installed.** The Nexus model, which this section is about, is a unit of its own now (section 21), because a take-over leaves every line it does not name as the stock unit has it, and that gave the Nexus a list of faults (21.1). The block below was cut out of `Standard.ini` and is kept in `backups\2026-11-24_220747-nexus-takeover-retired\takeover-block.txt`; `nexus-tank\retire_takeover.py restore` puts it back. Read this section as the record of how a take-over was done, and for the two test take-overs that are still in the file (`[APOC]`, `[HTNK]`). Where it speaks of "the block that is there" for the Bulldog, that was true until that day.

Use this when you are happy for a stock unit to change, or when you want a quick look at a model in game.

In this section `NAME` stands for the word you write after `Image=`. It is explained in "Words used in this guide" at the top.

### What it is

A block in `Standard.ini` named after a stock unit changes that unit in every Standard game. `Image=` points the unit at your model files. This was seen once, with the block below. **[CONFIRMED]** 2 April 2026. Lines that you do not write are expected to stay as the stock unit has them; "What you inherit" below says what the files show.

This is the block that put the Nexus model on the United States' Bulldog from 2 April to 24 Nov 2026 (lines 42 to 76 of `Standard.ini` on 22 Nov 2026), exactly as it was in the file:

```ini
[ETNK]
Image=FTNKNEXUS
Strength=800
Cost=1
Speed=8
Turret=yes
TurretAnim=FTNKNEXUSTUR
ROT=8
Owner=British,French,Germans,Americans,Alliance,Russians,Confederation,Africans,Arabs,YuriCountry
Prerequisite=
Primary=TankieGun
Voxel=yes

[TankieGun]
Damage=500
ROF=60
Range=7
Projectile=Invisible
Speed=100
Warhead=TankieWH
Report=PrismShotSound
IsLaser=yes
LaserInnerColor=255,50,50
LaserOuterColor=180,0,0
LaserOuterSpread=0,0,0
LaserDuration=15

[TankieWH]
Verses=100%,90%,80%,70%,60%,50%,100%,25%,100%,0%,0%
CellSpread=0.3
PercentAtMax=0.5
InfDeath=5
AnimList=TWLT070
Wall=yes
Wood=yes
```

It worked in game on 2 April 2026: the tank loaded and moved, and the laser was reported as good. **[CONFIRMED]** The block did not change until it was taken out on 24 Nov 2026; the four model files have not changed and are still in the game folder. **[FILES]**

The comment above this block in the file says "Make custom tank available for ALL factions". That comment is wrong. See "What you inherit" below.

### Steps

**Step 0: back up.** Close the game and the client. Then:

```powershell
$stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
New-Item -ItemType Directory -Force "backups\$stamp" | Out-Null
Copy-Item "Mental Omega\INI\Map Code\Standard.ini" "backups\$stamp\"
Copy-Item "Mental Omega\artmo.ini" "backups\$stamp\"
Set-Content "backups\last-backup.txt" $stamp
Get-ChildItem "backups\$stamp"
```

The last line must list two files: `artmo.ini` and `Standard.ini` (3.5).

**Step 1: read the stock unit.** Then you know what you will inherit. For the Bulldog:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" section ETNK
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" section ETNK --art
```

The first line prints the rules section `[ETNK]`, the second the art section `[ETNK]`. For another stock unit, type its ID in place of `ETNK` (table 6.4).

**Step 2: put your model files in the `Mental Omega` folder.** First choose your `NAME`. Make it like the one that works, `FTNKNEXUS`: capital letters A to Z and digits only, no spaces, at most 9 characters. Another kind of name is **[UNTESTED]**. Then name the files `NAME.vxl`, `NAME.hva`, `NAMETUR.vxl`, `NAMETUR.hva`. Then list the model files in the game folder:

```powershell
Get-ChildItem "Mental Omega\*.vxl", "Mental Omega\*.hva"
```

Find your four files in the list. Compare each name with your `NAME`, letter by letter. The check of section 4 cannot do this for you: it stops when the ID is a stock unit's.

**Step 3: change `Standard.ini`.** Open `Mental Omega\INI\Map Code\Standard.ini` and search (Ctrl+F) for the stock unit's header, for example `[ETNK]`.

- If the block is already there, change that block. `[APOC]` and `[HTNK]` are there; `[ETNK]` was there until 24 Nov 2026. Never add a second block with the same header. For a new model on the Bulldog, change only two lines: `Image=FTNKNEXUS` becomes `Image=NAME`, and `TurretAnim=FTNKNEXUSTUR` becomes `TurretAnim=NAMETUR`. Only the Nexus model under the name `FTNKNEXUS` has been seen working. Another model or another name on the Bulldog is **[UNTESTED]**.
- If it is not there, add a new block above `;END OF FILE`: the header, the line `Image=NAME`, and only the lines you want to change (for example `Strength=`, `Cost=`, `Speed=`, `Primary=`). **[UNTESTED]**

Save the file.

**Step 4: check the file format.** There is no check for a take-over block. But the check for the Arbalest also reports a damaged format of `Standard.ini`:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" check ARBL
```

While the Arbalest is installed, its last three lines must be the ones shown in 3.2, starting with `Result: 0 FAIL, 0 WARN`. A line that contains `lines without Windows (CRLF) endings` or `byte-order mark` means that the format of the file is damaged: run the two repair lines of section 4, step 6, and then the check again. A line that contains `below ';END OF FILE'` means that text stands below the last line: move it above `;END OF FILE`.

**Step 5: test.** Start a Standard skirmish as a country that can build the stock unit. For the Bulldog that is United States.

**Step 6: if the unit is invisible.** Find out whether your model or your block is at fault.

- On the Bulldog: put the two lines back to `Image=FTNKNEXUS` and `TurretAnim=FTNKNEXUSTUR`. That is the block that is known to work. Test again. If the tank shows now, your model files are at fault (section 7). If it does not show even then, something else was changed: put the last backup back (step 7).
- On another unit: change only its `Image=` line to `Image=FTNKNEXUS` and test again. If the unit shows now, your model files are at fault. If it is still invisible, the block is at fault. **[UNTESTED]**

**Step 7: undo a take-over.** Close the game and the client.

- A block that you added: delete it from `Standard.ini`. The stock unit is expected to be back in the next game. **[UNTESTED]** The model files can stay.
- A block that was already there: type its old lines back. For the Bulldog: `Image=FTNKNEXUS` and `TurretAnim=FTNKNEXUSTUR`.
- Or put the last backup back. This is right only if you made no backup after step 0:

```powershell
$stamp = Get-Content "backups\last-backup.txt"
Copy-Item "backups\$stamp\Standard.ini" "Mental Omega\INI\Map Code\Standard.ini"
Copy-Item "backups\$stamp\artmo.ini" "Mental Omega\artmo.ini"
```

They print nothing. Both INI files are then as they were at step 0.

Taking over a unit other than the Bulldog is **[UNTESTED]**. Pick a voxel unit with a turret if your model has one.

### What you inherit, and what the block cannot change

Read from the stock sections. **[FILES]** The effects in game are **[UNTESTED]** unless noted.

- **Name and icon stay the stock unit's.** The taken-over Bulldog is still called "Bulldog Light Tank" in an engine log (`debug\debug.20261122-163742.log`, line 937). **[FILES]** The stock art file and your loose `artmo.ini` have no section named `FTNKNEXUS`, so the icon and the fire position are expected to stay the stock Bulldog's. The old file `Mental Omega\artmd.ini` does hold a section `[FTNKNEXUS]`; the game is not expected to read that file (section 2).
- **Who can build it stays the same.** The stock Bulldog has `RequiredHouses=UnitedStates`, and the block does not change that. Only the United States gets it.
- **Deploy.** The stock Bulldog has `Convert.Deploy=ETNK2`. Deploying turns it into the unchanged "Bulldog (Painter)".
- **Elite weapon.** `ElitePrimary=105mmE` still applies, so an elite tank fires the stock gun.
- **Ammo.** `Ammo=4` still applies.

To open a taken-over unit to other factions, look at what Mental Omega's own Tech Share mode does. It removes the faction lock in two ways: a `RequiredHouses=` line with all twelve IDs (Bulldog: `INI\Map Code\Tech Share.ini`, lines 99 and 100), or the line `ForbiddenHouses=none` for a stock unit that has a `ForbiddenHouses=` line instead (Cavalier: lines 96 and 97; the Rhino, the Lasher and the Bison are the same kind). **[FILES]** It does not change `Owner=` or `Prerequisite=`, so the Bulldog still needs an Allied War Factory there. Doing the same in your block is **[UNTESTED]**.

### Four lines in the working block that are probably not needed

The block above is the only take-over block that was seen working. It contains four lines that are probably not needed:

- `Voxel=yes` and `TurretAnim=`. The stock files use the first only in the art file and the second only on buildings. **[FILES]** The Arbalest's rules section has neither, and its icon and model showed. **[CONFIRMED]** 22 Nov 2026. Its turret was reported to sit on the hull the same day (section 11).
- `Owner=` with the names of vanilla Yuri's Revenge. Those are not Mental Omega countries (6.1). **[FILES]** The Arbalest lists Mental Omega's countries, and its icon and model showed. **[CONFIRMED]** 22 Nov 2026
- `Prerequisite=` with nothing after it. The Arbalest has `Prerequisite=FACTORY`, and its icon and model showed. **[CONFIRMED]** 22 Nov 2026

So a NEW unit (Route B) does not need these four lines: the Arbalest has none of them, and its icon and model showed. Do not write them there. The check warns about `Voxel=` and `TurretAnim=` in a new unit's rules, and it fails the vanilla owner names.

For a take-over block, leaving them out is **[UNTESTED]**. You have two choices:

- Copy the block as it is, with the four lines. That is the form that is known to work. **[CONFIRMED]** 2 April 2026
- Leave the four lines out. Nobody has tried that on a take-over. **[UNTESTED]**

---

## 6. Reference tables

The tables were read from the stock files on 22 Nov 2026. **[FILES]** Where a cell says more than the files do, it carries its own label.

### 6.1 Countries

Use the ID column in `Owner=`, `RequiredHouses=` and `ForbiddenHouses=`.

| ID | Faction | Side |
|---|---|---|
| `UnitedStates` | United States | Allies |
| `Europeans` | Euro Alliance | Allies |
| `Pacific` | Pacific Front | Allies |
| `USSR` | Russia | Soviets |
| `Latin` | Latin Confederation | Soviets |
| `Chinese` | China | Soviets |
| `PsiCorps` | PsiCorps | Epsilon |
| `ScorpionCell` | Scorpion Cell | Epsilon |
| `Headquaters` | Epsilon Headquarters | Epsilon |
| `Guild1` | Haihead | Foehn |
| `Guild2` | Wings of Coronia | Foehn |
| `Guild3` | Last Bastion | Foehn |

`Headquaters` is spelled that way in the game. All twelve on one line:

```ini
Owner=UnitedStates,Europeans,Pacific,USSR,Latin,Chinese,PsiCorps,ScorpionCell,Headquaters,Guild1,Guild2,Guild3
```

The names in the old docs (`British`, `French`, `Germans`, `Americans`, `Alliance`, `Russians`, `Confederation`, `Africans`, `Arabs`, `YuriCountry`) do not exist in Mental Omega.

### 6.2 What decides who can build a unit

| Key | Role |
|---|---|
| `Owner=` | Countries the unit belongs to. With all twelve listed, the icon and the model were seen in a game played as United States. **[CONFIRMED]** 22 Nov 2026. The report does not say that one was built from the War Factory. |
| `RequiredHouses=` | If present, only these countries can build it. Stock uses it for faction-only units such as the Bulldog. **[FILES]** |
| `ForbiddenHouses=` | If present, these countries cannot. **[FILES]** |
| `Prerequisite=` | Buildings the player must own (6.3). |
| `TechLevel=` | Keep it between 1 and 10. The stock tanks in 6.4 use 2 or 9. **[FILES]** A value outside 1 to 10 on a new unit is **[UNTESTED]**. |

To make a new unit faction-only, the stock files suggest that a short `Owner=` list is not enough on its own. Of the ten stock tanks in 6.4 that belong to one country, six also have a `RequiredHouses=` line with that country (the Bulldog: `Owner=UnitedStates` and `RequiredHouses=UnitedStates`), and four have a `ForbiddenHouses=` line with the other countries of the side (the Rhino: `Owner=USSR` and `ForbiddenHouses=Chinese,Latin`). **[FILES]** So the thing to try is `Owner=` together with `RequiredHouses=`, as on the stock Bulldog. For a new unit this is **[UNTESTED]**.

### 6.3 Prerequisite names

| Name | Means any one of |
|---|---|
| `FACTORY` | Any of `GAWEAP`, `NAWEAP`, `YAWEAP`, `FAWEAP`, `GAWEAPB`, `NAWEAPB`, `YAWEAPB`, `FAWEAPB` (the `PrerequisiteFactory=` line under `[General]`). **[FILES]** The Arbalest has this value; its icon was seen in a United States game only. **[CONFIRMED]** 22 Nov 2026 |
| `ALLWEAP` | Allied War Factory (`GAWEAP`, `GAWEAPB`) |
| `SOVWEAP` | Soviet War Factory (`NAWEAP`, `NAWEAPB`, `NAFIST`) |
| `YURWEAP` | Epsilon War Factory (`YAWEAP`, `YAWEAPB`) |
| `FOEWEAP` | Foehn War Factory (`FAWEAP`, `FAWEAPB`) |
| `ALLRAX`, `SOVRAX`, `YURRAX`, `FOERAX` | Barracks of that side |
| `CONYARD` | Any Construction Yard |

In the stock files several names are joined with commas, for example `Prerequisite=ALLWEAP,GAMERC,GATECH` on the Abrams. **[FILES]** The usual rule is that the player then needs all of them. That rule was not tested here: the Arbalest has only one name. **[UNTESTED]** Any stock building ID can be used. To see what a stock unit needs, print its section (3.2).

### 6.4 Stock tanks to copy from or take over

| ID | Name | Owner | Required houses | Prerequisite | Cost | Strength | Weapon |
|---|---|---|---|---|---|---|---|
| `ETNK` | Bulldog Light Tank | UnitedStates | UnitedStates | ALLWEAP | 700 | 395 | 105mm |
| `MTNK` | Cavalier Medium Tank | Europeans | none | ALLWEAP | 750 | 450 | 105mmR |
| `KTNK` | Kappa Hover Tank | Pacific | Pacific | ALLWEAP | 750 | 420 | Hover105mm |
| `ABRM` | Abrams Tank | all Allies | none | ALLWEAP,GAMERC,GATECH | 1500 | 500 | 145mm |
| `HTNK` | Rhino Heavy Tank | USSR | none | SOVWEAP | 850 | 480 | 120mm |
| `JTNK` | Jaguar Battle Tank | Latin | Latin | SOVWEAP | 750 | 435 | 120mmJaguar |
| `CTNK` | Qilin Assault Tank | Chinese | Chinese | SOVWEAP | 900 | 510 | 120mmTiger |
| `APOC` | Catastrophe Tank | all Soviets | none | SOVWEAP,NATECHC | 1600 | 620 | CatastropheGren |
| `LTNK` | Lasher Light Tank | PsiCorps | none | YURWEAP | 700 | 420 | ATGUN |
| `QTNK` | Mantis Scrap Tank | ScorpionCell | ScorpionCell | YURWEAP | 600 | 310 | MantisGun |
| `DEVO` | Colossus | all Epsilon | none | YURWEAP,YAGVLT | 1550 | 670 | ColossusCannon |
| `ROACH` | Bison Combat Tank | Guild3 | none | FOEWEAP | 900 | 530 | RoachBlast |
| `DRACO` | Draco Light Tank | Guild2 | Guild2 | FOEWEAP | 750 | 420 | DracoCannon |

How to read two kinds of cell:

- "all Allies" is short for `Europeans,UnitedStates,Pacific`. "all Soviets" is short for `USSR,Latin,Chinese`. "all Epsilon" is short for `PsiCorps,Headquaters,ScorpionCell`. Never type those words into a file. Type the IDs.
- "none" means that the stock section has no `RequiredHouses=` line. The Cavalier, the Rhino, the Lasher and the Bison have a `ForbiddenHouses=` line instead (Rhino: `ForbiddenHouses=Chinese,Latin`). In a take-over that line is expected to still apply (section 5).

Some units use an art name different from their ID through an `Image=` line: the Cavalier uses `GTNK`, the Catastrophe uses `CATA`. Print the rules section to see.

### 6.5 Movement and armour

Copy `Locomotor=`, `MovementZone=` and `Armor=` from a stock unit that moves the way yours should. The main locomotor values in use among the 364 stock vehicles:

| Locomotor | Used by | Examples |
|---|---|---|
| `{4A582741-9839-11d1-B709-00A024DDAFD1}` | 262 ground vehicles | Cavalier, Bulldog, every tank in 6.4 except the Kappa |
| `{92612C46-F71F-11d1-AC9F-006008055BB5}` | 44 flying vehicles | Stallion Transport, Warhawk, Thor Gunship |
| `{2BEA74E1-7CCA-11d3-BE14-00104B62A16C}` | 29 ships | Horizon Destroyer, Dolphin, Aegis Cruiser |
| `{4A582742-9839-11d1-B709-00A024DDAFD1}` | 14 hover units | Kappa Hover Tank, Robot Tank, Voyager Transport |
| `{4A582747-9839-11d1-B709-00A024DDAFD1}` | 6 teleporting units | Chrono Miner, Ultra Miner, Quickshifter |
| `{4A582743-9839-11d1-B709-00A024DDAFD1}` | 4 burrowing units | Driller APC, Tyrant, Wormqueen |

Many stock vehicles use the plain armour values `light`, `medium` and `heavy`. Mental Omega also defines 238 armour types of its own (the `[ArmorTypes]` list in the rules), so a stock unit's `Armor=` may be something like `charon` or `apoc`. The Arbalest has the Bulldog's `medium`. Another value on a new unit is **[UNTESTED]**. Copy the value from a stock unit; do not invent one. The check does not test this line.

### 6.6 Weapons and sounds

**Reuse a stock weapon.** Any weapon name from the table in 6.4 should be usable in `Primary=`. Only `105mm` has been tried on a new unit; the others are **[UNTESTED]**. The Arbalest uses the Bulldog's `105mm`. Its icon and model showed with that line in place. **[CONFIRMED]** 22 Nov 2026. Later that day its shot was reported to leave from the tips of the rails, so the weapon fires. **[CONFIRMED]** Whether it was built at a War Factory or only seen as a starting unit was not said.

**Define your own.** A weapon and a warhead can be written in `Standard.ini` next to the unit, without being registered in any list. The `[TankieGun]` and `[TankieWH]` blocks of section 5 were written that way (they went out with the take-over on 24 Nov 2026), and the laser was reported as good. **[CONFIRMED]** 2 April 2026

Since 23 Nov 2026 `Standard.ini` also holds three weapons that were made by copying a complete stock weapon with its warhead and changing a few values: `ReaverArc` (from the Wormqueen's lightning bolt), `CerberusFlame` (from the Borillo's flamethrower) and `MolochCannon` (from the Centurion's siege gun). They are inside the installer's blocks near the end of the file. **[FILES]** They pass the check. Asked whether the three weapons look right, you answered "everything was perfect". **[CONFIRMED]** 23 Nov 2026, as one answer for everything; no single weapon was described. Copying a whole stock weapon and its warhead, and changing values only, is the safest way to a weapon of your own: every key in it is one the game knows.

Give your weapon and your warhead names that the stock game does not use. A block named like a stock weapon (for example `[105mm]`) would change that weapon for every unit that uses it, the same way a block named `[ETNK]` changes the Bulldog. **[UNTESTED]** Check a name with the command from section 4, step 1. Two examples:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" section 105mm
```

This prints a section. So `105mm` is a stock name. Do not use it for a weapon of your own.

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" section NexusStarburst
```

This answers `[NexusStarburst] does not exist in the stock rulesmo.ini  (so this ID is free there).` So the stock game does not use that name.

Type the second line with the name you want in place of `NexusStarburst`: once for your weapon, once for your warhead. Each must answer `does not exist`. Then search your own `Standard.ini` for the name:

```powershell
Select-String -Path "Mental Omega\INI\Map Code\Standard.ini" -Pattern "NexusStarburst" -SimpleMatch
```

For `NexusStarburst` this prints nine lines (`Primary=NexusStarburst`, `ElitePrimary=NexusStarburst`, `Weapon1=NexusStarburst`, `EliteWeapon1=NexusStarburst`, `[NexusStarburst]`, `Projectile=NexusStarburstP`, `Warhead=NexusStarburstWH`, `[NexusStarburstP]` and `[NexusStarburstWH]`), because that name is already yours; the search also finds the longer names that begin with it. For a new name the line must print nothing.

The lines of a weapon block:

| Key | Usual meaning | Stock `105mm` |
|---|---|---|
| `Damage=` | Damage of one shot | 65 |
| `ROF=` | Wait between shots. A smaller number fires more often | 45 |
| `Range=` | How far it reaches, in map cells (high ground and the range ring: 13.5) | 6 |
| `Warhead=` | Name of the warhead block | AP |
| `Projectile=` | Must name a projectile that exists. `Invisible` exists in the stock rules | CannonInviso |
| `Report=` | Firing sound, see below | LightTankAttack |

The keys and the values in the last column are what the stock weapon has. **[FILES]** The meanings are the usual ones for this engine. They were not measured in this game. **[UNTESTED]**

**Sounds.** A weapon's `Report=` should name a sound that is in the stock sound file. A name that is not there is expected to give a silent shot. **[UNTESTED]** Check a name:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" section LightTankAttack --sound
```

It prints the section `[LightTankAttack]`, so that sound exists. For a name that is not in the sound file it answers `does not exist in the stock soundmo.ini`.

| Name | Exists in the stock sound file? |
|---|---|
| `LightTankAttack` (the Bulldog's gun) | yes |
| `PrismTowerAttack` (the stock prism weapon) | yes |
| `PrismShotSound` (used by `TankieGun`, the Nexus's laser while it sat on the Bulldog) | no |
| `GenericTankRpt`, `intplasa` (used in the 2025 attempts) | no |

So the Nexus laser was most likely silent while it sat on the Bulldog; in April nothing was said about its sound. The Nexus tank's own weapons named `FutureTankAttack` (24 Nov 2026) and name `SeitaadAttack` (since 25 Nov 2026); both are in the sound file. **[FILES]**

What the shot looks like, the hit effect, the damage and the reach are in section 13. Animations of your own are in section 14.

### 6.7 Game modes

There are 25 mode files in `Mental Omega\INI\Map Code`. Of these, only the selected mode's file is used for a game. **[FILES]** Your blocks are only in `Standard.ini`, so your units exist only in Standard games. To have a unit in another mode, the same rules lines would go into that mode's file. **[UNTESTED]** The art section in `artmo.ini` does not belong to a mode: it is one file for the whole game.

---

## 7. Model files: what a working model has

This section is about what the game needs from the files, not about making a model.

The commands in this section show `NEWID`. For a Route A model, type your `NAME` in its place.

### 7.1 Facts from files that work

| Model | File | Size (X x Y x Z) | Section name | HVA section name | Normals mode | Team-colour range |
|---|---|---|---|---|---|---|
| Stock Bulldog | `etnk.vxl` | 57 x 32 x 32 | `Body` | `Body` | 4 | 16 to 31 |
| | `etnktur.vxl` | 57 x 26 x 15 | `Turret` | (blank) | 4 | 16 to 31 |
| Stock Rhino | `htnk.vxl` | 61 x 39 x 22 | `Body` | `Body` | 4 | 16 to 31 |
| | `htnktur.vxl` | 66 x 27 x 15 | `Turret` | `Turret` | 4 | 16 to 31 |
| Stock Catastrophe | `cata.vxl` | 90 x 59 x 36 | `Body` | `Body` | 4 | 16 to 31 |
| | `catatur.vxl` | 75 x 27 x 17 | `Turret` | `Turret` | 4 | 16 to 31 |
| Nexus (yours) | `FTNKNEXUS.vxl` | 69 x 100 x 31 | `body` | `body` | 4 | 16 to 31 |
| | `FTNKNEXUSTUR.vxl` | 33 x 83 x 18 | `turret` | `turret` | 4 | 16 to 31 |
| Arbalest (yours, made by script; the rebuilt model of 23 Nov 2026) | `ARBL.vxl` | 74 x 42 x 22 | `Body` | `Body` | 4 | 16 to 31 |
| | `ARBLTUR.vxl` | 84 x 36 x 20 | `Turret` | `Turret` | 4 | 16 to 31 |

**[FILES]** for every number in the table. The Nexus was seen in game. **[CONFIRMED]** 2 April and 22 Nov 2026 (on 22 Nov the Arbalest's model files were at first byte copies of the Nexus files). The Arbalest's first own model (62 x 36 x 18, turret 70 x 26 x 16), which replaced them later that day, was seen in game the same night. **[CONFIRMED]** 22 Nov 2026 (section 11). The rebuilt model in the table replaced it on 23 Nov 2026 and passes the check; after a game with it your report was "everything was perfect". **[CONFIRMED]** 23 Nov 2026, as one answer for everything. The stock models are the mod's own files and are taken to be good; in Standard games the Rhino and the Catastrophe currently point at test models instead (section 11).

### 7.2 Checklist

- **Four files**, named after the unit's art name: `NEWID.vxl`, `NEWID.hva`, `NEWIDTUR.vxl`, `NEWIDTUR.hva`.
- **Normals mode 4.** Every stock tank in 6.4 and your working model have 4. Of the 430 stock vehicle voxel files, 425 have 4 and five have 2 (one of them is the Foehn Construction Vehicle's hull); none has 0, which is what the Nexus had in November 2025. **[FILES]** Whether a value other than 4 would display for your model was never tested on its own.
- **Team-colour range 16 to 31**, like every file in 7.1. **[FILES]**
- **Length along X.** The hulls of all 13 stock tanks in 6.4 are longest along X. **[FILES]** The Nexus is longest along Y, and it needed the fix in 7.4.
- **Section names.** The Nexus uses `body` and `turret` in both files, the Arbalest's model `Body` and `Turret`. The stock Bulldog's turret HVA has a blank name, so the stock game itself does not follow the old rule "the names must match". **[FILES]** Matching names are still the safe choice.
- **A third pair is optional:** `NEWIDBARL.vxl` + `NEWIDBARL.hva` (gun barrel). Some stock tanks have one (`htnkbarl.vxl`, `gtnkbarl.vxl`, `ltnkbarl.vxl`), the Bulldog and the Catastrophe have none, and neither of your working units has one. **[FILES]** Adding one to your own unit is **[UNTESTED]**.

What the check (section 4, step 6) does with model files: it works for a new unit only (Route B). It reads the file names, the size, the normals mode and the team-colour range and reports what differs from the list above. It warns about a model that is longer along Y only while its HVA has no rotation. It does not look at section names, and in a file with several sections it reads the size and the normals mode of the first section only.

### 7.3 Fix: normals mode

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" set-normals "Mental Omega\NEWID.vxl" "Mental Omega\NEWIDTUR.vxl"
```

It prints one line per file. For a file that needed the fix, the line looks like this:

```
CHANGED  Mental Omega\NEWID.vxl: normals mode 2 -> 4   (backup: NEWID.vxl.bak)
```

The file was changed. The number in front of the arrow is the old value. The old file was saved under the name shown.

For a file that was already right, the line looks like this:

```
OK       Mental Omega\NEWID.vxl: normals mode is already 4, nothing changed
```

There was nothing to do, and no backup is made. The first-test files of section 4, step 2 give this line.

It sets one byte per section to 4 and saves a backup first. On the Nexus this is the same one-byte change that was made by hand on 2 April 2026: applied to a copy of `FTNKNEXUS.vxl.bak` whose mode byte was set back to 0, it reproduces `FTNKNEXUS.vxl.bak` byte for byte (checked 22 Nov 2026). **[FILES]**

### 7.4 Fix: a model that drives sideways

In April the Nexus loaded, but in your words at the time "the turret moves differently and the tank look like its drifting". The model's length runs along Y. The fix that worked was to leave the voxel data alone and overwrite the matrix in both HVA files with a 90-degree turn. **[CONFIRMED]** 2 April 2026. The matrices that were overwritten may also have held an offset (the older backup `FTNKNEXUS.hva.backup` does **[FILES]**), and the fix removed that at the same time, so it was never shown that the Y length alone was the cause. This command does the same:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" rotate-hva "Mental Omega\NEWID.hva" "Mental Omega\NEWIDTUR.hva"
```

For each file it prints two lines like these:

```
CHANGED  Mental Omega\NEWID.hva: 1 matrix(es) set to a 90-degree counter-clockwise turn   (backup: NEWID.hva.bak)
         first matrix before: 1 0 0 0 0 1 0 0 0 0 1 0
```

- This does not add a turn to what is already there. It overwrites the direction stored in the file with one fixed quarter turn. Running the same line twice gives the same file as running it once.
- It prints `CHANGED` every time, even when the numbers were already the same, and it saves another backup every time (`.bak`, then `.bak2`, `.bak3`).
- The line `first matrix before:` shows what the file held. `1 0 0 0 0 1 0 0 0 0 1 0` is no turn. `0 -1 0 0 1 0 0 0 0 0 1 0` is this fix, already applied.
- This replaces every number in the HVA matrices, including any offsets stored there. It writes exactly the matrix that is in your working HVA files (compared byte for byte on 22 Nov 2026). **[FILES]**
- **Never rotate the voxel data itself.** A script that did that (`rotate_vxl.py`) caused two fatal errors in April. **[CONFIRMED]**

If the tank then faces backwards, write the opposite quarter turn. That is the same line with `--cw` at the end:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" rotate-hva "Mental Omega\NEWID.hva" "Mental Omega\NEWIDTUR.hva" --cw
```

Its `CHANGED` lines say `clockwise turn`. Type `--cw` at the end of the line, as shown. In April the first direction that was tried was this one, and you called the result "reversed". The direction without `--cw` was the right one for the Nexus. **[CONFIRMED]** 2 April 2026. Which direction another model needs can only be seen in the game.

### 7.5 Not covered here

- **Lighting.** After the rotation the Nexus looked dark from behind and at the sides (**[CONFIRMED]** 2 April 2026), and a "normals remap" was run to fix it. Your next message was "ok great", without saying that the dark sides were gone. That remap is specific to the Nexus, whose normals were all one value, so do not reuse the snippet in doc 08. A model made with the kit of section 18 is written with proper normals by the tool; its validator reports them.
- Making models and icons: section 18.

### 7.6 Undo a fix

Each fix first saves the file as it was, under the same name with `.bak` added (`NEWID.vxl.bak`). If that name is taken it uses `.bak2`, then `.bak3`. The command prints the name it used. The one without a number is the oldest.

To put the files back as they were before the first fix:

```powershell
Copy-Item "Mental Omega\NEWID.vxl.bak" "Mental Omega\NEWID.vxl"
Copy-Item "Mental Omega\NEWIDTUR.vxl.bak" "Mental Omega\NEWIDTUR.vxl"
Copy-Item "Mental Omega\NEWID.hva.bak" "Mental Omega\NEWID.hva"
Copy-Item "Mental Omega\NEWIDTUR.hva.bak" "Mental Omega\NEWIDTUR.hva"
```

- Use only the lines for the fix you ran: the first two for 7.3, the last two for 7.4.
- They print nothing. A red `Cannot find path` error means that this fix made no backup, because it changed nothing.
- Then run the check again (section 4, step 6).

Do not restore `FTNKNEXUS.vxl.bak` or `FTNKNEXUSTUR.vxl.bak`. They are not backups of the working files (section 11).

---

## 8. Troubleshooting

For a new unit (Route B), run the check first:

```powershell
python "MentalOmega-Modding-Guide\scripts\mo_tool.py" check NEWID
```

It can find some of the causes in the rows marked with *. How to read its output is in section 4, step 6.

For a taken-over stock unit (Route A) there is no such check: the check stops when the ID is a stock unit's.

The column "Route" says where a row applies: A, B, or both.

| Route | Symptom | Likely cause | What to do | Basis |
|---|---|---|---|---|
| A, B | "Failed to initialize, please reinstall" at start | A rebuilt `expandmo` archive. In April this came from rebuilt 96/97/99, not from the tank. | Put the archives back as they were before the rebuild (10.4). | **[CONFIRMED]** April 2026 |
| A, B | Fatal error when the game or map loads | A damaged `.vxl`. In April: voxel data rotated by a script. | Restore the backup the tool named when it changed the file (7.6). If it began after a model was replaced (the Arbalest on 22 and on 23 Nov 2026, the three other units on 23 Nov 2026), put the files from before back: 10.2 for the Arbalest, 10.7 for the three units. | **[CONFIRMED]** April 2026 |
| B | Client shows "Interfering Files Detected" for `artmo.ini` | The loose art file is on the client's list. | Do not remove the file. Continue. If it blocks you, see 10.6. | **[UNTESTED]** |
| B | Unit not in the vehicle tab * | Not a Standard game; no `[VehicleTypes]` line; `Owner=` has wrong names; `Prerequisite=` or `TechLevel=` wrong | Section 4, step 5. Then "Where to look" below. | **[UNTESTED]** |
| B | The new unit shows but an earlier unit is gone, or neither shows | The second `[VehicleTypes]` line | Remove the new unit (section 4, step 8), test again, write the result into section 12. | **[UNTESTED]** |
| A | A taken-over unit is missing for other factions | The stock unit's `RequiredHouses=` | Section 5 | **[FILES]** |
| B | Unit listed, icon blank * | No art section, wrong `CameoPCX=` name, or the icon is not a 60x48 8-bit PCX | Section 4, steps 3 and 4 | **[UNTESTED]** |
| A, B | Unit invisible * | Route B: no art section, or no `Voxel=yes`. Both routes: model files not named after the art name | Route B: section 4, steps 2 and 4. Route A: section 5, step 6. For the Arbalest with its new model: the line in 10.2 puts the old files back. | **[UNTESTED]** |
| A, B | No turret * | The two `TUR` model files are missing, or `Turret=yes` is missing | Section 4, steps 2 and 5 | **[UNTESTED]** |
| A, B | Tank drives sideways, turret points the wrong way * | Model is long along Y (the same fix also wiped any offset stored in the old HVA matrix) | 7.4 | Symptom and fix **[CONFIRMED]** 2 April 2026. That the Y length alone was the cause was never shown (7.4). |
| A, B | Tank faces backwards after the rotation | Wrong direction | 7.4, the line with `--cw` | **[CONFIRMED]** April 2026 |
| A, B | Dark from some sides | Probably the model's normals: before the April remap every voxel of the Nexus had the same normal value. **[FILES]** | 7.5 | Symptom **[CONFIRMED]** 2 April 2026. That the remap cured it was not said in so many words. |
| A, B | Shot leaves from the wrong place | `PrimaryFireFLH=` in the art section | Section 4, step 4 | **[UNTESTED]** |
| A, B | Unit does not shoot * | `Primary=` names a weapon that is not defined; or the weapon's `Warhead=` or `Projectile=` names something that is not defined | Route B: run the check. Both routes: compare your weapon with `[TankieGun]` and `[TankieWH]` in section 5. | **[UNTESTED]** |
| A, B | A hit shows no explosion * | The warhead's `AnimList=` names an animation that the game does not know (not listed under `[Animations]`, or a typing mistake) | Search `Mental Omega\debug\debug.log` for the words `Failed to parse INI file content`. A line of that kind names the warhead and the animation. | From the Ares documentation, not seen here. **[UNTESTED]** |
| B | A hit with an animation of your own shows no explosion, and the log has no such line | The animation is listed under `[Animations]` in the mode file, but its settings stand only in `artmo.ini`. The game makes the animation from the list and then looks for a section with its name in the map code itself. Without that section it loads neither settings nor picture. | Give the animation its own section in `Standard.ini`, with the keys of its art section (10.8). | Read in the game's program on 23 Nov 2026. **[FILES]** Not seen in the game. **[UNTESTED]** |
| B | A building does not seem to move | Its animation only changes a few glowing pixels | Give it moving parts: section 17. | **[CONFIRMED]** 24 Nov 2026 |
| B | A building's shot starts above or beside its weapon | `PrimaryFireFLH=` was counted from the middle of the lot. A building counts from the middle of its sprite canvas. | 16.8 | **[CONFIRMED]** 24 Nov 2026 |
| B | A defence hits things outside the range ring it shows | It stands on higher ground and its projectile has `SubjectToElevation=yes` | 13.5; run `new-buildings\check_range.py` | Seen in the game: **[CONFIRMED]** 24 Nov 2026. The cure: **[FILES]**, not seen in the game. **[UNTESTED]** |
| A, B | Weapon is silent * | `Report=` names a sound that is not in the stock sound file | 6.6 | **[FILES]** for the missing name; that the shot is then silent is **[UNTESTED]** |
| B | Name shows as `MISSING:` and more text | `UIName=` points at a text label that does not exist | Write `UIName=NOSTR:` and then the name, as in the Arbalest's section | **[UNTESTED]** |
| A | A taken-over unit still has the old name and icon | That is how a take-over works | Use Route B for a new name and icon | **[FILES]** |
| A, B | The engine log says `Failed to exit object from factory - refunding money` | Seen once, for the `Cost=1` Bulldog, in a log of 22 Nov 2026. **[FILES]** A guess at the reason: a second tank was finished before the first had left the factory. | Use a normal cost | **[UNTESTED]** |
| A, B | Units vanish after the client updates | The updater may put back the stock `Standard.ini` | 10.5 | **[UNTESTED]** |
| B | The check says `the first 898681 bytes are not the stock art file` | The file was edited above the marker, or the mod was updated | 3.4 | **[FILES]** |

### Where to look

Look in this order.

1. `Mental Omega\spawnmap.ini`: the scenario the client wrote for the last game. Look here first. Search it for your ID:

```powershell
Select-String -Path "Mental Omega\spawnmap.ini" -Pattern "NEWID" -SimpleMatch
```

If it prints nothing, the last game never got your rules: it was not a Standard game, or the text is not in `Standard.ini`, or the client was open while you edited and did not read the file again (3.6, **[UNTESTED]**). For the game of 22 Nov 2026 the file holds `[VehicleTypes]`, `7411=ARBL` and `[ARBL]`. **[FILES]**

2. `Mental Omega\debug\debug.log`: the engine's log of the last game. Older games are kept next to it, with the date and time in the file name. Do not expect to find your unit in it: the log of the game in which the Arbalest worked contains neither `ARBL` nor `Arbalest`. **[FILES]** Read its last lines after a crash.
3. `Mental Omega\syringe.log`: written when the game starts. The one of the 22 Nov game ends with `Done with exit code 0` and `Exiting on success`. **[FILES]** It does not mention units.
4. `Mental Omega\Client\client.log`: what the client did before it started the game.

---

## 9. Things that do not work, and errors in the old docs

The old documents and the old scripts that this section names left the guide's folder on 25 Nov 2026 (`scripts\` below stands for the old `MentalOmega-Modding-Guide\scripts`). They are kept in `backups\2026-11-25-before-github-replace\MentalOmega-Modding-Guide`; their lessons stay here. Do not copy them back: the folder is public, and some of the old files hold a personal folder path.

### Things that were tried and must not be repeated

| What | What happened |
|---|---|
| Editing `Mental Omega\rulesmd.ini` or `artmd.ini` | The game does not take its rules from `rulesmd.ini` (section 2). **[FILES]** That it does not read `artmd.ini` either is reasoned, not tested. **[UNTESTED]** |
| Packing files into `expandmo02.mix` (`create_mix.py`, `prepare_tank.py`) | Not needed: loose files work. Those scripts also number the packed files in a way the game's archives do not use. **[FILES]** |
| Rebuilding `expandmo96`, `97` or `99` | "Failed to initialize" at start. **[CONFIRMED]** April 2026 |
| Art keys in the rules block (`Voxel`, `Cameo`, `PrimaryFireFLH` ...) | The stock rules file has none of these keys; they are all in the art file. **[FILES]** That they do nothing in a rules block is **[UNTESTED]**. |
| `Cameo=` / `AltCameo=` | Mental Omega's keys are `CameoPCX=` / `AltCameoPCX=`. **[FILES]** |
| Vanilla country names in `Owner=` | Not Mental Omega countries (6.1). **[FILES]** |
| Rotating voxel data (`rotate_vxl.py`) | Two fatal errors. **[CONFIRMED]** April 2026 |

The Bulldog block that worked until 24 Nov 2026 had an art key and the vanilla owner names in it (section 5). Do not write them into a new unit.

### Old scripts that are not safe

| Script | Problem |
|---|---|
| `scripts\fix_normals_mode.py` | Writes to the wrong byte (83 instead of 91 in the section tailer). It damages the file and does not set the mode. Use the `set-normals` command (7.3). |
| `scripts\auto_normalize_vxl.py` | Writes the same wrong byte, and reads the model size from the wrong place. |
| `scripts\validate_vxl.py` | Reads the model size from the wrong bytes (80 to 82 instead of 88 to 90), so "Dimensions are 0x0x0" can be a false alarm. Use the check (section 4, step 6). |
| `Mental Omega\validate_vxl.py` | A different, older script. It does not read the model size at all. It warns about any model file over 100,000 bytes and about section names other than body, turret or barrel; the working Nexus hull is 162,343 bytes, so neither warning means a fault. Not needed. |
| `scripts\create_mix.py`, `Mental Omega\create_mix.py`, `scripts\prepare_tank.py` | Build an archive nobody needs, with the wrong file-ID scheme. The copy in `Mental Omega` writes `expandmo02.mix` into the game folder when started. |
| `rotate_vxl.py` (project folder) | Caused the fatal errors. Started without arguments it rewrites `FTNKNEXUS.vxl` and `FTNKNEXUSTUR.vxl` in the game folder and makes no fresh backup. Do not run it. |
| `rebuild_all_mix.py`, `fix97_99.py` (project folder) | These made the rebuilt archives of 2 April 2026 that gave "Failed to initialize". Started without arguments, each rebuilds `expandmo` archives in the game folder (`96`, `97` and `99`, or `97` and `99`) and puts the rebuilt files in place of the ones the game uses. **[FILES]** Do not run them. |
| `scripts\fix_section_names.py`, `Mental Omega\fix_vxl_hva.py` | Not needed (7.2). `fix_vxl_hva.py` rewrites the live `FTNKNEXUS` files when started. |

### Statements in the old docs that are wrong

- README, doc 08: the faction names, and "available for all factions". The stock Bulldog has `RequiredHouses=UnitedStates`, and the block does not change that line, so the taken-over Bulldog is for United States only. **[FILES]**
- README "Quick Start": describes the older `TANKIE` setup. `TANKIE.vxl` no longer exists.
- Doc 03: "`Standard.ini` is loaded for all game modes". It is used for Standard only. Its full example puts art keys in the rules block and uses `Cameo=`. Its locomotor table (and the one in QUICK-REFERENCE) labels the teleport locomotor as "ships". Its armour table lists eleven types; the game has many more.
- Docs 03 and 04 (also QUICK-REFERENCE line 80 and doc 08 line 278): `TurretAnim=` is needed for a turret. No stock vehicle has it. **[FILES]**
- Doc 04 and QUICK-REFERENCE: the model size is at tailer bytes 80 to 82. It is at 88 to 90.
- Docs 03 (line 315), 04 (line 163), 05, 06 and QUICK-REFERENCE: files have to be in a MIX. They do not: loose files in the game folder work. **[CONFIRMED]** 2 April and 22 Nov 2026. (Doc 04 itself recommends loose files at line 83.)
- README, QUICK-REFERENCE and docs 01, 03, 04, 05 and 08: VXL and HVA section names must match. The stock Bulldog turret's do not.
- Doc 08: `PrimaryFireFLH=150,0,180` as part of the working setup. That line is only in `artmd.ini`, which the game is not expected to read (section 2); the taken-over Bulldog is expected to fire from the stock position.
- Docs 03 and 08, `Standard.ini`: `GenericTankRpt` and `PrismShotSound` as firing sounds. Neither is in the stock sound file.
- README "Mental Omega Unit IDs": lists the Lasher (`LTNK`) as Soviet and calls `MTNK` and `APOC` by their vanilla names. In the stock rules the Lasher's owner is PsiCorps, `MTNK` is the Cavalier and `APOC` the Catastrophe (6.4). **[FILES]**
- Doc 09, "Complete INI Configuration" and "Mech Workaround": art in `artmd.ini (or Standard.ini)`, `Cameo=`/`AltCameo=`, vanilla owner names, `Voxel=yes` and `TurretAnim=` in the rules block. Its "Walk/Mech" locomotor `{4A582744-9839-11d1-B709-00A024DDAFD1}` is used by stock infantry and by no stock vehicle. **[FILES]**
- QUICK-REFERENCE, docs 03 and 04: `SpeedType=Track` in the tank template. No stock vehicle has that line. **[FILES]**

---

## 10. Backups, undo, updates, playing online

### 10.1 The two INI files

- Before any change: the six backup lines in 3.5.
- Back to the last backup: the three restore lines in 3.5.
- Back to an older backup: with File Explorer, as described in 3.5.

### 10.2 Model files

The `set-normals` and `rotate-hva` commands save a backup next to the file before they change it (`.bak`, then `.bak2`, `.bak3` ...). An existing backup is never overwritten, and the command prints the name it used. How to restore one is in 7.6.

`FTNKNEXUS.vxl.bak` and `FTNKNEXUSTUR.vxl.bak` in the game folder are from April: the Nexus as it was before its lighting remap. **[FILES]** Do not restore them.

**The Arbalest's model.** The Arbalest has had three looks:

- placeholder parts (a copy of the Nexus model, a copy of the Catastrophe icon), until late on 22 Nov 2026;
- its first own model and icon, from then until 23 Nov 2026, seen working in the game (section 11) **[CONFIRMED]**;
- a rebuilt model and icon since 23 Nov 2026, 14:29: the same rail sniper, made after the game's steel-blue tanks. It passes the check. **[FILES]** After a game with it your report was "everything was perfect". **[CONFIRMED]** 23 Nov 2026, as one answer for everything.

To put the look confirmed on 22 Nov back, close the game and the client and run this in the project folder:

```powershell
python -I "arbalest-tank\install_arbalest_option.py" . "arbalest-tank\option-1-rail-sniper" 298,0,123 --apply
```

- Without `--apply` at the end it changes nothing and only lists what it would do. That form was run on 23 Nov 2026.
- With `--apply` it first copies the six `ARBL` and `arbl` files and `artmo.ini` into a new folder in `backups`. Then it replaces the six files and changes one line of `artmo.ini`, the `PrimaryFireFLH=` line of `[ARBL]`. No other unit is touched.
- The rebuilt look went in with the same program (folder `arbalest-tank\option-4-rail-sniper-rebuilt`, value `335,0,117`), on a sandbox copy first and then on your folder.
- Afterwards run the check for the Arbalest (3.2).

The six files of the first own model are also in `backups\2026-11-23_142959-arbalest-before-new-model`, with the `artmo.ini` of that moment.

The placeholder parts are in `backups\2026-11-22_224520-arbalest-before-new-model`, together with the `artmo.ini` of that moment. Should you ever want them back, close the game and the client and use this line:

```powershell
Copy-Item "backups\2026-11-22_224520-arbalest-before-new-model\*" "Mental Omega\"
```

- It prints nothing. It copies seven files: the six `ARBL` and `arbl` files and `artmo.ini`.
- It was tried on a sandbox copy on 22 Nov 2026: all seven files came back as they were.
- It puts the whole `artmo.ini` of that moment back. So use it only while you have added nothing else to `artmo.ini` since then: a section added later would be gone.
- **Since 23 Nov 2026 this is the case:** three units were installed after that moment (10.7). Their art would be gone, while their rules would stay in `Standard.ini`. Remove those three units first (10.7), or do not use this line.
- Afterwards run the check for the Arbalest (3.2). It must end with the three lines shown there.

### 10.3 Undo the Arbalest completely

There is a script for that: `backups\2026-11-22-arbalest\UNDO.ps1`. It deletes seven files: the whole loose `artmo.ini`, the four `ARBL` model files and the two `arbl` icons. Then it overwrites `Standard.ini` with the copy saved before the Arbalest. **[FILES]** Copies of the Arbalest's present model and icon stay in `arbalest-tank\option-4-rail-sniper-rebuilt`, those of its first own model in `arbalest-tank\option-1-rail-sniper`.

Use it only if nothing else of yours has gone into `artmo.ini` or `Standard.ini` since the Arbalest was added. Since 23 Nov 2026 that is no longer so: three more units are installed (10.7). Remove them first with the installer, or the script would destroy their art and their rules and leave their files and records behind. (The Arbalest's own `PrimaryFireFLH=` line was changed late on 22 Nov and again on 23 Nov 2026. That does not matter here: the script deletes that file.) A unit added later, or any other edit to `Standard.ini` (for example removing the December test blocks), would be lost. In that case remove the Arbalest by hand: section 4, step 8, with `ARBL` as the ID. Its line under `[VehicleTypes]` is `7411=ARBL`.

The script has not been run by anyone yet. **[UNTESTED]** This line starts it:

```powershell
& "backups\2026-11-22-arbalest\UNDO.ps1"
```

At its end it prints `Arbalest test removed; Standard.ini restored.` **[FILES]** After it, `Mental Omega\artmo.ini` is gone and `Standard.ini` has no `[VehicleTypes]` header.

If PowerShell answers that running scripts is disabled, change no setting. Remove the Arbalest by hand instead.

**When the Arbalest is gone** (after this script, or after you removed it by hand with section 4, step 8), section 4 is different in three places for your next new unit:

1. After the script, `Mental Omega\artmo.ini` is missing. Create it before anything else: 3.4, number 2. Removing the Arbalest by hand keeps the file.
2. Step 4: `artmo.ini` no longer ends with the Arbalest's section. It ends with two comment lines. The first of them contains `USER ADDITION`. Type your section below both.
3. Step 5: `Standard.ini` has no `[VehicleTypes]` header and no `[ARBL]` section. Type the header as the last paragraph of 5a says. For 5b, copy the block out of this guide and paste it in front of `;END OF FILE` in the same way. The text of this guide can carry other line endings than `Standard.ini`. If the check then reports `lines without Windows (CRLF) endings`, run the two repair lines of section 4, step 6.

Step 2 needs no change: its four lines copy the Nexus model files, and those stay.

### 10.4 Original archives

The four `expandmo` archives in the game folder differ from the mod's originals in four header bytes each. They were changed on 6 April 2026 so that XCC Mixer can open them, and the game was reported working afterwards. **[CONFIRMED]** 6 April 2026

On that day the untouched originals were in `Desktop\expandmo_originals`. That folder was looked for on 22 Nov 2026 and was not found.

A ZIP of the whole game folder as it was on 27 November 2025 is in your Downloads folder: `Mental Omega.zip`, about 1.07 GB. It was opened and read on 22 Nov 2026. **[FILES]** That date is before the archives were changed. Nobody has restored an archive from it yet. **[UNTESTED]**

If an archive ever has to be restored, copy only that one `expandmo` file out of the ZIP. Never unpack the whole ZIP over the game folder: it would put the November 2025 versions of `Standard.ini` and other files back.

### 10.5 Mod updates

The updater could not reach its server on 22 Nov 2026. **[FILES]** If it ever updates, it may put back the stock `Standard.ini`, and the stock art file may change. **[UNTESTED]**

After an update:

1. Copy your own blocks from your last backup into the new `Standard.ini`.
2. Write the stock files again: the command with `--force` in 3.3.
3. Run the check for every unit (section 4, step 6).
4. If the check says that the stock part of `artmo.ini` has changed, do 3.4.

### 10.6 The client's warning, online play and campaign

- **Client warning:** `artmo.ini` is on the client's forbidden-files list (`Resources\ClientDefinitions.ini`, the line `ForbiddenFiles=`), and the client has an "Interfering Files Detected" message for such files. **[FILES]** Whether it showed on 22 Nov was not reported; the client log shows the game was launched all the same. **[FILES]** Removing `artmo.ini` from that line to silence it is **[UNTESTED]**.
- **Online and campaign:** `artmo.ini`, `expandmo97.mix` and `expandmo99.mix` are on the client's modified-files list (`Resources\FHCConfig.ini`). **[FILES]** Those two archives have differed from the mod's originals in four header bytes each since 6 April 2026, so this install was already a changed one before `artmo.ini` was added. **[FILES]** Do not play online with this install. Campaign may show a modified-files screen. **[UNTESTED]**

### 10.7 Units that were installed with the installer

Reaver, Cerberus and Moloch were not typed in by hand. They were put in on 23 Nov 2026 by a small program, `arbalest-tank\kit\unit_bundle.py`, from the three folders in `new-units`. For each unit it did what section 4 does by hand: one line under `[VehicleTypes]`, the rules above `;END OF FILE`, the art at the end of `artmo.ini`, the files into the game folder, and then the check. It marks what it wrote with two comment lines, `; >>> UNIT` and `; <<< UNIT`, so that it can take exactly that out again. **[FILES]**

To see what is installed:

```powershell
python "arbalest-tank\kit\unit_bundle.py" status
```

On 23 Nov 2026 it printed the four lines under `[VehicleTypes]`, the line `9001=REAVZAP` under `[Animations]`, one line for each of the three units, and `added by hand (not managed by this tool): ARBL`. (Since the evening of that day two more lines stand under `[Animations]`. They belong to the Doomsayer, 10.8.)

To remove one of the three units, close the game and the client and run this line with the unit's ID (`REAV`, `CERB` or `MLCH`):

```powershell
python "arbalest-tank\kit\unit_bundle.py" remove REAV
```

- It refuses while the game or the client is running.
- It takes out the unit's line under `[VehicleTypes]`, its block in `Standard.ini`, its block in `artmo.ini` and its files, and it puts a copy of everything it removed into a new folder in `backups`.
- The other units are not touched. Run the check for each of them afterwards (3.2).
- It cannot remove the Arbalest, which was added by hand: for that see section 4, step 8.
- Removing was tried on a sandbox copy only: after a unit was installed and removed there, both INI files were the same as before, byte for byte. On your real folder only the install and the swap (below) have run so far.

To put a removed unit back:

```powershell
python "arbalest-tank\kit\unit_bundle.py" install "new-units\REAV"
```

It ends with `installed REAV` and the line `Result: 0 FAIL, 0 WARN` of the check. If the check finds a FAIL, the program puts everything back as it was and says `NOT INSTALLED`.

To give one of the three units a new look and nothing else (a new model, a new icon, a new fire position), close the game and the client and run:

```powershell
python "arbalest-tank\kit\unit_bundle.py" swap REAV "new-units\REAV"
```

- It replaces the files of the unit that it finds in that folder, and it sets the `PrimaryFireFLH=` value in the unit's art section. The value comes from the file `REAV_report.json` in that folder, or from `--flh 273,0,140` at the end of the line.
- Rules, weapons and the lines under `[VehicleTypes]` and `[Animations]` are not touched.
- First it copies the files it replaces, `artmo.ini` and its own record into a new folder, `backups\<time>-REAV-before-swap`. Afterwards it runs the check. If the check finds a FAIL, it puts everything back and says `NOT SWAPPED`.
- To go back to the look from before, run the same line with that backup folder in place of `new-units\REAV`.
- Tried on a sandbox copy with 23 checks. Among them: only the one fire-position line of `artmo.ini` changes, `Standard.ini` stays the same byte for byte, a damaged model is put back, and going back restores every file. **[FILES]**

On 23 Nov 2026 at 13:51 the three units got a rebuilt look this way. The request was to make them more realistic, at the quality of the game's own tanks. The rebuilt models follow the game's dark heavy tanks (Draco, Bison, Gharial): four dark greys painted flat, open tracks with road wheels, house colour in small patches, almost no glowing colours. `Standard.ini` did not change. In `artmo.ini` only the three fire-position lines changed: Reaver `273,0,140`, Cerberus `198,0,131`, Moloch `347,0,157`. All four units pass the check. **[FILES]** A game with the rebuilt look was played that evening (20:15, Standard, on (6) Sedona Pass; its log lists the same five starting unit types). Three questions were asked afterwards: does each turret sit on its hull and does each shot leave from the weapon's tip; do the units look at home next to the game's tanks; do the three weapons look right and does the Reaver's lightning end in a small burst. Your answer was "everything was perfect". **[CONFIRMED]** 23 Nov 2026, as one answer for everything: no single item was named, and no screenshot was sent. The answer also covered the burst, which by the reading of the game's program was probably never drawn (below). So read these labels as "nothing looked wrong to you in that game", not as a check of each item.

The first look is kept: its files are in `backups\2026-11-23_135125-REAV-before-swap`, `backups\2026-11-23_135126-CERB-before-swap` and `backups\2026-11-23_135127-MLCH-before-swap`, its scripts and picture in `new-units\round1`.

One game was played with the first look, on 23 Nov 2026 at 12:42. Its engine log (`debug\debug.log` of that time) shows three things. It has the line `Unit cost of 954 derived from 5 units totalling 4770 credits`, and 4770 is 120 + 700 + 1100 + 950 + 1900. The logs of the games before the Arbalest say `1 units totalling 120 credits`, and those since the Arbalest (`Cost=700`) say `2 units totalling 820 credits`. So the three new costs (1100, 950, 1900) came on top: the rules of all four units were read. It has no line with `Failed to parse INI file content`, so the name `REAVZAP` was accepted. And the game ran to a normal exit. **[FILES]** What the units, their weapons and the burst looked like in that game was not reported. **[UNTESTED]**

The Reaver also carries the first NEW animation: a line `9001=REAVZAP` under a new header `[Animations]` in `Standard.ini`, an art section `[REAVZAP]` in `artmo.ini`, and the sprite file `reavzap.shp` in the game folder (a renamed copy of a stock sprite). **[FILES]** That was not enough. On 23 Nov 2026 the game's program was read (10.8): for an animation that map code adds, the game takes settings and picture only from a section in the map code itself, and `Standard.ini` had no `[REAVZAP]` section. So the burst was most likely never drawn, although its name was accepted and nothing else was wrong. Nobody reported seeing it or missing it. **[UNTESTED]** Since 23 Nov 2026, 21:52, `Standard.ini` has that section; it went in as the pack `REAVFIX` (10.8). Whether the burst shows now is open question 15.

### 10.8 Packs: an infantry unit, an animation fix, four buildings on a map

On 23 Nov 2026 at 21:52 three more things went in. They are not vehicles, so a second installer put them in: `arbalest-tank\kit\packs.py`. It works like the first one (10.7), marks what it writes with `; >>> PACK` and `; <<< PACK` lines, and both installers can be used side by side. **[FILES]** A game with all three was played that evening, and the same night the pictures of the buildings and the body of the infantry unit were made anew (both below). After a second game, on 24 Nov 2026, the buildings got moving parts and the Stormspire's bolt was put right (also below). After a third game that afternoon the Stormspire's reach was cut back to its range ring (13.5).

```powershell
python -I "arbalest-tank\kit\packs.py" status
python -I "arbalest-tank\kit\packs.py" verify DOOM
python -I "arbalest-tank\kit\packs.py" install "new-infantry\DOOM" --dry-run
python -I "arbalest-tank\kit\packs.py" remove DOOM
```

- `install` refuses while the game or the client runs, and when a name, a number or a file collides. It first copies the files it will change into `backups\<time>-pack-<NAME>-before-install`, then writes, then runs its checks. If one check fails it puts everything back and says `NOT INSTALLED`.
- `remove` takes exactly those things out again and keeps them in `backups\<time>-pack-<NAME>-removed`.
- `verify` repeats the checks for an installed pack. On 23 Nov 2026 they were 5 (REAVFIX), 48 (DOOM) and 74 (SITE), all passed, and the check of the four tanks still said `0 FAIL, 0 WARN`. Since 24 Nov 2026 `SITE` has 109 checks: it carries ten animations instead of four, and the section of every animation in the map is compared with its copy in `artmo.ini`. All passed, and the tanks' check still says `0 FAIL, 0 WARN`. **[FILES]**
- Install, a damaged file, a refused second install and removal were tried on a sandbox copy with 64 checks (`arbalest-tank\kit\tests\test_packs.py`). After removing all three, `Standard.ini`, `artmo.ini` and the map were the same as before, byte for byte. **[FILES]** On 24 Nov 2026 the test ran again with the third version of `SITE`: 70 checks, all passed. **[FILES]**

**The first game with the packs.** 23 Nov 2026, 22:04 to 22:09: Standard, (6) Kalifornia Crisis.

- The engine log lists six starting unit types that cost 5370 together (the five of before, 4770, and the Doomsayer's 600), has no line `Failed to parse INI file content`, and the game ended normally. **[FILES]**
- The scenario the client put together for that game (`spawnmap.ini`) has `[Animations]` with 9001, 9011 and 9012 from `Standard.ini` and 86101 to 86104 from the map, and `[WeaponTypes]` and `[Warheads]` likewise. So the client merges sections of the same name from the map and from the mode file key by key; neither replaces the other. **[FILES]**
- Your report after that game: "everything looks good. I wouldn't say perfect, but it's good", and that the way it works "is almost perfect". **[CONFIRMED]** 23 Nov 2026, as one answer for everything: no single item was named and no screenshot came. Read it as: nothing looked broken to you. Which things you looked at was not said; the log shows only that the Doomsayer was one of the six starting unit types. Whether the Reaver's bolt now ends in a burst, whether the marker, the bombs and the blast show, and whether the buildings' lights pulse was not said. **[UNTESTED]**
- The same report asked for two corrections. The new art must have the realistic detail of the game's own buildings (you named the power plant and the radar). And the Doomsayer must be a figure of his own, not the Flak Trooper in other colours. Both were done the same night and installed at 23:21, and once more at 23:34 with two corrections (below).

**The second game.** 24 Nov 2026, about 10:50: Standard, (6) Kalifornia Crisis, with the second version of the art. You sent a screenshot (taken 10:53) and a report.

- Your words: "everything looks better, everything looks nice", "The graphics are way better", "everything looks realistic". **[CONFIRMED]** 24 Nov 2026 for the look of the four buildings in the game.
- The screenshot shows all four on the plaza, each with its coloured light on the ground, their house-colour parts in your teal, `+$60` over the Black Vault, the Stormspire shooting violet lightning, and the Doomsayer's icon in the infantry tab. **[CONFIRMED]** 24 Nov 2026 (your screenshot). You wrote that you love the lights that came "when we took control over it". Whether the coloured light is there before capture was not said. **[UNTESTED]**
- Fault 1, in your words: the middle of the Stormspire "is not moving. It doesn't have animation. The same as the power plant", and the dishes of the Array should move or light up. Measured afterwards: the animations of the second version only let glowing pixels grow brighter and dimmer by about a sixth, and on the Array that was 58 pixels. The game's own buildings redraw 2,000 to 12,000 pixels per frame. **[FILES]**
- Fault 2: the Stormspire's bolt started in the air above the tower. Measured on the screenshot: 30 pixels above the middle of the ball. **[FILES]**
- Both were put right the same day (the third version, below).

**The third game.** 24 Nov 2026, 14:06 to 14:10: Standard, (6) Kalifornia Crisis, with the third version of the buildings. You sent a screenshot (taken 14:10) and a report.

- Your words: "Perfect. Everything works just fine. I love how everything is." and "everything looks so perfect right now. Almost so perfect." **[CONFIRMED]** 24 Nov 2026, as one answer for everything: no single building or animation was named.
- The screenshot shows the Stormspire and the Black Vault captured, in your teal. The Stormspire's bolt starts in its ball, and the cage of claws is round the ball. The Vault has a flag on each of its two flagpoles and two glints of light. The selected Stormspire draws a range ring in your colour. The Doomsayer's icon is in the infantry tab. **[CONFIRMED]** 24 Nov 2026 (your screenshot). The flags, the claws and the glints exist only in the animation files, so the game draws both animation layers. A still picture cannot show that they move.
- The engine logs of that game and of a short one a minute before it list six starting unit types that cost 5370 together, have no line `Failed to parse INI file content`, and end normally. **[FILES]**
- The fault, in your words: "I can hit things further than its range". In the screenshot the bolt lands outside the ring. Measured on it: the ring is 8.47 cells wide to each side, and the bolt landed 10.12 cells from the middle of the tower. **[FILES]**
- The cause was the game's high-ground bonus. It was put right the same day at 14:27 with one changed line in the map file (13.5). **[FILES]** Not seen in the game. **[UNTESTED]**
- Not said: how the buildings look before capture and when damaged, and whether anything is too bright, too fast or too slow. **[UNTESTED]**

**What a new animation needs.** This was read in the game's program (`gamemd.exe`) on 23 Nov 2026, not seen in the game. **[FILES]** for the program, **[UNTESTED]** for the effect.

1. The sprite file, loose in the game folder, named like the animation (`doomblst.shp` for `DOOMBLST`).
2. A line under `[Animations]` in the mode file (or in the map file), with a number no other line there uses.
3. A section with the animation's name **in that same file**, holding its settings (`Rate=`, `Report=`, `Layer=` and so on).

The reason for step 3: when a game starts, the game makes a new animation from the list and then asks every animation to load itself from the map code. An animation whose name has no section there loads nothing, not even its picture. The art file is read for animations only once, when the program starts, and at that time an animation from map code does not exist yet. A copy of the section in `artmo.ini` does no harm and is kept for tools that read the art file.

The same holds for the animation of a building that a map adds (`ActiveAnim=`). A vehicle is different: it loads its art from `artmo.ini`. The Arbalest proved that. **[CONFIRMED]** 22 Nov 2026. An infantry unit loads its art from `artmo.ini` too: the Doomsayer's icon, which only his art section names, is in the infantry tab. **[CONFIRMED]** 24 Nov 2026. The same is expected for the picture of a projectile; his flare is the first here, and it was never named in a report. **[UNTESTED]** (The stock game lists some projectile pictures under `[Animations]` and leaves others out, for example `TORPEDO`; the flare `DOOMFLR` is not listed.)

**REAVFIX.** One section, `[REAVZAP]`, in `Standard.ini`: the settings the Reaver's impact animation already had in `artmo.ini` (10.7). Nothing else.

**DOOM, the Doomsayer.** An infantry unit for every side, built at a Barracks (`Prerequisite=BARRACKS`, `Cost=600`). He fires a small flare rocket; where it lands a red marker beam stands for a moment, then three bombs fall and go off.

- The idea, a marker that calls ordnance down after a short wait, is borrowed from other games. The mechanism is the game's own: the warhead has `PreImpactAnim=` (an animation that plays first; the damage comes when it ends), the way the stock Hammer Defense and the Athena strike have it.
- Every block is a stock block with new names and numbers: the rules from the Flak Trooper `[FLAKT]`, the rocket from `[WallbusterP]`, the warhead from `[HammerWH]`, the two animations from `[SWMARK]` and `[MINIMISS]`. `lint-weapon DoomFlare` passes.
- The flare (`doomflr.shp`), the marker with the falling bombs (`doommark.shp`, 40 frames) and the blast (`doomblst.shp`, 25 frames) are new pictures, painted by script (`new-infantry\build_effects.py`).
- The body. From 21:52 to 23:21 on 23 Nov 2026 `doom.shp` was the Flak Trooper's sprite in other colours. You asked for a real figure instead. Since 23:21 it is an original one: a hooded spotter in a long indigo coat with a house-colour hood and mantle, a glowing visor, a radio pack with a tall aerial and a stubby flare launcher. It is a jointed 3-D figure (`new-infantry\doomsayer.py`), posed for every picture and drawn with the game's camera (`arbalest-tank\kit\sprites\figkit.py`). No pixel comes from a stock sprite. **[FILES]** Not seen in the game. **[UNTESTED]**
- The file holds 301 pictures and 301 shadows in the order of the game's `[FlakSequence]`: standing, walking, firing, dropping prone, crawling, getting up, firing prone, two deaths, two idle moves, cheering and the parachute picture. So the art entry keeps `Sequence=FlakSequence`. Measured on the game's own troopers first: the eight facings run N, NW, W, SW, S, SE, E, NE; the soles are 0 to 3 pixels below the middle of the canvas; a standing body is 22 to 27 pixels tall; shadows are about half as long as a building's. **[FILES]**
- The build (`new-infantry\build_figure.py`) stops if a picture is empty, if one touches the edge of the canvas, or if the last pictures of a death differ from each other (the body must lie still). `new-infantry\DOOM\check_sheet.png` shows every move. **[FILES]**
- With the new body two art lines changed: `FireUp=2` (the flare leaves on the third firing picture) and `PrimaryFireFLH=30,36,192` (the launcher's mouth on that picture). The icon shows the new figure. **[FILES]** Whether the flare leaves at the launcher in the game has not been seen. **[UNTESTED]**
- Corrected at 23:34: the two idle moves and the cheer are each drawn in one direction only. The letter in their sequence line (`Idle1=56,15,0,S`) is a map direction: map south is the lower left of the screen (standing picture 3), map east the lower right (standing picture 5). Measured on the Flak Trooper: its Idle1 pictures equal its standing picture 3, its Idle2 pictures equal picture 5, its first death starts as picture 3 and its second as picture 5. The first build of the new body had drawn the idle moves and the cheer one step off (as pictures 4 and 6); he would have jumped an eighth of a turn whenever he idled. **[FILES]**
- One line of the Flak Trooper was left out on purpose: `Fearless=yes`. With it a soldier never drops prone.
- He exists in Standard games only, like the tanks. The lists he needs are in `Standard.ini`: `[InfantryTypes]`, `[WeaponTypes]`, `[Projectiles]`, `[Warheads]`, `[Animations]`.

**SITE, the Black Site.** Four new buildings that stand on one map, (6) Kalifornia Crisis, on the raised plaza in its middle, around the tech airfield. They belong to nobody until an Engineer captures them.

| Building | ID, cells | What it gives its owner | Copied from |
|---|---|---|---|
| Helion Reactor | `CAHLIO`, 3x3 | power (600) | Tech Nuclear Plant `[CANRCT]`, without its death explosion |
| Skywatch Array | `CASKYW`, 3x3 | shows the whole map | Tech Satellite Hack Center `[CACOMN]` |
| Black Vault | `CAVALT`, 3x3 | credits (60 at a time) | Tech Deposit Bank `[CABANK]` |
| Stormspire | `CASPIR`, 2x2 | a lightning tower that defends | capture keys of the Tech Turret `[CACANN]`, weapon of the Tesla Coil with violet bolts and, since 24 Nov 2026, without its high-ground bonus (13.5) |

- The buildings are in the map file itself: twelve added lines (four under `[Structures]`, four under `[Waypoints]`, one each under `[Triggers]`, `[Events]`, `[Actions]`, `[Tags]`) and one block at the end with `[BuildingTypes]`, `[Animations]`, the rules and the animations' sections. Stock maps add buildings of their own the same way. Taking those lines out again gives the stock map, byte for byte. **[FILES]**
- So they are on that map in every game mode, and on no other map.
- The trigger is a copy of the one the stock King-of-the-Hill maps use: at the start of the game it uncovers the ground around four waypoints, here the four buildings, so that you can see them from the first second.
- Each building carries a coloured light (the keys the stock Tech Protector has).
- Their art is in `artmo.ini`; their sprites are eleven files: for each building its picture (`cghlio.shp`), its main animation (`cghlio_a.shp`; the Stormspire has none) and its light animation (`cghlio_l.shp`). The pictures were made by script (`new-buildings`), measured against thirty of the game's own buildings. The map renderer that ships with the client draws all four on their lots: `new-buildings\SITE.png`. That is not the game, and it shows one moment of each animation only.
- Second version of the pictures, 23 Nov 2026, 23:21. The first pictures were clean grey shapes. Measured beside the game's Allied and Soviet power plants and the Soviet radar they had 70 to 93 colours per sprite and 80 to 90 % plain grey, against 104 to 134 colours and 19 to 26 % grey in the game's. The kit was rewritten to shade in true colour first and reduce to the palette afterwards (`arbalest-tank\kit\sprites\structkit.py`; ready-made parts in `new-buildings\parts.py`): mottled brick, sandstone and paving, polished steel with dark seams and reflections, brass and copper, riveted house-colour plates in pale stone frames, lit windows, a dark line round every part. All four buildings were modelled anew on it. Only the eight sprite files changed: the rules, the map lines and the art entries are the same, byte for byte. **[FILES]**
- How they were judged: on a scratch copy of the map the client's map renderer drew the plaza with the four buildings and four of the game's own placed beside them (Allied power plant, Tesla reactor, Soviet radar, Allied barracks). **[FILES]** In the game they look right to you (the second game, above). **[CONFIRMED]** 24 Nov 2026.
- They belong to nobody at first. The client's map renderer draws their house-colour parts light grey in that state; how the game colours them before capture has not been reported. **[UNTESTED]** After capture they take the owner's colour: teal in your screenshot. **[CONFIRMED]** 24 Nov 2026. The buildings carry colour of their own as well: brick, sandstone, brass, copper and glass.
- Corrected at 23:34: the Black Vault and the Stormspire got more house colour (a frieze, the tower bands and the ring under the dome; a band round the plinth and a collar under the coils). It is now 7.7 % of each sprite instead of 3 to 4 %, so the owner's colour can be read after capture. The Reactor has 11 %, the Array 7.5 %; the game's power plants and barracks have 8 to 14 %. **[FILES]**
- Third version, 24 Nov 2026, 12:51: the buildings move. Measured first on the game's own files: a main animation there redraws whole moving structures (the Tesla reactor 6,000 pixels per frame, the tech nuclear plant 10,800, the pump of the oil derrick 2,800). Its file holds the frames for the healthy building, then those for the damaged one, and where its entry says `Shadow=yes` one shadow per frame after all the pictures. Lights are separate small files with `UseNormalLight=yes`, so they stay bright on a dark map. Stock buildings that start without an owner keep whole parts only in the animation (the oil derrick's pump is not in its building picture; the Tech Protector's building picture is empty). **[FILES]** So the game must draw such animations before capture too; for our four that has not been seen. **[UNTESTED]**
- What moves now:

| Building | Main animation (drawn in the map's light) | Light animation (full brightness) |
|---|---|---|
| Skywatch Array | 40 frames: the big dish and its yoke turn once round, their shadow with them; the two small dishes spin the other way | 16 frames: the beacon on the lattice mast and the lamp on the roof aerial flash in turn, the screens behind the windows flicker |
| Helion Reactor | 36 frames: steam rises from the two coolant towers | 36 frames: two brass rings swing round the ball in opposite directions, the ball boils and swells, lamps run round the drum, the aerial lamp flashes |
| Black Vault | 24 frames: a flag flies on two towers, the wheel of the vault door turns | 24 frames: the lantern sends a beam round, light runs round the windows under the dome, the searchlight swings, the gold glints |
| Stormspire | none | 24 frames: lightning climbs the insulator stack, the three coils light up in turn, the ball flares, the cage of claws turns round the ball, the capacitor lamps light in turn |

- How a frame is made (`new-buildings\anim.py`): the whole building is rendered again with the parts in their new place, and the frame keeps the pixels that differ from the building picture. So a moving part hides what is behind it, and the dish's shadow moves over the paving. The big dish, the reactor's rings, the flags and the claws exist only in the animations, not in the building pictures, as on the game's own oil derrick. **[FILES]**
- The art entries: `ActiveAnim=` is the main animation; `ActiveAnimDamaged=` is the same file from its damaged frames on (`[CASKYW_AD]` has `Start=40`); `ActiveAnimTwo=` is the light animation, with a `ZAdjust` that is 20 nearer so that it is drawn in front. The Stormspire has only the lights. That makes ten animations instead of four; each has its line under `[Animations]` and its section in the map file. **[FILES]**
- What the third version changed in the still pictures you had approved: the Reactor's ball now stands on a narrow brass pedestal instead of in a wide bowl, and its level steel ring is wider, on arms that stand further out, so that the two rings can swing; the big dish, the flags (on two new flagpoles) and the Stormspire's claws are no longer in the building pictures; lamps that flash are drawn switched off there; and every picture was rendered again, which moved some shadow edges by a pixel. **[FILES]**
- The reactor's rings pass in front of the glowing ball and behind it. Two animation files cannot weave through each other, so the rings are in the light file together with the ball and are drawn at full brightness too. The same holds for the Stormspire's claws. On a dark map, or before the coloured ground light is on, this brass may look too bright against the building. That cannot be judged outside the game. **[UNTESTED]** The cure would be darker brass in the two light files. (In your screenshot of 24 Nov 2026, 14:10, the claws do not stand out on the captured Stormspire under its violet light. That is a reading of the picture, not something you said, and it says nothing about the time before capture.)
- The speeds were chosen for the game speed your client is set to ("6 Fastest": `GameSpeed=0` in `spawn.ini`). Every animation shows a picture for four game frames (`Rate=220`). If that speed runs at 60 game frames a second, the dish turns once in 2.7 seconds and the rings in 2.4, and one charge of the Stormspire takes 0.8. At half that speed everything takes twice as long.
- Two mistakes of the tools that this work found. A part added to a model moved the grid of its shadow map by a fraction of a cell, and with it every shadow edge of the building; it showed as stray pixels all over the Black Vault's animation. The grid now starts on a whole number. And the faint shadows the reactor's rings throw showed as single pixels blinking on still walls: the reactor's main animation now holds the steam only, and a main frame keeps a changed patch of the still building only if it touches a moving part or has six pixels or more. The first cure changes every picture a little, so the scripts no longer give the files of the second version; those are kept as a pack (below). **[FILES]**
- The Stormspire's bolt: `PrimaryFireFLH=0,0,531` became `0,0,320`. The game counts a building's fire point from the middle of the sprite canvas, which is the north corner of its foundation: 15 pixels up for every 104 of height. The first value was counted from the middle of the 2x2 foundation, one cell lower on the screen, and those are the 30 pixels of your screenshot. The game's own Tesla coil confirms the rule: its `0,0,375` lands on the middle of its ball. **[FILES]** In your screenshot of 24 Nov 2026, 14:10, the bolt starts in the ball. **[CONFIRMED]** 24 Nov 2026
- The Stormspire's reach. From 21:52 on 23 Nov to 14:27 on 24 Nov 2026 its weapon had the Tesla Coil's projectile `InvisibleHigh`. That projectile gets the game's high-ground bonus, the plaza is four height levels above the streets, and so the tower hit street targets up to 10.1 cells away while its ring shows 8 (the third game, above). Since 14:27 the weapon has `Projectile=Invisible`, the same projectile without the bonus: one changed line in the map file. Now it reaches 8 cells on the plaza and 7.8 down on the streets. The installer's 109 checks pass, and the new check `new-buildings\check_range.py` ends with `Result: 0 FAIL` (before the change: `72 cells outside the ring can be hit`). **[FILES]** Not seen in the game. **[UNTESTED]** The rule behind it, read in the game's program, is in 13.5.
- Seen since: after a game with the third version your report was "Perfect. Everything works just fine", and your screenshot shows parts that exist only in the animations, lit glints among them (the third game, above). **[CONFIRMED]** 24 Nov 2026, as one answer for everything. Still not reported, and not visible in that screenshot: the frames for the damaged building (torn flags, a sooty dish with a hole, thinner steam), the moving shadows on the ground, and the buildings before capture. **[UNTESTED]**
- What is still not at the level of the game's art: the surfaces are a little cleaner (the game's artists drew more small irregular wear), and the damaged pictures are scorch marks and holes placed by rule, not modelled wreckage.
- The first pictures are kept: `new-buildings\round1` (and `new-infantry\round1` for the first Doomsayer body). To go back, remove the pack and install the folder `round1\SITE` (or `round1\DOOM`) instead. That was tried on a sandbox copy on 23 Nov 2026: both installed and passed their checks. **[FILES]** The second version of the buildings (the pictures of your screenshot of 24 Nov 2026, with lights that only grow brighter and dimmer and the bolt height 531) is kept as a pack too: `new-buildings\round2\SITE`. To go back to it, remove `SITE` and install that folder. Tried on a sandbox copy on 24 Nov 2026. **[FILES]** The third version as it was in your screenshot of 14:10, with the long reach, is kept as `new-buildings\round3\SITE`. Tried on a sandbox copy the same day: it installs, and the range check fails on it, as it should. **[FILES]**
- The first ID that was tried for the reactor, `CAHELI`, turned out to be a stock building (a helipad). Check every new name against the stock files; the installers do.
- A stock map file was changed. Do not play online with it (10.6).
- Installing or removing `SITE` changes the lists of buildings and animations that this map carries. A game that was saved on this map before such a change may not load afterwards; start a new game. **[UNTESTED]**

**Taking them out again.** Close the game and the client. Each line removes one pack and leaves the others alone, so a problem can be narrowed down. If a game on Kalifornia Crisis does not start, take `SITE` out first.

```powershell
python -I "arbalest-tank\kit\packs.py" remove SITE
python -I "arbalest-tank\kit\packs.py" remove DOOM
python -I "arbalest-tank\kit\packs.py" remove REAVFIX
```

---

## 11. What is installed right now

As of 25 November 2026.

| Thing | Where | State |
|---|---|---|
| Nexus model on the Bulldog (Route A): retired | Until 24 Nov 2026, 22:07: `Standard.ini` lines 42 to 76. The block is kept in `backups\2026-11-24_220747-nexus-takeover-retired`. The files `FTNKNEXUS.vxl/.hva`, `FTNKNEXUSTUR.vxl/.hva` are still in the game folder | Seen working on 2 April 2026. **[CONFIRMED]** Taken out when the Nexus became a unit of its own (21); the Bulldog is expected to be the game's own again. **[UNTESTED]** Nothing reads the four files now; the first-test recipe of section 4 copies them. |
| The Nexus tank (a unit of its own, by the vehicle installer) | `Standard.ini`: `7420=NEXS`, the lines 9029 to 9033 under `[Animations]`, `9423=NexusShard` under `[WeaponTypes]`, a block between `; >>> UNIT` and `; <<< UNIT` lines; a block at the end of `artmo.ini`; `NEXS.vxl/.hva`, `NEXSTUR.vxl/.hva` and `NEXSTUR1` to `NEXSTUR7` (`.vxl/.hva`), `nexsicon.pcx`, `nexsuico.pcx`, five sprite files (`nexsmuz`, `nexsorb`, `nexsspl`, `nexshit`, `nexsexp`) | First installed 24 Nov 2026, 22:07, with a red laser, and once more at 22:17 with its end made the stock way. Since 25 Nov 2026, 00:05: a new paint, a turret that glows in eight stages as its weapon charges, and the starburst (21.3). Seen in the owner's game of 25 Nov 2026 (10:40): the screenshot shows its icon with the name NEXUS in the vehicle tab, several built tanks in the new paint with the owner's teal on the decks and the coil lit. **[CONFIRMED]** 25 Nov 2026 (screenshot). The owner's report of that game: it "does not seem to hit the targets correctly and effectively"; the screenshot shows the shot bursting in the air, far from what was aimed at (21.1). **[CONFIRMED]** 25 Nov 2026. Since 25 Nov 2026, 11:34, the third version is installed: the orb flies to the target and does the damage itself, and throws five rays from where it hits a vehicle or a soldier (21.3). It passes the check, and so does everything else. **[FILES]** The owner played three times with it installed on 25 Nov 2026, from 12:29 to 12:35, from 14:21 to 14:28 and from 17:04 to 17:09 (the last two on (6) Kalifornia Crisis, by `spawn.ini`); the logs end normally, have no line `Failed to parse INI file content`, and hold the same developer warnings as the clean games before. **[FILES]** Whether a Nexus was built in them is not known. **[UNTESTED]** The owner's report of 25 Nov 2026 (afternoon): a flyer of ours, forced (Ctrl) on the owner's own soldiers, tanks and aircraft, did them no damage; buildings it did damage. **[CONFIRMED]** 25 Nov 2026 (report). The cause, read in the files: the Tempest's warhead and both of the Nexus's had `AffectsAllies=no`. Since 14:41 the line is out of all three, and the Nexus went in again as number 7420, with its animations as 9029 to 9033 (13.10). It passes the check. **[FILES]** Not tried in a game. **[UNTESTED]** |
| The Nexus tank as a bundle | `nexus-tank` | The four original model files, the scripts, `paint.py`, the finished bundle `NEXS`, the other paint `paint-B`, the version of 24 Nov 2026 in `round1` and the second version of 25 Nov 2026 in `round2` (each installs as it is, 21.5), the owner's screenshot in `evidence-2026-11-25`, and `PREVIEW.png`. Running the five build lines of 21.4 again gives the same files, byte for byte (checked 25 Nov 2026 for the third version: the 38 files of `nexus-tank\NEXS`, 25 of them in the game folder, and the 23 files of `paint-B`). **[FILES]** |
| Arbalest Tank (Route B) | `Standard.ini` lines 97 to 164; `[ARBL]` at the end of `artmo.ini`; `ARBL.vxl/.hva`, `ARBLTUR.vxl/.hva`, `arblicon.pcx`, `arbluico.pcx` | Seen on 22 Nov 2026 with placeholder parts (a copy of the Nexus model, a copy of the Catastrophe icon): icon and model showed. **[CONFIRMED]** Later that day it got a model and an icon of its own (the "rail sniper" design, made by script) and the line `PrimaryFireFLH=298,0,123`. The new files pass the check of section 4, step 6. **[FILES]** That night five questions were asked about it: is the new icon in the vehicle tab, does the model show, does it face the way it drives, does the turret sit on the hull or float above it, does the shot leave from the tips of the rails. Your answer was "Yes to all this". **[CONFIRMED]** 22 Nov 2026. (The turret question was an either-or; the yes is read as: it sits on the hull.) The first game after the change ran to a normal end, and its engine log has no kind of line that the earlier logs did not have. **[FILES]** It still has the Bulldog's gun and stats. **[FILES]** On 23 Nov 2026 at 14:29 that model and icon were replaced by a rebuilt version (the same rail sniper, made after the game's steel-blue tanks) with `PrimaryFireFLH=335,0,117`. It passes the check. **[FILES]** After a game with the rebuilt look your report was "everything was perfect". **[CONFIRMED]** 23 Nov 2026, as one answer for everything (10.7). |
| Test blocks from December 2025 | `Standard.ini` lines 78 to 95, `[APOC]` and `[HTNK]`; `apoc_htruck.*`, `test_htruck.*` | Still in the file, and merged into the scenario of the 22 Nov game. **[FILES]** By the same mechanism as the Bulldog block they should make the Catastrophe Tank cost 1 with 9999 strength and the Rhino cost 1, each shown with a test model; nobody has reported what that looks like. **[UNTESTED]** To get the stock Rhino and Catastrophe back, delete both test blocks: from the `; ====` line above `; APOCALYPSE TANK TEST` down to the `Owner=` line under `[HTNK]` (lines 78 to 95 today). |
| Old copies of the Nexus model | `FTNKNEXUS.vxl.bak`, `FTNKNEXUSTUR.vxl.bak` (April 2026); `FTNKNEXUS.vxl.backup`, `FTNKNEXUS.hva.backup` (November 2025) | The two `.bak` files are the Nexus as it was before its lighting remap. The two `.backup` files are older still. **[FILES]** None of them is the working model. Do not restore them. |
| Old files the game is not expected to use | `Mental Omega\rulesmd.ini`, `artmd.ini`, `INI\FutureTank.ini`, `create_mix.py`, `TANKIETUR.*` | Old files. For the first two see section 2. Harmless as long as the scripts among them are not run. |
| Backups | `backups\2026-11-22-arbalest` | `Standard.ini.before-arbalest` (the file from before the Arbalest), `MANIFEST.txt` (a file list from the first install; it describes the placeholder files, not the present model), `UNDO.ps1` (10.3). No backup has been made with the six lines of 3.5 yet. The first run of those lines makes it. |
| Old guide documents | `backups\2026-11-22-old-writeups` | The seven old documents as they were before they got their notes on 22 Nov 2026, and the first draft of this guide. No INI files. |
| The guide's folder before it was published alone | `backups\2026-11-25-before-github-replace` | The whole folder `MentalOmega-Modding-Guide` as it was on 25 Nov 2026 before the old documents left it: docs `01` to `09`, `QUICK-REFERENCE.md`, the first `README.md`, the 13 old scripts, `blender_addon`, `hva and vxl`, the extracted examples, and its git history with the two commits of 12 Dec 2025. 111 files, compared one by one (SHA-256) with the folder they came from. Its remote line was then removed, so that the old history cannot be pushed from there by mistake. To read an old document, open it there; never copy one back into the guide's folder (section 9). |
| The Arbalest's placeholder parts | `backups\2026-11-22_224520-arbalest-before-new-model` | The six `ARBL` and `arbl` files and `artmo.ini` as they were before the Arbalest got its own model. How to put them back is in 10.2. |
| Tank designs and model tools | `arbalest-tank` | Four designs for the Arbalest. Options 1 to 3 with a picture of all three (`PREVIEW.png`); option 1 was the installed one from 22 to 23 Nov 2026. Option 4 (`option-4-rail-sniper-rebuilt`) is the rebuilt rail sniper that is installed now, with its script and its own `PREVIEW.png`. And the tools that made them (`kit`). How they are used is in section 18. |
| The Arbalest's first own model | `backups\2026-11-23_142959-arbalest-before-new-model`; also `arbalest-tank\option-1-rail-sniper` | The six files of the look confirmed on 22 Nov 2026, and the `artmo.ini` of the moment before the rebuilt look went in. How to put that look back is in 10.2. |
| Reaver, Cerberus, Moloch (Route B, by installer) | `Standard.ini`: `7412=REAV`, `7413=CERB`, `7414=MLCH` and three blocks between `; >>> UNIT` and `; <<< UNIT` lines; three blocks at the end of `artmo.ini`; `REAV`, `CERB` and `MLCH` model and icon files | Installed 23 Nov 2026 (10.7). Each has a model and an icon of its own and a weapon of its own: violet lightning, three streams of fire, a siege shell with a red shock ring and screen shake. All pass the check. **[FILES]** Their look was rebuilt on 23 Nov 2026 at 13:51 (10.7). The engine log of a game played earlier that day shows that their rules were read. **[FILES]** After a game with the rebuilt look your report was "everything was perfect". **[CONFIRMED]** 23 Nov 2026, as one answer for everything (10.7). The Reaver's impact burst is the exception: it was most likely never drawn (10.7). |
| First new animation | `Standard.ini`: `[Animations]` with `9001=REAVZAP`, and since 23 Nov 2026, 21:52, a section `[REAVZAP]` between `; >>> PACK REAVFIX` lines; `[REAVZAP]` in `artmo.ini`; `reavzap.shp` | The impact burst of the Reaver's lightning, a renamed copy of a stock sprite. Its name was accepted, but its picture was most likely never loaded while its settings stood only in `artmo.ini` (10.7, 10.8). **[FILES]** Whether it shows now has not been seen. **[UNTESTED]** |
| The three new units as bundles | `new-units` | For each unit a folder with its files (the rebuilt look), `rules.ini`, `art.ini` and `bundle.json`, the scripts that built them, and `PREVIEW.png` (first look and rebuilt look side by side). The scripts, picture and files of the first look are in `new-units\round1`. |
| The first look of the three units | `backups\2026-11-23_135125-REAV-before-swap` and the `CERB` and `MLCH` folders next to it | The six model and icon files of each unit and `artmo.ini` as they were before the rebuilt look. How to go back is in 10.7. |
| Installer records | `backups\unit-bundles` | One folder per installed unit: what was installed, and both INI files as they were just before. |
| Seraph, Tempest, Nova (hovering craft, by the vehicle installer) | `Standard.ini`: `7415=SRPH`, `7417=NOVA`, `7421=TMPS`, the lines 9013 to 9015, 9018, 9019 and 9034 to 9037 under `[Animations]`, and three blocks between `; >>> UNIT` and `; <<< UNIT` lines; three blocks at the end of `artmo.ini`; the `SRPH`, `TMPS` and `NOVA` model and icon files, nine sprite files (`srphmuz`, `srphhit`, `srphglo`, `tmpsmuz`, `tmpssmk`, `tmpshit`, `tmpsglo`, `novabls`, `novaglo`), `novaorb.vxl/.hva` and `tmpsmsl.vxl/.hva` | Installed 24 Nov 2026, 21:25 (20.5). Each has a model with a part that turns, an icon, a weapon and animations of its own. Each passes the check, and the checks of the tanks, the packs and the Stormspire's reach pass as before. **[FILES]** The owner's screenshot of 25 Nov 2026 shows the three icons, SERAPH, TEMPEST and NOVA, in the vehicle tab. **[CONFIRMED]** 25 Nov 2026 (screenshot). Nothing else about them has been reported: whether one was built, how it flies and shoots. **[UNTESTED]** Since 25 Nov 2026, 12:57, the Tempest fires a swarm of eight small missiles in place of its lightning, after the owner asked for an attack "suitable for a plane" (20.5); it was taken out and put in again for that. Every check passes. **[FILES]** The owner's games of 14:21 and 17:04 that day ran with it, and their logs are clean (see the Nexus row). **[FILES]** The report after it is about a flyer of ours forced on the owner's own units (below); nothing else about the swarm was said. **[UNTESTED]** At 14:41 the same day it went in once more, as number 7421, without the line `AffectsAllies=no` that its warhead had had since 12:57: the owner's forced attacks on their own units did no damage (13.10). It passes the check. **[FILES]** The Seraph's wide beam is the least certain piece; the same craft with another beam is ready (20.7). |
| The flyers as bundles | `new-aircraft` | The three build scripts, a folder per craft with its files, `rules.ini`, `art.ini` and `bundle.json`, the folder `SRPH-laser`, the folder `round1` (the Tempest with its lightning, as it was installed until 25 Nov 2026; it installs as it is, 20.7), and `PREVIEW.png`. Running the scripts again gives the same files, byte for byte (checked 25 Nov 2026: 81 files in the four folders, 31 of them in the game folder). **[FILES]** `candidates.py`, the folder `candidates` and `candidates\PREVIEW.png` are what the owner picked from. |
| Doomsayer (infantry, by the pack installer) | `Standard.ini`: `9421=DOOM` under `[InfantryTypes]`, lines under `[WeaponTypes]`, `[Projectiles]`, `[Warheads]` and `[Animations]`, a block between `; >>> PACK DOOM` lines; a block at the end of `artmo.ini`; `doom.shp`, `doomflr.shp`, `doommark.shp`, `doomblst.shp`, `doomicon.pcx`, `doomuico.pcx` | Installed 23 Nov 2026, 21:52 (10.8). A game with him was played at 22:04; your report was "everything looks good" (one answer for everything, 10.8). **[CONFIRMED]** 23 Nov 2026 as that one answer; nothing more specific was said. The log of that game lists him among the six starting unit types. **[FILES]** Since 23 Nov 2026, 23:21 (corrected at 23:34), his body is an original figure and the icon shows it (10.8); the installer's 48 checks pass and `lint-weapon DoomFlare` passes. **[FILES]** His icon is in the infantry tab in your screenshot of 24 Nov 2026. **[CONFIRMED]** Your report of that day ("everything looks nice") did not name him, so how the new body looks and moves in the game is not recorded. **[UNTESTED]** The same holds for the game of 14:06 that day: his icon is in the screenshot, and he was not named. |
| The Black Site: five buildings on (6) Kalifornia Crisis | `MapsMO\Standard\kalifornia.map`: fourteen added lines and a block between `; >>> PACK SITE` lines; a block at the end of `artmo.ini`; fourteen sprite files `cghlio`, `cgskyw`, `cgvalt`, `cgspir`, `cgvesl` (`.shp`, `_a.shp` except for `cgspir`, and `_l.shp`), 825,633 bytes together; since 25 Nov 2026, 15:04, also the lines of `[PreviewPack]` in the map and the lobby picture `MapsMO\Standard\kalifornia.png` | Installed 23 Nov 2026, 21:52 (10.8). Seen in the game of 22:04; your report was "everything looks good" (one answer for everything, 10.8). **[CONFIRMED]** 23 Nov 2026 as that one answer; nothing more specific was said. Since 23 Nov 2026, 23:21 (two of them corrected at 23:34), the eight sprite files were the second version (10.8); the installer's 74 checks passed, and the client's map renderer drew them on their lots. **[FILES]** Seen in the game of 24 Nov 2026: "The graphics are way better"; your screenshot shows them captured, in your colour, the Vault paying and the Stormspire shooting. **[CONFIRMED]** 24 Nov 2026. Since 24 Nov 2026, 12:51, the third version is installed (10.8): the buildings move, and the Stormspire's bolt height is 320 instead of 531. The installer's 109 checks pass and the map renderer draws them. **[FILES]** Seen in the game of 24 Nov 2026, 14:06: "Perfect. Everything works just fine"; your screenshot shows the bolt starting in the ball, the Vault's flags and the Stormspire's claws. **[CONFIRMED]** 24 Nov 2026, as one answer for everything (10.8). Since 24 Nov 2026, 14:27, the Stormspire's weapon has the projectile `Invisible`, so that it cannot hit anything outside its range ring (13.5); the 109 checks and the range check pass. **[FILES]** That change has not been seen in the game. **[UNTESTED]** Since 25 Nov 2026, 00:48 (again at 01:16 with its occupied picture), a fifth building stands with them: the Vessel, which soldiers can garrison (16.12). The installer's 135 checks and the range check pass, and the map renderer draws it on its lot. **[FILES]** Seen in the game of 25 Nov 2026 (10:40): "The vessel seems all right. Everything looks perfect. Everything is fine. I love how it garrisons people"; the screenshot shows it on the plaza. **[CONFIRMED]** 25 Nov 2026: it stands, and soldiers can garrison it. In the same message the owner asked whether it could not be made closer to photographs of the real one; two candidates made from photographs wait for a pick and are not installed (16.12). The owner's report of 25 Nov 2026 (afternoon): the map's picture in the skirmish screen, and the small one when a game starts, did not show the new buildings. **[CONFIRMED]** 25 Nov 2026 (report). Since 15:04 that day the pack also replaces both pictures; the installer's 137 checks and the range check pass (16.13). **[FILES]** The owner's game of 17:04 that day was on this map: the game loaded the new picture from the map and ended normally. **[FILES]** What the two pictures looked like was not reported. **[UNTESTED]** |
| The packs and what made them | `new-infantry` (Doomsayer, REAVFIX); `new-buildings` (the four buildings, the pack `SITE`) | Each has the build scripts, the finished pack folder and a `PREVIEW.png`. Running the scripts again gives the installed files, byte for byte: checked on 24 Nov 2026 for the eleven building sprites of the third version (every building was built twice), and on 23 Nov 2026 for the Doomsayer's body by drawing 31 of its 301 pictures again. **[FILES]** The first versions (installed from 21:52 to 23:21 on 23 Nov 2026) are in the two `round1` folders, the second version of the buildings (23 to 24 Nov 2026) in `new-buildings\round2`, the third version as it was before its reach was cut back (24 Nov 2026, 12:51 to 14:27) in `new-buildings\round3`. The building scripts of those folders are kept to read; the tools have changed since, so they no longer give those files. Each folder holds the finished pack, and that installs. `new-buildings\round4` holds the pack as it was before the Vessel (24 Nov 2026, 14:27 to 25 Nov 2026, 00:48), `new-buildings\round5` the pack as it was before the preview pictures (25 Nov 2026, 01:16 to 15:04; copied from the installer's record in `backups\2026-11-25_150425-pack-SITE-removed`). `new-buildings\PREVIEW.png` shows six moments of every animation; the files `anim.gif` in the five building folders show them moving. |
| Pack records | `backups\packs` | One folder per installed pack: a copy of the pack and a record of what was written. |
| The guide and the helper tool from before the afternoon of 24 Nov 2026 | `backups\2026-11-24-guide-before-range-fix-and-how-to-sections`, `backups\2026-11-24-mo_tool-before-animation-section-warning` | This guide as it was before the third game was recorded and sections 0 and 13 to 19 were added, and `mo_tool.py` as it was before it got its warning about an animation without a section (14.1). To go back, copy the kept file over the present one. The other tool changes of that afternoon are small and have no kept copy: the vehicle installer's `remove` no longer stops when a unit is removed twice within one second, and `make_sandbox.py`, `check_range.py`, `range_picture.py` and the two guide checks are new. |
| The guide and the helper tool from before the flyers | `backups\2026-11-24-guide-before-flyers-section`, `backups\2026-11-24-guide-before-flyers-were-built`, `backups\2026-11-24-mo_tool-before-flyer-width-note` | This guide before section 20 was written and before the flyers were built, and `mo_tool.py` as it was before its check accepted a flyer that is wider than long. Two more tool changes of that evening have no kept copy: `forge_build.py` takes a given seat height as it is (the Reaver still builds byte for byte), and `effects_sheet.py` was only used, not changed. |
| The guide and the helper tool from before the Nexus's second version | `backups\2026-11-25-guide-before-nexus-starburst`, `backups\2026-11-25-mo_tool-before-charge-turret-check` | This guide before section 21 was rewritten for the version of 25 Nov 2026, and `mo_tool.py` before its check looked at the turret files of a charge turret. To go back, copy the kept file over the present one. |
| The guide from before the Tempest's swarm | `backups\2026-11-25-before-tempest-swarm` | This guide as it was on 25 Nov 2026 at 12:50. No tool changed for the swarm. |
| The guide and two tools from before the Nexus's third version | `backups\2026-11-25-before-nexus-direct-hit` | This guide, `mo_tool.py` (before its warning about a weapon that only a projectile names) and the vehicle installer `unit_bundle.py` (before it could add a line under `[WeaponTypes]`), as they were on 25 Nov 2026 at 11:28. To go back, copy the kept file over the present one. |
| The guide and six tools from before the forced-attack cure and the preview pictures | `backups\2026-11-25-before-force-fire-fix` | This guide, `mo_tool.py` (before its warning about a line that spares a side), `packs.py`, `mapkit.py`, `make_sandbox.py`, `test_packs.py` (before they knew the preview pictures) and `new-buildings\make_pack.py`, as they were on 25 Nov 2026 before 14:41. The build scripts of the Nexus and the Tempest from before are in `nexus-tank\round3` and `new-aircraft\round2`. To go back, copy the kept file over the present one. |
| The guide and tools from before the playbook | `backups\2026-11-25-before-playbook` | This guide before section 1 became the playbook (`10-Adding-Units.md`), the guide with the playbook but before the fixes of the cold read (`10-Adding-Units-after-playbook.md`), and the tools as they were before that evening: `unit_bundle.py` (before `status` printed all six lists), `new-units\make_bundles.py` (before its count of rules sections was put right), `packs.py` (before the check for a stock sprite), `heights.py`, `forge.py` (its description) and the first `weapon_audit.py` (`weapon_audit_first.py`). To go back, copy the kept file over the present one. |
| The files from before the packs | `backups\2026-11-23_215212-pack-REAVFIX-before-install`, `backups\2026-11-23_215213-pack-DOOM-before-install`, `backups\2026-11-23_215214-pack-SITE-before-install` | `Standard.ini`, `artmo.ini` and the map as they were just before each pack went in. From the change to the second version at 23:21: `backups\2026-11-23_232138-pack-SITE-removed`, `backups\2026-11-23_232139-pack-DOOM-removed`, `backups\2026-11-23_232140-pack-DOOM-before-install`, `backups\2026-11-23_232142-pack-SITE-before-install` (the first sprites and icons are in the two `-removed` folders). From the corrections at 23:34: `backups\2026-11-23_233358-pack-SITE-removed`, `backups\2026-11-23_233359-pack-DOOM-removed`, `backups\2026-11-23_233400-pack-DOOM-before-install`, `backups\2026-11-23_233401-pack-SITE-before-install`. From the change to the third version of the buildings on 24 Nov 2026: `backups\2026-11-24_125128-pack-SITE-removed`, `backups\2026-11-24_125129-pack-SITE-before-install` (the sprites of the second version are in the `-removed` folder). From the change to the Stormspire's reach that afternoon: `backups\2026-11-24_142756-pack-SITE-removed`, `backups\2026-11-24_142757-pack-SITE-before-install`. |
| Stock reference | `stock-reference` | `rulesmo.ini`, `artmo.ini`, `soundmo.ini`, four icons (`cataicon.pcx`, `catauico.pcx`, `htnkicon.pcx`, `htnkuico.pcx`) |
| What was read in the game's program and measured | `arbalest-tank\kit\research` | `probe`: the listings of the parts of `gamemd.exe` and `Ares.dll` that this guide quotes (how map code and animations are loaded; the range test, the high-ground bonus and the range ring; the stages of a charge turret, 21.3; the order in which the kinds of block are read, the routine that throws pieces from an impact and the extension's splitting routine, 13.8 and 21.1; the gap between the shots of a salvo, the direction a homing shot leaves in and the turning of a spinning turret, 13.9), and the small read-only scripts that made them. `range`: the scripts that measured the ring on the screenshot of 24 Nov 2026, listed the stock buildings with a ring and printed the heights of the ground. `forge-notes`: the survey of the stock model files. Nothing in there changes a game file. |

Line numbers for `Standard.ini` in this guide are those of 22 Nov 2026. They shift as soon as lines are added or removed, so find a block by its header (`[ETNK]`, `[VehicleTypes]`, `[ARBL]`), not by its number.

---

## 12. Keeping this guide correct

This guide is only useful while its labels are true.

- When you see an **[UNTESTED]** item work in game, change it to **[CONFIRMED]** and add the date.
- When one turns out wrong, rewrite the sentence. Do not leave the wrong version beside the right one.
- Change one thing per test, so you know what the result belongs to.
- Add a line to the log below for every change to the guide.
- The guide is public on GitHub. Publish a change only when the owner asks ("Publishing the guide", below).

### Open questions worth testing next

1. Was the Arbalest built at a War Factory, or was it only seen as a starting unit? (That it shows, drives, carries its turret and shoots was answered on 22 Nov 2026 for the model it had then: section 11.)
2. Does the name show as "Arbalest Tank" in the sidebar tooltip?
3. Was an Arbalest among the starting units? What happens with `AllowedToStartInMultiplayer=no`?
4. Does the client show the "Interfering Files Detected" message, and does it only warn?
5. Do all four registered units show in the vehicle tab (Arbalest, Reaver, Cerberus, Moloch)? Four lines stand under `[VehicleTypes]` since 23 Nov 2026. (The engine log of the game of 23 Nov, 12:42, shows that the rules of all four were read: 10.7. Your report of that evening, "everything was perfect", did not say whether each was built from the sidebar.)
6. A new unit limited to one faction: `Owner=` together with `RequiredHouses=`, the way the stock Bulldog does it.
7. A changed `PrimaryFireFLH=` for a new model.
8. A unit in a second game mode.
9. A take-over block without the four lines that are probably not needed (section 5).
10. What do the Rhino and the Catastrophe look like and cost in a Standard game, with the December test blocks in place?
11. Is the Nexus laser silent? (By the files it was, while it sat on the Bulldog: its sound name is not in the game's sound file. That weapon is out since 24 Nov 2026; question 46 asks about the one of now.)
12. Do Notepad and VS Code save the two INI files without changing line endings or adding a byte-order mark?
13. Does the client notice an edit to `Standard.ini` that is made while it is open?

14. The three new weapons: do the Reaver's violet bolts, the Cerberus's fire and the Moloch's shell with its red ring and screen shake show and do damage? (Answered on 23 Nov 2026 with "everything was perfect", as one answer for everything; no single weapon was described.)
15. The Reaver's impact animation: does the bolt now end in a small blue-white burst? Until 23 Nov 2026, 21:52, it most likely never did (10.7). This is the first thing to look at in the next game: the Doomsayer's marker and blast and the buildings' lights reach the game the same way, so if the burst is missing, they are doubtful too.
16. The rebuilt look of the Arbalest, the Reaver, the Cerberus and the Moloch: does each model show with its turret on the hull, does it look at home next to the game's own tanks, and does each shot leave from the weapon's tip? A screenshot of one of them next to a stock dark tank would also show how close the preview pictures are to the game. (Answered on 23 Nov 2026 with "everything was perfect". No screenshot was sent, so how close the pictures are is still not measured.)
17. The Doomsayer: is his icon in the infantry tab of every side, and can he be built at a Barracks? (After the game of 23 Nov 2026, 22:04: "everything looks good", one answer for everything. Your screenshot of 24 Nov 2026 shows his icon in the infantry tab of the side you played.)
18. The Doomsayer under fire, with his new body (since 23 Nov 2026, 23:21): does he drop prone when he is hit, fire from the ground, get up again? Do both deaths look right, and does the body lie still at the end? Do his feet stay on the ground while he walks, or does he seem to slide or hover?
19. His weapon: does a red flare fly to the target, does the red marker beam with its rings stand there, do three bombs come down, and does the blast with its ring and smoke follow? Is the wait before the blast about right?
20. The Black Site: in a game on (6) Kalifornia Crisis, are the four buildings in the middle of the map, uncovered from the start, standing square on the plaza? (Your screenshot of 24 Nov 2026 shows all four on the plaza. Whether they are uncovered from the first second was not said.)
21. Do their lights pulse, and does each carry its coloured glow on the ground around it? Is that glow too strong? (Answered 24 Nov 2026: each carries its glow and you like it. The lights of the second version did not read as movement; that led to the third version.)
22. After an Engineer captures them: does the Reactor give power, does the Vault pay, does the Array show the map, does the Stormspire shoot violet lightning at enemies? Do the red parts take your colour? (Your screenshot of 24 Nov 2026: the Vault pays `+$60`, the Stormspire shoots violet lightning, the house-colour parts are in your teal. The Reactor's power and the Array's view of the map were not named.)
23. Does (6) Kalifornia Crisis still start in the other game modes it offers?
24. The second version of the art (since 23 Nov 2026, 23:21): do the four buildings now look at home beside the game's own power plants and radar? Does the Doomsayer look like one of the game's troopers, in size and in style? A screenshot would show how close the pictures drawn by the tools are to the game. (Answered 24 Nov 2026 for the buildings, with a screenshot: "The graphics are way better", "everything looks realistic". The Doomsayer was not named.)
25. Does the flare leave from the launcher's mouth, at his raised right hand (`PrimaryFireFLH=30,36,192`; if it leaves at his left, the middle number needs a minus sign), and does the launcher flash at the same moment (`FireUp=2`)?
26. When he stands idle for a while he looks around or kneels to listen to his radio, and at a victory he cheers. Does he keep his direction when such a move starts and ends, or does he jump to another direction?
27. The third version of the buildings (since 24 Nov 2026, 12:51), before anyone captures them: is the big dish on the Skywatch Array, and is it turning? Are the rings round the reactor's ball, the flags on the Vault, the claws round the Stormspire's ball? (These parts exist only in the animations. The game's own oil derrick is made the same way, so they are expected to be there. Your screenshot of 24 Nov 2026, 14:10, shows the flags and the claws on captured buildings. Before capture: still not said.)
28. Do the animations read as movement now: the dish turning with its shadow, the two rings swinging and the steam, the flags and the vault wheel, the lightning climbing the Stormspire? Is anything too fast or too slow? (Answered 24 Nov 2026 with "Perfect. Everything works just fine", as one answer for everything. Nothing was called too fast or too slow.)
29. Does the Stormspire's bolt now start in the ball (`PrimaryFireFLH=0,0,320`)? (Answered by your screenshot of 24 Nov 2026, 14:10: it does.)
30. When one of the four is badly damaged: does its animation go on with the damaged frames (a sooty dish with a hole, torn flags, thinner steam), or does a part vanish or jump?
31. Are the lights drawn in front of the moving parts (the beacon, the glints, the lit lamps), and do the dish's and the flags' shadows show on the ground?
32. The brass rings round the reactor's ball and the brass claws round the Stormspire's ball are drawn at full brightness, like lights. Do they look too bright against the building, above all before capture? (Not said. In the screenshot of 14:10 the claws do not stand out on the captured Stormspire; that is a reading of the picture.)
33. The Stormspire's reach (since 24 Nov 2026, 14:27). Select the tower, so that its ring shows. Does it leave alone a soldier who stands on the street outside the ring? Does it shoot one who stands about a cell inside the ring, down on the street and up on the plaza? (Right at the ring's line it does not shoot yet: the ring is drawn half a cell wider than the reach, as on the game's own Tesla Coil.)
34. Two things that were only tried on a rehearsal copy: a vehicle bundle that carries the section of its own animation in its rules (18.3), and a projectile of its own in a map file (13.5). Does each work in a game? (The first is answered: the Nexus's burst `NEXSSPL`, made that way, is in the owner's screenshot of 25 Nov 2026, 14.1.)
35. The flyers of section 20: which of the three candidates should be built into the game, the Seraph, the Tempest, the Nova, or several? (Answered 24 Nov 2026: "build all Seraph, Tempest and Nova". All three are installed since 21:25 that day.)
36. The three flyers in their first game: are the three icons in the vehicle tab, can each be built at a War Factory, does it lift off and hover at its height, does it move and turn like one of the game's own craft, and does the game run to a normal end? Afterwards `Mental Omega\debug\debug.log` must have no line with `Failed to parse INI file content`. (Your screenshot of 25 Nov 2026 shows the three icons, SERAPH, TEMPEST and NOVA, in the vehicle tab; the logs of the games of 24 Nov, 21:48, and 25 Nov, 10:40, have no such line and end normally. Whether one was built, and how it flies, was not said.)
37. Does each turning part turn all the time, and does it sit where it should: the halo on its mast above the Seraph, the fan in its well on the Tempest, the crystal in the middle of the Nova's ring? Is there a shadow on the ground under each craft?
38. The Seraph's beam: is there a wide violet beam from under the craft to its target? How wide and how bright is it, and does it fade within about a second? Do the violet flash under the craft and the plasma splash at the target show? If the beam does not show or looks wrong, the same craft with the other beam is ready (20.7).
39. The Tempest's lightning (24 Nov to 25 Nov 2026, 12:57): three blue-white bolts from under the fan. (Never reported on. On 25 Nov 2026 the owner asked for another attack: "electric shocks or lighning is not the best. i need something suitable for a plane. something entirely new and really nice." It was replaced the same day; questions 60 to 63 ask about the new one.)
40. The Nova: does it fly over its target, does a glowing orb fall straight down with a violet line behind it, and does the wide violet blast with its two rings and its smoke follow? Does it leave a burn mark?
41. The lights on the craft: a violet light on the hub of the halo, small arcs over the fan, the pulse of the core. Are they there, do they sit on the turning part, are they too strong or too weak?
42. When one of them is shot down: does it fall and crash like one of the game's own craft? And are cost, strength and damage about right beside the Warhawk and the Kirov?
43. The Nexus tank: is its icon (the tank in gunmetal with blue decks, "NEXUS") in the vehicle tab of the side you play, is it called "Nexus Tank", and can it be built at a War Factory? (Questions 43 to 48 of 24 Nov 2026 were about the version with the red laser. It was replaced on 25 Nov 2026, before any game. Your screenshot of 25 Nov 2026 shows the icon with the name NEXUS in the vehicle tab of the side you played, beside the Bulldog's own, and several built Nexus tanks. Whether the tooltip says "Nexus Tank" was not said.)
44. Its new paint: dark gunmetal, your team colour on the decks of the four track pods and on two plates of the turret, the coil on the barrel in blue-white light. Is it right, still too dark, or too much colour? (The other paint, steel blue with the colour only on the grilles, is one command away: 21.5. The screenshot of 25 Nov 2026 shows the paint as it was drawn: gunmetal, your teal on the decks, the coil pale. You did not comment on it this time.)
45. Its turret: when it turns to aim, does it stay on its ring on the hull? And the glow: after a shot, do the rings of the coil glow orange, then red, then light up blue-white one by one from the turret to the muzzle, and stay lit while it waits? Does the turret ever look wrong for a moment (a jump, a missing part) when the stage changes? (Not said yet; a still picture cannot show it.)
46. The second version's starburst (25 Nov 2026, 00:05 to 11:34): did the six pieces hit what was aimed at? (Answered 25 Nov 2026: it "does not seem to hit the targets correctly and effectively"; your screenshot shows the burst in the air above the tank and nothing at the target. Cause and cure: 21.1. It was replaced at 11:34; questions 55 to 58 ask about the new shot.)
47. When it is destroyed: does its own explosion (a fireball with a blue-white ring and smoke) show? When it becomes elite, does it still fire the starburst? Is there nothing on the deploy key?
48. Is the United States' Bulldog the game's own tank again (its own look, cost 700)? (The screenshot of 25 Nov 2026 shows the Bulldog's own icon in the vehicle tab. Its look and cost on the field were not said.)
49. Its numbers: cost 1700, strength 800, one shot of 200 damage every 90 frames, range 8, and five rays of 25. About right, or should it be stronger or cheaper?
50. The Vessel (since 25 Nov 2026, 00:48): is it on the west arm of the plaza of (6) Kalifornia Crisis, between the Black Vault and the airport, uncovered from the start? Does it look like the Vessel, and at home beside the game's buildings? (Answered 25 Nov 2026: "The vessel seems all right. Everything looks perfect. Everything is fine." The screenshot shows it on the plaza. You also asked whether it could not be closer to photographs of the real one: question 59.)
51. Can soldiers garrison it, up to ten? While they are inside, do the rim and two rings of landings show their side's colour (and not a damaged picture)? Does it take their side, and do their shots flash on the landings at the front of the vase? Can they be driven out, and does it look right while it is occupied? (Answered 25 Nov 2026 in part: "I love how it garrisons people." The colour while it is occupied, the firing flashes and driving the soldiers out were not named.)
52. Does the glass lift ride up the right-hand side and down again? Does the band of light climb the lattice and make the rim flash, and do the two red beacons blink?
53. When it is badly damaged and when it is destroyed: do the damaged picture, the crumbling sound and the explosion look and sound right?
54. It stands on three by three cells of the plaza's west arm. Does it get in the way of units crossing the plaza?
55. The Nexus's starburst as it is since 25 Nov 2026, 11:34. One shot at ONE enemy tank: does a blue-white orb fly from the tip of the barrel straight to the tank and burst ON it, also when the tank drives? Do five thin blue-white rays leap from the tank to the ground around it?
56. One shot into a GROUP, tanks or soldiers within five cells of each other: do the rays go to the others, each ending in a small blue burst, and do those lose a little health?
57. One shot at a BUILDING (hold Ctrl for a neutral one): the orb and its burst on the building, and no rays; that is how it is made. Does the building lose health with every shot (a concrete one 80 points)?
58. Does anything of your own side ever lose health from it, the Nexus itself when it shoots something right beside it? (Until 25 Nov 2026, 14:41, nothing of your side could: its warheads spared your side, and so a forced attack on your own units did nothing. Since then a ray that lands beside the tank can hurt your own units there, 13.10.)
59. The Vessel's look: A (the installed one), B (the honeycomb of the real one, with glass rails) or C (the same honeycomb, all copper)? The picture is `new-buildings\VESSEL-PICK.png` (16.12).
60. The Tempest's missile swarm (since 25 Nov 2026, 12:57). One salvo at ONE tank: do eight small missiles leave from under the fan one after another, each with a small flash and a launch sound? Do they spread out round the craft, then turn, and do all eight strike the tank, each with a small explosion?
61. Can you see the missiles themselves (small white darts with a red nose and a flame at the tail), each with a pale smoke trail and a thin line of light behind it? Or only some of that? Do they fly nose first? (Which end of a missile model the game takes for the nose was worked out from the stock missile files, not seen.)
62. One salvo at another FLYER, and one at something right UNDER the craft: do the missiles reach both?
63. Is the swarm about as strong as the lightning was? When several Tempests fire together, is the smoke too thick, and does the game stay smooth?
64. The small blue arcs over the Tempest's fan are left from its lightning. Keep them, or change them to an engine glow?
65. A forced attack, since 25 Nov 2026, 14:41. Hold Ctrl and attack with the Tempest one of your own soldiers, one of your own tanks and one of your own flyers; then with the Nexus the soldier and the tank (its shot has `AA=no`, so it cannot aim at flyers). Do they lose health now?
66. The same with the other new units (Arbalest, Reaver, Cerberus, Moloch, Seraph, Nova, Doomsayer) on one of your own tanks and soldiers, and with the Seraph also on one of your own flyers: does each do damage? None of their warheads ever had a line that spares a side, so each should.
67. The skirmish screen: pick (6) Kalifornia Crisis. Does its picture show the five buildings at the middle crossing, with their coloured light on the ground?
68. The loading screen at the start of a game on that map: its small map picture shows buildings as grey dots. Are there grey dots now on the five lots around the middle crossing? (Each building is only a few dots at that size.)
69. A rank: when one of the new units has killed enemies worth 4.5 times its own price (22.3), does it get the rank badge and flash, and do you hear the promotion? Kills of your own units do not count.
70. More for the ranks of the new units (22.7): an elite weapon of its own for each (for example more rays for the Nexus, more missiles for the Tempest), a look of its own for elite units (a second model the game swaps in when the unit becomes elite), both, or neither?

### Publishing the guide

The guide's folder is the public GitHub repository `sh4faq/Red-Alert-2--Modding-Guide` (remote `origin`, branch `master`). Until 25 Nov 2026 it showed the version of 12 Dec 2025: docs `01` to `06`, the quick reference and 13 old scripts; this guide, docs `07` to `09` and `mo_tool.py` had never been committed. That day the owner asked for the old version to be replaced by this guide ("clean the old one and just put this new one") and chose, when asked: this guide alone, a fresh history and no other tools. So the history starts with one commit of 25 Nov 2026, pushed over the old one.

Four files are published: `README.md`, `.gitignore`, this guide and `scripts\mo_tool.py`. The README says that the other tools named here stay in the project folder.

Publish only when the owner asks, and only those files, each named (never the whole folder at once). Before a commit, run these two lines from the project folder. The first must list only the files you mean to publish; the second must print nothing (the brackets keep it from finding its own line in this guide):

```powershell
git -C "MentalOmega-Modding-Guide" status --short
git -C "MentalOmega-Modding-Guide" grep --untracked -n -I -i -e "[a-z]:.use[r]s" -e "appdat[a]"
```

The owner's name and e-mail address must not be in the files either: look for them yourself, and never write them into this guide. After the push both lines below must print the same commit number:

```powershell
git -C "MentalOmega-Modding-Guide" rev-parse HEAD
git -C "MentalOmega-Modding-Guide" ls-remote origin master
```

### Change log

| Date | Change |
|---|---|
| 22 Nov 2026 | First version. Written after the Arbalest test confirmed that a brand-new unit works. |
| 22 Nov 2026 | Revised after three reviews: a first-time reader, a fact check and a completeness check. Labels were lowered to what was really reported. Backup, undo and restore got exact commands. Every command line was run on a sandbox copy of the game folder, except the undo script of 10.3. Nothing new was tested in the game. |
| 22 Nov 2026 | Tested again by a second reader, who ran every command once more on a sandbox copy. Seventeen corrections followed, among them: how to put your own ID into a pasted command, two repair lines for damaged line endings, and two more unsafe scripts in section 9. The old documents got a note that points here. Nothing new was tested in the game. |
| 22 Nov 2026 | The Arbalest got a model and an icon of its own (the rail sniper design) and `PrimaryFireFLH=298,0,123`. The first-test model in section 4, step 2 is now the Nexus model. The new model has not been tested in the game yet. |
| 22 Nov 2026 | The Arbalest's own model, icon, turret seat and fire position were confirmed in the game: five questions, answered with "Yes to all this". Labels changed in sections 4, 5, 6.6, 7, 10.2, 11 and 12. |
| 23 Nov 2026 | Three more units (Reaver, Cerberus, Moloch) were installed with an installer, each with a weapon of its own, and the first new animation was registered. The check now also checks weapons of your own; `lint-weapon` is new. Sections 3.2, 4, 6.6, 8, 10 and 11 follow the files as they are now; 10.7 is new. Nothing of this has been seen in the game yet. |
| 23 Nov 2026 | Reaver, Cerberus and Moloch got a rebuilt look (models and icons made after the game's dark heavy tanks), put in with the installer's new `swap` command. Only their three fire-position lines changed in `artmo.ini`. 10.7, 11 and 12 follow. The log of a game played before the swap shows that the rules of the three units were read and that the new animation's name was accepted. Nothing about how the units look in the game has been reported. |
| 23 Nov 2026 | The Arbalest got a rebuilt model and icon too (the same rail sniper, made after the game's steel-blue tanks) and `PrimaryFireFLH=335,0,117`. Its first own model, the one confirmed on 22 Nov, is kept and can be put back (10.2). Sections 4, 7, 8, 10.2, 10.3, 11 and 12 follow. What was confirmed for the earlier model stays marked as such; the rebuilt one has not been tested in the game. |
| 23 Nov 2026 | Your report after a game with the rebuilt looks: "everything was perfect". It is recorded as one answer for everything asked (10.7); the labels in sections 4, 6.6, 7, 10.2, 10.7, 11 and 12 follow. The Reaver's impact burst stays unconfirmed. |
| 23 Nov 2026 | Read in the game's program: an animation that map code adds needs its own section in the map code, so the Reaver's burst was most likely never drawn (8, 10.7, 10.8). Installed with a second installer, `packs.py`: that section (`REAVFIX`), an infantry unit with a weapon and three animations of its own (Doomsayer), and four new buildings placed on the map (6) Kalifornia Crisis. 10.8 is new; section 4 (other kinds of unit), 8, 11 and 12 follow. Nothing of this has been seen in the game. |
| 23 Nov 2026 | The first game with the packs (22:04, Kalifornia Crisis): the log and the merged scenario are recorded in 10.8, and your report ("everything looks good", one answer for everything) with its two corrections. |
| 23 Nov 2026 | Second version of the art, installed at 23:21: the four buildings were modelled anew with a rewritten kit (true-colour shading, textured materials), and the Doomsayer got an original body (301 pictures drawn from his own jointed figure) and a new icon. Rules, map lines and the buildings' art entries did not change; two art lines of the Doomsayer did. 10.8, 11 and 12 follow. The new art has not been seen in the game. |
| 23 Nov 2026 | Corrections at 23:34 after a review: the Doomsayer's idle and cheer pictures were turned to the direction the game expects (measured on the Flak Trooper); the Black Vault and the Stormspire got more house colour. Labels in 10.8 and 11 were lowered to what was actually said after the game of 22:04. |
| 24 Nov 2026 | Your report and screenshot after a game with the second version: the buildings look right ("The graphics are way better"), are captured in your colour, the Vault pays and the Stormspire shoots; the Doomsayer's icon is in the infantry tab. Two faults: the buildings did not seem to move, and the Stormspire's bolt started above the tower. Recorded in 10.8; labels in 10.8, 11 and 12 follow. |
| 24 Nov 2026 | Third version of the buildings, installed at 12:51: real moving parts (a turning dish, swinging rings, steam, flags, lightning) made by rendering the whole building again for every frame, a main animation and a light animation per building as in the game's own files, and `PrimaryFireFLH=0,0,320` for the Stormspire (a building's fire point counts from the middle of the sprite canvas). Eleven sprite files and ten animations instead of eight and four. 10.8, 11 and 12 follow; questions 27 to 32 are new. None of it has been seen in the game. |
| 24 Nov 2026 | Your report and screenshot after a game with the third version (14:06): "Perfect. Everything works just fine"; the screenshot shows the bolt starting in the ball and parts that exist only in the animations. One fault: the Stormspire hit targets outside its range ring. The cause, read in the game's program, is the high-ground bonus that the Tesla Coil's projectile carries. Since 14:27 the weapon has the projectile `Invisible` (one line of the map file), and a new check, `new-buildings\check_range.py`, tests it on the map. 8, 10.8, 11 and 12 follow; question 33 is new. The change has not been seen in the game. |
| 24 Nov 2026 | The guide now also says how things are made, so that the work can be handed on: section 0 (start here) and sections 13 to 19 (weapons, hits, damage and reach; animations; an infantry unit; a building on a map; a building that moves; a tank's model and icon; the mistakes made). Every command line printed in them was run as it is printed on 24 Nov 2026; the build lines gave the installed files again, byte for byte. Two install lines name things that are installed already; they were run with `--dry-run` and answered `NOTHING DONE`. The sections record what was done and measured from 22 to 24 Nov 2026; nothing in them was newly tested in the game. |
| 24 Nov 2026 | A reader who had only this guide planned three new things from it (a fifth building with a flame weapon, a tank with a painted explosion, a second soldier) and reported where it left them guessing. Added after that: which check fits which kind of thing and how to pick list numbers (0), the armour list and an example (13.4), arcing shots and a projectile of the pack's own (13.5), what `LoopEnd=` means (14.5), what to change for another soldier (15.7), for a fifth building (16.11) and for a tank with its own hit effect, and how to rehearse a vehicle (18.3). Four statements were corrected (the keys of the blast and the marker, the Stormspire's art keys, the figure build's checks, the count of projectiles). The tools changed with it: `mo_tool.py` warns when an animation that `Standard.ini` lists has no section there; `make_sandbox.py --units` makes a rehearsal copy for the vehicle installer; `check_range.py` knows arcing shots; `blacksite.py` can list a projectile of its own; the vehicle installer's `remove` no longer stops when a unit is removed twice within one second. Question 34 is new. The reader said they could not have done the three things from the guide as it was. What he asked for was added, but nobody has read the result cold yet. |
| 24 Nov 2026 | Flyers were researched after the owner asked what could be made: how the game's 95 flyers are built, move and attack (from its rules, art and model files), what the public documentation adds, and three candidates of our own with a spinning part each (Seraph, Tempest, Nova), drawn in one preview. Section 20 is new, question 35 with it. Nothing was installed, and nothing in the section has been in a game. |
| 24 Nov 2026 | The owner picked: "build all Seraph, Tempest and Nova". All three were finished (everything that turns on the turning axis, more small parts, icons in the sky), given a weapon each from stock blocks, seven painted animations, a light that stays on the craft and, for the Nova, a falling orb with a projectile of its own. They were rehearsed on a copy of the game files, first as bare bundles, and installed at 21:25 with the vehicle installer. Every check passes. Section 20 was rewritten: 20.5 to 20.9 say what was built, how, how to take it out, and what is proven. Sections 0, 4, 11, 12, 13.3 and 19 follow; questions 36 to 42 are new. Every command line printed in section 20 was run as printed; the three build lines gave the installed files again, byte for byte, and the remove and switch lines were run on a rehearsal copy. Nothing of it has been in a game. |
| 24 Nov 2026 | A correction. The first version of section 20, and two messages to the owner, said that the game has thick lasers in a colour of their own (the key `IsBigLaser=`), and then that the Magnetron's beam is drawn as the extension's laser wave. Both were wrong: the game never uses `IsBigLaser=`, and the Magnetron's weapon takes another branch. Read in the game's program the same evening, with the order in which a weapon's beam kinds exclude each other (20.4). The Seraph was built on what the code says: the laser wave, with no stock example, and a second version of its weapon from stock parts as a way back (20.7). `mo_tool.py check` now accepts a flyer that is wider than long. |
| 24 Nov 2026 | The Nexus tank became a unit of its own, `NEXS`, after the owner asked for its mistakes to be fixed without changing its look, for animations of its own and for an icon. Its model is the same, voxel for voxel; the turret now turns about its own ring (`TurretOffset=-52`), the shot leaves at the barrel's tip, and it has an icon, a red laser copied from the stock Future Tank with a sound, a painted flash, hit effect and explosion, and real numbers in place of the test values (cost 1 and 500 damage became 1700 and 180). Installed at 22:07 with the vehicle installer; then the take-over block of the Bulldog was cut out of `Standard.ini` with a small script that can put it back. At 22:17 the unit went in once more, with its end made as a death weapon of its own in place of an `Explosion=` line. Both steps were rehearsed on a copy first, with the way back. Section 21 is new; sections 0, 3.2, 4, 5, 6.6, 9, 11, 12, 13.2 and 19 follow; questions 43 to 48 are new. Measured for it on stock tanks: the first number of `PrimaryFireFLH` counts from the turret's own pivot (21.2). Nothing of it has been in a game. |
| 25 Nov 2026 | The Nexus tank's second version, after the owner asked for a glowing animation on the turret, some colour, and a new kind of attack: a new paint (the black plates dark gunmetal, the team colour on whole plates, the coil in light colours that the game draws at full brightness), a turret that changes in eight stages as the weapon charges (read in the game's program: the stage follows the reload time), and the starburst, the stock Seitaad Ballista's splitting shot with six pieces. Six animations painted in blue-white, a new icon, and a second paint ready to swap in. The first install of it, at 23:58 on 24 Nov, had taken over the Ballista's orb warhead with its blast radius of four cells; it was replaced at 00:05, before any game (19). `mo_tool.py check` now checks every turret file of a charge turret. Section 21 was rewritten (21.3 to 21.6 are new or new in part); sections 0, 3.2, 4, 6.6, 11, 12, 13.2, 13.3, 14.1, 14.2, 19 and 20.4 follow; questions 43 to 48 were rewritten for this version, and question 49 is new. Every command line printed in section 21 was run as printed; the build lines gave the installed files again, byte for byte, and the three ways back were rehearsed on copies. Nothing of it has been in a game. |
| 25 Nov 2026 | A fifth building on (6) Kalifornia Crisis, after the owner asked for "the vessel" and said which one: the Vessel of Hudson Yards, as a landmark that soldiers can garrison. Its rules are those of the game's own Space Needle; its ten firing points count from the centre of the sprite canvas (measured on the Space Needle's own sprite); its model is a lattice of flights and landings worked out layer by layer; a glass lift and a climbing band of light make it move. It went in with the Black Site pack, installed again at 00:48, and once more at 01:16 with the picture the game shows while soldiers are inside (the first build would have looked damaged then) and `Remapable=yes`; the other four buildings came out as before. 16.12 is new; sections 0, 11, 12, 14.1, 16, 16.2 and 16.11 follow; questions 50 to 54 are new. Every command line of 16.12 was run as printed; the pack and the way back were rehearsed on a copy. Not seen in a game. |
| 25 Nov 2026 | The owner's report and screenshot after a game with the Nexus's second version and the Vessel (10:40). Confirmed by the picture: the Nexus as a unit of its own with its icon, its paint and its lit coil; the Bulldog's own icon; the icons of the three flyers in the vehicle tab; the Vessel on the plaza, and in the owner's words that soldiers can garrison it. One fault: the Nexus's shot "does not seem to hit the targets correctly and effectively"; the picture shows it bursting in the air near the tank. The cause, from the files and the two programs: the weapon was a copy of an artillery piece's, whose missile goes off where its `ProjectileRange=` ends; and its piece weapon had no line under `[WeaponTypes]`, which all 110 stock weapons named by a projectile have. Since 11:34 the third version is installed: an orb that homes on its target and does the damage itself (stock direct-fire blocks), and five rays from where it hits a vehicle or a soldier, the game's own way of throwing pieces from a hit, read in the program. The vehicle installer can register a weapon under `[WeaponTypes]` now, and `mo_tool.py` warns about a piece weapon that is not listed. 13.8 is new; sections 0, 3.2, 11, 12, 13.2, 13.3, 14.1, 14.2, 19, 20 and 21 follow; questions 55 to 59 are new, 43 to 51 carry the answers. Every command line printed in section 21 was run as printed; the build lines gave the installed files again, byte for byte, and the four ways back were rehearsed on a copy. The third version has not been in a game. |
| 25 Nov 2026 | A new attack for the Tempest, after the owner asked for one "suitable for a plane" in place of the lightning and to look up the attack craft of science fiction: a swarm of eight small homing missiles. The weapon is the stock Old Longbow's salvo, the flight and the warhead the stock Quickshifter's; the missile is a small model of our own with a pale smoke trail, a launch flash and an explosion, all painted new. Read in the game's program for it: the shots of a salvo leave 3 to 5 frames apart, a homing shot leaves in the direction the turret points (so from a craft whose turret never stops turning the missiles spread by themselves), and where a projectile's picture, model and trail are read from. Installed at 12:57 after a rehearsal on a copy; the lightning version is kept in `new-aircraft\round1`. 13.9 is new; sections 0, 11, 12, 13.3, 14.1, 14.2 and 20 follow; question 39 was rewritten, questions 60 to 64 are new. Every command line printed for it was run as printed; the build lines gave the installed files again, byte for byte. Not seen in a game. |
| 25 Nov 2026 | The owner's report after a game with the Tempest's swarm (afternoon): a flyer of ours, forced (Ctrl) on the owner's own soldiers, tanks and aircraft, did them no damage, only buildings; the map's pictures in the skirmish screen and at the start of a game did not show the new buildings; and a question about ranks ("tiers"). The cause of the first was the line `AffectsAllies=no` in the Tempest's warhead and in both of the Nexus's; it is out since 14:41, the check warns about it, and the build scripts stop on it (13.10). Both preview pictures are now part of the map pack and were installed at 15:04 (16.13). Ranks were read in the game and the extension and written down; nothing about them was changed (22). New: a list of what to check before anything counts as finished (23), three rows in section 19, questions 65 to 70. |
| 25 Nov 2026 | Section 1 is now the playbook, after the owner asked for the guide to hold "everything that we did and how we learned how to do things and the one way to do certain things ... when I say, oh, create a new unit, the model knows what to do, where to go, and how to do it exactly, step by step": the first steps for every request, eight rules, a recipe for each kind of thing (tank, flyer, soldier, building, attack, effect, fault, change), what to do after a game, how things were found out, and how each thing is named. The old short version is 1.14; sections 4 and 5 point to the playbook. The tank recipe (1.3) was followed to the end with a throw-away ID on a rehearsal copy. Two read-only tools are new: `weapon_audit.py` and `find_unit.py`; `unit_bundle.py status` prints all six lists of `Standard.ini`; `new-units\make_bundles.py` prints the right number of rules sections. Old numbers in 14.1, 15.7 and 20.6 were replaced. The owner's game of 17:04 on (6) Kalifornia Crisis ran with everything installed and a clean log (11, 16.13). The owner's message that evening, "That was perfect. I love everything that you gave me so far. Everything is literally perfect", named no item; no label was changed for it, and questions 59 and 65 to 70 stay open. |
| 25 Nov 2026 | A cold read of the playbook by a fresh reader with only this guide, who planned four jobs nobody had done (a railgun tank with its own hit, a sniper, a radar dome on the map, a fault report); the report is `arbalest-tank\kit\research\guide\coldread_2026-11-25.md`. No step blocked, but four holes let every check pass with a wrong result, and all were closed: a copied soldier kept the stock sprite's `Image=` (now in 1.5, and `packs.py verify` fails on it: 49 checks for `DOOM`); the "see it on the map before the install" line drew the old pack (1.6, 16.7, 23); `t.muzzle` was said to set the fire point and is not read (1.3, 18.3); the name check could not see weapons, warheads and animations (`find_unit.py --exact`). Also: a way to find a stock unit by its weapon (`find_unit.py --key`), the kinds of shot and the `shot:` column of `weapon_audit.py`, the colours of a hit's light and of a painted effect, a soldier template that is not of the Flak layout, the `%%` in the soldier pack script, rehearsal lines for a soldier (run with the Doomsayer), buildings that let their owner see, asking when a request or report is unclear, narrowing a fault down with a stock picture, `round` folder names, `pick_sheet.py` for candidates, `heights.py` now lists every building, the installers' numbers as they really are chosen. |
| 25 Nov 2026 | Published on GitHub alone, after the owner asked why the guide was not there and wished the outdated version replaced: "clean the old one and just put this new one". Asked three questions, the owner chose this guide only, a fresh history and no other tools. The old documents and scripts left the guide's folder for `backups\2026-11-25-before-github-replace`; a new `README.md` says what the guide is, where to start, and that its tools stay in the project folder. Sections 0, 9 and 11 say where things are now; section 12 says how to publish. |

---

## 13. A weapon of your own: the shot, the hit and the damage

Section 6.6 says how to name a weapon and how to check its sound. This section is about what happens when it fires: what flies, what shows where it lands, how much damage it does and how far it reaches.

### 13.1 The chain

```
unit        [MYUNIT]    Primary=MyGun
weapon      [MyGun]     Damage, ROF, Range        how hard, how often, how far
                        Report=                   the firing sound
                        Anim=                     a flash at the muzzle
                        Projectile=MyShot         what flies
                        Warhead=MyGunWH           what happens where it lands
projectile  [MyShot]    Inviso=yes                nothing is drawn (beams, bolts, bullets)
                        or Image=MYPIC            a flying picture
warhead     [MyGunWH]   Verses=                   damage against each kind of armour
                        CellSpread=               how wide the blast is
                        AnimList=MYHIT            THE HIT EFFECT: plays where the shot lands
                        PreImpactAnim=MYMARK      plays first; damage and hit effect follow when it ends
animation   [MYHIT]     a sprite of its own       section 14
```

All of these blocks stand in the same file as the thing that fires: `Standard.ini` for a unit of the Standard mode, the map file for a building of a map pack. **[FILES]**

### 13.2 The safe way: copy a complete stock weapon and change values

Every weapon that works here was made this way. A copied block holds only keys the game knows.

| Weapon | Fired by | Copied from | What was changed | Hit effect |
|---|---|---|---|---|
| `ReaverArc` | Reaver | `WormqueenBolt` and its warhead | Damage 85, ROF 95, Range 7.5, three bolts per volley, violet bolt colours, sound | `REAVZAP` (a stock picture under a new name, 14.3) |
| `CerberusFlame` | Cerberus | `BorilloFlamethrower` and its warhead | Damage 50, ROF 32, Range 6, three streams per volley, blast radius 1.8 cells | stock `NPLMEXP` (napalm burst) |
| `MolochCannon` | Moloch | `CenturionCannon` and its warhead | Damage 230, ROF 210, Range 14, blast radius 2.5 cells, screen shake 8, a red flash, more debris | stock `IRONEXP` (red shock ring) |
| `DoomFlare` | Doomsayer | weapon keys of `QuadMortar`, rocket of `WallbusterP`, warhead of `HammerWH` | Damage 150, Range 9.5, not closer than 2.5, blast radius 2 cells | `DOOMMARK` first, then `DOOMBLST` (both painted new, 14.4) |
| `StormspireBolt` | Stormspire | `CoilBolt` and `ElectricCoil` of the Tesla Coil | Damage 170, ROF 100, violet bolt colours, projectile `Invisible` (13.5), without the Tesla Coil's three `Versus.` lines (13.4) | stock `TSTIMPCT` |
| `NexusStarburst` (since 25 Nov 2026; direct since 11:34 that day) | Nexus tank | the Piranha's `PiranhaMissile`; the Salamander's bolt projectile; the Ballista fragment's warhead, twice; the Prism Tank's fragment `CometFragment` for the rays (21.3) | an orb that homes on its target and does 200; from a vehicle or soldier it hits, five rays of 25 to enemies within five cells; ROF 90, Range 8, no minimum range | flash `NEXSMUZ`, burst `NEXSSPL`, ray hit `NEXSHIT`, flying picture `NEXSORB` (all painted new) |
| `NexusLaser` (24 to 25 Nov 2026, never in a game) | Nexus tank | the Future Tank's `FTankLaser` and its warhead `FutureAP` | Damage 180, ROF 80, Range 7.5, one shot instead of two, red, the sound named on the weapon | a flash and a hit painted new; the bundle is kept in `nexus-tank\round1` |
| `TankieGun` (out since 24 Nov 2026) | Nexus model on the Bulldog | written by hand (section 5) | a red laser, with a sound name the game does not have | stock `TWLT070` |

**[FILES]** for every block. The three vehicle weapons: "everything was perfect", **[CONFIRMED]** 23 Nov 2026 as one answer for everything. The Stormspire shoots violet lightning: **[CONFIRMED]** 24 Nov 2026 (your screenshots). The old Nexus laser `TankieGun`: **[CONFIRMED]** 2 April 2026. `NexusLaser` was never in a game. The first `NexusStarburst`, a shot that split in the air, was: it burst far from the target (21.1). **[CONFIRMED]** 25 Nov 2026. The direct one of 11:34 that day was installed during the owner's games of 25 Nov 2026 at 12:29, 14:21 and 17:04, whose logs are clean; nothing about it was reported. **[UNTESTED]** The Doomsayer's flare, marker, bombs and blast were never named in a report. **[UNTESTED]**

How a copy is made: `new-units\make_bundles.py` has a small function for it.

```python
reaver_gun = change(stock('WormqueenBolt'),
                    set={'Damage': '85', 'ROF': '95', 'Range': '7.5', 'Warhead': 'ReaverArcWH'},
                    remove=('MinimumRange', 'FireWhileMoving', 'Ammo'))
```

`stock()` prints the stock section through `mo_tool.py section`. `change()` replaces values, drops lines, adds lines, and stops if it is told to set a key that the stock section does not have. By hand the same thing is: print the stock weapon and its warhead (3.2), paste both under new names, change numbers.

Where the blocks are registered:

- The three vehicle weapons stand in `Standard.ini` without a line in any list, and they work. **[CONFIRMED]** 23 Nov 2026 (one answer for everything).
- The pack installer also writes list lines for a pack's weapons, projectiles and warheads (`[WeaponTypes]`, `[Projectiles]`, `[Warheads]`), the way the stock rules list theirs. **[FILES]** Read in the two programs on 25 Nov 2026: a weapon that a unit names needs no line, a weapon that only a projectile names does (13.8). Whether a projectile or a warhead ever needs one was not read; those of our vehicle weapons have none and work. **[FILES]**
- An animation is different: it must be listed, and it needs a section of its own in the same file (14.1).

### 13.3 The keys that shape the shot and the hit

The values are those of the installed blocks. **[FILES]** The meanings are the usual ones for this engine; except where this guide says otherwise they were not measured here. **[UNTESTED]**

| Block | Key | What it does | Installed example |
|---|---|---|---|
| weapon | `Damage=` | Damage of one shot before armour is counted | 85 (Reaver), 230 (Moloch) |
| weapon | `ROF=` | Wait between shots or volleys. Smaller fires more often | 32 (Cerberus), 210 (Moloch) |
| weapon | `Range=` | Reach in cells (13.5) | 7.5, 14 |
| weapon | `MinimumRange=` | Nothing closer than this is shot at | 2.5 (Doomsayer), 3 (Moloch) |
| weapon | `Burst=` | Shots per volley | 3 (Reaver, Cerberus) |
| weapon | `Speed=` | Speed of the projectile. 100 for beams and bolts that arrive at once | 100, 30 (the flare), 1 (the siege shell, which flies an arc) |
| weapon | `Report=` | Firing sound; must exist in the stock sound file (6.6) | `TeslaTankAttack` |
| weapon | `Anim=` | Flash at the muzzle; a stock animation in every weapon here | `PULSMUZ`, `COILMUZZ`, `GCMUZZLE` |
| weapon | `IsElectricBolt=true`, `Bolt.Color1=` to `Bolt.Color3=` | A lightning bolt from the fire point to the target, and the colours of its three strands | `190,60,255` / `125,0,255` / `255,255,255` (violet) |
| weapon | `IsLaser=yes`, `LaserInnerColor=`, `LaserOuterColor=`, `LaserDuration=` | A laser line and its colours | the Nexus's laser of 24 Nov 2026 (`nexus-tank\round1`); none installed now |
| weapon | `Wave.IsBigLaser=yes` | A wide beam, the extension's laser wave. Only one kind of beam is drawn per weapon, so not together with `IsLaser`, `IsElectricBolt` or `IsRadBeam` (20.4). Not seen in a game | the Seraph |
| weapon | `Bright=yes` | A flash of light on the ground | Cerberus, Moloch |
| projectile | `Inviso=yes`, `Image=none` | Nothing is drawn in flight | stock `Invisible`, `InvisibleHigh`, `InvisibleMedium` |
| projectile | `Image=` | The flying picture: an animation's name (14.2) | `DOOMFLR` |
| projectile | `ROT=`, `Acceleration=`, `Arm=` | A rocket that turns towards its target | 20, 10, 2 (the flare) |
| projectile | `CourseLockDuration=` | A homing shot keeps the direction it left in for that many frames, then starts to turn (13.9) | 8 (the Tempest's missiles) |
| weapon | `Burst=` | How many shots one attack fires. They leave 3 to 5 frames apart, at random, unless the unit has `BurstDelay0=` to `BurstDelay3=` (13.9) | 8 (the Tempest) |
| projectile | `Splits=yes`, `Cluster=`, `AirburstWeapon=` | The shot splits into `Cluster=` pieces of the weapon named in `AirburstWeapon=` (13.8) | nothing now; the Nexus's second version had 6 pieces (21.1) |
| projectile | `Ranged=yes`, and the weapon's `ProjectileRange=` | The shot goes off after that many cells of flight, wherever it is then; without the line it flies on to its target (13.8) | nothing now; the Nexus's second version had 2.5 and burst in the air, far from the target (21.1) |
| projectile | `RetargetAccuracy=`, `AroundTarget=` | The share of the pieces that keeps the first target; with `AroundTarget=yes` the others look for targets near it | nothing now; the second version had 0.75, yes |
| projectile | `ShrapnelWeapon=`, `ShrapnelCount=` | Pieces thrown from where the shot hits a vehicle or a soldier (13.8) | `NexusShard`, 5 (the Nexus) |
| projectile | `AA=`, `AG=` | May it be shot at things in the air, on the ground | `no`, `yes` |
| projectile | `SubjectToElevation=` | The high-ground bonus (13.5) | `no` (the flare); `yes` in stock `InvisibleHigh` |
| projectile | `SubjectToCliffs=`, `SubjectToWalls=`, `SubjectToBuildings=` | What stops the shot | `no` (the flare) |
| warhead | `Verses=` | Eleven percentages: the damage against each basic armour (13.4) | `100%,80%,60%,50%,40%,30%,10%,10%,10%,70%,100%` |
| warhead | `Versus.<armour>=` | The same for one of Mental Omega's own armour names | `Versus.defense=250%` (Moloch) |
| warhead | `CellSpread=`, `PercentAtMax=` | Radius of the blast in cells, and the share of the damage that arrives at its edge | 2.5 and .35 (Moloch); .3 (a bolt: one target) |
| warhead | `AnimList=` | The hit effect | `REAVZAP`, `IRONEXP` |
| warhead | `PreImpactAnim=` | An animation before the damage | `DOOMMARK` |
| warhead | `InfDeath=` | Which death a killed soldier plays: 3 thrown through the air, 4 burning, 5 electrocuted | 5 (bolts), 4 (fire), 3 (bombs) |
| warhead | `ProneDamage=` | Damage to a soldier who lies on the ground | `50%` |
| warhead | `Wall=`, `Wood=` | May it damage walls, trees and wooden things | `yes` |
| warhead | `ShakeXlo=`, `ShakeXhi=`, `ShakeYlo=`, `ShakeYhi=` | The screen shakes at the hit | 8 (Moloch), 1 and 2 (Doomsayer) |
| warhead | `MinDebris=`, `MaxDebris=` | Pieces thrown up at the hit | 6 and 10 (Moloch) |
| warhead | `Bright=yes`, `CombatLightSize=`, `CLDisableGreen=`, `CLDisableBlue=` | A flash of light at the hit, its size, and its colour (green and blue switched off leaves red) | Moloch: 150 %, red |
| warhead | `Sparky=yes` | Sparks and fires at the hit | most of them |

### 13.4 Damage in numbers

- A hit does `Damage` times the warhead's percentage for the target's armour. With `Damage=85` and 50 % against that armour a bolt does about 42.
- `Verses=` has eleven places, for the eleven basic armours in the engine's order: none, flak, plate, light, medium, heavy, wood, steel, concrete, special_1, special_2. Soldiers wear the first three, vehicles the next three, buildings the next three. This order is the engine's usual one; it was not measured in this game. **[UNTESTED]**
- Mental Omega has 238 more armour names (6.5). Each of them counts as one of the eleven basic ones, and the stock list `[ArmorTypes]` says as which: `flak_t1=flak` (the Doomsayer's armour counts as flak), `defense=steel`. Print the list with `python "MentalOmega-Modding-Guide\scripts\mo_tool.py" section ArmorTypes`. **[FILES]**
- A warhead may give one of those names a number of its own with `Versus.<name>=`. The stock warheads do that a lot, and a copied warhead brings those lines with it. Keep them unless you know what each one is for. (The Stormspire's warhead left out the Tesla Coil's three: `Versus.camo.PassiveAcquire=no`, `Versus.s_siren2=-100%`, `Versus.wormq=-100%`.) **[FILES]**
- Example: a cannon that is strong against tanks and weak against soldiers has high numbers in places 4 to 6 and low ones in places 1 to 3. The Moloch's `Verses=35%,35%,35%,120%,120%,120%,...` is built that way. Before you judge a result in the game, look up which basic armour the target's `Armor=` counts as.
- A blast (`CellSpread` above about 1) hurts everything inside its radius, less towards the edge (`PercentAtMax`). A warhead with `CellSpread=.3` hits one target.
- To make a weapon stronger or weaker, change `Damage=` first. Change `Verses=` only to move the weapon between roles (against soldiers, against tanks, against buildings), and compare with the stock warhead it was copied from.

### 13.5 How far it reaches: range, high ground and the range ring

This was found on 24 Nov 2026. Your screenshot of that day (14:10) shows the Stormspire's bolt landing outside the ring that the selected tower draws round itself. Measured on the screenshot: the ring is 8.47 cells wide to each side, and the bolt landed 10.12 cells from the middle of the tower. **[FILES]**

What the game does, read in its program (`gamemd.exe`; the ring in `Ares.dll`). **[FILES]** for the program. The listings are in `arbalest-tank\kit\research\probe`: `dis_6F7220.txt` (the range test), `dis_6F6F60.txt` (the bonus), `dis_6F77B0.txt` (where the distance is measured from), `dis_ares_10049A94.txt` (the ring).

- **The range test.** The game measures the straight line from the middle of the shooter to the target, in three dimensions. A cell is 256 units long, a height level 104 units. So against a target on lower or higher ground a weapon reaches a little less far over the map than its `Range=` says.
- **The high-ground bonus.** If the weapon's projectile has `SubjectToElevation=yes` and the shooter stands higher than the target, the range grows. The stock rules set it in the section `[ElevationModel]`: `ElevationIncrement=4`, `ElevationIncrementBonus=2`, `ElevationBonusCap=2`. That is 2 cells for every 4 levels of height, and at most 2 cells in all. The game also adds the height itself, so from four levels up a weapon with `Range=8` reaches 10.4 cells over the map instead of 8.
- **Which weapons get it.** Of the 355 projectiles in the stock list `[Projectiles]`, 95 have `SubjectToElevation=yes`, 211 have `no` and 49 do not have the key. `InvisibleHigh` and `InvisibleMedium`, which most beams and bolts use, have `yes`: 41 of the 42 stock lightning weapons get the bonus, the Tesla Coil's among them. A projectile without the key does not get it: the program's default is no. The stock projectile `Invisible` is `InvisibleHigh` without that key. **[FILES]**
- **The ring.** A building with `HasRadialIndicator=true` draws a ring round its middle while it is selected, in its owner's colour. Its radius is `RadialIndicatorRadius=` if the building has that key, and otherwise the `Range=` of its `Primary` weapon in whole cells (7.5 gives 7). The ring is drawn about half a cell wider than that number. It knows nothing of the high-ground bonus. **[FILES]** That the ring shows: **[CONFIRMED]** 24 Nov 2026 (your screenshot).
- **A target that is a building** is reached from further away: the range grows by a quarter of a cell for every cell of the target's width plus its height (a 3x3 building: one and a half cells). **[FILES]** for the program.
- **A shot that flies an arc** (`Arcing=yes` on the projectile: shells, flame streams) is tested in another way. The distance is measured flat over the map, and the high-ground bonus is the 2 cells alone. The game then also tests whether the shot can fly that arc. **[FILES]** for the program (`dis_6F70E0.txt`).

So a defence that stands on a plateau shoots further than its ring shows. The four buildings stand on the plaza of (6) Kalifornia Crisis at height level 6; the streets round it are at level 2. The Stormspire's weapon was a copy of the Tesla Coil's with its projectile `InvisibleHigh`: range 8, ring 8, and street targets were hit up to 10.1 cells away. The game's own Tesla Coil would do the same on that plaza.

**The cure**, installed 24 Nov 2026, 14:27: one line of the weapon, in the map file.

```ini
Projectile=Invisible
```

Now the tower reaches 8 cells on the plaza and 7.8 cells down on the streets. No unit and no spot on the ground outside the ring can be hit. **[FILES]** Not seen in the game. **[UNTESTED]** The projectile itself is not new to this game folder: the Nexus laser of section 5 has fired through `Invisible` since April 2026. **[CONFIRMED]** 2 April 2026, for that weapon.

Two things to know when you test it. The ring is drawn half a cell wider than the reach, so a soldier who stands right at the ring's line is not shot yet; a little further in he is. The game's own Tesla Coil has the same half-cell band. And an enemy building is still reached from a little further away than a unit (the list above); that too is the game's own rule.

A weapon whose stock projectile draws a picture or flies an arc cannot take `Invisible`: a flamethrower's `FlameProj` has `Image=FRING` and `Arcing=yes` and would lose both. Such a weapon gets a projectile of its own: the stock section copied under a new name, with `SubjectToElevation=no`, and a line under `[Projectiles]`. The Doomsayer's `DoomFlareP` was made that way from `WallbusterP`. In a map pack the section goes into `WEAPONS` in `new-buildings\blacksite.py` and its name into `PROJECTILE_NAMES` there. Tried on a rehearsal copy on 24 Nov 2026, with a copy of `Invisible` named `StormspireShot`: the pack installed with 110 checks and the range check passed. **[FILES]** A projectile of its own in a map file has not been in a game. **[UNTESTED]**

**The check.** `new-buildings\check_range.py` reads the map, the rules and the heights of the ground and works out, cell by cell, where every armed building with a ring can hit.

```powershell
python -I -B "new-buildings\check_range.py"
```

Before the cure it ended with `FAIL: 72 cells outside the ring can be hit; the farthest is 10.12 cells away`, the same distance as the hit in your screenshot. Since the cure it ends with:

```
  PASS: nothing outside the ring can be hit (farthest reach 7.91 cells)

Result: 0 FAIL
```

Add `--game` and a folder to check a rehearsal copy (16.10) instead of the game. The check knows straight shots and arcing shots. It looks at cells, so it does not show the longer reach against buildings. `new-buildings\range_picture.py` draws its result onto the map renderer's picture of the plaza: `new-buildings\RANGE.png` shows what the tower could hit before the cure and what it can hit now.

Rules for new work:

- A defence that shows a ring gets a projectile without `SubjectToElevation=yes`, unless it can only ever stand on level ground. Run the check.
- If the long reach is wanted, keep the stock projectile and give the building `RadialIndicatorRadius=` with the longer number. Then the ring is right for targets on low ground and too wide for targets on the same level. **[UNTESTED]**
- Vehicles and infantry show no ring. Leave them the stock behaviour: the Reaver's `InvisibleMedium` gives it the high-ground bonus that the stock weapon it was copied from has.

### 13.6 Checks before and after a game

- A vehicle of your own: `mo_tool.py check ID` also checks its weapon, projectile, warhead, sounds and animations. A single weapon block in `Standard.ini`: `mo_tool.py lint-weapon NAME` (3.2). Neither is for infantry, for buildings or for a weapon in a map file: the table in section 0 says which check fits.
- A pack: `packs.py verify NAME` (10.8). An armed building: `check_range.py` (13.5).
- After a game: search `Mental Omega\debug\debug.log` for `Failed to parse INI file content`. A line of that kind names a warhead and an animation the game did not know (section 8). None of the games since 22 Nov 2026 has such a line. **[FILES]**

### 13.7 Sounds and voices

Every new unit uses stock sounds and stock voices: the Doomsayer speaks with the Flak Trooper's voice (`VoiceSelect=FlakTroopSelect`), the buildings answer like the stock tech buildings, the weapons use stock firing sounds. **[FILES]** A sound file of your own has never been tried. **[UNTESTED]** It would need an entry in the sound file `soundmo.ini`, which is inside an archive like the rules.

### 13.8 A shot that throws pieces: from the air, or from where it hits

Two different things in this game make one shot into several. Both were read in the programs on 25 Nov 2026, after the Nexus's splitting shot missed in a game (21.1). The listings are in `arbalest-tank\kit\research\probe`: `dis_46A310_shrapnel.txt`, `dis_679A10_type_load_order.txt`, `dis_ares_splits.txt`; a summary with the addresses is in `arbalest-tank\kit\research\aircraft\splits_and_airburst.md`. **[FILES]** for all of it; none of it was watched in a game. **[UNTESTED]**

**From the air: `Splits=yes` (the extension).** For artillery that should scatter. The stock Seitaad Ballista's second weapon is the model: its missile climbs, and where the weapon's `ProjectileRange=` ends it goes off and throws `Cluster=` pieces of the weapon `AirburstWeapon=`.

- A `Ranged=yes` projectile loses the distance it flies from its range every frame and goes off at zero (the extension's hook at 0x467B94 of `gamemd.exe`). The range is the weapon's `ProjectileRange=`. A weapon without that line is not cut short this way: the stock Salamander's bolt is `Ranged=yes`, has no such line and a reach of 10.5 cells (without the line the extension gives a weapon 100,000 leptons, about 390 cells: the value stored at 0x100549AA of `Ares.dll`). So `ProjectileRange=` is not a reach: it is the place where the shot ends, however far away the target is.
- The pieces start at the place of the burst, heading straight down, and steer from there (the extension's routine at 0x1001A090 of `Ares.dll`). A piece keeps the first target with the chance `RetargetAccuracy=`; otherwise it takes a unit or building within five cells of that target that its warhead may hurt, or, when there are none left, a random cell within three cells.
- The missile itself does nothing: the Ballista's has `Damage=1` and a warhead of 3 %.
- The extension's documentation adds: the piece weapon's `Speed=` must be 19 or more.

**From where it hits: `ShrapnelWeapon=` (the game itself).** For a shot that should hit its target and then reach what stands near. The stock Prism Tank is the model (`LargeCometP`: `ShrapnelWeapon=CometFragment`, `ShrapnelCount=5`); 34 stock projectiles carry the key. The routine is at 0x46A310 of `gamemd.exe`:

- It runs when the shot goes off, before the damage is counted (0x469A3F to 0x469A51, the damage at 0x469A83): pieces are thrown also when the hit destroys the target.
- Nothing is thrown when the cell of the hit holds nothing, or when the first thing in it is a building (0x46A3E0 to 0x46A406). So a hit on a vehicle or a soldier throws pieces; a hit on a building or on bare ground does not. That is the game's rule, not a setting; the extension has no key for it.
- The routine then goes through the cells round the hit, ring by ring, as far as the piece weapon's `Range=` in whole cells (not the cell of the hit itself). The first thing in a cell gets a piece if it is not the firer and does not belong to the firer's side or an ally (0x46A4E5 to 0x46A509). Something that belongs to nobody counts as not allied, so a neutral building takes a piece too.
- Pieces that are left over go to random cells within two cells of the hit (0x46A930 to 0x46ADCD).
- A piece is a shot of the piece weapon, started at the place of the hit. If that weapon is a laser or an electric bolt, the game draws the beam from the hit to the piece's target, for the left-over pieces too (0x46A887 to 0x46A8CC and 0x46AD3E to 0x46ADB9); for that the firing unit must still be alive.
- Of the 34 stock projectiles with the key, 25 throw a piece that is invisible and instant and 9 throw one that flies in an arc; none throws a piece that homes. Use one of the first two kinds.
- If the shot's warhead has `NukeMaker=yes`, neither pieces nor damage happen (0x469A2C). Not a key of any block of ours.

**Either way, list the piece weapon under `[WeaponTypes]`.** The game reads every weapon block, then every projectile block, then every warhead block (0x679B10, 0x679B33 and 0x679B56 of `gamemd.exe`). A weapon that a unit names (`Primary=`, `Weapon1=`, `DeathWeapon=` ...) exists by then. A weapon that only a projectile names (`ShrapnelWeapon=`, `AirburstWeapon=`) is created while the projectiles are read (0x46C2C6 and 0x46C305), after the weapons were read. The extension's list `[WeaponTypes]` creates its weapons before all of that (its hook at 0x679A15). All 110 stock weapons that a projectile names (24 by `ShrapnelWeapon=`, 86 by `AirburstWeapon=`) have their line there. **[FILES]**

- In a vehicle bundle: `"register": {"Animations": [...], "WeaponTypes": ["NexusShard"]}` in `bundle.json`. The vehicle installer adds the line (one above the highest number of that list, at least 9001) and takes it out again on `remove`; it stops when the bundle's `rules.ini` has no section of that name. Since 25 Nov 2026; the installer from before is kept (section 11).
- In a pack: a line under `"WeaponTypes"` in the pack's lists, as the Doomsayer's two weapons have.
- `mo_tool.py check` and `lint-weapon` print `WARN ... this weapon has no line under [WeaponTypes]` for a piece weapon that is not listed, and a `PASS` line for one that is.

**What the Nexus uses** is the second kind: an orb that homes on its target and does the damage, and five rays from where it hits (21.3).

### 13.9 A salvo of homing missiles: how they leave, and their picture

Read in `gamemd.exe` on 25 Nov 2026 for the Tempest's swarm (20.5). The listings are in `arbalest-tank\kit\research\probe`: `dis_6FE4F0_fire_bullet_launch.txt`, `dis_6FCFA0_reload_and_burst_delay.txt`, `dis_740F80_unit_fire_facing.txt`, `dis_736A70_turret_spins.txt`. **[FILES]** None of it was watched in a game. **[UNTESTED]**

- **The gap between the shots of a salvo.** After each shot of a weapon with `Burst=` the game asks how long to wait (0x6FCFA0). While shots of the salvo are left, the answer is the unit's `BurstDelay0=` to `BurstDelay3=` for the first four gaps, if the unit has those lines, and otherwise a random 3, 4 or 5 frames (0x6FD04E to 0x6FD09B). After the last shot the weapon's `ROF=` counts. Stock units use the lines: the Perun Flagship has `BurstDelay0=0`, so its bolts leave together. The extension has no hook in that part.
- **The direction a homing shot leaves in.** A shot that homes (`ROT=` above 0) is not aimed at its target when it leaves: it starts in the direction the firing unit's weapon points, which for a unit with `Turret=yes` is the turret's direction (0x6FE8EE to 0x6FE95C; the unit's part is 0x740F80). A shot without `ROT=` is aimed at the target (0x6FE902 to 0x6FE945). With `CourseLockDuration=` the homing shot keeps that first direction for so many frames, then turns by at most its `ROT=` a frame. The extension has no hook between 0x6FE8EE and 0x6FE9B2.
- **A turret that never stops turning.** For a unit with `TurretSpins=yes` the game tells the turret every frame to turn on by 8/256 of a circle (0x736A8E to 0x736AD0). How fast it really turns then (the turret's own turning speed may limit it) was not pinned down.
- So a homing salvo from such a unit spreads by itself: each shot leaves 3 to 5 frames after the one before, in the direction the turret has turned to by then. One stock craft is made that way, the Aerial Fortress Irkalla (`GotterBow`, four slow darts with `CourseLockDuration=25` and `ROT=5`); it scatters on purpose (`Inaccurate=yes`). For shots that must hit, take the lock-and-turn values of a stock weapon that hits, unchanged: the Tempest has the Quickshifter's (`CourseLockDuration=8`, `ROT=20`).
- **Where the picture of a projectile comes from.** `Image=` stands in the projectile's rules block. When that block is read, the art keys are read with it, from the art file under the section named by `Image=`: `Trailer=`, `SpawnDelay=`, `Rotates=`, `Flat=`, `AnimLow=`, `AnimHigh=`, `AnimRate=` and `AnimPalette=` by the projectile's own loader (0x46C20E to 0x46C3E9), and `Voxel=`, `UseLineTrail=`, `LineTrailColor=` and `LineTrailColorDecrement=` by the loader that every kind of object shares (0x5F9582 to 0x5F9624, called at 0x46BEFB). That shared loader is the one that reads a vehicle's `Voxel=yes`, which works for all our vehicles. `TrailerSeperation=` stands in the stock art sections of projectiles, but the projectile's loader does not read it; how close the puffs of a trail lie is `SpawnDelay=`, in frames.
- **The trail animation** named in `Trailer=` is looked up among the animations and made new, and empty, if it is not there (0x428B80). So a trail animation of your own needs the three things of 14.1 like every other animation; the animations are read before the weapons and projectiles (13.8).
- **A missile model.** The game's own `fmisl.vxl` and `smisl.vxl` are 10 by 2 by 2 voxels; the nose points to +X and the file's origin lies near the nose, eight voxels from the tail. `new-aircraft\build_flyers.py` (`write_missile`) writes one the same way.
- Thirteen weapons of stock flying vehicles fire a visible homing shot (counted in `stock-reference\rulesmo.ini`): the Wolfhound's four missiles, the Old Longbow's two and the Quickshifter's three among them.

### 13.10 A forced attack (Ctrl), and the line that spares a side

The owner's report of 25 Nov 2026 (afternoon), after a game with the Tempest's swarm: "when I press control, it kind of makes me make it attack into anything. So I tried doing that with an airplane, another, like, you know, another aircraft to attack it. But when it does, it doesn't perform any type of damage. ... It does damage buildings, but infantry, tanks, it doesn't." **[CONFIRMED]** 25 Nov 2026 (report). The craft is not named. Of our three flyers only the Tempest's warhead had the line below.

**The cause.** A warhead with `AffectsAllies=no` (a key of the extension) does no damage to the units and buildings of the firer's own side and of its allies. Three warheads of ours had it: the Nexus's `[NexusStarburstWH]` and `[NexusShardWH]`, which are copies of the stock Ballista fragment `SeitaadMissileFragWH` and kept its line on purpose, so that a ray landing beside the tank could not hurt its own side; and the Tempest's `[TempestSwarmWH]`, where it was added for the same reason. Forced on the owner's own units, those attacks hit and did nothing. The buildings that took damage were most likely the city's, which belong to no player; the report does not say which. **[FILES]** No other warhead of ours has a line of that kind (`AffectsAllies=`, `AffectsEnemies=`, `AffectsOwner=`). In the stock rules 106 warheads have `AffectsAllies=no` and 98 `AffectsEnemies=no`, for example `ColossusWH` and `GravitronFieldWH`; most of the stock warheads have neither.

**The cure**, installed 25 Nov 2026, 14:41: the line is out of all three warheads (the Nexus and the Tempest were taken out and put in again, 21.5 and 20.7). The two build scripts, `nexus-tank\make_bundle.py` and `new-aircraft\make_bundles.py`, stop if a line of that kind gets in again, and `mo_tool.py check` warns about it. Before the cure, `check TMPS` printed:

```
  WARN  [TempestSwarmWH] has AffectsAllies=no: a forced attack (Ctrl) on a unit of that side does NO damage. Take the line out unless that is meant
```

Now it prints `PASS  [TempestSwarmWH] spares no side: a forced attack hurts whatever it is aimed at`, and `check NEXS` the same for both of its warheads. **[FILES]**

The price of the cure: a ray of the Nexus that lands on a random cell beside the tank (13.8) can now hurt a unit of its own side that stands there. **[UNTESTED]**

**What a weapon can be aimed at, forced or not.** Three things decide it. Look at all three for every weapon of a new unit (the list is in 23):

| Lines | Where | What they decide | Ours |
|---|---|---|---|
| `AA=`, `AG=` | the projectile | `AA=yes`: it can be aimed at flyers. `AG=no`: not at the ground | Only the Seraph's and the Tempest's shots have `AA=yes`. The shots of the tanks, the Nova, the Doomsayer and the Stormspire have no `AA=` line or `AA=no`, as the stock weapons they were copied from; they cannot be aimed at a flyer |
| `Verses=`, `Versus.NAME=` | the warhead | the share of the damage for each armour: `Verses=` for the 11 basic ones, a `Versus.` line for one of the 238 further armours of the game's list `[ArmorTypes]` (the list gives each of them a share or a basic armour to copy). 0% does no damage | The Nexus's two warheads do nothing to flyers: 21 lines `Versus.f_...=0%` (every flyer armour of the game, among them `f_light`, which the stock Invader and our three flyers wear) and 0% for `special_2` (flying rockets and missiles: `V3ROCKET`, `V2ROCKET`, `DMISL`, `CMISL`, `PSBOM`). All of it comes with the stock Ballista fragment, a weapon against ground targets, and was left as it is: the Nexus cannot aim at a flyer anyway. Every warhead, the stock ones too, does nothing to 15 special armours of that list, for example `special` (23 stock units, such as `SPYP` and `DMCV`) |
| `AffectsAllies=`, `AffectsEnemies=`, `AffectsOwner=` | the warhead | `no` spares that side | None, since 14:41 |

**How to test it in a game**, the owner's way: hold Ctrl and attack, with each new unit, one of your own soldiers, tanks and flyers, and a neutral building. Each must lose health; a flyer only from a weapon with `AA=yes`, and any target only if its armour is not one the weapon does nothing to by design (the `does nothing to:` column of `weapon_audit.py`). Kills of your own units give no rank (22.3). Questions 65 and 66 in section 12.

---

## 14. An animation of your own: explosion, marker, flying picture

### 14.1 What every new animation needs

Read in the game's program on 23 Nov 2026 (10.8 tells how). **[FILES]** for the program.

1. **The sprite file**, loose in the game folder, named like the animation in small letters: `doomblst.shp` for `DOOMBLST`. A section may name another file with `Image=`.
2. **A line under `[Animations]`** in the same file as the thing that uses it (the mode file, or the map file), with a number no other line there uses. The numbers in use in `Standard.ini` are printed by `unit_bundle.py status` (1.1); in the map 86101 to 86113 are used.
3. **A section with the animation's name in that same file**, with its settings. Without it the game makes the animation from the list and then loads neither settings nor picture, and says nothing about it in its log.
4. A copy of that section in `artmo.ini`. The tools read it there. It does no harm.

For a vehicle bundle this means: the animation's section must be in the bundle's `rules.ini` as well as in its `art.ini` (18.3). Since 24 Nov 2026 `mo_tool.py check` and `lint-weapon` print a WARN when an animation that `Standard.ini` lists has no section there.

The flying picture of a projectile is the exception: `DOOMFLR` has its section only in `artmo.ini` and is not listed, like some stock projectile pictures. **[FILES]** Not confirmed in the game by a report of its own. **[UNTESTED]** The Nexus's orb (`NEXSORB`, since 25 Nov 2026) is listed and has its section in both files, the way the stock flying picture `STAKFIRE` is listed in the stock rules. Neither way has been seen in a game with a picture of ours. **[UNTESTED]** An animation of ours that a warhead plays was seen on 25 Nov 2026: the Nexus's burst `NEXSSPL`, drawn in its blue, in the owner's screenshot. **[CONFIRMED]** 25 Nov 2026. It is made the way this section says: a sprite file, a list line, a section in both files, the animation palette.

### 14.2 Where an animation is named

| Named in | When it plays | Used here |
|---|---|---|
| weapon `Anim=` | At the muzzle, when the weapon fires | Stock animations only |
| projectile `Image=` | While the shot flies | `DOOMFLR`, a small burning red ball with a line trail; `NEXSORB`, the Nexus's orb |
| `Trailer=` in the art section of a projectile's picture | Dropped behind the shot, one every `SpawnDelay=` frames (13.9) | `TMPSSMK`, the pale smoke behind the Tempest's missiles |
| warhead `PreImpactAnim=` | Where the shot lands, before the damage. Damage and hit effect come when it ends | `DOOMMARK`: a red marker beam with closing rings, then three bombs falling in |
| warhead `AnimList=` | Where the shot lands, with the damage | `REAVZAP`, `DOOMBLST`; stock `NPLMEXP`, `IRONEXP`, `TSTIMPCT` |
| building art `ActiveAnim=` and `ActiveAnimTwo=` | On a building, all the time | Section 17 |

### 14.3 Way one: a stock picture under a new name

The quick way to a hit effect of your own, and the right first test in a new place. `REAVZAP` is the sprite of the stock animation `TSLAEXPE`, copied as `reavzap.shp`, with the stock section's keys under the new name.

To choose a stock animation by eye:

```powershell
python -I -B "new-units\effects_sheet.py" "new-units\effects_candidates.png" TSLAEXPE NPLMEXP IRONEXP
```

It draws the named stock animations side by side, each with the palette its art section names. The sprite files it reads are in `arbalest-tank\kit\sprites\stock`; it takes missing ones out of the archives into that folder.

### 14.4 Way two: paint it

`arbalest-tank\kit\sprites\fxkit.py` paints an effect picture by picture and stores it in the game's animation palette. The worked example is `new-infantry\build_effects.py`: it makes the Doomsayer's flare (8 pictures), marker (40) and blast (25).

```powershell
python -I -B "new-infantry\build_effects.py"
```

It writes the three sprite files and three overview pictures (`sheet_flare.png`, `sheet_mark.png`, `sheet_blast.png`) into `new-infantry\DOOM`.

How a picture is painted:

- A picture is a few layers of numbers: `heat` (fire, from nothing to white hot), `glow` (coloured light, such as a red beam), `smoke` and `solid` (hard dark shapes, such as a falling bomb). Calls such as `fireball`, `puff`, `ring`, `streak`, `dot` and `body` add to them; `to_index` turns the layers into palette colours.
- The middle of the canvas is the point the game puts the animation at. For a hit effect that is the point of impact on the ground. `x` runs to the right, `y` down.
- A circle that lies on the ground is drawn twice as wide as high.
- Nothing is random: every "noise" comes from a seed, so the same script gives the same file.
- The palette is `anim.pal`. The kit's copy is `arbalest-tank\kit\sprites\base\palettes\anim.pal`. Colour 0 is see-through.

To look at any sprite file:

```powershell
python -I "arbalest-tank\kit\sprites\shpkit.py" info "new-infantry\DOOM\doomblst.shp"
python -I "arbalest-tank\kit\sprites\shpkit.py" sheet "new-infantry\DOOM\doomblst.shp" "arbalest-tank\kit\sprites\base\palettes\anim.pal" "blast.png"
```

`info` prints the size and the number of pictures; `sheet` draws all pictures into one image; `gif` in place of `sheet` writes a moving picture.

### 14.5 The keys of an animation's section

Copy them from the stock animation that behaves the way yours should. The Doomsayer's marker has the keys of the stock strike marker `SWMARK`, his blast those of `MINIMISS`, the Reaver's burst those of `TSLAEXPE`. **[FILES]** Some values were changed on purpose. The marker has no `CustomPalette=` line (the stock marker is drawn in another palette, ours in the animation palette), another sound, and `Rate=450` instead of 400. The blast has `Translucent=no` instead of `yes` and `Rate=450` instead of 500.

| Key | What it does | Installed example |
|---|---|---|
| `Rate=` | Speed. A picture stays for 900 divided by this number of game frames (worked out from stock values, not measured) | 450 (marker, blast): 2 game frames per picture |
| `Report=` | A sound when it starts | `BeaconPlaced`, `ExplosionKirov` |
| `UseNormalLight=yes` | Drawn at full brightness, not darkened by the map's light. For fire, beams and lamps | marker, blast, building lights |
| `Layer=` | `ground` or `top`: under or over units | `top` (marker), `ground` (building animations) |
| `ZAdjust=`, `YSortAdjust=` | In front of or behind things near it | -452 and 150 (marker), copied from stock |
| `Crater=yes`, `Scorch=yes` | Leaves a hole and a burn mark on the ground | blast |
| `Translucent=`, `Normalized=` | See-through drawing, and a timing setting | `no` for both in all of ours. The stock blast `MINIMISS` has `Translucent=yes`; ours is drawn solid |
| `Start=`, `LoopStart=`, `LoopEnd=`, `LoopCount=` | Which pictures play and how often. `LoopEnd=` is the number AFTER the last picture that plays (read in the program; the stock Allied power plant has 8 pictures and `LoopEnd=8`, and its damaged twin starts at 8). `LoopCount=-1` plays for ever | building animations (17.4) |
| `Shadow=yes` | The second half of the file holds one shadow per picture | the turning dish (17) |
| `Image=` | The sprite file, if it is not named like the animation | `CGSKYW_A` |

A flying picture (`DOOMFLR`, in `artmo.ini` only) has other keys: `AnimPalette=yes` (use the animation palette), `Start=0`, `End=7`, `LoopCount=1`, `Rate=300`, and for its tail `UseLineTrail=yes`, `LineTrailColor=255,40,24`, `LineTrailColorDecrement=24`. They are the keys of stock `STAKFIRE`. **[FILES]**

### 14.6 What has been seen

- That the game accepts the names: no game since 23 Nov 2026 has a `Failed to parse INI file content` line in its log. **[FILES]**
- Building animations made this way are drawn in the game: after the third version your report was "Perfect. Everything works just fine", and your screenshot shows the Stormspire's cage and the Vault's flags, which exist only in animations. **[CONFIRMED]** 24 Nov 2026 (17.7).
- The Reaver's burst, the Doomsayer's flare, marker, bombs and blast were never named in a report. **[UNTESTED]** They are open questions 15 and 19.

---

## 15. An infantry unit with a body of its own

The worked example is the Doomsayer (10.8). His body is an original jointed figure. No pixel of his sprite comes from a stock sprite.

### 15.1 What an infantry unit consists of

| Piece | Where | Doomsayer |
|---|---|---|
| Rules block and a line under `[InfantryTypes]` | `Standard.ini` | `[DOOM]`, `9421=DOOM`: the Flak Trooper's block with his own name, price, weapon and owners |
| Weapon, projectile, warhead, animations | `Standard.ini` | section 13, section 14 |
| Art block | `artmo.ini` | `[DOOM]`: `Sequence=FlakSequence`, `FireUp=2`, `PrimaryFireFLH=30,36,192`, `SecondaryFireFLH=30,36,192`, `CameoPCX=doomicon.pcx`, `AltCameoPCX=doomuico.pcx`, `Remapable=yes`, `Crawls=no` |
| One sprite file with every picture of the body | game folder | `doom.shp`: 301 pictures and 301 shadows |
| Two icon files | game folder | `doomicon.pcx`, `doomuico.pcx` |

The rules: print a stock soldier (`mo_tool.py section FLAKT`), copy the block, and change the name, the price, `Primary=`, `Prerequisite=` and `Owner=`. Compared with the Flak Trooper the Doomsayer's block lacks the second weapon (and its `AirRangeBonus=`), the lines for fighting from inside buildings (`Occupier=`, `OccupyWeapon=` and their like) and `Fearless=yes`. **[FILES]** `Prerequisite=BARRACKS` with all twelve owners is meant to make him buildable at every side's barracks. **[FILES]** His icon is in the infantry tab of the side you played, in both screenshots of 24 Nov 2026. **[CONFIRMED]** 24 Nov 2026 for that side. The other sides were not shown. **[UNTESTED]**

### 15.2 The sprite file and its sequence

The art block names a sequence. The sequence says which pictures of the file belong to which move. The stock `[FlakSequence]`, which the Doomsayer's file follows:

| Move | Line in `[FlakSequence]` | Pictures | Count |
|---|---|---|---|
| Standing | `Ready=0,1,1` | 0 to 7 | 1 for each of 8 directions |
| Walking | `Walk=8,6,6` | 8 to 55 | 6 for each direction |
| Idle move 1 | `Idle1=56,15,0,S` | 56 to 70 | 15, one direction |
| Idle move 2 | `Idle2=71,15,0,E` | 71 to 85 | 15, one direction |
| Death 1 | `Die1=86,15,0` | 86 to 100 | 15 |
| Death 2 | `Die2=101,15,0` | 101 to 115 | 15 |
| Firing | `FireUp=116,6,6` | 116 to 163 | 6 for each direction |
| Parachute | `Paradrop=164,1,0` | 164 | 1 |
| Lying and crawling | `Prone=165,1,6`, `Crawl=165,6,6` | 165 to 212 | 6 for each direction |
| Dropping down | `Down=213,2,2` | 213 to 228 | 2 for each direction |
| Getting up | `Up=229,2,2` | 229 to 244 | 2 for each direction |
| Firing from the ground | `FireProne=245,6,6` | 245 to 292 | 6 for each direction |
| Cheering | `Cheer=293,8,0,E` | 293 to 300 | 8, one direction |

How to read a line: the first number is the first picture, the second how many pictures one direction has, the third how far on the next direction starts (0: the move has one direction only). The sequence also has `Guard=` and `Panic=`, which reuse the standing and the walking pictures, and `Die3=` to `Die5=`, which point at picture 0. After the 301 pictures the file holds 301 shadow pictures in the same order. **[FILES]**

A new figure may have another layout. Then it needs a sequence section of its own. That has not been tried: following a stock sequence is the safe way. **[UNTESTED]**

### 15.3 Directions

Measured on the game's own soldiers. **[FILES]**

- The eight directions of a move come in this order on the screen: up, up-left, left, down-left, down, down-right, right, up-right.
- The letter at the end of a sequence line (`Idle1=56,15,0,S`) is a map direction, not a screen direction: map south is the lower left of the screen (standing picture 3), map east the lower right (standing picture 5).
- So the idle moves and the cheer must be drawn in those two directions, and each death must start in the direction the game expects (death 1 as picture 3, death 2 as picture 5). The first build of the Doomsayer had them one step off; he would have jumped an eighth of a turn whenever he idled. The mistake was found by comparing with the Flak Trooper's file, not in the game.
- The tools name a picture by its screen direction. In `figure_report.json` and on the check sheet, "facing S" is picture 4, the one that looks at the camera, and "facing SW" is picture 3, which the game calls map south.

### 15.4 Size and place on the canvas

Measured on the game's own soldiers. **[FILES]**

- A standing body is 22 to 27 pixels tall. The Doomsayer's body is 24; the aerial on his back reaches 29.
- The soles are 0 to 3 pixels below the middle of the canvas, and the body is centred on it sideways.
- The canvas must have room for the lying and the fallen figure: 88 x 84, the Flak Trooper's.
- Shadows are short: about half as long as a building's.
- House colour is 11 to 27 % of a figure. Stock soldiers are stocky; a slim realistic figure looks wrong beside them.

### 15.5 Dropping to the ground and dying

- A soldier drops to the ground under fire unless his rules say `Fearless=yes`. The Flak Trooper has that line; the Doomsayer's block leaves it out on purpose.
- The moves for it are in the table: dropping down, lying and crawling, firing from the ground, getting up. Every one of them must be drawn, in all eight directions.
- A death has one direction and 15 pictures. Its last pictures must be the same picture: the body lies still. The build stops if they differ.
- Which death plays is chosen by the warhead that kills him: `InfDeath=1` plays death 1, `InfDeath=2` death 2. Other values play one of the game's own death animations (burning, electrocuted) in place of his pictures, which is why `Die3=` to `Die5=` point at picture 0. These are the usual meanings for this engine; they were not measured here. **[UNTESTED]**
- `Crawls=no` in the art block is the Flak Trooper's value and was kept. The usual meaning of `yes`: a soldier who lies down moves on his belly. Not tried. **[UNTESTED]**
- Whether the Doomsayer drops, crawls, fires from the ground and dies properly in the game has not been reported. **[UNTESTED]** (question 18)

### 15.6 Where the shot leaves

- `FireUp=2`: the shot leaves on the third firing picture (they count from 0).
- `PrimaryFireFLH=30,36,192`: the launcher's mouth on that picture, counted from the soldier's own position: forward, sideways, up. (A building counts differently: 16.8.)
- Both come from the figure itself: the build writes them into `new-infantry\DOOM\figure_report.json`. From there they are typed by hand into the art text in `new-infantry\make_pack.py` (`FireUp=`, `PrimaryFireFLH=`, `SecondaryFireFLH=`).
- Not seen in the game. **[UNTESTED]** (question 25: if the flare leaves at his left hand, the middle number needs a minus sign.)

### 15.7 Making the figure

Three files do it.

| File | What it is |
|---|---|
| `arbalest-tank\kit\sprites\figkit.py` | The tool: a body made of balls, capsules and boxes, posed by joint angles, drawn with the game's camera and light, reduced to the unit palette. It also draws the shadow. |
| `new-infantry\doomsayer.py` | The figure (coat, hood, visor, radio pack, launcher), his poses (standing, aiming, lying, crouching, the two deaths) and the plan of all 301 pictures. |
| `new-infantry\build_figure.py` | Draws every picture and shadow and writes `doom.shp`, an overview `check_sheet.png` and `figure_report.json`. |

```powershell
python -I -B "new-infantry\build_figure.py"
python -I -B "new-infantry\build_icon.py"
python -I -B "new-infantry\make_pack.py"
python -I -B "new-infantry\make_preview.py"
```

- The first line takes about three minutes. It stops if a picture is nearly empty, if a picture or a shadow touches the edge of the canvas, if the last pictures of a death differ from each other, or if the house colour is under 9 % or over 38 %.
- The second writes the two icons: the figure drawn large, in the stock icon frame with the name band (`pcxkit.make_cameo_pair`, as for the tank icons).
- The third writes the pack folder `new-infantry\DOOM` (and `REAVFIX`). Its texts are the single source of the rules and the art.
- The fourth draws `new-infantry\PREVIEW.png`.
- Look at `check_sheet.png` before anything else. It shows every move in every direction.

**Another soldier: what to change.** The scripts are written for the Doomsayer. Nobody has made a second soldier with them yet. **[UNTESTED]**

1. Copy `doomsayer.py` under a new name. Change the figure and the poses. Keep the plan of the 301 pictures, so that `Sequence=FlakSequence` still fits.
2. Copy `build_figure.py`. Change the module it loads (`import doomsayer as D`) and the folder and file it writes (`DOOM`, `doom.shp`). With the same plan, the firing picture it measures (`D.fire(2)`, the picture the shot leaves on, `FireUp=2`; for another figure the one its shot leaves on) and the two ranges of death pictures it compares (96 to 100 and 108 to 115) stay.
3. Copy `build_icon.py`, and `build_effects.py` if he has effects of his own. Change the names in them.
4. Copy `make_pack.py`. Take out its `REAVFIX` part, which belongs to the Reaver. Change every name (`DOOM`, `DoomFlare`, `DoomFlareE`, `DoomFlareP`, `DoomStrikeWH`, `DOOMFLR`, `DOOMMARK`, `DOOMBLST`, the file names). Give the list lines new numbers: one above the highest of each list that `unit_bundle.py status` prints (1.1).
5. Run the figure build. Then type `FireUp=` and the fire point from the new `figure_report.json` into the art text of your pack script (15.6).
6. Run the pack script, look at the check sheet, rehearse on a copy (16.10), install, and run `packs.py verify` with the new pack's name.

### 15.8 Installing

```powershell
python -I "arbalest-tank\kit\packs.py" install "new-infantry\DOOM" --dry-run
python -I "arbalest-tank\kit\packs.py" install "new-infantry\DOOM"
python -I "arbalest-tank\kit\packs.py" verify DOOM
```

On a game folder that does not have the pack yet, the first line only says what would be written. The Doomsayer is installed, so today the first line answers `NOTHING DONE: pack DOOM is already installed (record found); remove it first`, and the second would answer the same. `verify` ends with `checks: 49 passed, 0 FAILED` (48 until 25 Nov 2026, when it learned to refuse a soldier drawn with a stock sprite, 1.5). 10.8 has the rest. `mo_tool.py check` is made for vehicles and prints three false FAILs for him; his weapon can be checked with `mo_tool.py lint-weapon DoomFlare`.

### 15.9 What has been seen

- His icon is in the infantry tab. **[CONFIRMED]** 24 Nov 2026 (your screenshots of 10:53 and 14:10).
- The game of 23 Nov, 22:04, listed him among the six starting unit types. **[FILES]**
- How the body looks and moves, the drop to the ground, the deaths, the flare, the marker and the blast: never named in a report. **[UNTESTED]** (questions 18, 19, 25, 26)
- What is still short of the game's own soldiers: less pixel-level detail than a stock trooper drawn by hand.

---

## 16. A building on a map

The worked example is the Black Site: five buildings on (6) Kalifornia Crisis (10.8; the fifth, the Vessel, since 25 Nov 2026: 16.12). Everything about them is written down in one file, `new-buildings\blacksite.py`: where they stand, their rules, their art entries, their weapon, and the lines the map gets. The pack is made from it.

### 16.1 Why through a map

A building needs a place. The game's own maps bring buildings of their own: the map file holds a list `[BuildingTypes]` and a rules section for each. **[FILES]** A map pack does the same. So the buildings are on that one map in every game mode, and on no other map. **[FILES]** A building that players build from the sidebar has not been tried. **[UNTESTED]**

### 16.2 What the map file gets

Fourteen lines in sections the stock map already has (twelve until 25 Nov 2026), and one block of new sections at its end. **[FILES]**

| Section | Line | Meaning |
|---|---|---|
| `[Structures]` | `1026804=Neutral,CASPIR,256,83,89,0,None,0,0,1,0,0,None,None,None,0,0` | Number (above the map's highest), owner, type, strength (256 is full), cell x, cell y. The rest is copied from the map's own lines. The cell is the top corner of the lot. |
| `[Waypoints]` | `93=90084` | A free waypoint number, and the cell in the middle of the building as y times 1000 plus x |
| `[Triggers]`, `[Events]`, `[Actions]`, `[Tags]` | one line each | A copy of the trigger of the stock King-of-the-Hill maps: at the start it uncovers the ground round the waypoints of the buildings, so they can be seen from the first second |

The block at the end holds:

- `[BuildingTypes]` with one line per building (numbers 86001 to 86005) and `[Animations]` with one line per animation (86101 to 86113). Use numbers far above the stock ones.
- `[WeaponTypes]` and `[Warheads]` lines for the Stormspire's weapon.
- A rules section per building, the weapon and its warhead.
- A section per animation (14.1).

Taking those lines and that block out again gives the stock map, byte for byte. The installer checks the stock map by its hash before it writes. **[FILES]**

### 16.3 The rules of a building

Copy a stock tech building that does what yours should do, and change little.

| Building | Copied from | Changed |
|---|---|---|
| Helion Reactor `CAHLIO` | Tech Nuclear Plant `[CANRCT]` | no explosion when it dies; `Power=600` |
| Skywatch Array `CASKYW` | Tech Satellite Hack Center `[CACOMN]` | nothing in what it does (`SpySat=yes`) |
| Black Vault `CAVALT` | Tech Deposit Bank `[CABANK]` | 60 credits at a time instead of 40 |
| Stormspire `CASPIR` | the capture keys of the Tech Turret `[CACANN]`, the fixed weapon of the Tesla Coil `[TESLA]` | a weapon of its own (13.2, 13.5); `HasRadialIndicator=true`; needs no power |
| The Vessel `CAVESL` (since 25 Nov 2026) | Seattle Space Needle `[CASEAT01]`, the game's own garrisonable landmark | its name, `Strength=1200`, `LeaveRubble=no`, a warm light; none of the capture keys below (16.12) |

The keys the first four share make a building that belongs to nobody and can be captured: `Owner=Neutral`, `Capturable=yes`, `NeedsEngineer=yes`, `Unsellable=yes`, `TechLevel=11`, `BaseNormal=no`, `LeaveRubble=no`, `RadarVisible=yes`. **[FILES]** That they can be captured, take the owner's colour, pay and shoot: **[CONFIRMED]** 24 Nov 2026 (10.8).

**The coloured light on the ground.** Each building has five lines for it, the keys the stock Tech Protector has:

```ini
LightVisibility=2600
LightIntensity=0.01
LightRedTint=0.7
LightGreenTint=0.01
LightBlueTint=0.75
```

These are the Stormspire's (violet). The three tints mix the colour. **[CONFIRMED]** 24 Nov 2026: the lights show after capture, and you like them. Whether they show before capture was not said. **[UNTESTED]**

### 16.4 The art entry and the file names

This is the Stormspire's block in `artmo.ini`, as the pack wrote it:

```ini
[CASPIR]
Image=CGSPIR
Normalized=no
Remapable=yes
Foundation=2x2
Height=7
NewTheater=yes
CanHideThings=true
CanBeHidden=false
OccupyHeight=3
DamageFireOffset0=-2,34
DamageFireOffset1=29,10
PrimaryFireFLH=0,0,320
ActiveAnim=CASPIR_L
ActiveAnimDamaged=CASPIR_L
ActiveAnimZAdjust=-15
ActiveAnimYSort=362
ActiveAnimPowered=no
```

- The keys are those of the stock Tech Nuclear Plant `[CANRCT]` on all four, with each building's own `Foundation=` and `Height=`. The Stormspire's `ActiveAnimZAdjust=-15` is the value of the stock 2x2 Tech Power Plant `[CAPLANT]`, its `ActiveAnimYSort=362` that of the stock oil derrick. The two `DamageFireOffset` lines say where fire burns on a damaged building. They are the 3x3 plant's on all four; for the 2x2 Stormspire they were not fitted. **[FILES]**
- `Image=CGSPIR` with `NewTheater=yes`: the sprite file is `cgspir.shp`. The second letter of the name stands for the kind of landscape; `G` is the one that fits every landscape, and the stock tech buildings use it the same way (`[CANRCT]` has `Image=CGNRCT`). So name an ID `CA....` and its file `cg....shp`.
- `Remapable=yes`: the house-colour parts take the owner's colour.
- `Foundation=`: the lot in cells. `Height=`: copied from a stock building of similar height.
- `PrimaryFireFLH=`: where the shot starts (16.8). Only for a building with a weapon.
- The `ActiveAnim` lines: section 17.

### 16.5 The picture file

Measured on thirty of the game's own buildings (`arbalest-tank\kit\sprites\stock-buildings`). **[FILES]**

- **Six pictures:** the building, the damaged building, the damaged building once more, then a shadow for each of the three. Shadow pixels have colour number 1. A building that soldiers can garrison shows its third picture while they are inside (16.12).
- **The anchor:** the middle of the canvas is the top (north) corner of the lot. Checked with the client's map renderer: a flat test slab covered its 3x3 lot to the pixel.
- **The camera:** a cell edge is 42.43 pixels long in the model. A point (x, y, z) of the model lands on the screen at x = (x - y) x 0.7071, y = (x + y) x 0.3536 - z x 0.866.
- **The light:** from the upper left. Tops are brightest, the left wall is lit, the right wall keeps about half the light. A 1x1 tower's shadow falls 0.78 pixels right and 0.14 up for every pixel of height.
- **The palette:** the unit palette. Colours 16 to 31 are the house colour. The game's building pictures never use 200 to 203 or 240 to 254; its small light files use 240 to 244.
- **The look,** on the game's power plants, radars and barracks: 100 to 134 colours in one sprite, 6 to 30 % house colour in large riveted panels, only 20 to 45 % plain grey, textured materials (brick, corrugated sheet, speckled stone), glossy metal and glass, and a dark line at the foot.

### 16.6 Making the picture

`arbalest-tank\kit\sprites\structkit.py` builds a building from solid shapes (boxes, cylinders, balls, rings, many-sided prisms, dishes), gives every shape a material (brick, sandstone, paving, steel, brass, copper, glass, house-colour plate and more), shades it in true colour with soft shadows and reflections, and only then reduces the picture to the palette. `new-buildings\parts.py` has ready-made small parts: doors, rows of windows, railings, ladders, pipes with flanges, tanks, stacks, masts, lamps. The four build scripts (`build_helion.py`, `build_array.py`, `build_vault.py`, `build_spire.py`) are the examples; `build_spire.py` is the shortest.

What took the pictures from "model railway" to the game's look (the first version was sent back for it, 10.8):

- one massive structure on the lot, not several small ones;
- a dark olive cobbled pad, not light concrete;
- seams a full pixel wide and nearly black, and a dark line round every part and at the foot;
- dark rivets on house-colour plates that sit in pale stone frames;
- brass and copper accents, and a bright streak down every polished upright cylinder;
- brick that is mottled, never one flat brown;
- a strong second light on the shaded side, so that right-hand walls keep their form;
- enough house colour to read the owner after capture: 7 to 11 % here, 8 to 14 % on the game's own.

What is still short of the game's art: the surfaces are a little cleaner than hand-finished ones, and the damaged pictures are scorch marks and holes placed by rule.

### 16.7 Judging the picture: the map renderer

A sheet of numbers is not enough; the first version passed its numbers and still looked wrong. The test that decides is to see the draft on the map beside the game's own buildings. The client ships a map renderer (`Mental Omega\Map Renderer`). Two scripts run it on copies in a work folder; the game folder is only read.

```powershell
python -I -B "new-buildings\gate_map.py" . "$env:TEMP\mo-gate" "$env:TEMP\mo-gate.png"
python -I -B "new-buildings\render_site.py" "$env:TEMP\mo-site" --installed
```

- The first draws the plaza with the sprites from the four build folders and four of the game's own buildings placed beside them (Allied power plant, Tesla reactor, Soviet radar, Allied barracks). Look at the result at its real size and enlarged.
- The second draws the installed map as it is and writes `new-buildings\SITE.png`. Without `--installed` it draws the stock map with the pack laid over it in memory, so a pack can be seen before it is installed; that works only while the game folder holds the stock map, and with `SITE` installed the script stops (`the map in the game folder is not the stock file`). Then install the new pack on a rehearsal copy and draw the copy: `--installed --game` with the copy's `Mental Omega` folder (1.6, step 7; 16.12). Either way it writes `new-buildings\SITE.png`.
- Both take `--daylight` (without the map's dusk light). `gate_map.py` takes `--game` with a folder (a rehearsal copy, 16.10); `render_site.py` takes it only together with `--installed`.
- The renderer shows one moment of every animation. It shows that a moving part is there and where; it cannot show that it moves.
- A building that belongs to nobody is drawn with light grey house-colour parts by the renderer.
- Never run the renderer on the game's own files or with its options that change a map (section 0).

`new-buildings\make_preview.py` puts the renderer's picture and six moments of every animation into `new-buildings\PREVIEW.png`, and writes a moving picture `anim.gif` into each building's folder.

### 16.8 Where a building's shot starts

`PrimaryFireFLH=0,0,H` puts the start of the shot H x 15 / 104 pixels above the middle of the sprite canvas. That middle is the top corner of the lot, not its middle. **[FILES]**

- Measured twice. The game's own Tesla Coil has `0,0,375`: 54 pixels above the canvas middle, which is the middle of its ball. And the Stormspire's first value, 531, had been counted from the middle of its 2x2 lot: in your screenshot of 24 Nov 2026 (10:53) the bolt started 30 pixels above the ball.
- The right value comes from the model: `anim.fire_flh()` in the build script gives `0,0,320` for the Stormspire's ball. In your screenshot of 14:10 the bolt starts in the ball. **[CONFIRMED]** 24 Nov 2026
- Vehicles and infantry count their fire point from the unit's own position (15.6, 18.3). Only buildings count from the canvas.

### 16.9 A building with a weapon

Its ring and its real reach are two different things: read 13.5 and run `check_range.py`. Its weapon block stands in the map file with the building.

### 16.10 Pack, rehearsal, install

```powershell
python -I -B "new-buildings\build_spire.py"
python -I -B "new-buildings\site_preview.py" "$env:TEMP\mo-site-preview"
python -I -B "new-buildings\make_pack.py"
python -I "arbalest-tank\kit\tests\make_sandbox.py" . "$env:TEMP\mo-sandbox"
python -I "arbalest-tank\kit\packs.py" --root "$env:TEMP\mo-sandbox" remove SITE
python -I "arbalest-tank\kit\packs.py" --root "$env:TEMP\mo-sandbox" install "new-buildings\SITE"
python -I -B "new-buildings\check_range.py" --game "$env:TEMP\mo-sandbox\Mental Omega"
```

1. A build script writes its sprite files and a report into the building's folder (`new-buildings\CASPIR`). The three other buildings have their own scripts. The Stormspire takes about a minute, the Skywatch Array six. A full build also writes `anim.gif` into that folder, under the map's dusk light; `make_preview.py` writes it again in daylight.
2. `site_preview.py` makes the two preview pictures of the map with the buildings (16.13). `make_pack.py` writes the pack folder `new-buildings\SITE` from `blacksite.py`, the building folders and those pictures. It refuses if the art entries do not match the files (numbers of pictures, speeds, the fire point), and if the pictures were made from other sprite files or places. It writes over the pack folder: if the version in it is installed and you are about to change it, copy the folder to a new `round` folder first (section 0).
3. `make_sandbox.py` copies exactly the files the installer reads and writes into a new folder outside the project. The folder must not exist yet.
4. With `--root` the installer works on that copy. A pack that is installed must be removed before its new version goes in. The install ends with `checks: 137 passed, 0 FAILED` (since 25 Nov 2026, 15:04: five buildings and the two pictures).
5. The range check on the copy must end with `Result: 0 FAIL`.

Then the same on the game, with the game and the client closed:

```powershell
python -I "arbalest-tank\kit\packs.py" remove SITE
python -I "arbalest-tank\kit\packs.py" install "new-buildings\SITE"
python -I "arbalest-tank\kit\packs.py" verify SITE
python -I -B "new-buildings\check_range.py"
```

The installer's own test installs, damages, refuses and removes on a copy it makes itself:

```powershell
python -I "arbalest-tank\kit\tests\test_packs.py" "$env:TEMP\mo-packtest" . "new-infantry\REAVFIX" "new-infantry\DOOM" "new-buildings\SITE"
```

It ends with `84 of 84 checks pass` (25 Nov 2026, with the two pictures). Its first folder must not exist yet.

### 16.11 One more building, or another map

**One more building on the plaza: what to do.** Done once, on 25 Nov 2026, for the Vessel (16.12); these are the steps it took.

1. Find a free, level lot. This line prints the heights of the ground round the plaza, and every building whose north corner lies in that part of the map, stock ones and ours (since 25 Nov 2026; before, only the first four of ours):

```powershell
python -I "arbalest-tank\kit\research\range\heights.py" "arbalest-tank\kit" "Mental Omega\MapsMO\Standard\kalifornia.map" 66 100 66 104
```

   The four numbers are the first and last column (x) and the first and last row (y) to print. The plaza is the area of level 6. The picture `new-buildings\SITE.png` shows what else stands there. The installer refuses a lot that is not level or not free.
2. Write a build script: copy `build_spire.py` (2x2) or one of the 3x3 scripts and change it (17.3).
3. In `blacksite.py`: a line in `BUILDINGS` (ID, file name, name, lot, top cell, script), its rules in `RULES`, its art numbers in `ART`. If it has a weapon: the weapon's and the warhead's sections in `WEAPONS`, their names in `WEAPON_NAMES` and `WARHEAD_NAMES`, and a projectile of its own in `PROJECTILE_NAMES` if it needs one (13.5).
4. In `make_preview.py`: one line for the new ID in `ROLE` and one in `MOVES`. Without them the preview stops with an error. Its title line names the number of buildings ("five buildings"); change that too.
5. The numbers take care of themselves: each building gets the next number in the lists, the next waypoint (the Vessel got 94; 95 to 97 are free in the stock map) and one more action in the reveal trigger.
6. Copy the present pack folder to a new `round` folder (section 0).
7. Build, make the pack, rehearse, run the range check, install (16.10).

- A name that the stock rules or the stock art already use is refused by the installer. Check it first (section 0).
- Another map: `blacksite.py` names the map file and the hash of its stock version at its top, and the cells of the buildings. The reveal trigger uses waypoint numbers 90 to 94 and the trigger numbers of the stock King-of-the-Hill maps; check that the other map does not use them. Not tried. **[UNTESTED]**
- A changed map file is one more reason not to play online with this install (10.6).

### 16.12 The fifth building: the Vessel, a landmark that soldiers can garrison

The owner asked on 24 Nov 2026 for "the vessel as like a separate building that gets generated within the maps", and when asked what "the vessel" was, answered on 25 Nov 2026: "You know the vessle in nyc? Thats the building. I want it to get occupied with military as well." So it is the Vessel of Hudson Yards in New York, as a building on the plaza of (6) Kalifornia Crisis that soldiers can garrison. It is installed since 25 Nov 2026 as the fifth building of the pack `SITE` (first at 00:48, and at 01:16 once more with the picture it shows while soldiers are inside). Seen in the owner's game of 25 Nov 2026 (10:40): "The vessel seems all right. Everything looks perfect. Everything is fine. I love how it garrisons people"; the screenshot shows it on the plaza. **[CONFIRMED]** 25 Nov 2026: it stands on its lot, and soldiers can garrison it. Its lift, its lights, the colour it shows while it is occupied and the firing flashes were not named. **[UNTESTED]** In the same message the owner asked: "you weren't able to make it more realistic based on the actual vessel photos and stuff, or that's the closest thing you got to it." The answer is at the end of this section: the installed model was made without a photograph in front of it, and two models made from photographs are ready to pick from.

**What it is to the game: a copy of the game's own garrisonable landmark.** 176 stock buildings have `CanBeOccupied=yes`. The Vessel's rules are those of the stock Seattle Space Needle `[CASEAT01]` (the Gateway Arch `[CASTL04]` has the same garrison keys), with its own name, `Strength=1200`, `LeaveRubble=no` (our sprites have no rubble picture) and a warm coloured light on the ground like the other four buildings. **[FILES]** It does NOT get the capture keys of the other four (`Capturable=yes`, `NeedsEngineer=yes` and the rest of `COMMON` in `blacksite.py`): it is taken by putting soldiers into it, like the game's civilian buildings, and `TechLevel=-1` means nobody can build it. Its rules section, exactly as it is in the map file:

```ini
[CAVESL]
UIName=NOSTR:The Vessel
Name=The Vessel
TechLevel=-1
Strength=1200
Insignificant=yes
Nominal=yes
Points=5
Armor=garrison_a
UC.PassThrough=1%
UC.DamageMultiplier=2%
Explosion=GBLDEXP1,GBLDEXP2,GBLDEXP3,GBLDEXP4,GBLDEXP5,GBLDEXP6,GBLDEXP7,GBLDEXP8,GBLDEXP9,GBLDEXP10
DebrisAnims=DBRI-WM1,DBRI-WM2,DBRI-WM3,DBRI-WM4,DBRI-WM5,DBRI-WM6
MaxDebris=12
MinDebris=6
BaseNormal=no
Sight=8
ClickRepairable=no
CanBeOccupied=yes
MaxNumberOccupants=10
LeaveRubble=no
DieSound=MonumentCrumble
CanOccupyFire=yes
Chronoshift.Allow=no
LightVisibility=2600
LightIntensity=0.01
LightRedTint=0.75
LightGreenTint=0.42
LightBlueTint=0.15
```

**Where the soldiers fire from.** A garrisonable building's art has ten points `MuzzleFlash0=` to `MuzzleFlash9=`, where the flash of a soldier's shot appears. They count in screen pixels from the centre of the sprite canvas, the north corner of the lot, like a building's fire point (16.8). The ten points of the stock Space Needle land on its deck, its shaft and its base when they are drawn that way on its own sprite; counted from the middle of the lot they land in the air beside it. **[FILES]** The picture and the script that drew it are in `arbalest-tank\kit\research\garrison` (`needle_muzzle.png`, `needle_muzzle.py`; the sprite `cuseat01.shp` comes from the base game's archive and was read with `arbalest-tank\kit\research\probe\d2_basegame.py`). The Vessel's ten points are landings that face the camera, from the rim down, worked out from the model by `muzzle_flashes()` in `new-buildings\build_vessel.py`. `make_pack.py` refuses to write the pack if the art entry and the model disagree. The other art keys are those of the stock garrisonable buildings (`OccupyHeight=7`, two `DamageFireOffset` points), but with `Remapable=yes` (below). Its art section, exactly as it is in `artmo.ini`:

```ini
[CAVESL]
Image=CGVESL
Normalized=no
Remapable=yes
Foundation=3x3
Height=8
NewTheater=yes
CanHideThings=true
CanBeHidden=false
OccupyHeight=7
DamageFireOffset0=9,30
DamageFireOffset1=0,3
MuzzleFlash0=33,-22
MuzzleFlash1=0,-17
MuzzleFlash2=-33,-22
MuzzleFlash3=16,-9
MuzzleFlash4=-16,-9
MuzzleFlash5=27,-3
MuzzleFlash6=0,2
MuzzleFlash7=20,17
MuzzleFlash8=0,20
MuzzleFlash9=0,39
ActiveAnim=CAVESL_A
ActiveAnimDamaged=CAVESL_AD
ActiveAnimZAdjust=-5
ActiveAnimYSort=562
ActiveAnimPowered=no
ActiveAnimTwo=CAVESL_L
ActiveAnimTwoDamaged=CAVESL_L
ActiveAnimTwoZAdjust=-25
ActiveAnimTwoYSort=562
ActiveAnimTwoPowered=no
```

**What it looks like with soldiers inside.** The sprite of a garrisonable building has one more kind of picture. The game's own Space Needle and Texas office tower have eight frames each: the building, the damaged building, the building with house colour on it (the Needle on its deck and its legs, the office tower on its roofs), the rubble, then a shadow for each. **[FILES]** (`arbalest-tank\kit\research\garrison\stock_garrison_frames.png`, drawn with `frames_of.py` in the same folder.) A post on the Project Perfect Mod forums (thread "Garrisoned Structure Doesn't Reveal it's under captured.", 19 Feb 2021) says that the game shows that third picture while soldiers are inside; it was not read in the game's program. The sources and the pictures are listed in `arbalest-tank\kit\research\garrison\README.md`. The first build of the Vessel had the order of our tech buildings, so its third picture was the damaged one: garrisoned, it would have looked damaged (19). Now the third picture is the Vessel with its rim and two rings of landings in house colour, made by `occupied()` in `build_vessel.py`; `new-buildings\anim.py` uses such a function for the third picture when a build script has one, and the other buildings are built as before. The Vessel has `LeaveRubble=no`, so it needs no rubble picture, and its file keeps the six frames the installer checks. It has `Remapable=yes`, as the other four buildings have and as 4 of the 176 stock garrisonable buildings have (76 have `no`, 96 do not set it), so that the colour is the one of the soldiers' side. Whether the game shows the house colour of the occupant on a stock building with `Remapable=no` was not read. That the third picture shows in this game, and in which colour: **[UNTESTED]** Three stock garrisonable buildings have an animation as well (`ActiveAnim=`: the Tower of London, the MassiveSoft Campus, the Concession Stand), as the Vessel has. **[FILES]**

**The model.** This is the installed one. It was made from what was remembered of the shape, without a picture; what the photographs show instead is at the end of this section. `new-buildings\build_vessel.py` builds it with the kit of 16.6:

- Eight rings of landings, ten landings to a ring, every ring turned by half a step against the one below. Each landing is joined to the two above it by a flight of stairs, so the flights form the lattice of diamond-shaped openings. (The real one has 80 landings and 154 flights, and is 46 m high, 15 m across at the foot and 46 m at the rim.) The radius grows from 16.5 world pixels at the foot to 55 at the rim.
- A flight runs round the vase, so its width points to the axis. It has steps on top (light treads with risers), a copper soffit below and a copper parapet on both sides. The shapes are worked out layer by layer from the two families of slanting lines (`lattice()`), not stacked from boxes.
- A plaza of granite pavers with planters, trees, benches and four lamp posts, on the dark cobbled pad the other buildings stand on.
- The copper is a material of its own (`vessel_cu`) with little mirror and fine grain. With more of either the lattice looked speckled at the game's size.

**What moves** (17): a main animation `CAVESL_A` (40 pictures, `Rate=110`, about 5.5 seconds a loop at the client's speed), in which a glass lift rides up the right-hand side on two rails, waits, comes down and waits. And a light animation `CAVESL_L` (24 pictures, `Rate=180`): a band of warm light climbs the lattice from the foot to the rim and makes the rim flash, two red beacons on the rim blink in turn, and the plaza lamps are lit. Light pixels that the lift covers in any picture are left out of the light file (17.2): 55 of them.

**Where it stands.** Cells 74 to 76 by 82 to 84, on the west arm of the plaza between the airport and the Black Vault, free and level at height 6. The pack gives it the structure line 1026805, waypoint 94 and a fifth action of the reveal trigger.

**What changed in the pack's tools.** The other four buildings come out as before: their rules and art sections were compared line by line, and only the lists gained the Vessel's lines.

- `blacksite.py`: the Vessel's line in `BUILDINGS`, its rules, its art entry. `COMMON_FOR` names a building that does not get the common capture keys. An art entry may carry `remap`, `occupy`, `fire_offsets` and `muzzle`.
- `make_pack.py` checks the `MuzzleFlash` and `DamageFireOffset` points against the model.
- `make_preview.py` has the Vessel's lines in `ROLE` and `MOVES`, and its title says five buildings.

The pack as it was before the Vessel is kept in `new-buildings\round4\SITE`, with the three scripts as they were; that folder installs as it is.

**Build, make the pack, rehearse** (16.10):

```powershell
python -I -B "new-buildings\build_vessel.py"
python -I -B "new-buildings\make_pack.py"
python -I "arbalest-tank\kit\tests\make_sandbox.py" . "$env:TEMP\mo-sandbox-vessel"
python -I "arbalest-tank\kit\packs.py" --root "$env:TEMP\mo-sandbox-vessel" remove SITE
python -I "arbalest-tank\kit\packs.py" --root "$env:TEMP\mo-sandbox-vessel" install "new-buildings\SITE"
python -I -B "new-buildings\check_range.py" --game "$env:TEMP\mo-sandbox-vessel\Mental Omega"
python -I -B "new-buildings\render_site.py" "$env:TEMP\mo-site-vessel" --installed --game "$env:TEMP\mo-sandbox-vessel\Mental Omega"
```

Run as printed on 25 Nov 2026. The build takes about nine minutes; two runs of the version without the occupied picture gave the same files, byte for byte. `make_pack.py` answers `wrote SITE: 14 files (825633 bytes), 13 animation types, 14 map lines`, and the pack equals what is installed. On the copy the install ended with `checks: 135 passed, 0 FAILED`, the range check with `Result: 0 FAIL`, and the map renderer drew the Vessel on its lot into `new-buildings\SITE.png`. The installer's own test with all three packs (16.10) ends with `76 of 76 checks pass`. **[FILES]** The two folders named in the lines must not exist yet; `render_site.py` needs `--installed --game` here, because the map in the game folder is not the stock file any more.

Then for real, with the game and the client closed:

```powershell
python -I "arbalest-tank\kit\packs.py" remove SITE
python -I "arbalest-tank\kit\packs.py" install "new-buildings\SITE"
python -I "arbalest-tank\kit\packs.py" verify SITE
python -I -B "new-buildings\check_range.py"
```

On 25 Nov 2026 at 00:48, and again at 01:16 with the occupied picture, the install and the check ended with `checks: 135 passed, 0 FAILED`, the range check with `Result: 0 FAIL`. **[FILES]**

**The way back** to the four buildings without the Vessel, with the game and the client closed:

```powershell
python -I "arbalest-tank\kit\packs.py" remove SITE
python -I "arbalest-tank\kit\packs.py" install "new-buildings\round4\SITE"
```

Rehearsed on the copy on 25 Nov 2026: the map came back byte for byte. `artmo.ini` came back with the same lines, but the pack's block now stands after the blocks of the vehicle installer, because an install always appends at the end of the file. **[FILES]** The live file had the same move when the pack went in again at 00:48.

A reinstall changes the map file, so saved games made on (6) Kalifornia Crisis before it may not load (10.8).

**A second model, made from photographs (25 Nov 2026). Not installed: the owner picks.**

Six photographs of the real Vessel were fetched from Wikimedia Commons after the owner's question. They are in `new-buildings\vessel-photos`; its `README.md` names the author and the licence of each and what was read from it. They show three things that the installed model has wrong:

| | The installed model (A) | The photographs | The second model |
|---|---|---|---|
| The lattice | Eight rings of ten small landings, joined by long thin flights: a net of diamond-shaped openings | A honeycomb: a level of landings every storey, five landings to a level, each level turned by 36 degrees against the one below. A landing is a long flat platform, a flight is short, so the openings are wide flat hexagons and the whole reads as stacked rings that step up and down by one storey | Sixteen levels of five landings, 7 world pixels apart; a flight has a run of 11, and the landing takes the rest of the step |
| The outline | Nearly a cone | A cup: already wide a third of the way up | The radius grows with the height to the power 0.62 (the installed one: 1.10) |
| The colour | 24 % of the vase's pixels are on the unit palette's pink-brown colours (numbers 101 to 107) and 21 % on its dull browns (155 to 163); 2 % on its oranges | A deep orange-brown copper with golden highlights; grey decks and steps; glass balustrades | A redder, deeper copper as the material: in candidate C 18 % of the vase's pixels are on the palette's oranges (182 to 191) and 20 % on its red-browns (108 to 110). Grey decks between two copper strips |

The numbers known of the real one, 80 landings and 154 flights, fit both readings (8 times 10, and 16 times 5); only a picture tells which is right (19).

`new-buildings\build_vessel2.py` builds the second model in two versions: **B** with a thin pale rail of glass on the outer edge of every deck, and **C** (with `--no-rails`) all in copper. Rules, lot, the lift, the lights, the picture with soldiers inside and the way the firing points are worked out are those of the installed model. `new-buildings\vessel_pick.py` draws the picture to pick from, `new-buildings\VESSEL-PICK.png`: three of the photographs, then A, B and C, each drawn from its sprite file (A from the one in the game folder) three times: in the tool's even light, under the light of the map (6) Kalifornia Crisis, and with soldiers inside under that light. The row under the map's light is the one to judge by: it is close to what the game shows, and duller than the tool's light.

```powershell
python -I -B "new-buildings\build_vessel2.py" --still
python -I -B "new-buildings\build_vessel2.py" --still --no-rails
python -I -B "new-buildings\build_vessel2.py"
python -I -B "new-buildings\build_vessel2.py" --no-rails
python -I -B "new-buildings\vessel_pick.py"
```

Run as printed on 25 Nov 2026, from the project folder. The first two are a quick look while the model is being changed: about ten seconds each, three pictures into `new-buildings\vessel-v2\B\CAVESL` and `new-buildings\vessel-v2\C\CAVESL`. The next two are the full builds, about eight minutes each: the three sprite files with the lift's and the lights' animations, the damaged picture and the picture with soldiers inside, and the kit's own pictures (`sheet.png`, `anim.gif`, `gate.png`), into the same two folders. Both ran to their end; the kit stops a build when a picture is empty, touches the edge of its canvas, or when a moving part leaves a hole in the building's picture. Each full build was run twice; the second run gave the same three sprite files, byte for byte. The last line needs the full builds and answers with the path of `VESSEL-PICK.png` and its size, 2237 by 2220. **[FILES]** Nothing of this is in the game, and neither candidate has been drawn on the map by the client's renderer yet (16.7). **[UNTESTED]**

What stays unlike the photographs at the game's size, whichever is picked: a storey is about five pixels high, so single steps, people and the mirror of the undersides cannot show; and the game's light on the map makes the copper duller than in the tool's pictures (`sheet.png` has a tile "under the map light").

**If the owner picks B or C**, in this order:

1. Copy `new-buildings\SITE` to the next free `round` folder, `new-buildings\round6\SITE` if no other change came first (1.6, step 5), and put `build_vessel.py`, `blacksite.py`, `make_pack.py` and `site_preview.py` beside it as they are, so that the installed pack stays installable (section 0).
2. Make the picked model the building's script: copy `build_vessel2.py` over `build_vessel.py`, and in the copy set `OUT = HERE`, so that it writes into `new-buildings\CAVESL`; for C also set `RAILS = False`. Build it (`python -I -B "new-buildings\build_vessel.py"`). Its three sprite files must be the candidate's, byte for byte.
3. In `blacksite.py`, in `ART['CAVESL']`, replace the ten `muzzle` points and the two `fire_offsets` by the ones that `build_vessel.py --points` prints. Both candidates give the same: `(0,-22) (33,-22) (-33,-22) (0,-12) (31,-11) (-31,-11) (29,-1) (-29,-1) (0,19) (22,30)` and `(0,30) (0,0)`. `make_pack.py` checks them against the model.
4. Run `site_preview.py` (16.13; `make_pack.py` refuses the pictures of the old model), then `make_pack.py`, then the rehearsal lines and the install lines above, then `render_site.py`, to see it on the map beside the other four.
5. Record the pick and the install here and in section 11, and ask question 59's follow-up in section 12: does it look like the photographs now?

The way back afterwards: `remove SITE` and `install "new-buildings\round6\SITE"`.

### 16.13 The map's two preview pictures

The owner's report of 25 Nov 2026 (afternoon): the picture of (6) Kalifornia Crisis in the skirmish screen, and the small one when a game starts, "doesn't show the new buildings that we included. It should." **[CONFIRMED]** 25 Nov 2026 (report). Until then a pack changed the map and left both pictures as they were.

**Where each picture comes from** (read in the client's files and in the game's program on 25 Nov 2026):

| Picture | Where it is | Who reads it |
|---|---|---|
| In the skirmish screen | `Mental Omega\MapsMO\Standard\kalifornia.png`, 774 x 299, beside the map. The client's list of maps, `Mental Omega\INI\MentalOmegaMaps.ini`, gives it `PreviewSize=774,299` | the client |
| On the loading screen | the sections `[Preview]` (`Size=0,0,170,62`) and `[PreviewPack]` inside the map. The client writes the map with the game's settings to `Mental Omega\spawnmap.ini` | the game: the loading screen (gamemd 0x5535A7) calls a reader (0x641EE0, 0x641B00) with the name of that file |

The radar during a game is drawn from what stands on the map and needs no picture. **[UNTESTED]** that the five show on it.

**What is in `[PreviewPack]`.** Base64 text in numbered lines of 70 characters. Decoded: blocks, each starting with two 16-bit numbers (the bytes in the block, the bytes it unpacks to), packed with LZO1X; unpacked, three bytes (red, green, blue) for each pixel, row after row. The game unpacks a block into room for 16384 bytes (gamemd 0x55C720); its own writer makes blocks of 8192 (0x6418B0). The stock picture of this map has four blocks that unpack to 8192, 8192, 8192 and 7044 bytes. It shows a building as grey (red 120, green 124, blue 120) where it stands: 81% of the pixels under the 122 stock buildings of this map are that grey; the rest lie under trees and start marks. **[FILES]**

**How the two new pictures are made** (`new-buildings\site_preview.py`):

1. The skirmish picture. The client's map renderer draws the whole map twice, on copies: as it is, and with the five buildings, both with the settings of 16.7. The two drawings differ all over the map, not only at the buildings: the renderer picks among the variants of some ground pictures, and its choice changes when the map's contents change. Those differences have no direction. (Drawn twice from the same files, it gives the same picture, pixel for pixel.) The script keeps the blocks of half a cell that got clearly brighter or darker, or mostly different, and that hang together with the places of the five buildings: the buildings and the light of their lamps. There the stock picture gets the shrunk drawing with the buildings, fading into the stock picture at the edge; every other pixel stays as it was. First it checks that the shrunk drawing of the stock map lies on the stock picture without a shift: the mean difference is 6.4 of 255, and one pixel off is worse. **[FILES]**
2. The stock picture has 256 colours, and none of them is the ground lit by the new lamps: a first try in those colours came out speckled white, orange and purple. The new picture is saved with full colour, a kind of file the client already shows for a stock map (`compactcombat.png`). **[FILES]**
3. The loading picture: the stock one with the 40 cells of the five lots painted that grey, two pixels for each cell (the rule found on the stock buildings). It is packed with the LZO1X packer that ships with the map renderer (`arbalest-tank\kit\lzo_pack.ps1` loads the renderer's library from the copy in the work folder), so its blocks have the stock layout: four blocks that unpack to 8192, 8192, 8192 and 7044 bytes. The kit's own unpacker and the renderer's both give the picture back byte for byte. **[FILES]** A first try packed each block as one long plain stretch: both unpackers read it, but no stock map of the game has such a block, so that was not used.
4. `make_pack.py` puts four files into the pack (`preview-lobby.png`, `preview-lobby-stock.png`, `previewpack.txt`, `previewpack-stock.txt`) and an entry `"preview"` into `pack.json`. It refuses pictures made from other sprite files or places, and pictures made with `--reuse` (which takes the drawings of an earlier run, for trying things out). After any change to a building, run `site_preview.py` again.

```powershell
python -I -B "new-buildings\site_preview.py" "$env:TEMP\mo-site-preview"
python -I -B "new-buildings\make_pack.py"
```

Run as printed on 25 Nov 2026: the first line took a few seconds and ended with `wrote SITE-preview and PREVIEW-CHECK.png (left stock, right with the buildings: lobby, lobby x4, loading x4)`; its pictures were the installed ones, pixel for pixel, and the pack that `make_pack.py` then wrote equals the installed pack in all 21 files. **[FILES]** The work folder must lie outside the game folder.

**What the installer does with them.** `packs.py install` puts the pack's skirmish picture in place of the stock one (it refuses if the file there is not the stock picture the pack names) and the pack's `[PreviewPack]` lines in place of the stock ones; `verify` checks both (`the lobby picture MapsMO/Standard/kalifornia.png is the pack's`, `the loading-screen picture in the map unpacks (170 x 62) and is the pack's`); `remove` puts both stock ones back, and refuses if the picture was changed by something else. On a copy, taking the pack out gave back the stock map and the stock picture, byte for byte, and the installer's test passes 84 of 84 checks. **[FILES]** Installed 25 Nov 2026, 15:04, with `checks: 137 passed, 0 FAILED`. **[FILES]** The owner played (6) Kalifornia Crisis at 17:04 that day: the scenario the client wrote for that game held the new loading picture, and the game loaded the map and ran to a normal end, with no `Failed to parse` line in its log. **[FILES]** What the two pictures looked like was not reported: questions 67 and 68. **[UNTESTED]**

The older packs in `new-buildings\round1` to `round5` have no pictures. With one of them installed, the skirmish screen and the loading screen show the stock city.

**The way back** to the five buildings with the stock pictures, with the game and the client closed:

```powershell
python -I "arbalest-tank\kit\packs.py" remove SITE
python -I "arbalest-tank\kit\packs.py" install "new-buildings\round5\SITE"
```

Rehearsed on a copy on 25 Nov 2026: the install ended with `checks: 135 passed, 0 FAILED`, the skirmish picture was the stock one again and the map held the stock `[PreviewPack]`; `"new-buildings\SITE"` in the second line brought both new pictures back with `checks: 137 passed, 0 FAILED`. **[FILES]** The picture inside the map is the one part that only the game can test; one game has loaded it without trouble (above). If a game on this map ever fails to start, these two lines are the first thing to try.

**What it looks like.** `new-buildings\PREVIEW-CHECK.png`: on the left the stock pictures, on the right the new ones; at the top the skirmish picture, in the middle its centre four times as large, at the bottom the loading picture four times as large. In the skirmish picture the five buildings and their coloured light stand at the middle crossing. In the loading picture each building is a few grey dots.

**Another map.** `site_preview.py` is written for the Black Site (it reads `blacksite.py`). `arbalest-tank\kit\previewkit.py` (read, write and swap the section), `lzo_pack.ps1`, the entry `"preview"` in `pack.json` and the installer work for any map pack.

---

## 17. A building that moves

### 17.1 What the game's own buildings do

Measured on the stock files on 24 Nov 2026. **[FILES]**

- The **main animation** of a building redraws whole moving structures: 2,000 to 12,000 pixels in every picture, 8 to 46 pictures, house colour included, drawn in the map's light like the building. (Tesla reactor 6,000 pixels, tech nuclear plant 10,800, the pump of the oil derrick 2,800.)
- Its file holds the pictures for the healthy building, then those for the damaged one. Where its section says `Shadow=yes`, one shadow per picture follows after all the pictures (the oil derrick's file: 32 + 32 + 64).
- **Lights** are separate small files (8 to 56 pixels, colours 240 to 253) with `UseNormalLight=yes`, so they stay bright on a dark map.
- Stock buildings that start without an owner keep whole parts only in the animation: the oil derrick's pump is not in its building picture, and the Tech Protector's building picture is empty.

The second version of our buildings only let 58 to 700 glowing pixels grow brighter and dimmer by about a sixth. In the game that read as "no animation" (10.8).

### 17.2 The method

`new-buildings\anim.py` makes the animations.

- For every picture the WHOLE building is rendered again with its moving parts in their new place. The picture keeps only the pixels that differ from the building picture. Drawn over the building, that is exactly the full render: a moving part hides what is behind it, and its shadow moves over roof and paving.
- A moving part carries its texture with it: its rivets and seams are taken in the part's own coordinates, so they do not swim while it turns.
- **Two layers for each building, as in stock:** a main animation `<ID>_A` (the moving structure, in the map's light, with pictures for the damaged building and, where wanted, shadows) and a light animation `<ID>_L` (lamps, glow, arcs, at full brightness, drawn in front).
- Two animation files cannot weave through each other. A part that passes both in front of and behind something glowing goes into the light file together with it: the Reactor's rings with its ball, the Stormspire's claws with its ball. Never rely on two files staying in step.
- A lamp that flashes is drawn switched OFF in the building picture. The light file adds it lit. A lamp drawn lit in the picture never seems to change.

### 17.3 What a build script provides

Every `build_*.py` describes one building for `anim.py`:

| Name in the script | What it is |
|---|---|
| `ID`, `FILE`, `NAME` | The building's ID (`CASPIR`), the name of its sprite files (`cgspir`) and its name in reports |
| `CANVAS`, `FOUND` | The size of the sprite canvas in pixels and the lot: `(174, 140)` and `'2x2'` for the Stormspire, `(480, 340)` and `'3x3'` for the three others |
| `GLOW` | How far the light of glowing parts reaches over the building, and how strong it is: `(6.0, 0.60)` for the Stormspire |
| `HOLES`, `DAMAGE_SEED` | Optional. How many holes the damaged picture gets, and a number that changes where they fall |
| `static(res)` | Everything that never moves. Flashing lamps are switched off here. |
| `rest(s, damaged)` | Optional. Moving parts in their first position that belong into the building picture itself (the Vault's door wheel). |
| `MAIN = dict(frames=40, rate=220, shadow=True)` or `None` | The main animation: how many pictures, how fast, with shadows or not. `flat=True`: only flat drawings such as steam, nothing is rendered for it (the Reactor). |
| `parts(s, k, n, damaged)` | Adds the moving parts in position `k` of `n`. |
| `main_overlay(img, k, n, ctx, damaged)` | Optional. Flat drawings on a main picture (steam). |
| `LIGHTS = dict(frames=16, rate=220)` | The light animation. |
| `light_parts(s, j, n)` | Optional. Moving parts that are drawn with the lights (rings, claws). |
| `lights(s, j, n)` | Switches lamps on and moves the glow for light picture `j` of `n`. |
| `lights_overlay(img, j, n, ctx)` | Optional. Flat drawings on a light picture (arcs, glints). |
| `keep(s)` | What the damaged picture must leave alone. |
| `occupied(s)` | Optional, for a building soldiers can garrison: paints the look while they are inside, which becomes the third picture (16.12). |
| `fire_point()` | Optional. The fire point of a building with a weapon (16.8). |

The last line of a build script starts the build and names three of the game's buildings to compare the look with: `A.main(sys.modules[__name__], donors=('ngradr', 'ggpowr', 'ggpile'))`. The shared steps (damaging a model, the comparison pictures) are in `new-buildings\common.py`.

```powershell
python -I -B "new-buildings\build_array.py" --quick
python -I -B "new-buildings\build_array.py"
```

- `--quick` draws every fourth picture, coarser, and writes only a moving preview (`quick.gif`) into the building's folder. Use it while shaping the movement.
- The full build writes the building picture (`cgskyw.shp`), the main animation (`cgskyw_a.shp`), the light animation (`cgskyw_l.shp`), a report and preview pictures. A 3x3 building takes about six seconds per picture; the Array's 80 main pictures take several minutes.
- The build stops if a picture is empty, if anything touches the edge of the canvas, or if a pixel of the building picture is missing in a picture.

### 17.4 The entries

The Skywatch Array's art block and its three animations, as the pack wrote them into `artmo.ini`. The three animation sections stand in the map file too (14.1).

```ini
[CASKYW]
Image=CGSKYW
Normalized=no
Remapable=yes
Foundation=3x3
Height=5
NewTheater=yes
CanHideThings=true
CanBeHidden=false
OccupyHeight=3
DamageFireOffset0=-2,34
DamageFireOffset1=29,10
ActiveAnim=CASKYW_A
ActiveAnimDamaged=CASKYW_AD
ActiveAnimZAdjust=-5
ActiveAnimYSort=562
ActiveAnimPowered=no
ActiveAnimTwo=CASKYW_L
ActiveAnimTwoDamaged=CASKYW_L
ActiveAnimTwoZAdjust=-25
ActiveAnimTwoYSort=562
ActiveAnimTwoPowered=no

[CASKYW_A]
Image=CGSKYW_A
NewTheater=yes
Normalized=no
Start=0
LoopStart=0
LoopEnd=40
LoopCount=-1
Rate=220
Layer=ground
Shadow=yes

[CASKYW_AD]
Image=CGSKYW_A
NewTheater=yes
Normalized=no
Start=40
LoopStart=40
LoopEnd=80
LoopCount=-1
Rate=220
Layer=ground
Shadow=yes

[CASKYW_L]
Image=CGSKYW_L
NewTheater=yes
Normalized=no
Start=0
LoopStart=0
LoopEnd=16
LoopCount=-1
Rate=220
Layer=ground
Shadow=no
UseNormalLight=yes
```

- `ActiveAnim=` is the main animation. `ActiveAnimDamaged=` is the same file from its damaged pictures on: `[CASKYW_AD]` has `Start=40`.
- `ActiveAnimTwo=` is the light animation. Its `ZAdjust` is 20 nearer than the main one's, so it is drawn in front.
- `ActiveAnimPowered=no`: the animation runs without power. A captured tech building has none of its own.
- The numbers for `ZAdjust` and `YSort` are those of the stock Tech Nuclear Plant for a 3x3 lot (-5 and 562). For the 2x2 Stormspire `YSort` is 362, as on the stock oil derrick.
- A file with `Shadow=yes` holds 40 + 40 pictures and then 80 shadows. `packs.py verify` checks that.
- A building with nothing but lights (the Stormspire) has only `ActiveAnim=<ID>_L`.
- `LoopEnd=` is the number after the last picture that plays (14.5): 40 pictures, `LoopEnd=40`. The damaged pictures are 40 to 79, with `LoopEnd=80`.
- A 2x2 building with a main animation has not been made here. Take its `ZAdjust` numbers from a stock 2x2 building that has one, such as `[CAPLANT]`. **[UNTESTED]**

### 17.5 Speed

- Every animation here has `Rate=220`: a picture stays for four game frames (900 divided by the rate; worked out from stock values, not measured).
- The client is set to its fastest game speed (`GameSpeed=0` in `spawn.ini`). If that runs at 60 game frames a second, the dish turns once in 2.7 seconds, the Reactor's rings in 2.4, and one charge of the Stormspire takes 0.8. At half that speed everything takes twice as long. **[UNTESTED]** as numbers; nothing was called too fast or too slow.
- The files `anim.gif` in the four building folders play at that speed.

### 17.6 Mistakes this work found

- **Shadow edges that shifted.** A part added to a model moved the grid of its shadow map by a fraction of a cell, and with it every shadow edge of the building. It showed as stray pixels all over the Black Vault's animation. The grid now starts on a whole number.
- **Blinking dots on still walls.** The faint shadows of the Reactor's rings changed single pixels by one palette step. Now a main picture keeps a changed patch of the still building only if it touches a moving part or has six pixels or more, and the Reactor's main animation holds the steam only.
- **A black underside.** The underside of the white dish is always in shade and came out as a black shape for half the turn. It is painted over-white with dark ribs.
- **A glint under a moving part.** A sparkle placed on the Vault's wheel was hidden by the turning wheel. Light pixels that a moving part ever covers are removed from the light file; the glint moved to the door's rim.
- **Speeds planned for the wrong game speed.** They were first worked out for 30 game frames a second; the client runs at its fastest setting.

### 17.7 What has been seen

- After the third version your report was "Perfect. Everything works just fine. I love how everything is." **[CONFIRMED]** 24 Nov 2026, as one answer for everything: no single animation was named.
- Your screenshot of that game (14:10) shows, on captured buildings: a flag on each of the Vault's two flagpoles (main animation), two glints on the Vault (light animation), the cage of claws round the Stormspire's ball (light animation), the bolt starting in the ball. **[CONFIRMED]** 24 Nov 2026. A still picture cannot show movement, but these parts exist only in the animation files, so the game draws both layers.
- Not reported: the parts before capture, the pictures for the damaged buildings, the shadows on the ground, and whether the brass rings and claws, which are drawn at full brightness, ever look too bright. **[UNTESTED]** (questions 27, 30, 31, 32)

---

## 18. A vehicle's model and icon, made by script

Sections 4 and 7 say what the game needs from model files. This section says how the models of the Arbalest, the Reaver, the Cerberus and the Moloch were made, so that the next one can be made the same way.

### 18.1 The tools

All in `arbalest-tank\kit`. Each file starts with a full description.

| File | What it does |
|---|---|
| `forge.py` | Shapes and materials: a hull, a turret and if wanted a separate barrel, built from boxes, cylinders, wedges and swept shapes |
| `forge_stock.py` | The painter and the detail parts of the game's dark heavy tanks: running gear, tiles, seams, panels, hazard marks, grilles, drums, rods, coil stacks, and the daylight icon |
| `forge_build.py` | `build_unit()`: writes every file of the unit |
| `vxlkit.py`, `pcxkit.py` | Model files and icon files. Each reads and writes the game's own files byte for byte |
| `voxrender.py` | Draws the previews: the game's view in eight directions, side and top views |
| `validate_model.py` | Checks a hull and turret pair against what the stock tanks do |

A build script is one Python file. `new-units\build_reaver.py` is the example to copy.

```powershell
python -I -B "new-units\build_reaver.py"
```

It writes into `new-units\REAV`: the four model files, the two icons, a contact sheet (`REAV_sheet.png`: eight directions at real size and enlarged), the validator's report, and `REAV_report.json` with the sizes and the fire point. It prints the validator's verdict, a line that starts with `PrimaryFireFLH 273,0,140`, and two lines of numbers about the paint.

### 18.2 The look of the game's tanks

Measured on the game's own model files on 23 Nov 2026 (the survey of all 480 is in `arbalest-tank\kit\research\forge-notes`). **[FILES]** The first versions of the three units ignored it and looked like toys beside the game's tanks.

The dark heavy tanks (Draco, Bison, Gharial):

- The armour is painted FLAT in four neutral greys (palette numbers 58, 56, 54, 60, with a little 62, 52, 50, 48). No speckle, and no lighter tops: the light edges seen in the game come from the game lighting the model.
- Glowing colours (240 to 255): none. Light greys (32 to 47): under 0.3 %.
- House colour: 3 to 6 % of a hull, 5 to 12 % of a turret, in small crisp patches. A hull also needs at least 1 % house colour among all its voxels, or the validator fails it.
- Accents are tiny: orange hazard marks, a little violet, a red lamp.
- Open running gear: a track band, round road wheels, a dark gap between them, a fender with a slot under its edge.
- Proportions: a hull 60 to 78 long, 40 to 50 wide, 17 to 23 high; 30 to 38 high with the turret.

The olive and the steel-blue tanks are painted differently: lighter with height and on faces that look up, over five to seven shades. The rebuilt Arbalest is the example (`arbalest-tank\option-4-rail-sniper-rebuilt\build_arbl.py`).

How a draft is judged: drawn between stock tanks at real size and enlarged, until it does not stand out (`new-units\make_preview.py` writes `new-units\PREVIEW.png`; helpers in `arbalest-tank\kit\compare`). The pictures are drawn by the kit's own renderer, not by the game. No screenshot of a new tank beside a stock one has been sent, so how close that renderer is to the game is not measured. **[UNTESTED]**

### 18.3 From a script to a unit in the game

1. Pick an ID that is free (section 4, step 1).
2. Copy `new-units\build_reaver.py` under a new name. Change the name at its end and the shapes. In the kit's models the front is +X, the unit's left is +Y, up is +Z. The fire point is worked out by the validator, from the barrel it finds among the turret's voxels: check the lines `barrel tip` and `suggested PrimaryFireFLH` in its report against the weapon's tip on the sheet. `t.muzzle` in the script is not read by the build (found by a cold read on 25 Nov 2026). If the tip it finds is wrong, give the value by hand in `make_bundles.py` (1.3, step 3).
3. Run the script. The validator must say PASS.
4. Look at the contact sheet and at the unit between stock tanks.
5. Add the unit to `new-units\make_bundles.py`: its rules are the proven `[ARBL]` block with your numbers, its weapon a copy of a stock weapon (13.2). Run it. It writes `rules.ini`, `art.ini` and `bundle.json` into the unit's folder. It writes the folders of all its units again, and it takes the `[ARBL]` block from the installed `Standard.ini`; for the three installed units that gives the same files as before (checked 24 Nov 2026).
6. Install the folder, with the game and the client closed (10.7):

```powershell
python "arbalest-tank\kit\unit_bundle.py" install "new-units\REAV"
```

7. The installer runs the check (`mo_tool.py check`) and puts everything back if it fails. (The Reaver is installed, so for its folder the line of step 6 answers `NOTHING DONE: Standard.ini already has these sections`. Use it with the folder of a new unit.)

**A tank with a hit effect of its own.**

- Put the sprite file into the unit's folder: a stock picture under a new name (14.3) or a painted one (14.4).
- In `make_bundles.py`, name the file in `extra_files=[...]` and the animation in `register={'Animations': ['MYHIT']}`, and put the animation's section into BOTH texts: the art text and the rules text. The rules text is what the game loads the animation from (14.1).
- The Reaver's entry in that script is not the model for this. It has the section in the art text only; its section for the rules came later, as the pack `REAVFIX`.
- The check tells you. Without the section in the rules, `mo_tool.py check` prints a line that starts with `WARN  animation` and ends the unit with `0 FAIL, 1 WARN`. With it, a copy of the Reaver's bundle installed on a rehearsal copy with `Result: 0 FAIL, 0 WARN` (24 Nov 2026). **[FILES]** Seen since: the Nexus's burst `NEXSSPL`, made the same way, is in the owner's screenshot. **[CONFIRMED]** 25 Nov 2026 (14.1)

**Rehearsing a vehicle.**

```powershell
python -I "arbalest-tank\kit\tests\make_sandbox.py" . "$env:TEMP\mo-sandbox-units" --units
python "arbalest-tank\kit\unit_bundle.py" --root "$env:TEMP\mo-sandbox-units" --sandbox status
python "arbalest-tank\kit\unit_bundle.py" --root "$env:TEMP\mo-sandbox-units" --sandbox remove REAV
python "arbalest-tank\kit\unit_bundle.py" --root "$env:TEMP\mo-sandbox-units" --sandbox install "new-units\REAV"
```

- With `--units` the copy also gets the helper tool, the records and the files of the installed vehicles, and the game's four archives as hard links: no copy is made, and nothing writes to them. The folder must not exist yet. Delete it afterwards; that removes the links, not the game's archives.
- `--sandbox` tells the installer that it works on a copy.
- The last two lines take the Reaver out of the copy and put it in again. The install ends with `Result: 0 FAIL, 0 WARN` and `installed REAV`. For a new unit, run only the install line, with its folder.

A new look for a unit that is already installed needs only steps 2 to 4 and the installer's `swap` (10.7). It changes the model files, the icons and the one `PrimaryFireFLH=` line.

### 18.4 The icon

- Two files, 60 x 48 pixels, 8-bit PCX: the icon and its veteran twin with a gold chevron (section 4, step 3).
- `build_unit()` makes both: the unit drawn in daylight, in the stock icon frame, with the name in the stock small letters on the dark band at the bottom.
- An icon carries no house colour: the game's own do not.
- For a light-coloured unit the picture washes out unless the icon is made a little darker (`gamma=0.98, gain=0.96` in the call of `cameo_day`).

### 18.5 What has been seen

- The Arbalest's first own model: five questions, "Yes to all this". **[CONFIRMED]** 22 Nov 2026 (section 11). So the kit's rules hold in the game: the front is +X, the turret sits on the hull, the shot leaves at the worked-out fire point, the icon shows.
- The rebuilt looks of all four: "everything was perfect". **[CONFIRMED]** 23 Nov 2026, as one answer for everything (10.7).

---

## 19. Mistakes made on the way

Each of these cost a round. The cure is in the section named.

| What was done | What happened | The rule now | Read |
|---|---|---|---|
| A new animation was listed under `[Animations]` and its settings put only into `artmo.ini` | It was most likely never drawn, and no log said so | An animation needs a section of its own in the file that lists it. The check warns about it since 24 Nov 2026 | 14.1 |
| A stock soldier's sprite in other colours was given out as a new unit | Sent back: "you didn't create the actual infantry" | A new unit is an original figure | 15 |
| Building pictures were judged by a sheet of numbers | They looked like clean grey models beside the game's | Judge on the map, beside the game's own buildings | 16.7 |
| Building animations only made glowing pixels brighter and dimmer | "It doesn't have animation" | Whole parts move; measure pixels per picture against stock | 17.1 |
| A building's fire point was counted from the middle of its lot | The bolt started 30 pixels above the tower | A building's fire point counts from the middle of the canvas | 16.8 |
| A tower on a plateau got the Tesla Coil's projectile | It shot two cells further than its ring showed | A defence with a ring gets a projectile without the high-ground bonus; run the range check | 13.5 |
| The idle moves and the cheer of a soldier were drawn one direction off | Found on the stock file before it reached a game | The letter in a sequence line is a map direction | 15.3 |
| A name was taken without checking the stock art | `CAHELI` was a stock helipad | Check every name against stock rules and stock art; the installers do | 0 |
| Speeds were worked out for 30 game frames a second | Everything would have run twice as fast as planned | Read the game speed the client is set to | 17.5 |
| A tool was changed after a version was installed | The scripts no longer gave that version's files | Keep the finished pack folder of every version | 10.8 |
| A part was added to a model | Every shadow edge shifted, stray pixels everywhere | Fixed in the tool; build twice and compare when in doubt | 17.6 |
| A key was taken for working because six stock weapons carry it (`IsBigLaser=`), and the Magnetron's beam was taken for a laser wave because its weapon has the line `Wave.IsBigLaser=yes` | The owner was told twice that the game has a thick laser in a colour of its own. Neither was true. Found in the game's program before anything was built on it | A key in the stock rules shows that the game accepts the name, not that anything uses it. For a new kind of effect, find the code that draws it, or a stock unit that visibly does it | 20.4 |
| A flyer's report file held the fire point that the tank validator works out | Found before use: the installer's `swap` would have moved the fire point off the turning axis | The flyers' build script writes the flyer's own fire point into the report | 20.6 |
| A model that was meant to be a tank of its own was put on a stock tank with a take-over block | It kept everything the block did not name: the Bulldog's name and icon, its four-shot magazine, its deploy into another tank, its elite cannon, its fire point, its one country. It stayed like that from April to November | A model that should be a unit goes in as a new unit (section 4 or a bundle). A take-over is for a quick look at a model | 5, 21 |
| A turret file was made with the hull's middle as its origin, although its ring lies behind the middle | The turret swung round in a circle when it turned (by the files) | The turret file's origin is its own ring; `TurretOffset=` puts it over the ring. Prove a change of this kind by drawing the unit with the turret straight, before and after: the pictures must be the same | 21.2 |
| A unit got an `Explosion=` line for its own end while it kept the stock death weapon | Found before a game: no stock ground tank has both, so what the two do together is not known | For anything a unit does, find the stock units that do it and count how they are set up, before adding a key | 21.2 |
| The Ballista's orb warhead was copied whole for the Nexus's orb, with its `CellSpread=4` | Found before a game, after a first install: with the stock rule `MinDamage=1` every unit within four cells of the burst, the Nexus and its friends among them, would have lost a point at every shot | A copied block brings every key with it. Read what each key does in its new place, and prefer the stock block made for the same purpose (the Godsbane's orb warhead has no radius) | 21.3 |
| A garrisonable building got the picture order of our tech buildings (healthy, damaged, damaged again) | Found before a game, in the review: the game shows the third picture while soldiers are inside, so the Vessel would have looked damaged whenever it was garrisoned | Look at all the pictures of a stock sprite of the same kind, not only the first | 16.12 |
| A tank's gun was copied from an artillery piece: the Seitaad Ballista's missile, which is made to go off in the air where its `ProjectileRange=` ends and to scatter pieces | Found by the owner in a game (25 Nov 2026): the shot burst in the air, 2.5 cells from the tank, whatever was aimed at, and "does not seem to hit the targets correctly and effectively" | Before copying a weapon, read what the stock unit that carries it is for. A shot that must hit what is aimed at is copied from a direct-fire weapon, and it does its damage itself | 13.8, 21.1 |
| A weapon that only a projectile named (`AirburstWeapon=`) got no line under `[WeaponTypes]` | Found after the owner's report, by comparing with stock: all 110 stock weapons that a projectile names are listed. The game reads the weapons before the projectiles, so such a weapon is created too late to be read in that pass | Register the piece weapon (`"WeaponTypes"` in `bundle.json` or in the pack's lists). The check warns now | 13.8 |
| A building was modelled from what was remembered of its shape, with no picture in front of it | The Vessel came out as a net of diamonds; the real one is a honeycomb of long landings. The owner asked whether it could not be closer to the photographs | For a real building, get photographs first, also one from above at the game's angle, and count what they show | 16.12 |
| A warhead was given `AffectsAllies=no` (the Tempest's), or kept it from the stock warhead it was copied from (the Nexus's two), so that stray pieces could not hurt the firer's own side | Found by the owner in a game (25 Nov 2026): forced (Ctrl) on the owner's own soldiers, tanks and flyers, the attack did no damage | Never give a warhead a line that spares a side, and take it out of a copied stock block. The check warns about it since 25 Nov 2026. Test a forced attack on your own units (23) | 13.10 |
| Buildings were added to a map, and the map's two preview pictures were left as they were | Found by the owner (25 Nov 2026): the skirmish screen and the loading screen showed the city without them | A map pack carries both pictures. `make_pack.py` refuses a pack without them since 25 Nov 2026 | 16.13 |
| The new units kept the ranks of their templates, and seven of the nine fire the same weapon as elite | Not a fault: the game's ranks work. The owner asked about ranks (25 Nov 2026) | Decide a new unit's ranks with the unit: what it gains, whether elite fires a better weapon, whether a rank changes its look | 22 |

---

## 20. Flyers: what the game does, and the three craft that were built

Researched and built on 24 Nov 2026. That evening the owner looked at three candidates in one picture and said "build all Seraph, Tempest and Nova". Since 24 Nov 2026, 21:25, all three are installed. The owner's screenshot of 25 Nov 2026 shows their three icons in the vehicle tab (20.8); nothing else about them has been reported. Since 25 Nov 2026, 12:57, the Tempest fires a swarm of missiles in place of its lightning (20.5). So whatever this section says about what they do in a game is **[UNTESTED]** unless it is marked otherwise; what it says about files and about the game's program is **[FILES]**.

Where the research is: `arbalest-tank\kit\research\aircraft`. `stock_aircraft.py` lists everything that flies in the stock rules (`stock_flyers_full.txt` is its full output for 23 of them). `flyer_models.py` and `flyer_placement.py` measure the stock model files (`flyer_models.txt`, `flyer_placement.txt`). `web_report.md` is what the public documentation says (ModEnc and the Ares documentation), with a source link for every point and a list of things that exist only in the Phobos extension, which this game does not have.

### 20.1 Two kinds of flyer

| | A hovering craft | A true aircraft |
|---|---|---|
| Stock examples | Warhawk, Thor Gunship, Kirov, Invader, Basilisk, Pteranodon: 44 in all | Harrier, Stormchild, Black Eagle, Barracuda, Dybbuk: 51 in all, cargo planes and carrier drones among them |
| What it is to the game | A vehicle. One line under `[VehicleTypes]`, the "jumpjet" way of moving | Its own list, `[AircraftTypes]` |
| How it attacks | Flies to its target and stays in the air beside or over it | Flies passes from an airfield and returns to reload (`Ammo=`, `AirportBound=yes`, `Dock=`) |
| How it gets in | The same list, installer and check as our four tanks (4, 10.7, 18). Our three craft went in this way | A list that was never tried through map code here |

**[FILES]** A jet, or a carrier with drones (`Spawns=`), needs `[AircraftTypes]` and is a later step. **[UNTESTED]** Two things the documentation says about that step: a true aircraft of our own must be a voxel model, and a bomb with `Vertical=yes` does not fall straight when a true aircraft drops it (the Kirov, a hovering vehicle, is not affected).

The keys that make a vehicle hover, as the stock Basilisk has them: `Locomotor={92612C46-F71F-11d1-AC9F-006008055BB5}`, `MovementZone=Fly`, `SpeedType=Hover`, `BalloonHover=yes` (it never lands), `HoverAttack=yes`, `Crashable=yes`, `ConsideredAircraft=yes`, `Category=AirPower`, `TooBigToFitUnderBridge=true`, and the flight numbers `JumpjetSpeed=`, `JumpjetClimb=`, `JumpjetCrash=`, `JumpJetAccel=`, `JumpjetTurnRate=`, `JumpjetHeight=` (475 to 900 in stock), `JumpjetWobbles=`, `JumpjetDeviation=`, `JumpjetNoWobbles=`. (`JumpJet=yes` stands in 12 of the 44, the helicopters; the Invader, the Ruiner and the Basilisk do without it.) Their armour is one of the flying armours (`f_light`, `f_medium`, `f_heavy`); the stock anti-air weapons have `Versus.f_...` lines for them, so keep one of these. **[FILES]** From the documentation: `JumpjetWobbles=0` crashes the game; to stop the wobble use `JumpjetNoWobbles=yes`. Copy a stock flyer's block whole and these pitfalls stay away.

The rules of a flyer must be copied from a stock flyer, not from `[ARBL]` as `new-units\make_bundles.py` does for tanks. Some stock blocks name their own ID in a line (`UnloadingClass=COMA`); change those. The Ruiner's block is not a good one to copy: it has `RequiredHouses=Neutral` and the prerequisite `AILOCK`. The Invader's (`[DISK]`) is.

Where a hovering craft is built: at a War Factory, like a tank. The stock Rejuvenator is a hovering craft with `Prerequisite=FACTORY,CASLAB` for all sides, so the general factory name works for a flyer. **[FILES]**

Who can shoot at a flyer: only a weapon whose projectile has `AA=yes` (documentation). The Seraph's projectile, the stock `InvisibleAll`, and the Tempest's missile have `AA=yes` and `AG=yes`: they may shoot at things in the air and on the ground. The Nova's bomb falls; it is for the ground. **[FILES]** for the keys.

### 20.2 What the stock flyer models are like

Measured on 27 of them. **[FILES]**

- **Size.** Bigger than tanks: a Harrier is 80 x 53 x 17 units, the Basilisk 90 x 74 x 22, the Thor 110 x 64 x 30, the Invader's saucer 66 across, the Gravitron 100 across, the Harbinger 137 x 150. The Bulldog's hull is 56 x 30.
- **Paint by faction.** The Allied craft (Warhawk, Thor, Harrier, Stormchild, Paradox Engine) are slate blue, palette numbers 89 to 95. The Soviet ones (Vulture, Wolfhound, Kirov) are olive, 71 to 77. The Epsilon ones (Invader, Basilisk, Ruiner, Gravitron) are brown-olive, 119 to 125, with greys. The Foehn ones (Quetzal, Harbinger, Alanqa) and the Black Eagle are the flat dark greys 58, 56, 54 and 60 of the dark heavy tanks (18.2). House colour is 5 to 15 % in crisp patches, and there are no glowing colours at all (0.0 % on 26 of 27).
- **Ours** are painted like the last group. Beside a Warhawk or a Ruiner they look darker. That is the difference between two of the game's own paint schemes, and it is the look the owner picked.
- **Place.** The underside of the model lies on its origin, as on a tank. The game lifts the whole model to its flight height.
- **Shadow.** The art key `ShadowIndex=` names the section that throws the shadow; a number without a section crashes the game (documentation). Ours have one section and no such key.

### 20.3 A part that moves

Two ways are in the stock files. **[FILES]**

- **A turret that never stops turning.** `Turret=yes` and `TurretSpins=yes` in the rules, speed with `TurretROT=`: the Invader, the Ruiner, the Gravitron and the Irkalla. The spinning part is the turret file. Its weapons have `OmniFire=yes`, or the craft could only fire when the turret happens to point at the target; and their fire point is on the turning axis (`PrimaryFireFLH=0,0,-45` on the Invader), because a fire point off the axis would go round with the turret. This is the way our three craft use: the kit writes a hull and a turret file already.
- **Several pictures of the model in one HVA file.** Rotors: the Warhawk's model has three sections and two HVA frames, the Perun's four and four. Their art has `ShadowIndex=0`, `UseBuffer=yes` and `DisableShadowCache=yes`. The documentation says such frames play while a hovering craft is in the air, one frame for every game frame. Not tried here, and the kit's build step writes single-section files. **[UNTESTED]**

### 20.4 What an attack can look like

Every key in this table is used by the stock rules. **[FILES]** What each looks like in a game with our values is **[UNTESTED]**, except where a row says otherwise.

| Effect | Keys | Stock example |
|---|---|---|
| Laser line | `IsLaser=yes`, `LaserInnerColor=`, `LaserOuterColor=`, `LaserOuterSpread=`, `LaserDuration=`. A thin line | Invader, Warhawk. A laser of our own: **[CONFIRMED]** 2 April 2026 (the Nexus) |
| Thick laser in the owner's colour | `IsLaser=yes`, `IsHouseColor=yes`, `LaserThickness=4`. All seven stock weapons with `LaserThickness=` also have `IsHouseColor=yes`; the documentation says it works only with it and "has low quality" | Raccoon; `Megalaser` |
| Laser with a trail of small pictures | `IsLaser=yes` together with `IsDetachedRailgun=true` (or `IsRailgun=true`) and `AttachedParticleSystem=`. The named system puts a small animation every few steps along the beam | `AntaresBeam`, `InfernoRailgun`, `MarauderRailgun`, `RailguneerBlast`; the Ruiner's magenta ray with violet rings (`RuinerRay` with `RuinerSys`). This is how the game makes its big beams |
| Wide beam in any colour | `Wave.IsBigLaser=yes` (or `Wave.IsLaser=yes`), and `Wave.Color=` if wanted: the extension's "laser wave". The weapon must not have `IsLaser` (below) | No stock weapon draws one (below). The Seraph is the first |
| Lightning | `IsElectricBolt=true`, `Bolt.Color1=` to `Bolt.Color3=`, several at once with `Burst=` (all of them go to the same target) | Perun Flagship. Bolts of our own: **[CONFIRMED]** 23 Nov 2026 for the Reaver (as one answer for everything) and 24 Nov 2026 for the Stormspire (your screenshots) |
| Wavy beam | `IsRadBeam=yes`, `Beam.Color=`, `Beam.Duration=`, `Beam.Amplitude=` | 16 stock weapons |
| The Magnetron's wave | `IsMagBeam=yes`, `Wave.Color=` | 8 stock weapons |
| Rockets | A projectile with `ROT=` and a voxel picture; in its art `UseLineTrail=yes`, `LineTrailColor=`, `Trailer=` (a smoke animation). Several at once with `Burst=`; how they leave: 13.9 | Warhawk, Wolfhound; 49 stock projectiles have a voxel picture and a trail. Ours: the Tempest's swarm of eight since 25 Nov 2026 (20.5) |
| Shot that splits | A projectile with `Splits=yes`, `Cluster=` and `AirburstWeapon=`; with `Ranged=yes` it splits after the weapon's `ProjectileRange=`; `RetargetAccuracy=` and `AroundTarget=` choose the pieces' targets | Seitaad Ballista (twelve pieces), Godsbane, Foxtrot, Uragan, Harbinger. Ours: the Nexus's second version of 25 Nov 2026, which burst far from its target (21.1); nothing of ours uses it now. How it works: 13.8 |
| Bombs | A projectile with `Vertical=yes` and `DetonationAltitude=`; weapon `Range=1` with `CellRangefinding=yes`. The falling picture is a voxel on the Kirov's bomb | Kirov. (`Dropping=yes` does not drop anything in this engine, the documentation says.) |
| Pulse round the craft | `AreaFire=yes`, a warhead with a wide `CellSpread=`, a ring animation in `AnimList=`, `Ripple.Radius=` | Gravitron, Thor |
| Flash at the muzzle | `Anim=` with one name, or with eight names, one for each direction | Pteranodon |
| Glow that stays on the craft | In the unit's rules `AttachEffect.Animation=` and `AttachEffect.Duration=` | Ruiner (15), Perun (60) |
| Line behind the craft | In the unit's art `UseLineTrail=yes`, `LineTrailColor=`, `LineTrailColorDecrement=` | Paradox Engine |

**Only one kind of beam per weapon.** Read in the game's program on 24 Nov 2026 (`gamemd.exe`, 0x6FF4CC to 0x6FF5F5, and the extension's hook `TechnoClass_Fire_OtherWaves`). When a weapon fires, the game goes down one list and draws the first kind the weapon has: a laser (`IsLaser`), lightning (`IsElectricBolt`), a wavy beam (`IsRadBeam`), an eruption (`IsRadEruption`), and last a wave (`IsMagBeam`, or the extension's `Wave.IsLaser` and `Wave.IsBigLaser`). So a weapon with `IsLaser=yes` and `Wave.IsBigLaser=yes` shows only the thin laser. The sonic wave (`IsSonic`) stands outside this list: its test comes before it, so it goes together with any of them. **[FILES]** A particle trail (`AttachedParticleSystem=`) is expected to go with any of them too, because stock weapons such as `RuinerRay` and `AntaresBeam` have a laser and a trail in one block; the code for the trail was not read. **[UNTESTED]**

**The old key `IsBigLaser=` does nothing.** The game reads it and stores it. Nothing reads the stored value again, except one routine that walks through all of a weapon's stored values, most likely for its checksum (searched in `gamemd.exe` and in `Ares.dll`). Six stock weapons carry the key, the Scavenger's `RuptureBeam` among them; they are ordinary thin lasers. **[FILES]** The first version of this section said, because of that key, that the game had thick lasers in a colour of their own. That was wrong (19).

**The laser wave.** The extension has the wide beam under another name: `Wave.IsLaser=yes` and `Wave.IsBigLaser=yes`. Its code makes such a wave only for a weapon that does NOT have `IsMagBeam=yes`. The one stock weapon with `Wave.IsBigLaser=yes`, the Magnetron's `MagneticBeam`, has `IsMagBeam=yes` as well and therefore gets the Magnetron's own wave. So no weapon of the game draws a laser wave, and the Seraph's is the first. **[FILES]** What the code says about it: a wave starts with a strength of 160, loses 6 in every game frame and is removed below 32, so it shows for 22 game frames; a new shot makes a new wave and does not wait for the old one; for a weapon with `AmbientDamage=` the extension goes through the cells along the beam in every frame (its routine is named `WaveClass_DamageCell`). **[FILES]** Expected, not read: the damage at the target comes from the weapon's projectile and warhead, as with any weapon. The documentation gives violet (64,0,96) as the colour when `Wave.Color=` is not set. How wide and how bright the beam is on the screen is not known. **[UNTESTED]**

**A projectile of our own needs no list line.** When a weapon names a projectile that does not exist yet, the game makes it (read at 0x46C790 in `gamemd.exe`). The words `[Projectiles]` and `[WeaponTypes]` are not in the game's program at all; the extension has them. What it does with `[WeaponTypes]` was read on 25 Nov 2026: it creates the listed weapons before the game reads the weapon blocks, and a weapon that only a projectile names needs that (13.8). What it does with `[Projectiles]` was not read. Our vehicle weapons and warheads have no list lines and work (13.2). **[FILES]**

Also checked in the programs: `Ares.dll` reads `Beam.Color`, `Beam.Amplitude`, `Wave.Color`, `LaserThickness`, `Bolt.Color1` and `AttachEffect.Animation`; `gamemd.exe` reads `TurretSpins`, `IsRadBeam`, `IsMagBeam`, `BalloonHover`, `HoverAttack` and `JumpjetNoWobbles`. One stock line has `Strafing.Shots=`, but neither program has that word, so it does nothing here. **[FILES]**

A muzzle flash, a hit effect or a glow of our own is an animation and needs the three things of 14.1.

### 20.5 The three craft

Installed on 24 Nov 2026 at 21:25 with the vehicle installer, from `new-aircraft\SRPH`, `new-aircraft\TMPS` and `new-aircraft\NOVA`; the Tempest once more on 25 Nov 2026 at 12:57, with another weapon (below). `new-aircraft\PREVIEW.png` shows them beside the game's Ruiner, Invader and Warhawk and a tank; each folder has a moving picture `attack.gif`. The pictures are drawn by the kit, not by the game: the flash, the hit effects, the smoke and the lights are the installed pictures, placed where the game should play them; the beam and the falling orb are sketches, and so is the ring the Tempest's missiles leave in. (The picture the owner picked from is kept as `new-aircraft\candidates\PREVIEW.png`.)

| ID | Name | Shape and size | The part that spins | Weapon | Copied from | What was changed |
|---|---|---|---|---|---|---|
| `SRPH` | Seraph, halo gunship | A dart with swept wings and a forked nose, 114 x 90 x 22 | A halo on three spokes, on a mast | `SeraphLance`: the wide violet laser wave, a flash under the craft, a plasma splash | Weapon keys of the Invader's `DiskLaser`; warhead `InfernoRailgunWH` | The five laser lines taken out and `Wave.IsBigLaser=yes` put in; Damage 90, ROF 75, Range 7, sound `RuinerAttack`, `Bright=yes`; flash `SRPHMUZ`, hit effect `SRPHHIT`; soldiers die electrocuted; the flash of light without green |
| `TMPS` | Tempest, storm wing | A crescent wing whose tips reach forward and end in coils, 107 x 152 x 25 | A lift fan in its back | `TempestSwarm` (since 25 Nov 2026): eight small homing missiles in one salvo. Until then `TempestArc`, three blue-white bolts | The Old Longbow's `LongbowStrike`; the Quickshifter's `PhalanxProjectile` and `PhalanxWH`; the art of the stock missile `SMISL` | Below |
| `NOVA` | Nova, ring bomber | A thick ring with a bridge and two engines, 121 x 106 x 24 | A crystal core in the middle of the ring | `NovaBomb`: a glowing orb dropped straight down, a wide violet blast | The Kirov's `BlimpBomb`, `BlimpBombP` and `BlimpHE` | Damage 260, ROF 60, blast radius 2.4 cells, the flash of light without green; the projectile `NovaOrbP` has the picture `NOVAORB`, a voxel orb of our own with a violet line trail; hit effect `NOVABLS` |

| | Cost | Strength | Armour | Speed | Flight height | Sounds and voices of |
|---|---|---|---|---|---|---|
| Seraph | 1300 | 430 | `f_light` | 30 | 550 | the Invader |
| Tempest | 1500 | 540 | `f_medium` | 24 | 650 | the Ruiner |
| Nova | 2000 | 900 | `f_medium` | 14 | 800 | the Gravitron |

All three are built at a War Factory by every side, as our tanks are (`Owner=`, `Prerequisite=FACTORY` and `TechLevel=2` are taken from `[ARBL]`). **[FILES]**

**The unit block** is the stock Invader's `[DISK]` block, whole, with these changes: the name; `Primary=` and `ElitePrimary=` are our weapon; `Owner=`, `Prerequisite=` and `TechLevel=` as above; cost, strength, speed, height and turning speeds; the sounds; `Secondary=DiskDrain`, `Drain.Local=` and `VoiceSecondaryWeaponAttack=` (the Invader's drain beam) are taken out; three lines are added for the light on the craft, the keys of the stock Ruiner: `AttachEffect.Duration=15`, `AttachEffect.Animation=` and `AttachEffect.PenetratesIronCurtain=yes`. **The art block** is the Invader's with our two icons, `PrimaryFireFLH=0,0,-10` (on the turning axis, just under the belly) and `Remapable=yes`. **[FILES]**

The Seraph's weapon, exactly as it is in `Standard.ini`:

```ini
[SeraphLance]
Damage=90
ROF=75
Range=7
Projectile=InvisibleAll
Speed=100
Report=RuinerAttack
Warhead=SeraphLanceWH
Bright=yes
Anim=SRPHMUZ
OmniFire=yes
Wave.IsBigLaser=yes
```

It has none of `IsLaser`, `IsElectricBolt`, `IsRadBeam`, `IsRadEruption` and `IsMagBeam`, each of which would be drawn in place of the wave (20.4), and no `Burst=`. `new-aircraft\make_bundles.py` stops if one of them gets in.

**The Tempest's swarm (since 25 Nov 2026, 12:57).** The owner wrote on 25 Nov 2026: "i need you now to create a new attack for the tempest. electric shocks or lighning is not the best. i need something suitable for a plane. something entirely new and really nice. lookup scifi attack planes and build and install its attacking method onto tempest". Looked up: what the attack craft of science fiction fire comes down to four things, swarms of small missiles with curving smoke trails (the "missile circus" of Japanese animation, first drawn in 1980 and famous since 1982), rocket pods, rotary cannon, and plasma bolts or bombs. What was found, with the links, is in `arbalest-tank\kit\research\aircraft\scifi_attack_craft.md`. The swarm was taken: nothing in this install fires missiles yet, and the game has every part for it. The lightning version was never reported on; it is kept in `new-aircraft\round1\TMPS` and installs as it is (20.7).

What it does: eight small missiles leave from under the fan, one every 3 to 5 frames. Each starts in the direction the turning fan points at that moment, flies straight for eight frames while it gathers speed, then turns onto the target and hits it. So they leave in a spread round the craft and close in on the target from several sides (13.9 has the reading; how wide the spread is depends on how fast the fan turns, which was not pinned down). Each missile does its own damage where it hits. **[FILES]** Not seen in a game. **[UNTESTED]**

The weapon and the missile's flight, exactly as they are in `Standard.ini`:

```ini
[TempestSwarm]
Damage=17
ROF=65
Range=7.5
Burst=8
Projectile=TempestSwarmP
Speed=50
Warhead=TempestSwarmWH
Report=LongbowMissileAttack
Anim=TMPSMUZ
OmniFire=yes

[TempestSwarmP]
Arm=1
High=yes
Shadow=no
AA=yes
AG=yes
Image=TMPSMSL
CourseLockDuration=8
ROT=20
SubjectToCliffs=no
SubjectToElevation=no
SubjectToWalls=no
Acceleration=10
```

The missile's picture, exactly as it is in `artmo.ini`:

```ini
[TMPSMSL]
Voxel=yes
Rotates=yes
UseLineTrail=yes
LineTrailColor=255,214,150
LineTrailColorDecrement=20
Trailer=TMPSSMK
TrailerSeperation=32
SpawnDelay=1
```

Every block is a stock block with a few changed lines. `make_bundles.py` prints the changes and writes them to `new-aircraft\TMPS\departures.txt`:

| Our block | Is the stock block | Changed |
|---|---|---|
| `[TempestSwarm]`, the weapon | `LongbowStrike`, the missile salvo of the stock flyer Old Longbow | damage 50 to 17, `ROF` 60 to 65, range 7 to 7.5, two missiles to eight, speed 80 to 50; our projectile, warhead and launch flash. The sound `LongbowMissileAttack` and `OmniFire=yes` stay |
| `[TempestSwarmP]`, the flight | `PhalanxProjectile`, the missile of the stock Quickshifter (three in a salvo) | our picture; `Scalable=yes` taken out (twelve of the thirteen stock projectiles with that line carry a sprite; ours is a model). `CourseLockDuration=8`, `ROT=20` and `Acceleration=10` are the stock values |
| `[TempestSwarmWH]`, the hit | `PhalanxWH` | our explosion `TMPSHIT`; the `Verses=` line of the lightning's warhead, so that each kind of target takes what it took before. A line `AffectsAllies=no` was added at first and taken out again on 25 Nov 2026, 14:41 (13.10) |
| `[TMPSMSL]`, the picture (art) | `SMISL`, a stock missile model | the colour of the line trail; our smoke `TMPSSMK` as the trail; `SpawnDelay=1` added, a puff every frame (the stock flare `FLAREE` has it) |

- **About as strong as the lightning was.** Eight times 17 is 136; the three bolts did 135. A salvo with its seven gaps and `ROF=65` takes about as long as the three bolts with `ROF=85` did. `make_bundles.py` stops if the swarm is weaker or slower than that. Three things differ, all from the copied stock warhead and from what a missile is: a soldier lying down takes half (`ProneDamage=50%`; the lightning's warhead had no such line); the blast is a little wider (`CellSpread=.5` for `.3`); and the lightning struck at once, while a missile needs about a second to arrive, so a target can be gone or dead by then.
- **It hits.** The projectile has no key of a scattering, splitting or proximity shot, and the script stops if one gets in. Its warhead has a small blast (`CellSpread=.5`). It hurts whatever it hits, your own units too when you force it on them (Ctrl); from 12:57 to 14:41 on 25 Nov 2026 it spared your own side and so did nothing to them (13.10).
- **The unit has no `BurstDelay` line.** With one, the missiles would leave together and all one way (13.9); the script stops if one gets in.
- **The missile** is a model of 60 voxels, 11 long: white with a dark band, a yellow band and a red nose, four fins, and a flame at the tail in colours the game does not darken. `new-aircraft\build_flyers.py` writes `tmpsmsl.vxl` and `tmpsmsl.hva`. No projectile picture of ours has been seen in a game yet (the Nova's orb and the Nexus's orb were never reported); how the game loads one was read (13.9). If the model does not show, the trails still do.
- **The sounds** are stock: `LongbowMissileAttack` at each launch, `Explosion15` at each hit (the sound of the Quickshifter's own hit effect). Both are in the sound file. **[FILES]**
- **What was left alone:** the craft, its numbers, its icon, and the small arcs over its fan (`TMPSGLO`), which are from its lightning days (question 64).

**The nine animations.** All painted new (14.4) with `new-aircraft\build_effects.py`; each has its sprite file, its line under `[Animations]` (9013 to 9015, 9018, 9019 and, since 25 Nov 2026, 14:41, 9034 to 9037) and its section in both INI files.

| Name | What it is | Pictures | Its keys are those of |
|---|---|---|---|
| `SRPHMUZ` | The flash under the Seraph when the beam starts | 9 | stock `DISKMUZ` without its sound, with `Rate=450` |
| `SRPHHIT` | The plasma splash where the beam lands | 15 | stock `TNKIMPCT`, with `Translucent=no` and `Rate=450` |
| `TMPSMUZ` | The puff of flame and smoke under the Tempest's fan at each launch | 6 | stock `DISKMUZ` without its sound, with `Rate=450` |
| `TMPSSMK` | One puff of a missile's trail: a spark, then pale vapour that swells and tears | 8 | stock `FSMOKE`, the smoke of the stock missiles, as it is |
| `TMPSHIT` | Where a missile lands: a white-hot flash, a small fireball, sparks, a ring on the ground, smoke. (Until 25 Nov 2026: sparks, crawling arcs and a shock ring, in blue-white) | 14 | the Quickshifter's hit `XGRYMED1` without its crater, with `Normalized=no` and `Rate=450` |
| `NOVABLS` | The orb going off: a flash, two rings, a wide violet fireball, smoke | 22 | our `DOOMBLST` (from stock `MINIMISS`): a sound, a crater and a burn mark |
| `SRPHGLO`, `TMPSGLO`, `NOVAGLO` | The light on the turning part: a violet light on the halo's hub, small arcs over the fan, the pulse of the core | 8 each, played round and round | stock `RUINIDLE` without its own palette, with `Rate=450`; `Translucency=25` |

A light is 8 pictures of two game frames each, and the craft renews it every 15 game frames, the way the Ruiner renews its 16-frame light every 15.

### 20.6 How they were made: the steps for the next flyer

Three scripts in `new-aircraft`, run in this order from the project folder. Each starts with a description of itself.

```powershell
python -I -B "new-aircraft\build_flyers.py"
python -I -B "new-aircraft\build_effects.py"
python -I -B "new-aircraft\make_bundles.py"
```

1. **`build_flyers.py`** holds the three shapes and writes a folder for each craft: the four model files, the two icons, a contact sheet and a report. For the Nova it also writes the orb (`novaorb.vxl`, `novaorb.hva`), for the Tempest its missile (`tmpsmsl.vxl`, `tmpsmsl.hva`). It prints one line per craft that ends with `the turning part clears the hull at all 96 angles`, and stops if it does not. Things a flyer needs that a tank does not:
   - Everything that turns is built on the turning axis, x = 0 and y = 0 of the hull: the mast, the fan's well, the core. The turret turns about the hull's origin.
   - `seat` is given by hand: the height at which the underside of the turning part sits (23, 19 and 0).
   - The icon shows the craft in the sky (`cameo_sky` in that script), with no shadow on a ground.
   - The validator's verdict does not count (it says FAIL: it compares with a tank). The script writes the flyer's own fire point into the report, because the installer's `swap` reads it there.
2. **`build_effects.py`** paints the nine animations into the same folders, with one overview picture each (`sheet_srphhit.png` and so on). The middle of a canvas is the point the game puts the animation at. For a light on the craft that point is the craft's origin, the middle of its underside, so the light is painted ABOVE the middle: one voxel of height is 0.866 pixels on the screen.
3. **`make_bundles.py`** writes `rules.ini`, `art.ini` and `bundle.json` into each folder, a fourth folder `SRPH-laser` (20.7), and for the Tempest `departures.txt`. It prints one line per folder. Every block is a copy of a stock block with the changes of 20.5, made with the same small function as for the tanks (13.2), and the script stops if a copied block no longer has a key it wants to change.

These three lines were run as printed on 24 Nov 2026 and gave the same files again, byte for byte: 51 files compared, 27 of them in the game folder. Run as printed again on 25 Nov 2026 with the Tempest's swarm, together with the line of step 7: the 81 files of the four folders came out the same, byte for byte, and the 31 files of the three bundles are the ones in the game folder. **[FILES]**

4. **Rehearse on a copy** (18.3), with the new craft's folder in the last line:

```powershell
python -I "arbalest-tank\kit\tests\make_sandbox.py" . "$env:TEMP\mo-sandbox-flyers" --units
python "arbalest-tank\kit\unit_bundle.py" --root "$env:TEMP\mo-sandbox-flyers" --sandbox status
python "arbalest-tank\kit\unit_bundle.py" --root "$env:TEMP\mo-sandbox-flyers" --sandbox install "new-aircraft\SRPH"
```

   The copy holds what is installed, so for a craft that is in already the last line answers `NOTHING DONE`. Before the real install the three craft were put into such a copy first as bare bundles (the candidate models and stand-in sprites: `make_bundles.py --bare <folder>`), then finished; every install ended with `Result: 0 FAIL, 0 WARN`. Delete the copy afterwards.

5. **Install**, with the game and the client closed, one craft at a time:

```powershell
python "arbalest-tank\kit\unit_bundle.py" install "new-aircraft\SRPH"
python "arbalest-tank\kit\unit_bundle.py" status
```

   On 24 Nov 2026 each install ended with `Result: 0 FAIL, 0 WARN` and `installed SRPH` (then `TMPS`, then `NOVA`). Today the first line answers `NOTHING DONE: Standard.ini already has these sections: seraphlance, seraphlancewh, srph, srphglo, srphhit, srphmuz`. The second printed then, among other lines, `[VehicleTypes] in Standard.ini: 7411=ARBL, 7412=REAV, 7413=CERB, 7414=MLCH, 7415=SRPH, 7416=TMPS, 7417=NOVA`; since 25 Nov 2026, 14:41, the list ends `7415=SRPH, 7417=NOVA, 7420=NEXS, 7421=TMPS`, because the Nexus and the Tempest were taken out and put in again that day.

6. **Check** each craft with `python "MentalOmega-Modding-Guide\scripts\mo_tool.py" check SRPH`. All eight vehicles end with `Result: 0 FAIL, 0 WARN`. Since 24 Nov 2026 the check accepts a flyer that is wider than long (the Tempest; the stock Harbinger is too); for a tank that still gives a WARN.

7. **The picture**: `python -I -B "new-aircraft\make_preview.py"` writes `new-aircraft\PREVIEW.png`, the three `attack.gif` and `new-aircraft\TMPS\TMPS_attack.png`. It flies the Tempest's missiles by the rules of 13.9, with a guessed turning speed of the fan.

For a fourth craft: add a shape to `build_flyers.py` and its name to `MAKERS` there, its animations to `SETS` in `build_effects.py`, and a `unit(...)` block to `make_bundles.py`. Check its ID and every new name against the stock rules and art first (0). The three scripts write over their folders, so copy the folder of an installed craft before you change it (0).

### 20.7 The Seraph's other beam, and taking a craft out

The Seraph's wide beam is the one thing here that no stock weapon does. If it does not show, or looks wrong, the same craft is ready with a beam made of stock parts only: the Ruiner's laser in violet with its trail of violet rings (`new-aircraft\SRPH-laser`; the weapon is a copy of `RuinerRay` with real damage). With the game and the client closed:

```powershell
python "arbalest-tank\kit\unit_bundle.py" remove SRPH
python "arbalest-tank\kit\unit_bundle.py" install "new-aircraft\SRPH-laser"
```

To return to the wide beam, run the same two lines with `"new-aircraft\SRPH"`.

**Back to the Tempest's lightning** (the version of 24 Nov 2026), with the game and the client closed:

```powershell
python "arbalest-tank\kit\unit_bundle.py" remove TMPS
python "arbalest-tank\kit\unit_bundle.py" install "new-aircraft\round1\TMPS"
```

Rehearsed on a copy on 25 Nov 2026, there and back: both installs ended with `Result: 0 FAIL, 0 WARN`. **[FILES]** The swarm went in the same way on 25 Nov 2026 at 12:57, with `"new-aircraft\TMPS"` in the second line; the installer answered `number 7419 under [VehicleTypes]` and the animation numbers 9025 to 9028, and all eight vehicles, the three packs and the range check passed afterwards. **[FILES]** Saved games from before may not load.

**Back to the swarm as it was from 12:57 to 14:41 on 25 Nov 2026** (its warhead spares your own side, 13.10), with the game and the client closed:

```powershell
python "arbalest-tank\kit\unit_bundle.py" remove TMPS
python "arbalest-tank\kit\unit_bundle.py" install "new-aircraft\round2\TMPS"
```

Rehearsed on a copy on 25 Nov 2026, there and back: the install ended with `Result: 0 FAIL, 1 WARN`, the warning being the check's one about that line, and `"new-aircraft\TMPS"` in the second line brought the present swarm back with `Result: 0 FAIL, 0 WARN`. **[FILES]**

To take a craft out altogether:

```powershell
python "arbalest-tank\kit\unit_bundle.py" remove SRPH
python "arbalest-tank\kit\unit_bundle.py" remove TMPS
python "arbalest-tank\kit\unit_bundle.py" remove NOVA
```

All of this was run on a rehearsal copy on 24 Nov 2026, not on the game folder: the switch to the other beam and back ended with `Result: 0 FAIL, 0 WARN`, and after the three removals both INI files were the same as before the flyers went in, byte for byte, with none of their files left. **[FILES]** The files from before each install are in `backups\unit-bundles\SRPH`, `TMPS` and `NOVA`.

A new look for an installed craft goes in with the installer's `swap` (10.7). On a copy, `swap SRPH "new-aircraft\SRPH"` left the fire point at `0,0,-10`. **[FILES]**

### 20.8 What is proven and what is not

| Piece | State |
|---|---|
| A new vehicle through `[VehicleTypes]`, its model, turret seat, icon | **[CONFIRMED]** for tanks (22 and 23 Nov 2026) |
| The files of the three craft: rules, art, models, icons, sprites, list lines | In place; the check passes for each. **[FILES]** |
| That the game starts and runs with them, and that they are in the vehicle tab | The games of 24 Nov 2026, 21:48, and of 25 Nov 2026, 10:40, 12:29, 14:21 and 17:04, started and ran to a normal end with them installed; their logs have no `Failed to parse` line. **[FILES]** The owner's screenshot of 25 Nov 2026 shows the icons SERAPH, TEMPEST and NOVA with their names in the vehicle tab. **[CONFIRMED]** 25 Nov 2026 (screenshot). Whether one was built is not known |
| The hover keys on a unit of our own; built at a War Factory | **[UNTESTED]**; 44 stock units hover, the stock Rejuvenator is built that way |
| A forced attack (Ctrl) on your own units | From 12:57 to 14:41 on 25 Nov 2026 the Tempest's warhead spared your own side; the owner's report of a flyer of ours that did no damage to the owner's own soldiers, tanks and aircraft fits it. **[CONFIRMED]** 25 Nov 2026 as a fault. The line is out since 14:41. **[FILES]** The Seraph's and the Nova's warheads never had such a line. **[FILES]** Not tried since. **[UNTESTED]** |
| A turning turret on a model of our own, and where it sits | **[UNTESTED]**; 4 stock units have one |
| A fire point under the craft | **[UNTESTED]**; the Invader has one |
| The Seraph's wide beam | **[UNTESTED]**, and the least certain piece: the extension's code for it was read, but no stock weapon uses it |
| The Tempest's missile swarm (since 25 Nov 2026) | Stock blocks with a few changed lines; how the missiles leave was read in the program (13.9). **[FILES]** Not seen. **[UNTESTED]** Its lightning (until then) was never reported on |
| A projectile picture of our own: the Nova's orb, the Tempest's missile and its smoke trail | How the game loads them was read (13.9); the models load without trouble, since the games of 24 and 25 Nov ran with the Nova's orb installed. **[FILES]** None has been seen in flight. **[UNTESTED]** |
| The Nova's bomb with a projectile and a voxel picture of our own | **[UNTESTED]**; the Kirov's bomb is built the same way |
| The nine new animations | The three things of 14.1 are there. Building animations made this way are drawn (17.7); a painted hit effect of a unit was never named in a report. **[UNTESTED]** |
| A light that stays on a craft of our own | **[UNTESTED]**; the Ruiner and the Perun have one |
| The shadow | The hull throws it. Whether the turning part throws one is not known: the stock craft whose whole body is the turret carry a flat plate as hull. **[UNTESTED]** |
| The reach | No ring on a flyer. `InvisibleAll` has no high-ground bonus (13.5) |
| Balance: cost, strength, damage | Set by eye beside the stock craft. **[UNTESTED]** |

What to look at in the first game is in section 12, questions 36 to 42.

### 20.9 What the tools needed for a flyer

- The rules come from a stock flyer: `new-aircraft\make_bundles.py` does that. `new-units\make_bundles.py` builds from `[ARBL]` and is for tanks.
- `validate_model.py` holds every model against the Bulldog; its verdict does not count for a flyer.
- `forge_build.py` takes a given seat height as it is since 24 Nov 2026 (a ring ship has no hull under its turret axis to measure).
- `mo_tool.py check` accepts a flyer that is wider than long since 24 Nov 2026; the tool from before is kept in `backups\2026-11-24-mo_tool-before-flyer-width-note`.
- The vehicle installer needed no change for the flyers. It added lines under `[VehicleTypes]` and `[Animations]` only, and that is enough for them: a weapon that a unit names, a warhead and a projectile of our own need no list line (20.4). Since 25 Nov 2026 it can also add a line under `[WeaponTypes]`, for a weapon that only a projectile names (13.8); the flyers have no such weapon.

---

## 21. The Nexus tank as a unit of its own

The Nexus was the first model in this install. From 2 April to 24 Nov 2026 it sat on the United States' Bulldog (section 5). On 24 Nov 2026 the owner wrote that it works but "has a lot of errors", that the tank itself and its look should stay, and asked for the mistakes to be fixed, for new animations for it and for its attack, for it to behave "same as the others", and for an icon of its own. That evening it became a unit of its own, `NEXS`, with a red laser (21.2), and the take-over block went out of `Standard.ini`: the Bulldog is the game's own again. Before that version had been in a game, the owner asked for more: "a special animation on the turret, a glowing animation", some colour ("I honestly don't like that it's fully black"), and "a different type of projectile or attack", "something new". Since 25 Nov 2026, 00:05, the unit has a new paint, a turret that glows as its weapon charges, and a new weapon, the starburst (21.3). The owner played that second version on 25 Nov 2026 (the game of 10:40) and reported, with a screenshot: "The Nexus system does not seem to hit the targets correctly and effectively. So you can take a look at this picture and it shows where I'm aiming at and where it's actually shooting." The screenshot shows the tank as a unit of its own, its icon, its paint and its lit coil (21.6), and the fault: the shot bursts in the air, far from what is aimed at (21.1). Since 25 Nov 2026, 11:34, the third version is installed: the starburst is a direct shot now, an orb that flies to the target and does the damage itself (21.3). The third version was installed during three of the owner's games on 25 Nov 2026 (12:29, 14:21, 17:04); nothing about it was reported. What this section says about files is **[FILES]**; what it says about the game is **[UNTESTED]** unless it carries a **[CONFIRMED]** with its date.

Everything is in `nexus-tank`: the four original model files (`original`), the scripts, the paint rules (`paint.py`), the finished bundle (`NEXS`), the other paint (`paint-B`), the version of 24 Nov 2026 (`round1`), the second version of 25 Nov 2026 (`round2`), the owner's screenshot of that day (`evidence-2026-11-25`) and `PREVIEW.png`.

### 21.1 What was wrong, and why

A take-over changes only the lines it names; every other line stays the stock unit's (section 5). Nearly all the faults come from that. They are worked out from the files; none was reported from a game one by one.

| Fault | Cause | Cure |
|---|---|---|
| It had the Bulldog's name and icon | The block named neither, and there was no art section for the model | A unit of its own has both |
| Only the United States could build it | The Bulldog's `RequiredHouses=UnitedStates` stayed | The owner list of our tanks: every side |
| Four shots, then a long pause | The Bulldog's `Ammo=4` and `EmptyReload=100` stayed | No such lines |
| The deploy key turned it into another tank | The Bulldog's `Convert.Deploy=ETNK2`, the stock "Bulldog (Painter)", stayed | No such line |
| Once elite it fired the stock cannon | The Bulldog's `ElitePrimary=105mmE` stayed | `ElitePrimary=` is its own weapon |
| The shot left under and in front of the barrel | With no art section of its own it kept the Bulldog's `PrimaryFireFLH=240,0,120` | `PrimaryFireFLH=271,0,158`, the tip of its own barrel |
| The turret walked round in a circle when it turned | The turret's ring lies 8.6 units behind the middle of the hull, and the game turned the turret about the hull's middle | The turret file's origin is its own ring now, and `TurretOffset=-52` puts it back over the ring |
| No firing sound | `Report=PrismShotSound`: the game's sound file has no such name (6.6) | A sound that is in the file |
| It cost 1 and did 500 damage a shot | Values of the first test | Real numbers (21.2) |
| Four lines that do nothing or name countries the game does not have | Section 5 | The block is made from `[ARBL]`, which has none of them |

On 24 Nov 2026 two things about the model were left as they were, on purpose. The first was changed on 25 Nov 2026 at the owner's request (21.3):

- **House colour.** The model carried house colour only in its darkest shade (palette 31, about 2 % of its voxels, scattered), which shows as black. So the tank showed almost nothing of its owner's colour. Brightening those voxels was tried and gave scattered specks, not a clean band.
- **Light.** Almost every voxel has the same normal value, so the game lights the whole tank evenly and the shading is what is painted on it. That is the look the owner knows and likes; real normals would change it. It is unchanged.

The two test take-overs from December 2025, `[APOC]` and `[HTNK]`, are still in `Standard.ini` and were not touched (section 11).

**The fault of the second version's weapon (25 Nov 2026).** This one was reported from a game. The owner aimed at a tall building beside the tank. The picture (`nexus-tank\evidence-2026-11-25\screenshot_2026-11-25_104313.png`; the detail, eight times enlarged, in `screenshot_burst_x8.png`) shows the blue ring of the burst in the air in front of the building, about 146 pixels above the middle of the tank, and no piece and no hit anywhere. **[CONFIRMED]** 25 Nov 2026 (the owner's screenshot) for what the picture shows. The causes are worked out from the files and from the two programs (13.8). **[FILES]**

| Fault | Cause | Cure |
|---|---|---|
| The shot bursts in the air near the tank, whatever is aimed at | The weapon was a copy of the stock Seitaad Ballista's second weapon. That is an artillery piece made to scatter: its missile is `Ranged=yes`, climbs (`Lobber=yes`) and goes off where the weapon's `ProjectileRange=` ends, 2.5 cells from the muzzle in our copy (3 in the stock block). If it climbs at about 45 degrees, 2.5 cells of flight put the burst about 100 pixels above the muzzle on the screen; the muzzle is about 45 pixels above the middle of the tank, and the picture shows the burst 146 above it | A shot that flies to its target: the projectile of a stock direct-fire weapon, and no `ProjectileRange=` line |
| The orb itself does nothing | The Ballista's missile only carries the pieces: `Damage=1` and a warhead of 3 % | The orb does the weapon's damage itself |
| What the pieces do is uncertain by design | Every piece starts at the place of the burst, heading straight down, and steers from there; one in four takes another target within five cells of the first, or a random cell (13.8) | No splitting. The rays start where the orb hits (`ShrapnelWeapon=`, 13.8) |
| The piece weapon had no line under `[WeaponTypes]` | `NexusShard` was named only by the orb's projectile. The game reads the weapons before the projectiles, so such a weapon is created too late to be read in that pass; all 110 stock weapons that a projectile names are listed, ours was not (13.8). Whether it was read in the game of 25 Nov is not settled. For it: the game did not stop at the burst, and the extension's splitting routine reads the piece's projectile without a test (0x1001A0E1 to 0x1001A0FE of `Ares.dll`). Against it: the order of reading, and that the picture shows no piece | The ray weapon is registered: `9423=NexusShard` |

The rule behind the first three: a copied weapon behaves like the unit it was made for (19).

### 21.2 What was done on 24 Nov 2026

**The shape stays the owner's, voxel for voxel.** On 24 Nov 2026 `NEXS.vxl`, `NEXS.hva` and `NEXSTUR.hva` were byte copies of `FTNKNEXUS.vxl`, `FTNKNEXUS.hva` and `FTNKNEXUSTUR.hva`, and `NEXSTUR.vxl` differed from `FTNKNEXUSTUR.vxl` in two numbers only: the turret's bounds along its length are moved by 8.618 units, so that the file's origin lies on the turret's own ring (it was 8.65 units away, it is 0.33 now). The art line `TurretOffset=-52` moves the turret back by the same distance. With the turret pointing straight ahead the tank was drawn the same as before, pixel for pixel, in all eight directions (checked with the kit's renderer); with the turret turned it now stays on its ring. **[FILES]** The move in the file and the offset in the art use the same conversion from leptons to model units, so this check does not test that conversion: in the game the turret may sit a fraction of a pixel off. `TurretOffset=` is new here; 58 stock tanks have one. **[UNTESTED]** Since 25 Nov 2026 the colours differ (21.3); the voxels, their normals and the two bound numbers are as they were.

**Where the first number of the fire point counts from.** Measured on stock tanks that have a `TurretOffset`: the first number of `PrimaryFireFLH` divided by the distance of the barrel's tip from the TURRET FILE's own origin gives the same value as on tanks without an offset (Draco 6.26, Charon 6.15, Wormqueen 6.32, Catastrophe 6.15, Kappa 6.37; the Bulldog, without an offset, 6.17). Counted from the middle of the unit the values scatter from 6.9 to 8.7. So the fire point counts from the turret's own pivot. **[FILES]** For the Nexus that gives `271,0,158`.

**The unit** is our proven `[ARBL]` block with these changes: the name "Nexus Tank"; its own weapon in `Primary=` and `ElitePrimary=`; armour `heavy`; the voices and the engine sound of the stock Future Tank (`FTankSelect`, `FTankMove`, `FTankAttackCommand`, `FutureTankMoveStart`); a death weapon of its own, `DeathWeapon=NexusDeath`, for its own end (below); and the numbers below. Since 25 Nov 2026 it has five lines more (21.3).

| | On the Bulldog | Since 24 Nov 2026 |
|---|---|---|
| Cost | 1 | 1700 |
| Strength | 800 | 800 |
| Speed | 8 | 6 |
| Damage | 500 a shot | 180 a shot (24 Nov); six pieces of 40 (25 Nov, 00:05 to 11:34); 200 a shot since then, and five rays of 25 (21.3) |
| Wait between shots (`ROF`) | 60 | 80 (24 Nov); 90 since 25 Nov |
| Range | 7 | 7.5 (24 Nov); 8 since 25 Nov |
| Who builds it | United States | every side, at a War Factory |

The old numbers made it cost nothing and kill most things with one shot. The new ones are set by eye beside the Future Tank (two shots of 100 every 90) and our Moloch.

**The weapon of 24 Nov 2026** was the stock Future Tank's red laser, `FTankLaser`, as `[NexusLaser]`: one shot instead of two, the red of the old Nexus laser, damage 180, our flash, and `Report=FutureTankAttack` (in the stock block that sound sits in the muzzle animation `LASMUZF`, so it had to be named on the weapon when the animation was replaced). Its warhead was the Future Tank's `FutureAP` with our hit effect. It was replaced before it was in a game; the bundle is kept in `nexus-tank\round1\NEXS`.

**Its end.** The game's ground tanks explode in one of two ways, and never in both: 128 have a line `Explosion=`, and 99, the Bulldog and our `[ARBL]` among them, have `DeathWeapon=UnitDeathWeapon`, whose warhead `UnitDeathWH` names the usual explosions in `AnimList=`. A few stock tanks with an end of their own have a death weapon of their own (Iron Dragon, Mantis, Roadrunner). The Nexus is made that way: `[NexusDeath]` and `[NexusDeathWH]` are copies of those two stock blocks with `AnimList=NEXSEXP`, so its own explosion plays in place of the usual one. A weapon named in `DeathWeapon=` is made by the game the way one named in `Primary=` is (read in `gamemd.exe` at 0x7122F1), so it needs no list line; the check goes through it like the main weapon. **[FILES]** (The first install, at 22:07, had an `Explosion=NEXSEXP` line on top of the stock death weapon. No stock ground tank has both, so the unit was put in once more at 22:17, made the stock way.)

**Three animations** were painted for it on 24 Nov 2026 (14.4): a red flash, a red hit effect and its explosion with a red ring. Since 25 Nov 2026 they are blue-white: six from 00:05, five since 11:34 (21.3).

**The take-over is retired.** `nexus-tank\retire_takeover.py` cut the four comment lines and the sections `[ETNK]`, `[TankieGun]` and `[TankieWH]` out of `Standard.ini` (827 bytes, 41 lines) and kept the file from before and the block in `backups\2026-11-24_220747-nexus-takeover-retired`. The model files `FTNKNEXUS*.vxl` and `.hva` are still in the game folder; nothing reads them now, and the first-test recipe of section 4 still copies them. The version of 24 Nov went in that way: first `unit_bundle.py install`, then `python -I "nexus-tank\retire_takeover.py" retire`. The script refuses to retire the take-over while `NEXS` is not installed, so the tank is never gone from the game.

### 21.3 What was done on 25 Nov 2026: paint, a glowing turret, the starburst

**The paint.** Only colour numbers change. The voxels and their normals stay the owner's, and `build_nexus.py` stops if one of them would change. The rules are in `nexus-tank\paint.py`:

- More than half of the hull was palette 61 to 63, which is black. Above the tracks and wheels every dark grey is now four steps lighter, the middle greys less, the light greys not at all: a dark gunmetal, like the game's own dark tanks (18.2). The tracks and wheels stay black.
- The team colour sits on whole plates: the decks of the four track pods round their silver grilles, and two raised plates on the turret's roof. That is 12.4 % of the voxels, in middle shades. The scattered voxels of shade 31 are lifted to shade 25, so they no longer show as black.
- The coil on the barrel (five silver rings with green wraps) and the two lit vents at the rear are light now. They use the unit palette's colours 240, 246, 248 and 250 to 253. In the game's light table for voxels (`voxels.vpl`, 32 pages of 256 colour numbers) each of these maps onto itself on every page, so the game draws them at full brightness whatever light falls on the tank. `build_nexus.py` stops if one of them does not. The six unit palettes that the game carries in its archives, one for each kind of landscape, have the same colours at these numbers. **[FILES]** In the owner's screenshot of 25 Nov 2026 the coil's rings are pale blue-white on tanks at rest. **[CONFIRMED]** 25 Nov 2026 (screenshot). Whether they stay as bright in every light was not looked at.
- A second paint is built beside it, `nexus-tank\paint-B`: the decks steel blue, the team colour only on the four grilles. It goes in with `swap` (21.5).

The owner's screenshot of 25 Nov 2026 shows several Nexus tanks in this paint: gunmetal, the decks of the track pods in the owner's teal. **[CONFIRMED]** 25 Nov 2026 (screenshot), as a reading of the picture; the owner did not comment on the paint this time.

**The turret that glows as it charges.** Three stock tanks have a turret that changes while their weapon reloads: the Tesla Cruiser (five turret files), the Prism Tank (four) and the Plague Splatter. Read in `gamemd.exe` on 25 Nov 2026; the listings are in `arbalest-tank\kit\research\probe` (`dis_6FA4FB_charge_stage.txt`, `dis_717880.txt`, `dis_71402A_isgattling.txt`, `dis_712892_turretcount.txt`, `dis_6FF29E_reload_time.txt`, `dis_5F7A90_turret_files.txt`, `dis_70DC70.txt`):

- A unit with `IsChargeTurret=true`, a `TurretCount=` above 0 and no `IsGattling=yes` gets a turret stage every frame: the time left until its weapon may fire again, times `TurretCount`, divided by the time the weapon's reload takes, and at most `TurretCount` minus 1 (0x6FA505 to 0x6FA5B8; the test for a count above 0 is the routine at 0x717880, and `IsGattling` is the flag read at 0x71401E). So the highest stage shows right after a shot, the stages count down while the weapon reloads, and stage 0 shows when it is ready and stays until the next shot.
- The game draws the turret file of that stage. Stage 0 is `NEXSTUR.vxl`, stage 1 `NEXSTUR1.vxl`, and so on: the file names are made from `%sTUR` and `%sTUR%d` and loaded at 0x5F7A90 into a table with 18 places. **[FILES]**

The Nexus has eight stages. The eight files are the same turret, voxel for voxel, and differ only in the colours of the coil:

| Stage | What the coil shows |
|---|---|
| 7 | Just fired: the five rings glow orange-hot |
| 6 | Cooling: dark red |
| 5 | The ring nearest the turret lights up blue-white |
| 4, 3, 2 | Two, three, four rings |
| 1 | All five, the wraps blue |
| 0 | Ready: all five, and the mouth of the barrel glows |

With the reload time of 90 the coil runs through them in 90 game frames, about one and a half seconds at the client's fastest speed (17.5), and stays lit until the next shot. **[UNTESTED]** It is a light that follows the weapon, not an animation that runs all the time: a tank that does not shoot shows stage 0 all the time. A light that runs all the time would have to be attached to the unit (`AttachEffect.Animation=`, 20.4); it would sit at the middle of the tank, 52 leptons in front of the turret's ring, and would not turn with the turret. Not done.

The rules got five lines, written the way the stock Tesla Cruiser `[TTNK]` has them (`Primary=` stays as well). Exactly as they are in `Standard.ini`, at the end of the `[NEXS]` block:

```ini
TurretCount=8
WeaponCount=1
Weapon1=NexusStarburst
EliteWeapon1=NexusStarburst
IsChargeTurret=true
```

The art got `Weapon1FLH=` beside `PrimaryFireFLH=`, as all three stock charge-turret tanks have it. The art section, exactly as it is in `artmo.ini`:

```ini
[NEXS]
Voxel=yes
Remapable=yes
TurretOffset=-52
Weapon1FLH=271,0,158
PrimaryFireFLH=271,0,158
CameoPCX=nexsicon.pcx
AltCameoPCX=nexsuico.pcx
```

`mo_tool.py check` looks at all eight turret files since 25 Nov 2026: for a unit with `IsChargeTurret=true` it checks `<ID>TUR1` to the last stage like the first, and it warns when `WeaponCount=`, `Weapon1=` or `Weapon1FLH=` is missing (3.2).

**The starburst, direct since 25 Nov 2026, 11:34.** One orb of light leaves the barrel, flies straight to what is aimed at, follows it if it moves, and does the weapon's damage where it hits. If it hits a vehicle or a soldier, five rays of light leap from there to other enemies within five cells; when there are fewer than five, the rest go to the ground within two cells. Against a building, or on bare ground, there is the orb and its burst and no rays: that is the game's own rule for pieces thrown from a hit, and the stock Prism Tank's beam follows it too (13.8). **[FILES]** Not seen in a game. **[UNTESTED]** The second version's shot, which burst in the air, is described in 21.1; its bundle is kept in `nexus-tank\round2\NEXS`.

Every block is a stock block with a few changed lines. `make_bundle.py` prints the changes and writes them to `nexus-tank\NEXS\departures.txt`:

| Our block | Is the stock block | Changed |
|---|---|---|
| `[NexusStarburst]`, the weapon | `PiranhaMissile`, a plain shot that homes on its target | damage 70 to 200, `ROF` 75 to 90, range 6.5 to 8, speed 80 to 60; our projectile, warhead and flash; the sound `SeitaadAttack`; `MinimumRange=0.5` taken out |
| `[NexusStarburstP]`, the orb's flight | `SalamanderProj`, the bolt of the stock Salamander: `ROT=100`, no `Inaccurate` | our picture; two lines added, `ShrapnelWeapon=NexusShard` and `ShrapnelCount=5` (the Prism Tank's `LargeCometP` has 5 as well) |
| `[NexusStarburstWH]`, the orb's hit | `SeitaadMissileFragWH`, the warhead of the Ballista's fragments | our burst `NEXSSPL`; `Verses=50%,50%,25%,120%,110%,100%,50%,45%,40%,50%,0%` |
| `[NexusShard]`, a ray | `CometFragment`, the Prism Tank's fragment | our warhead; the beam's two colours. Its damage of 25 and its `Range=5` are the stock values |
| the ray's projectile | the stock `SmallCometP` itself: invisible, there at once | nothing; no block of ours |
| `[NexusShardWH]`, where a ray lands | `SeitaadMissileFragWH` | our hit effect `NEXSHIT`; `Verses=40%,35%,25%,120%,110%,100%,50%,45%,40%,50%,0%` |

The weapon and the orb's flight, exactly as they are in `Standard.ini`:

```ini
[NexusStarburst]
Damage=200
ROF=90
Range=8
Projectile=NexusStarburstP
Speed=60
Warhead=NexusStarburstWH
Report=SeitaadAttack
Anim=NEXSMUZ

[NexusStarburstP]
Arm=2
Shadow=no
Proximity=no
Ranged=yes
AA=no
AG=yes
Image=NEXSORB
ROT=100
SubjectToCliffs=no
SubjectToElevation=no
SubjectToWalls=no
Acceleration=40
ShrapnelWeapon=NexusShard
ShrapnelCount=5
```

The ray, exactly as it is in `Standard.ini`:

```ini
[NexusShard]
Damage=25
ROF=110
Range=5
Projectile=SmallCometP
Speed=100
Warhead=NexusShardWH
Bright=no
LaserOuterSpread=155,255,255
LaserInnerSpread=155,255,255
LaserOuterColor=70,130,255
LaserInnerColor=215,235,255
LaserDuration=25
IsLaser=true
IsHouseColor=false
```

Why it is made this way:

- **The templates are direct-fire weapons.** `PiranhaMissile` is the one weapon of the stock Piranha Minisub: a plain shot that homes on one target and does its damage where it hits. `SalamanderProj` is the bolt that the stock Salamander, a hovering gunship, fires at targets on the ground (`AA=no`, `AG=yes`); the missile of the stock Stryker IFV, `AAHeatSeekerB`, has the same twelve keys with a slower turn. The orb's block carries no key of a splitting or scattering shot (`make_bundle.py` stops if one gets in), and the weapon has no `ProjectileRange=`.
- **Both warheads hurt whatever they hit.** `SeitaadMissileFragWH` has `CellSpread=.5` and `AffectsAllies=no`. The second line was kept at first, so that a ray landing on a random cell beside the tank could not cost the Nexus or its own side anything (with the stock rule `MinDamage=1` a blast radius costs everything in it at least one point, 19). It also made a forced attack on your own units do nothing, which the owner found on 25 Nov 2026. Since 14:41 that day the line is out of both (13.10).
- **The ray weapon is listed:** `9423=NexusShard` under `[WeaponTypes]` (13.8). The bundle registers it.
- **The orb alone is at least the laser of 24 Nov,** armour kind by armour kind, rays not counted: `make_bundle.py` stops otherwise.
- **The sounds** are the Ballista's: `SeitaadAttack` when it fires, `SeitaadExp` where the orb hits. Both are in the sound file. **[FILES]** Where a ray lands there is no sound: five come at once.

What one shot does (13.4): 200 before armour; against a medium tank 220, a heavy tank 200, a soldier in flak armour 100, a concrete building 80. The laser of 24 Nov 2026 did 162, 144, 90 and 18, every 80 frames; the second version's six pieces, if all six had hit, 264, 240, 84 and 96. Each ray does 25 before armour to what it strikes: 27 to a medium tank, 25 to a heavy one, 8 to a soldier in flak armour. **[FILES]** for the arithmetic; **[UNTESTED]** in the game.

Three things to know about the rays (the reading is in 13.8): they go for whatever stands in the cells round the hit and is not on the firer's side or allied to it, a neutral building included; none come from a hit on a building or on bare ground; and the game draws them only while the firing tank is alive.

**Five animations**, painted new (14.4) with `nexus-tank\build_effects.py`, all in the blue-white of the coil. Each has its sprite file, its line under `[Animations]` (9020 to 9024 until 25 Nov 2026, 14:41; since then 9029 to 9033) and its section in both INI files. The five files are the same, byte for byte, as in the second version; that one had a sixth, a piece in flight (`NEXSSHD`), which nothing uses now.

| Name | What it is | Pictures | Its keys are those of |
|---|---|---|---|
| `NEXSMUZ` | The flash at the barrel's tip | 7 | stock `LASMUZF` without its sound |
| `NEXSORB` | The orb in flight, with a short tail | 10, round and round | the stock flying picture `STAKFIRE` (animation palette, a line trail) |
| `NEXSSPL` | Where the orb hits: a flash, two rings, six jets | 11 | our hit effect of 24 Nov, with the sound `SeitaadExp` |
| `NEXSHIT` | Where a ray lands: a small burst, a ring, sparks, a burn mark | 11 | our hit effect of 24 Nov, without a sound |
| `NEXSEXP` | The tank's own end: a flash, a fireball with a blue-white ring, smoke | 18 | our blasts (from stock `MINIMISS`), without a sound of its own |

`NEXSSPL` was seen in the game of 25 Nov 2026, when it was still played in the air: the owner's screenshot shows it in its blue. **[CONFIRMED]** 25 Nov 2026 (screenshot). The others: **[UNTESTED]**

The orb is the flying picture of a projectile. It is listed under `[Animations]` and has a section in `Standard.ini` too, the way the stock flying picture `STAKFIRE` is listed in the stock rules (the Doomsayer's `DOOMFLR` has an art section only, 14.1). Which of the two the game needs was not tested. **[UNTESTED]** The orb's section, exactly as it is in `artmo.ini`:

```ini
[NEXSORB]
AnimPalette=yes
Start=0
End=9
LoopCount=1
Rate=300
AnimLow=0
AnimHigh=9
AnimRate=1
Shadow=no
UseLineTrail=yes
LineTrailColor=150,190,255
LineTrailColorDecrement=24
```

**The icon** shows the tank in its new paint, in blue team colour, in the stock icon frame (18.4).

**Numbers.** Cost 1700, strength 800, speed 6, armour `heavy`, as on 24 Nov 2026. The weapon's numbers are in `nexus-tank\make_bundle.py`; to change them, change them there, run it, and put the bundle in again (21.5).

### 21.4 The steps

From the project folder. Each script starts with a description of itself.

```powershell
python -I -B "nexus-tank\build_nexus.py"
python -I -B "nexus-tank\build_nexus.py" B
python -I -B "nexus-tank\build_effects.py"
python -I -B "nexus-tank\make_bundle.py"
python -I -B "nexus-tank\make_preview.py"
```

- The first writes the hull, the eight turret stages, the two icons, a contact sheet and a report into `nexus-tank\NEXS`. It stops if a file in `original` is not the one it was written for, if a voxel or a normal would change, or if a light colour is not one in the game's table.
- The second writes the other paint into `nexus-tank\paint-B`.
- The third paints the five animations; it stops if a picture is empty or touches the edge of its canvas.
- The fourth writes `rules.ini`, `art.ini`, `bundle.json` and `departures.txt` (every changed line of every copied stock block). It stops if a line of the Bulldog or of the old take-over gets into the unit, if a charge-turret line or an art key is not one that the Tesla Cruiser has, if a key of a splitting or scattering shot gets into the orb's block, if a warhead could hurt friends or has a wide blast, if the orb alone is weaker than the laser of 24 Nov, or if the art names another number of pictures than a sprite file holds.
- The fifth draws `nexus-tank\PREVIEW.png` and `nexus-tank\NEXS\attack.gif`. The rays and the orb's tail in those pictures are a sketch of what the game draws.

Run as printed on 25 Nov 2026 for the third version, the five lines gave the same files again, byte for byte: the 38 files of `nexus-tank\NEXS` (the 25 that are in the game folder, `rules.ini`, `art.ini`, `bundle.json`, `departures.txt`, the report, the sheets and the moving picture) and the 23 files of `paint-B`. **[FILES]**

Rehearsed first on a copy (18.3):

```powershell
python -I "arbalest-tank\kit\tests\make_sandbox.py" . "$env:TEMP\mo-sandbox-nexus3" --units
python "arbalest-tank\kit\unit_bundle.py" --root "$env:TEMP\mo-sandbox-nexus3" --sandbox remove NEXS
python "arbalest-tank\kit\unit_bundle.py" --root "$env:TEMP\mo-sandbox-nexus3" --sandbox install "nexus-tank\NEXS"
```

Run as printed on 25 Nov 2026 with the third version installed. The copy holds the game files as they are, so the second line took the unit out (`removed NEXS`) and the third put it in again; it ended with `Result: 0 FAIL, 0 WARN` and `installed NEXS`, and the copy's `Standard.ini` was the installed one again except for the time in the marker line. **[FILES]** The folder named in the first line must not exist yet.

Then for real, with the game and the client closed:

```powershell
python "arbalest-tank\kit\unit_bundle.py" remove NEXS
python "arbalest-tank\kit\unit_bundle.py" install "nexus-tank\NEXS"
```

On 25 Nov 2026 at 00:05 (the second version) and at 11:34 (the third) the second ended with `Result: 0 FAIL, 0 WARN` and `installed NEXS`, and all eight vehicles, the three packs and the range check passed afterwards. At 11:34 the installer also wrote `NexusShard under [WeaponTypes] as number 9423`. **[FILES]** (A first install of the second version at 23:58 on 24 Nov had the Ballista's own orb warhead with `CellSpread=4`. It was replaced seven minutes later the same way, before any game.)

### 21.5 The way back, and changing it

With the game and the client closed. Five ways, each rehearsed on a copy of the game files on 25 Nov 2026: the first with the third version installed as it is since 14:41, the four others with it as it was at 11:34.

**Back to the third version as it was from 11:34 to 14:41** (its warheads spare your own side, 13.10):

```powershell
python "arbalest-tank\kit\unit_bundle.py" remove NEXS
python "arbalest-tank\kit\unit_bundle.py" install "nexus-tank\round3\NEXS"
```

On the copy the install ended with `Result: 0 FAIL, 2 WARN`: the two warnings are the check's ones about that line. `"nexus-tank\NEXS"` in the second line brought the present version back with `Result: 0 FAIL, 0 WARN`. **[FILES]**

**Back to the second version** (the same paint and turret; the shot that bursts in the air, 21.1):

```powershell
python "arbalest-tank\kit\unit_bundle.py" remove NEXS
python "arbalest-tank\kit\unit_bundle.py" install "nexus-tank\round2\NEXS"
```

On the copy the install ended with `Result: 0 FAIL, 1 WARN`. The warning is the new one about its piece weapon, which has no line under `[WeaponTypes]`. **[FILES]**

**Back to the version of 24 Nov 2026** (black, the red laser, one turret file):

```powershell
python "arbalest-tank\kit\unit_bundle.py" remove NEXS
python "arbalest-tank\kit\unit_bundle.py" install "nexus-tank\round1\NEXS"
```

On the copy the install ended with `Result: 0 FAIL, 0 WARN`. **[FILES]** (When this was first rehearsed, on 25 Nov 2026 before the Vessel went in, it gave both INI files as they were before 25 Nov, except the time in the marker line above the block.)

**The other paint** (steel blue decks):

```powershell
python "arbalest-tank\kit\unit_bundle.py" swap NEXS "nexus-tank\paint-B"
```

`swap` replaces the hull, the eight turret files and the two icons, keeps the animations, and prints the line that goes back (`swap NEXS` with the folder in `backups` that it kept). On the copy, going back gave paint A's files byte for byte. **[FILES]** `swap` sets `PrimaryFireFLH=` only. The Nexus's art also has `Weapon1FLH=`, which a charge turret's weapon uses. Both paints have the same fire point, so that does not matter here; a look with another fire point needs `remove` and `install`.

**Back to the take-over of April** (the Nexus on the Bulldog):

```powershell
python -I "nexus-tank\retire_takeover.py" restore
python "arbalest-tank\kit\unit_bundle.py" remove NEXS
```

- The first line alone puts the Nexus back on the Bulldog, as it was from April; the new unit stays too.
- Both lines, in this order, give the state from before 24 Nov 2026, 22:07: on the copy `Standard.ini` came out the same as then, byte for byte (the kept file is `backups\2026-11-24_221725-removed-NEXS\record\before-install\Standard.ini`). `artmo.ini` loses the Nexus's block and is otherwise today's, with the Vessel's art, which came later. **[FILES]**
- The script looks for the kept block in the `backups` folder of the project folder it works on. On a rehearsal copy, copy `backups\2026-11-24_220747-nexus-takeover-retired` into the copy's `backups` first; without it the script answers `NOTHING DONE: no kept block found in backups`.
- The second line alone leaves no Nexus in the game at all, because the take-over is out. The installer does not warn about that. To go back, run the first line first.

New numbers or another weapon: change `nexus-tank\make_bundle.py`, run it, then `remove NEXS` and `install "nexus-tank\NEXS"`. If the version in `nexus-tank\NEXS` should stay installable, copy that folder to a new `round` folder first (section 0).

A reinstall changes the lists in `Standard.ini`: since 25 Nov 2026, 11:34, the numbers 9023 and 9024 under `[Animations]` name other animations than in the hours before, 9025 is gone, and `[WeaponTypes]` has the line 9423. Saved games from before a reinstall may not load (as for the map, 10.8). **[UNTESTED]**

Since 25 Nov 2026, 14:41, the Nexus is number 7420 under `[VehicleTypes]` and its five animations are 9029 to 9033; the Tempest, which went in again right after it, is 7421 with 9034 to 9037. **[FILES]**

### 21.6 What is proven and what is not

| Piece | State |
|---|---|
| The model as such: that the game draws these voxels | **[CONFIRMED]** 2 April 2026 on the Bulldog, and 22 Nov 2026 when the Arbalest wore a copy |
| The files of the unit: rules, art, models, icon, sprites, list lines | In place; the check passes. **[FILES]** |
| That it shows as a unit of its own, with its icon | **[CONFIRMED]** 25 Nov 2026 (screenshot): the icon with the name NEXUS stands in the vehicle tab beside the Bulldog's own, and several Nexus tanks are on the field. Seen for the side the owner played; for every side: **[UNTESTED]** |
| The new paint | **[CONFIRMED]** 25 Nov 2026 (screenshot): gunmetal, the decks in the owner's teal. No comment from the owner on it yet |
| The coil drawn light | **[CONFIRMED]** 25 Nov 2026 (screenshot): the rings are pale blue-white on tanks at rest |
| The eight turret stages | Read in the program **[FILES]**; a still picture cannot show them. **[UNTESTED]** No charge turret of our own has been watched in a game |
| The turret on its ring with `TurretOffset=-52` | Nothing looks wrong in the screenshot; not looked at while turning. **[UNTESTED]** |
| The fire point at the barrel's tip | **[UNTESTED]**; worked out by the rule measured on stock tanks |
| The second version's starburst (00:05 to 11:34) | **[CONFIRMED]** 25 Nov 2026 as a fault: the burst plays in the air near the tank, and the owner's report is that it does not hit (21.1) |
| The direct starburst (since 11:34) | Stock blocks with a few changed lines, and the game's routine for the rays read in the program. **[FILES]** Three games ran with it installed (25 Nov 2026, 12:29, 14:21 and 17:04), and their logs are clean; the owner's report of that afternoon does not name the Nexus. **[FILES]** Not seen. **[UNTESTED]** |
| A forced attack (Ctrl) on your own units | Until 14:41 on 25 Nov 2026 both warheads spared your own side; the owner's report of that afternoon, for a flyer of ours with the same line, is that such an attack did no damage. **[CONFIRMED]** 25 Nov 2026 as a fault. The line is out since 14:41. **[FILES]** Not tried since. **[UNTESTED]** |
| Its sounds | The two names are in the sound file. **[FILES]** Not reported. **[UNTESTED]** |
| The five animations | `NEXSSPL` is in the screenshot, in its blue: **[CONFIRMED]** 25 Nov 2026. The other four: **[UNTESTED]** |
| That the Bulldog is the game's own again | Its block is out of the file. **[FILES]** Its own icon stands in the vehicle tab in the screenshot: **[CONFIRMED]** 25 Nov 2026. Its look and cost on the field: **[UNTESTED]** |

What to look at in the next game is in section 12: questions 55 to 58 and 65 for the shot, 45 and 47 for what is still open.

---

## 22. Ranks: veteran and elite

The owner asked on 25 Nov 2026: "what is the tier kind of thing for it? Because other ones have tiers when they kill enough kind of infantry or tanks and they do a great job, they get like one tier up. So, are we going to have tiers? Is it going to, like, you know, change colors or change the way it looks and heal by itself?" This section is what was found that day in the game's rules, and read in the game's program and in the extension (the listings are in `arbalest-tank\kit\research\probe`, the files named `dis_ares_*` and `dis_702D40_register_destruction.txt`). It is **[FILES]** unless it says otherwise. No rank of a unit of ours has been watched in a game.

### 22.1 The three ranks

A unit starts as a rookie, becomes a veteran and then elite. The game keeps one number for it, its experience: 1 or more is veteran, 2 is elite (the extension compares with 1.0 and 2.0, and so do the game's own tests at 0x74FF90, 0x74FFC0 and 0x750010). `VeteranCap=2` in `[General]` of the stock rules is the top.

A unit earns ranks unless its block says `Trainable=no`; the game sets `Trainable=yes` before it reads a unit's block (gamemd 0x71138E). None of our units says `no`, so all nine earn ranks. 38 of the 174 armed stock vehicles say `no`.

### 22.2 What a rank gives

Each unit has two lists: `VeteranAbilities=` and `EliteAbilities=`. An elite unit has both: the game's armour code applies `STRONGER` to an elite unit if either list has it (gamemd 0x6FDCB7 to 0x6FDCE7), and the extension does the same for `SELF_HEAL` (0x10044EC2 to 0x10044EFF). The strength of each comes from `[General]` of the stock rules (read at gamemd 0x66EEA4 to 0x66EF94):

| Ability | What it does in this game |
|---|---|
| `STRONGER` | damage taken is divided by `VeteranArmor=1.4` (gamemd 0x6FDCF3); at least 1 point is still taken |
| `FIREPOWER` | damage done is multiplied by `VeteranCombat=1.4` (0x6FDC4B, 0x6FE3D2) |
| `FASTER` | speed is multiplied by `VeteranSpeed=1.25` (0x4DB1FA) |
| `ROF` | the reload time is multiplied by `VeteranROF=1.0`: no change (0x6FD13F) |
| `SIGHT` | uses `VeteranSight=0.0`; not read further, none of ours has it |
| `SELF_HEAL` | the unit repairs itself (22.5) |

Our nine units got the lists of the stock units they were copied from: `VeteranAbilities=STRONGER` and `EliteAbilities=SELF_HEAL,FIREPOWER,FASTER`, the most common pair of the stock rules (138 of the armed stock vehicles have it). So:

| Rank | Every one of our units |
|---|---|
| Rookie | as built |
| Veteran | takes damage divided by 1.4 (about 71%) |
| Elite | takes damage divided by 1.4, does 1.4 times the damage, moves 1.25 times as fast, repairs itself, and fires its elite weapon (22.4) |

### 22.3 How a unit earns it

Read in the game where a kill is recorded (0x702D40) and in the extension (0x1004EEF0, 0x1004EE30):

- Only a kill counts, and only a kill of something that is not of the killer's side or an ally's. For a unit of one's own or an allied side the value is 0 (gamemd 0x702E6C). **Forced attacks on your own units give no experience.**
- The value of a kill is the victim's price; twice that if the victim was a veteran, three times if it was elite (0x702E79 to 0x702E99).
- The killer gets the value divided by (its own price x `VeteranRatio`) as experience; the stock rules have `VeteranRatio=4.5`. So a unit is veteran once it has killed enemies worth 4.5 times its own price, and elite at 9 times.
- The extension also gives experience to the unit that carries the killer, to the unit that spawned it and to the one that mind-controls it, if their blocks ask for it (keys `Experience.*`); a crate can promote (`Veteran=` under `[Powerups]` of the stock rules), and a building can promote what a spy's side builds (keys `SpyEffect.*Veterancy`). None of that is set on our units.

| Unit | Price | Enemies worth this make it veteran | elite |
|---|---|---|---|
| Arbalest | 700 | 3,150 | 6,300 |
| Reaver | 1,100 | 4,950 | 9,900 |
| Cerberus | 950 | 4,275 | 8,550 |
| Moloch | 1,900 | 8,550 | 17,100 |
| Seraph | 1,300 | 5,850 | 11,700 |
| Tempest | 1,500 | 6,750 | 13,500 |
| Nova | 2,000 | 9,000 | 18,000 |
| Nexus | 1,700 | 7,650 | 15,300 |
| Doomsayer | 600 | 2,700 | 5,400 |

(The price is what the unit costs its owner, so a side with cheaper units needs a little less.)

### 22.4 The elite weapon

An elite unit fires `ElitePrimary=` in place of `Primary=` (and `EliteSecondary=`; for a unit with many weapons, like the Nexus, `EliteWeapon1=` and so on). Of the 174 armed stock vehicles, 92 have another weapon as elite, 30 the same, and 52 no such line. A stock elite weapon is mostly the same weapon with another warhead or another projectile: of the 92, 33 differ only in the warhead, 25 only in the projectile, and 14 in nothing at all. In the middle case the damage stays the same (the elite damage is between 0.53 and 1.50 times the normal one). An example: the stock tank gun `105mm` and its elite `105mmE` differ in the warhead, `AP` and `RHINAPE`, whose shares against light, medium and heavy armour are 5 points higher.

Ours: the Arbalest fires the stock elite gun `105mmE` as elite and the Doomsayer its own `DoomFlareE`; the seven others fire the same weapon at every rank. Their elite gain is the 1.4 times damage of `FIREPOWER`.

### 22.5 Repairing itself

Read in the extension (0x10044E80, 0x1004B820):

- A unit repairs itself if its block says `SelfHealing=yes` (then at every rank), or if `SELF_HEAL` is in a list of its rank. Our three flyers have `SelfHealing=yes`, copied from the stock Invader; the six others repair themselves when elite.
- One step every `RepairRate=` minutes of `[General]`: `RepairRate=.03` times 900 game frames a minute is one step every 27 frames. A unit's block can set its own rate with `SelfHealing.Rate=`; 4 stock units do.
- Each step gives 1 point of health, up to full health. The extension also reads `SelfHealing.%sAmount` and `SelfHealing.%sMax` (a share of full health where it stops), with a rank in place of `%s` (its names `Rookie`, `Veteran`, `Elite` stand in the extension). No stock unit uses them, and they have not been tried. **[UNTESTED]**

### 22.6 What a rank shows, and a look of its own

- **The badge.** A unit without `Insignia.` lines shows the game's own rank badge, like the stock tanks. 192 stock vehicles hide it with `Insignia.Veteran=dummy`, and the heroes have their own (`herostbr`, `herostar`). Ours have no such lines.
- **The moment of promotion** (extension 0x10046AF0): the unit flashes (`VeteranFlashTimer=45` and `EliteFlashTimer=180` frames in the stock rules) and a sound plays, the rules' `UpgradeVeteranSound` or `UpgradeEliteSound`, or the unit's own `Promote.VeteranSound=` or `Promote.EliteSound=` (54 stock units have their own).
- **A look of its own.** The extension can turn a unit into another unit when it is promoted: `Promote.VeteranType=` and `Promote.EliteType=` name the unit it becomes (read at 0x1003F139 and 0x1003F14F, used at 0x10046BF8 and 0x10046C59). The change itself (0x10043650) turns a vehicle only into a vehicle, a flyer into a flyer and a soldier into a soldier, and keeps the health as a share of the full health. The other unit has its own model, paint, weapons and abilities. That is the only way found to change how a unit looks with its rank. No stock unit of this game uses it, so it has not been seen working here. **[UNTESTED]**
- **Colours.** Nothing in the rules or among the extension's key names changes a unit's colours with its rank (searched on 25 Nov 2026: the 64 names in the extension and the 55 in the game that have to do with ranks). The house colour stays. Only a second unit can look different.

### 22.7 What could be added to our units

Offered to the owner on 25 Nov 2026 (question 70), not done, so that the next game tests the cure of 13.10 alone:

1. An elite weapon for each of the seven that have none, made the way the stock ones are made: the same weapon with a stronger warhead or a better shot. For example more rays from the Nexus's orb, more missiles in the Tempest's salvo.
2. A look of its own for elite units: a second unit for each (its model in another paint or with more light), not buildable, named by `Promote.EliteType=`. A new look is new art: candidates in one picture first, as always (section 0).
3. A promotion sound of its own: `Promote.EliteSound=` with a sound the game has.

### 22.8 How to see it in a game

Fight enemies with one unit until it has killed 4.5 times its own price (the table in 22.3): the rank badge appears, the unit flashes and the promotion is heard. As elite it moves faster and repairs itself. A crate can promote too. Kills of your own units do not count. Question 69.

---

## 23. Before it counts as finished: a list by kind

Made on 25 Nov 2026 from everything in section 19, after the owner asked for the guide to say how to prevent those mistakes "when we're making a tank or an aircraft or an infantry or anything else". Each line names what shows it. A line that only a game can show says so; ask the owner about it in section 12.

**Everything new**

| Item | What shows it |
|---|---|
| Copied from a stock thing that does the same job (a tank's gun from a tank's gun, not from an artillery piece) | Reading the stock block with `mo_tool.py section` (3.2). The build scripts of the Nexus and the flyers write what they changed into `departures.txt` in the bundle folder |
| Every name new, not a stock name and not one of ours | `find_unit.py --exact NAME` answers `0 found` for every new name (1.3, step 2); `mo_tool.py check ID` prints `the name is not used by the stock rules` for each block |
| Every list line in place: the unit, every animation, a weapon that only a projectile names | `mo_tool.py check ID` and `packs.py verify NAME` |
| Built in its own folder; the installed version copied to a `round` folder before anything installed is changed | By hand (section 0) |
| Rehearsed on a copy, then installed with the installer while the game and the client are closed | The installers' own checks: `Result: 0 FAIL`, `0 FAILED` |
| After the owner's game: no line `Failed to parse INI file content` in the game's log | `Mental Omega\debug\debug.log` of that game (section 0) |

**Every weapon**

| Item | What shows it |
|---|---|
| No line that spares a side (`AffectsAllies=no`, `AffectsEnemies=no`, `AffectsOwner=no`), none kept from a copied stock warhead | `python -I "arbalest-tank\kit\weapon_audit.py"` must end with `Result: 0 WARN`; it reads the weapons of vehicles, soldiers and map buildings (1.2). For a vehicle `mo_tool.py check ID` warns as well (13.10) |
| `AA=` on the projectile decided: should it be aimed at flyers? | `weapon_audit.py` prints `AA=` for every weapon (13.10) |
| `Verses=` with 11 values; a 0% only where the stock template has it | `mo_tool.py check ID` counts the values; `weapon_audit.py` prints the armours a weapon does nothing to |
| It hits what it is aimed at: no line that bursts it in the air, splits or scatters it, unless that is the point | `weapon_audit.py` prints such lines in its `shot:` column; the Nexus's and the flyers' build scripts stop on them (21.1) |
| A building's weapon reaches no further than its range ring | `check_range.py` (13.5) |
| In a game: forced (Ctrl) on one of your own soldiers, tanks and flyers and on a neutral building, each loses health | The owner (questions 65 and 66) |

**Every unit: a tank, a flyer, a soldier**

| Item | What shows it |
|---|---|
| Ranks decided: `VeteranAbilities=`, `EliteAbilities=`, an elite weapon or the same weapon on purpose, `Trainable=` only if it should not earn ranks | Reading the unit's block (22). The check does not look at ranks |
| A flyer: `SelfHealing=` as its template has it | Reading the block (22.5) |
| A unit of a pack (a soldier) is drawn with its own art: no `Image=` of a stock unit | `packs.py verify NAME` fails on it since 25 Nov 2026 (1.5) |
| The fire point at the weapon's tip | `barrel tip` in `NEWID_validator.txt` against the sheet (1.3, step 3); in the game, the owner |
| Its icon in the tab, its model drawn, the shot leaving the barrel | The owner's screenshot |

**Every building on a map**

| Item | What shows it |
|---|---|
| The map's two preview pictures made again after any change | `make_pack.py` refuses old pictures; `packs.py verify SITE` checks both are installed (16.13) |
| Something on it visibly moves | The owner (17) |
| Seen on its lot before the install | `render_site.py` with `--installed --game` and the rehearsal copy (1.6, step 7; 16.7) |

**Every animation**

| Item | What shows it |
|---|---|
| A line under `[Animations]` and a section of its own in the file that lists it | `mo_tool.py check ID` warns (14.1); `packs.py verify NAME` for a pack |
