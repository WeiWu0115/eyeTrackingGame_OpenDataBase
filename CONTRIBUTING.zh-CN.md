# 参与共建 Gaze Atlas

[English guide](CONTRIBUTING.md) · [网站参与入口](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/contribute.html)

欢迎推荐游戏、补充来源、翻译介绍，以及改进无障碍体验、设计、文档和代码。

## 提交游戏

使用[网站表单](https://sharkburger.github.io/eyeTrackingGame_OpenDataBase/contribute.html#submit)、[中文 GitHub 表单](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/issues/new?template=new-game-zh.yml)或[英文 GitHub 表单](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/issues/new?template=new-game-en.yml)。可任选中文或英文填写，附游戏名称、交互方式、设备、平台和官方项目、作者资料或原始论文。图片附出处与署名。

网站先生成投稿预览，随后由你在 GitHub 确认发布公开 Issue。维护者审核来源、确定分类、整理中英文记录，再安排收录。希望署名时可填写 GitHub 用户名。

修正已有资料时，使用[资料修正表单](https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/issues/new?template=correction.yml)，附条目 ID 或页面链接。

## 通过 Pull Request 贡献

1. Fork 仓库，为一个明确的修改创建分支。
2. 编辑 `data/` 与 `en/data/` 中对应 JSON，或修改网页文件。
3. 运行导出与检查命令。
4. 提交 Pull Request，说明修改、一手来源和检查结果。
5. 根据审核意见完善；维护者合并后由 GitHub Pages 发布。

## 数据约定

主目录位于 `data/games.json` 和 `en/data/games.json`，记录数组为 `games`。

可从已有条目开始编辑。`id` 使用稳定、唯一的小写英文与连字符，中英文保持一致。版本差异可在标题中说明。`tags`、`design_intent`、`eye_role`、`entry_type` 与 `genre_family` 使用两种语言共用的规范值；介绍、类别名称和展示文本分别本地化。`verified_at` 使用 `YYYY-MM-DD` 表示来源核查日期。

记录来源明确描述的操作、眼动用途、设备、版本、获取方式和研究背景。研究条目附研究设计、样本与发表类型。来源使用带标题的 HTTP／HTTPS 链接。

主目录涵盖眼控、辅助、注视响应、眨眼、多模态输入与游戏研究中的眼动测量。

## 图片与署名

填写 `image_url`、`image_source`、`image_kind`、`image_credit` 和 `image_license`。优先采用来源明确、授权适合的官方或贡献者图片。灰色 donut 占位图路径为根目录的 `assets/image-placeholder.svg`，英文页面使用 `../assets/image-placeholder.svg`；类型填“配图占位”，署名 Gaze Atlas，许可 CC BY 4.0。首页继续使用彩色 donut 插画。

贡献收录后，可将 GitHub 用户名加入 `data/contributors.json`，每人一条记录。角色可选 `maintenance`、`data`、`translation`、`code`、`design`、`review`、`documentation`、`accessibility`。维护者也通过此文件记录已采纳的 Issue 投稿。条目可使用 `contributors` 数组记录贡献者用户名，网站详情会展示署名。

## 检查与预览

在仓库根目录使用 Python 3.10 或更新版本运行：

```sh
python3 scripts/sync_catalog.py
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests
```

同步脚本更新 CSV、综述统计与记录数量。请检查并提交这些生成文件。

自动检查涵盖 ID 和标题唯一性、必填字段、分类、来源 URL 格式、图片文件、中英文对应、CSV 一致性、统计、贡献者记录和本地链接。GitHub Actions 会在主分支推送与 Pull Request 中运行这些检查、测试和 JavaScript 语法检查。维护者结合原始来源审核内容与图片权利。

本地预览使用 `python3 -m http.server 8765`，然后访问 `http://localhost:8765/` 或 `http://localhost:8765/en/`。

## 协作与授权

围绕项目友善交流，贡献由维护者审核。原创描述与数据使用项目的 CC BY 4.0 条款，代码使用 MIT。第三方图片和论文保留原授权，并随来源记录。修改条目时保留证据链接和贡献者署名。
