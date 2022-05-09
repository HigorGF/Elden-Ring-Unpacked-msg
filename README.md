# elden-ring-data/msg

Elden Ring Data: the /msg folder, extracted and translated to web-friendly formats like JSON.

For other folders, see [elden-ring-data](https://github.com/elden-ring-data)

## What data is included

In-game text localized to other languages, such as:

- names and descriptions of items, NPCs, places
- dialogue from NPCs, menus, world interactions
- tips from loading screens and tutorials

Original: `ELDEN RING\Game\Data0.bdt`

Extracted: `ELDEN RING\Game\msg\{$LANG}\{$TYPE}.msgbnd.dcx`

Translated: `elden-ring-data\msg\{$LANG}\{$TYPE}.msgbnd.dcx.json`

## How this data was generated

1. Used UXM_2.4_ER to extract game files
2. Used SoulsFormats to load
3. Wrote C# code to export to JSON

## Thanks

Meowmaritus: UXM_2.4_ER

JKAnderson: SoulsFormats
