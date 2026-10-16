# Gaze Atlas · Eye-Tracking Game Open Database

An open, bilingual database of eye-tracking games and interactive research projects. Browse commercial titles, indie games, accessible gaze experiences, training activities, and academic prototypes, with images, descriptions, hardware details, and primary sources.

**Updated October 16, 2026:** 122 records in the main collection. The Training games page presents seven Brain Game Center training games and the gaze research framework also included in the main collection.

## Explore

- [English website](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/)
- [Chinese website](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/)
- [Research review and classification](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/review.html)
- [Cognitive and perceptual training collection](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/related-training.html)

The website supports keyword search and filters for category, genre, design purpose, gaze role, hardware, interaction, and research population. Projects from UCSD PoNG and other institutions use the same classification; institutional provenance accompanies their sources.

## Collection coverage

| Primary category | Records |
| --- | ---: |
| Commercial games | 34 |
| Indie & small games | 22 |
| Accessible gaze games | 16 |
| Research prototypes | 26 |
| Training & serious games | 22 |
| Research observation & datasets | 2 |
| **Total** | **122** |

Cross-cutting tags identify 24 records with Steam sources, 51 research-related records, 33 training records, seven VR records, and four documented award winners. Tags overlap across categories. Records represent individual games, prototypes, activity suites, and research environments.

The related training collection covers **Poly Rules!, Recollect, Recall, Remember Bee, Saving Memo, Sightseeing, and Listen**, alongside a **gaze-contingent perceptual-learning framework**. Its entries describe cognitive flexibility, memory, vision, hearing, and gaze-driven research displays.

## Open data

| Dataset | English | Chinese |
| --- | --- | --- |
| Main collection — 122 records | [JSON](en/data/games.json) · [CSV](en/data/games.csv) | [JSON](data/games.json) · [CSV](data/games.csv) |
| Related training — 8 records | [JSON](en/data/related-training.json) · [CSV](en/data/related-training.csv) | [JSON](data/related-training.json) · [CSV](data/related-training.csv) |
| Review method and counts | [JSON](en/data/review-method.json) | [JSON](data/review-method.json) |

Records include stable IDs, titles, descriptions, categories, genres, design purposes, gaze roles, input methods, hardware, platforms, populations, evaluation details, edition context, image credits, and source links. Matching IDs connect the two language editions.

CSV files use UTF-8 with BOM for spreadsheet compatibility. Arrays and objects are stored as JSON-encoded strings. The main JSON file contains a `games` array; the related training file contains an `entries` array.

## Sources and images

Documentation draws on official game pages, developers, hardware makers, research teams, original papers, and award records. Research details identify the study design, sample, and publication context.

Images are labeled as official screenshots, project media, collection overviews, app icons, or collection artwork. Each entry includes image provenance and rights information.

## Contribute

[Suggest a game or submit a correction](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/issues/new), or open a pull request. Include:

- A primary source describing the game and its interaction.
- Hardware, platform, edition, and access information.
- An image source, credit, and rights information.
- Research details and a verification date where applicable.

Use stable IDs and keep the English and Chinese editions, JSON, CSV, and review counts synchronized.

## Run locally

The website uses static HTML, CSS, and JavaScript. From the repository root, run:

```sh
python3 -m http.server 8765
```

Open [the English edition](http://localhost:8765/en/) or [the Chinese edition](http://localhost:8765/). GitHub Pages publishes the repository's `main` branch from the root directory.

## Licensing

Original descriptions, database arrangement, and original diagrams use [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribute **Gaze Atlas contributors**, retain source references, and identify modifications.

Website code uses the [MIT License](LICENSE). Third-party images, trademarks, papers, and games retain their original rights and licensing terms.

甜甜圈眼睛插画由项目维护者提供，用于首页与目录配图，插画权利由提供者保留。
