# Gaze Atlas · 眼动游戏开放数据库

收录 121 条游戏、研究原型、活动套件与研究环境记录，提供图片、简介、交互方式和来源。资料更新：2026-10-16。

## 浏览

- [中文目录](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/)
- [英文目录](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/en/)
- [研究综述](review.html)
- [认知与知觉训练专题](related-training.html)：7 款游戏与 1 项眼动研究框架。

## 数据

主目录：[JSON](data/games.json)、[CSV](data/games.csv)。相关训练专题：[JSON](data/related-training.json)、[CSV](data/related-training.csv)。CSV 使用 UTF-8 BOM，数组与对象以 JSON 字符串保存。

字段包括稳定 ID、名称、类别、玩法类型、设计目的、眼动角色、交互方式、设备、平台、研究人群、评估、版本资料、图片与来源。中英文使用对应 ID。来源机构保留在文献与项目链接中，各项目按统一分类浏览。

## 资料与图片

资料来自官方游戏页、开发者、设备厂商、研究团队、论文与奖项记录。评估字段记录研究设计与样本；年份说明见各项目资料。图片类型与署名随条目提供，包括官方截图、项目配图、集合概览和原创机制示意。

## 授权与贡献

原创简介、数据编排和原创示意采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，署名 Gaze Atlas contributors 并保留来源。网站代码采用 [MIT](LICENSE)。第三方图片、商标、论文与游戏保留原权利人的授权。

通过 GitHub Issues 或 pull request 提交游戏与修订，附原始来源、设备、版本、图片署名和日期，并同步更新中英文 JSON 与 CSV。

## 本地预览

GitHub Pages 发布 main 分支根目录。本地使用 `python3 -m http.server 8765`，访问 http://localhost:8765/ 。
