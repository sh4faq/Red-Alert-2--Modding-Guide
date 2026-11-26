# Red Alert 2 Mental Omega 3.3.6 Modding Guide

One guide for modding an install of Mental Omega 3.3.6, a mod for Red Alert 2: Yuri's Revenge: new tanks, flyers and soldiers, their weapons and effects, buildings on a map and the map's preview pictures. For each kind of thing it says how it is made, step by step with the commands, how it is checked before it goes into the game, and what went wrong on the way.

**Read [10-Adding-Units.md](10-Adding-Units.md).** Start with its section 0, then section 1, the playbook: one recipe for each kind of request.

| File | What it is |
|---|---|
| [10-Adding-Units.md](10-Adding-Units.md) | The guide |
| [scripts/mo_tool.py](scripts/mo_tool.py) | The guide's helper tool (its section 3.2): prints the game's own rules and art, takes files out of the game's archives, checks a new vehicle. It never changes the archives |

## Before you use it

- The guide is the working handbook of one install. Its commands are for PowerShell on Windows and start in the project folder. That folder holds the game (`Mental Omega`), this repository (as `MentalOmega-Modding-Guide`) and the folders of the tools and units that the guide names, such as `arbalest-tank\kit`, `new-units` and `new-buildings`. Only `mo_tool.py` is published here; the other tools are not.
- Every claim that matters carries a label: **[CONFIRMED]** seen working in the game, with the date; **[FILES]** read from the game's files or logs; **[UNTESTED]** reasoned, not tried.
- Nothing here rebuilds a game archive: new things go in as loose files and as lines in the game's INI files. One stock map of this install is changed, so the install is not for online play.
- Until 25 November 2026 this repository held older documents (docs 01 to 06, a quick reference and old scripts). The guide replaces them; its section 9 lists what they got wrong.

Last checked against the game: 25 November 2026.
