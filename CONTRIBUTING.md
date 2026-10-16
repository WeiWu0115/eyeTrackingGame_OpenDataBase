# Contributing to Gaze Atlas

[中文指南](CONTRIBUTING.zh-CN.md) · [Website contribution hub](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/contribute.html)

We welcome game suggestions, sources, translations, accessibility improvements, design, documentation, and code.

## Suggest a game

Use the [website form](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/contribute.html#submit), [English GitHub form](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/issues/new?template=new-game-en.yml), or [Chinese GitHub form](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/issues/new?template=new-game-zh.yml). Write in either language. Include the title, interaction, hardware, platform, and an official project page, author resource, or original paper. Add image provenance and credit when available.

The website prepares a preview. You review and publish the contribution as a public GitHub issue. Maintainers check the source, identify the appropriate collection, prepare the bilingual record, and review it for inclusion. Include your GitHub username if you would like contribution credit.

For corrections, use the [correction form](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/issues/new?template=correction.yml). Linking the record ID or page helps reviewers find it.

## Contribute through a pull request

1. Fork this repository and create a branch for one focused change.
2. Edit the relevant JSON records in `data/` and `en/data/`, or edit the website files.
3. Run the export and validation commands below.
4. Open a pull request describing the change, primary sources, and checks performed.
5. Address reviewer feedback. Maintainers merge accepted contributions and GitHub Pages publishes the site.

### Data files

| Collection | Chinese | English | Record array |
| --- | --- | --- | --- |
| Main collection | `data/games.json` | `en/data/games.json` | `games` |
| Related training | `data/related-training.json` | `en/data/related-training.json` | `entries` |

Use an existing record as a starting point. Give it a unique, stable, lowercase, hyphenated `id`, matching in both languages. Distinguish editions in titles where relevant. Both language versions use the same canonical `tags`, `design_intent`, `eye_role`, `entry_type`, and `genre_family`; descriptions, categories, and interface-facing text are localized. Record a source-review date in `verified_at` as `YYYY-MM-DD`.

Document what the source establishes: game controls, gaze behavior, hardware, edition, availability, and research context. Research records identify study design, sample, and publication type. Source URLs use HTTP or HTTPS and have descriptive titles.

The main collection covers gaze control, gaze assistance, gaze-responsive interaction, blinking, multimodal input, and gaze measurement in game/research environments. The related training collection covers training and perceptual learning with documented eye tracking. A project that appears in both collections shares the same ID, with `main_collection_id` on its related-training record.

### Images

Include `image_url`, `image_source`, `image_kind`, `image_credit`, and `image_license`. Reference official media or contributor-owned artwork with suitable rights. The shared placeholder is `assets/image-placeholder.svg` at the root, or `../assets/image-placeholder.svg` from `en/`. Label it `Image placeholder`, credit `Gaze Atlas`, and use `CC BY 4.0` for that placeholder asset. The colorful donut-eye artwork remains the homepage illustration.

### Contribution credit

After an accepted contribution, add your GitHub username to `data/contributors.json`, with one or more roles: `maintenance`, `data`, `translation`, `code`, `design`, `review`, `documentation`, or `accessibility`. Use one entry per username. Maintainers can credit accepted issue-based research submissions through the same file. Records optionally carry a `contributors` array of credited GitHub usernames. The website reads the credits file; GitHub also records merged code contributions in the repository history.

## Run checks

From the repository root, using Python 3.10 or newer:

```sh
python3 scripts/sync_catalog.py
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests
```

The sync command regenerates CSV exports, shared-record metadata, review statistics, and documented counts. Review its changes and include generated files in your pull request.

Validation checks unique IDs and titles, required fields, classifications, source URL structure, image files, bilingual alignment, CSV consistency, statistics, contributor credits, and internal links. Tests exercise accepted data and deliberately invalid fixtures. GitHub Actions runs validation, tests, and JavaScript syntax checks on pushes to `main` and pull requests. Maintainers also review the source content and image rights.

To preview the website:

```sh
python3 -m http.server 8765
```

Open `http://localhost:8765/en/` or `http://localhost:8765/`.

## Review and licensing

Keep discussions respectful and focused on the project. Contributions are reviewed by the maintainers. Share original descriptions and data contributions under the repository's CC BY 4.0 terms, and code under MIT. Record third-party media and paper rights with their sources. Credit contributors and retain evidence links when updating a record.
