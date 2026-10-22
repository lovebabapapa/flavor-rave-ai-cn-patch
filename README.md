# Flavor Rave 简体中文补丁

> 面向《Flavor Rave》及其全部官方 / 联动 DLC 的简体中文**数据补丁**。
> 当前版本：**v1.0.0** · 覆盖 19 个模组 · 274 个文本文件 · 约 2700 条文本

| | |
|---|---|
| **适用游戏版本** | **FNF: Flavor Rave V2.5.2 FULLY BREWED!** |
| 补丁版本 | v1.0.0 |
| 安装方式 | 文件覆盖（先装 DLC，再覆盖补丁） |
| 项目仓库 | https://github.com/lovebabapapa/flavor-rave-ai-cn-patch |
| **原作 GameBanana** | https://gamebanana.com/mods/410436 |
| **原作源码** | https://github.com/Jorge-SunSpirit/Flavor-Rave-Public |


> ⚠️ 补丁的路径与字段结构均按 **V2.5.2 FULLY BREWED!** 校准。
> 若游戏更新到更高版本，可能出现文件缺失、字段结构变化或文本错位，请等待对应补丁更新后再使用。
> 目前原作已基本停止更新，V2.5.2 可视为长期基线版本。

---

## ⚠️ 重要声明

1. **本补丁大量使用 AI 生成译文。** 初版由大语言模型批量翻译，之后经过人工校对与 AI 二次修订。译文可能存在语气偏差、双关处理不当、术语不统一等残留问题——欢迎提交修订。
2. **本补丁与游戏原作者无关**，不含任何游戏本体资源（不含图片、音频、谱面）。仅包含文本 JSON、少量重绘的带字图片，以及三段注入式中文字幕脚本。
3. **请先备份游戏目录**。使用本补丁造成的任何问题由使用者自行承担。

---

## 功能覆盖

| 内容 | 状态 | 数量 |
|---|---|---|
| 剧情过场对话（主线 + 全部 DLC） | ✅ | 37 个文件 |
| SynSun 电视百科 / 人物档案 / 曲目介绍 | ✅ | 78 个文件 |
| 结算画面台词（角色 S~D 评价） | ✅ | 30 个文件 |
| Flavorpedia 图鉴（角色 / 地点 / 物品 / 侧栏） | ✅ | 17 个文件 |
| 成就（名称 / 条件 / Showman 台词） | ✅ | 9 个文件 |
| 职员表 / 画廊说明 | ✅ | 28 个文件 |
| 周目名 / 章节分组 / 地点名 / 曲名 | ✅ | 71 个文件 |
| UI 语言表（选项 / 修改器 / 菜单 / 判定 / 歌词） | ✅ | 289 项 |
| 剧情字条（Introtext，人工重绘） | ✅ | 4 张 |
| Lua 中文字幕（saff 片头 / Restless 前段 / 船歌信件 / Home Brew 结束图） | ✅ | 4 处 |
| DLC 下载菜单 | ❌ | 远程 JSON + 字体限制，需改源码 |
| 歌曲标题卡动画 | ❌ | 仅歌名艺术字，属美术风格 |
| 评分字样 / 主菜单 logo / 轮盘彩蛋 | ❌ | 界面 / 美术类 |

**未覆盖的详细说明见补丁内 `汉化说明.txt` 的「未覆盖内容（及原因）」。**

---

## 安装

```text
1. 备份游戏安装目录（整个文件夹复制一份）
2. 把补丁内所有文件按相同相对路径覆盖到游戏根目录
     assets/data/...  →  <游戏目录>/assets/data/...
     mods/<DLC名>/... →  <游戏目录>/mods/<DLC名>/...
3. 启动游戏
```

### 升级 / 重装

- 补丁是「文件覆盖」型，**直接覆盖即可升级**，不影响存档。
- **新装了 DLC 之后，请等补丁更新并重新覆盖一次**——否则新 DLC 的内容会显示英文（补丁里没有它的文件）。顺序永远是：**先装 DLC，再覆盖补丁**。
- 不要与其他汉化补丁混装（会互相覆盖 `language*.json`）。

### 回滚

用备份目录覆盖回去，或删除本补丁写入的文件。

---

## 常见问题

| 问题 | 原因 / 解法 |
|---|---|
| 进游戏还是英文 | 覆盖层级错了（放进了子文件夹），或 `assets/preload` 残留目录未清理 |
| 新装 DLC 后新内容英文 | 正常，等补丁更新后重新覆盖 |
| 游戏版本不是 V2.5.2 | 不保证兼容。补丁按 V2.5.2 FULLY BREWED! 校准，版本不符可能出现缺文件或文本错位 |
| 中文变方块 / 空白 | `assets/data/languageFont.json` 未覆盖（它指向游戏内嵌 CJK 字体） |
| 某句很怪 / 人名被翻译 | AI 初译残留，欢迎按「文件 + 行号 + 建议」提交 |
| 会和别的 MOD 冲突吗 | 纯谱面 MOD 一般不冲突；带 `language*.json` 的会互相覆盖 |
| 会改存档 / 判定吗 | 不会，只替换文本资源与三段 Lua 字幕脚本 |

---

## 项目结构

```text
ainiee/
├── pipeline.py            # 主流水线：extract / set_titles / reinject
├── postfix.py             # 术语与措辞的全局替换规则表（最重要）
├── menu_zh.py             # UI 语言表（Option / Gameplay / Flavor）
├── restore_images.py      # 人工修图 → sprite atlas 回填
├── build.py               # 打包发布（版本号注入 + zip + sha256）
├── manual_files/          # 不走流水线、必须随补丁发布的手工资源
├── source_files/          # 游戏原始英文 JSON 快照（回填时的底板）
├── AiNiee输入/            # 抽取出的待译骨架 (*.i18n.json)
├── out/                   # 译文（*.i18n_translated.json）★ 改译文主要在这里
├── 汉化底稿/              # UI 三张语言表的中文底稿
├── 汉化素材_图片/         # 图片类资源的逐帧导出（供人工修图）
├── 汉化输出/FR_CN_补丁/   # 构建产物
└── docs/维护指南.md       # 给后继者的完整工作流说明
```

### 想继续人工优化？

**改一句台词**（最常见）：

1. 打开 `out/<对应文件>.i18n_translated.json`
2. 改掉对应 key 的 `text` / `name`
3. 跑 `python pipeline.py reinject` —— 补丁会重新生成
4. 把 `汉化输出/FR_CN_补丁` 覆盖到游戏

**改一类术语**（全局）：编辑 `postfix.py` 的替换表，重跑 `reinject`。

详细流程、踩坑清单、加新 DLC 的步骤 → **[docs/维护指南.md](docs/维护指南.md)**

---

## 版本

当前 **v1.0.0**，变更历史见 [CHANGELOG.md](CHANGELOG.md)。

发布时执行：

```bash
python build.py
```

会校验 `manual_files` 完整性、生成 `汉化输出/FR_CN_patch_v<版本>.zip` 与对应 sha256。

---

## 反馈

- **译误 / 语气问题** → [提交译误反馈](https://github.com/lovebabapapa/flavor-rave-ai-cn-patch/issues/new?template=translation-error.yml)（填文件路径 + 行号 + 建议译法）
- **新 DLC 未汉化** → [请求支持新 DLC](https://github.com/lovebabapapa/flavor-rave-ai-cn-patch/issues/new?template=new-dlc.yml)（填 DLC 名 + 来源链接 + 安装后的文件夹名）
- 提交前请先确认使用的是 [最新版本](https://github.com/lovebabapapa/flavor-rave-ai-cn-patch/releases) 且游戏为 V2.5.2

---

## 许可与致谢

- 本项目中的**脚本与工具链**：MIT License
- 本项目中的**译文文本**：CC BY-SA 4.0（转载 / 二次修改请保留出处与相同许可）
- 游戏本体、角色、美术、音乐版权归 **Team TBD / Flavor Rave 原作者** 所有：
- GameBanana 页面：https://gamebanana.com/mods/410436
- 上游公开源码：https://github.com/Jorge-SunSpirit/Flavor-Rave-Public：
- GameBanana 页面：https://gamebanana.com/mods/410436
- 上游公开源码：https://github.com/Jorge-SunSpirit/Flavor-Rave-Public
- 感谢原作者与各 DLC 作者创作的优秀作品；感谢所有提交译误反馈的玩家

> 本项目不提供游戏本体，请支持正版。
