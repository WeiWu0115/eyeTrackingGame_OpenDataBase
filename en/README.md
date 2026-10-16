# Gaze Atlas · Eye-Tracking Game Open Database

122 records covering games, research prototypes, activity suites, and research environments, with images, descriptions, interaction details, and sources. Updated October 16, 2026.

## Browse

- [English collection](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/)
- [Chinese collection](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/)
- [Research review](review.html)
- [Cognitive and perceptual training](related-training.html): seven games and one gaze research framework.

## Data

Main collection: [JSON](data/games.json), [CSV](data/games.csv). Related training: [JSON](data/related-training.json), [CSV](data/related-training.csv). CSV uses UTF-8 with BOM; arrays and objects are JSON-encoded strings.

Fields include stable ID, title, category, genre, design purpose, gaze role, interaction, hardware, platform, population, evaluation, edition context, images, and sources. Matching IDs connect both languages. Institutional provenance accompanies citations, and shared categories organize browsing.

## Documentation and images

Sources include official game pages, developers, hardware makers, research teams, papers, and award records. Evaluation fields describe study design and samples. Each record explains its year and edition context. Image types and credits identify official screenshots, project media, collection overviews, and collection artwork.

## Licensing and contributions

Original descriptions, arrangement, and original diagrams use [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribute Gaze Atlas contributors and retain sources. Website code uses [MIT](../LICENSE). Third-party images, trademarks, papers, and games retain their original terms.

Contribute through GitHub Issues or pull requests. Include primary sources, hardware, editions, image credits, and dates. Keep both language editions and JSON/CSV exports synchronized.

## Local preview

GitHub Pages publishes the main branch and root directory. Run `python3 -m http.server 8765` from the repository root and visit http://localhost:8765/en/ .

The donut-eye artwork is supplied by the project maintainer for the homepage and collection imagery; its artwork rights remain with its contributor.
