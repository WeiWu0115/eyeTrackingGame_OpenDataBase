# Gaze Atlas · 眼动游戏开放数据库

中文精选目录，涵盖商业游戏、无障碍眼控游戏与研究原型。扩展版共 121 条，资料核查日期：2026-10-16。不是穷尽性清单，未逐款实机测试。

## 浏览与部署

本站采用纯静态 HTML、CSS 和 JavaScript，无须安装依赖。GitHub Pages：仓库 Settings → Pages → Deploy from a branch → main → / (root) → Save。

本地预览：在本目录运行 `python3 -m http.server 8765`，浏览 http://localhost:8765 。不要直接双击 index.html，浏览器可能阻止本地数据读取。

## 数据文件

- `data/games.json`：UTF-8，包含版本信息与 games 数组；网站直接从此文件读取。
- `data/games.csv`：UTF-8 BOM，便于电子表格软件打开。数组字段编码为 JSON 字符串。

主要字段：`id` 稳定编号；`title` 原名；`title_zh` 中文名（部分为说明性译名）；`category` 项目类别；`genre` 类型；`device` 设备；`platform` 平台；`interaction` 交互类别；`description` 原创中文简介；`features` 机制标签；`sources` 证据链接；`image_url` 图片地址；`image_source` 图片所在页面；`image_credit` 归属；`image_kind` 图片性质；`image_license` 图片许可；`availability` 可用性；`notes` 限制；`year` 仅已核实的年份，其余留空；`verified_at` 核查日期。

## 收录方法

优先采用游戏厂商、眼动设备厂商、SpecialEffect、作者项目页及学术出版资料。收录眼动参与输入、游戏响应或眨眼检测的案例；另加入明确标注“仅测量”的研究环境，不能视为可眼控游玩的零售游戏。不把支持头动的设备列表自动当作支持眼动的证据。

商业游戏通常仍需键鼠或手柄。无障碍眼控依赖适配软件与硬件。研究原型不保证有可下载的成品；原型的机构背景不代表机构认证。gEYEded 记录的出版商全文页访问受限，收录依据是可检索摘要，详见条目 notes。

图片引用官方页面或作者项目的现有资源，没有复制为开放图库。gEYEded 和 Gaze and voice 条目使用原创机制示意，明确标注“非游戏截图”；数独条目使用集合首页，明确标注图片性质。远程图片可能失效，网站提供回退说明与图片出处。

## 开放许可

原创简介、字段编排和原创机制示意采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，署名 “Gaze Atlas contributors”，保留来源并注明修改。事实本身不因本项目获得独占权。第三方图片、商标、源网页内容、论文与游戏本身不受本许可覆盖，其权利由原权利人保留。游戏免费或源码可见并不等于开源，原项目许可请自行查阅。

站点代码采用 MIT，见 LICENSE。数据下载不要求注册、API 密钥或付费。

## 贡献

通过 GitHub Issue 报告错误或提交 Pull Request。新增条目请提供官方／作者证据、图片出处与版权信息、设备、平台、眼动机制、可用性和核查日期。请勿将推测写成已确认的兼容性。修改 JSON 后同步 CSV。建议通过浏览器验证搜索、筛选、详情与手机布局。

## 扩展综述（2026-10-16）

完整综述见 [review.html](review.html)，检索与分类记录见 [data/review-method.json](data/review-method.json)。新增字段包括 tags、design_intent、eye_role、genre_family、entry_type、awards、target_users、evaluation、customizability、evidence。主要类别互斥，标签可交叉；游戏套件按一条计数。121 条不等于 121 款独立可玩游戏。历史或停售状态见每条 availability 和 notes。