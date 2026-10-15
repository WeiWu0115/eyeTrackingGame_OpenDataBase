# Gaze Atlas · Eye-Tracking Game Open Database

An English-language curated collection of commercial games, accessible gaze games, and research prototypes. The first edition contains 16 entries. Source verification date: October 15, 2026. This is not an exhaustive list; entries have not all been tested hands-on.

## Languages

- [English website](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/)
- [Chinese website](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/)

The Chinese edition is preserved at the repository root. This English edition has its own interface, dataset, and concept illustrations in `en/`. Source references and game IDs match across editions.

## Data and fields

`data/games.json` is UTF-8 and contains schema information and a `games` array. The English website reads this file directly. `data/games.csv` is UTF-8 with a BOM for spreadsheet compatibility; array values are JSON-encoded strings.

Fields: `id` stable identifier; `title` original title; `subtitle` English explanatory subtitle; `category` project category; `genre`; `device` hardware; `platform`; `interaction`; `description`; `features`; `sources` evidence links; `image_url`; `image_source` source page; `image_credit`; `image_kind`; `image_license`; `availability`; `notes` limitations; `year` verified year where available, otherwise null; `verified_at` source verification date.

## Selection and verification

Sources prioritize developers, hardware makers, SpecialEffect, author project pages, and academic publications. Entries use gaze for input or game responses. Blink detection is labeled separately. Studies that only observe player attention are excluded. A device's head-tracking compatibility is not automatically treated as evidence of gaze support.

Commercial games typically still require a keyboard and mouse or controller. Accessible gaze play requires compatible hardware and software. Research prototypes may not have a playable public release. Institutional affiliation does not imply institutional endorsement. Access to the gEYEded publisher full text was restricted; that entry records information from the accessible indexed abstract, as stated in its notes.

Images are referenced from official or author sites, not distributed as an open image library. Two research entries use original interaction diagrams explicitly labeled as concept illustrations, not screenshots. The Sudoku entry uses the collection home screen. Remote images may become unavailable; source links remain available in each entry.

## Licensing

Original descriptions, database arrangement, and concept illustrations use [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribute “Gaze Atlas contributors,” retain source references, and identify modifications. Facts are not exclusively owned by this project. Third-party images, trademarks, source text, papers, and games are excluded and retain their original rights. Free access or visible source code does not automatically mean open-source licensing; consult each original project.

Website code uses MIT; see [LICENSE](../LICENSE). Dataset downloads require no account, API key, or payment.

## Contributing and deployment

Use GitHub Issues or pull requests to suggest games or corrections. Include official or author evidence, image attribution and rights, hardware, platform, interaction, availability, and a verification date. Do not present assumptions as confirmed compatibility. Keep JSON and CSV synchronized and update both languages when revising facts.

GitHub Pages publishes the repository's `main` branch and root directory. No build step is required. For local preview, serve the repository root with `python3 -m http.server 8765`, then open http://localhost:8765/en/ . Opening the HTML directly may prevent the browser from loading JSON.
