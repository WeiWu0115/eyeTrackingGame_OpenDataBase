# Gaze Atlas · Eye-Tracking Game Open Database

122 records covering games, research prototypes, activity suites, and research environments, with images, descriptions, interaction details, and sources. Updated October 16, 2026.

## Browse

- [English collection](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/)
- [Chinese collection](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/)
- [Research review](review.html)

## Data

Main collection: [JSON](data/games.json), [CSV](data/games.csv). CSV uses UTF-8 with BOM; arrays and objects are JSON-encoded strings.

Fields include stable ID, title, category, genre, design purpose, gaze role, interaction, hardware, platform, population, evaluation, edition context, images, and sources. Matching IDs connect both languages. Institutional provenance accompanies citations, and shared categories organize browsing.

## Documentation and images

Sources include official game pages, developers, hardware makers, research teams, papers, and award records. Evaluation fields describe study design and samples. Each record explains its year and edition context. Image types and credits identify official screenshots, project media, collection overviews, and image placeholders.

## Licensing and contributions

Original descriptions, arrangement, and original diagrams use [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribute Gaze Atlas contributors and retain sources. Website code uses [MIT](../LICENSE). Third-party images, trademarks, papers, and games retain their original terms.

Contribute through GitHub Issues or pull requests. Include primary sources, hardware, editions, image credits, and dates. Keep both language editions and JSON/CSV exports synchronized.

## Local preview

GitHub Pages publishes the main branch and root directory. Run `python3 -m http.server 8765` from the repository root and visit http://localhost:8765/en/ .

The donut-eye artwork is supplied by the project maintainer for the homepage; its artwork rights remain with its contributor.

## Community contributions

Use **Contribute** in the website navigation to submit a game, open English or Chinese GitHub forms, read the guide, inspect automated checks, or view contributor credits.

- [Contribution hub](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/contribute.html)
- [Contributor credits](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/contributors.html)
- [Contribution guide](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/blob/main/CONTRIBUTING.md) · [Chinese guide](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/blob/main/CONTRIBUTING.zh-CN.md)
- [Catalog validation runs](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/actions/workflows/validate-data.yml)

For data changes, run `python3 scripts/sync_catalog.py`, `python3 scripts/validate_catalog.py`, and `python3 -m unittest discover -s tests` from the repository root. Accepted research, translation, code, and design contributions can be credited in `data/contributors.json` and each record’s optional `contributors` field.
