# 更新日志

## v1.0.1 — 2026-10-22 · 补全死亡台词

### 修复与补全
- **新增：全部死亡台词（GAME OVER 语音字幕）** —— 33 个角色、74 句
  此前整块遗漏（文本存放在 `characters/gameover/*.json` 的 `goSound` 字段，
  不在原抽取白名单内）。基础游戏 16 个角色 + 全部 DLC 17 个角色均已覆盖，
  每句的 `:dur:` 语音计时保持与原版一致
- 修复 `酸莓` → `Sour`（timeshock 章节人名误译）

### 管线
- `FILE_RULES` 新增 `characters/gameover/` 类型，`EXTRACTORS` 新增 `goSound.*.subtitles`（subtitle 模式）
- 新增 `batch_gameover.py` 批次脚本（按分句生成，含逐句计时）


> **适用游戏版本**：FNF: Flavor Rave **V2.5.2 FULLY BREWED!**
> 补丁的路径与字段结构按该版本校准；游戏若更新需等待对应补丁版本。
>
> **原作**：[GameBanana](https://gamebanana.com/mods/410436) · [上游源码](https://github.com/Jorge-SunSpirit/Flavor-Rave-Public)
>
> **原作**：[GameBanana](https://gamebanana.com/mods/410436) · [上游源码](https://github.com/Jorge-SunSpirit/Flavor-Rave-Public)

## v1.0.0 — 2026-10-22 · 首个正式版

首个公开版本，覆盖基础游戏与全部 19 个模组（含 4 个剧情/联动 DLC、10 个播报员替换包）。

### 覆盖
- 剧情过场 37 个文件 · 电视百科 78 · 结算台词 30 · 图鉴 17 · 成就 9 · 职员表/画廊 28 · 周目与曲名 71
- UI 语言表 289 项（选项菜单、Modifiers、暂停菜单、判定、两首带歌词歌曲的实时歌词）
- 4 张剧情字条人工重绘（Ignatius / Caramelize 开场）
- Lua 中文字幕 4 处：saff 电影片头、Restless 前段歌词、船歌信件台词、Home Brew 结束画面

### 术语规范（本版确立）
- 角色名一律保留英文（Sour / Sweet / Spicy / Saffron / Showman…）
- 地名意译：恩辛克（地区）/ 恩辛克城 / 唐辛子镇 / 新唐辛子 / 剩饭区
- 曲名统一「英文（中文）」格式
- 周目分组统一：联动故事 / DLC 章节 / 间章 N

### 修复
- 修复 `results` 与 `synsun` 抽取规则顺序冲突（角色名 synsun 的结算台词 21 行漏译）
- 修复 `character.*.place` 字段未进抽取白名单
- 修复擦除行尾空格的正则误吞换行
- 修复 Modifiers 菜单名称与取值键位缺失（滚动类型/速度、生命增减、失误即死等 10 项）
- 修复播报员选择菜单中 6 个角色名被意译
- 修复 `reinject` 清空补丁目录导致手工资源丢失（引入 `manual_files` 清单机制）

---

## 预发布历程（0.x，未公开）

| 版本 | 内容 |
|---|---|
| v0.1–v0.3 | 搭管线（AiNiee i18next JSON），基础游戏 186 文件初翻，覆盖率 96.6% |
| v0.4–v0.6 | 补译窗口 + 3 张 UI 语言表，修「短词被过滤导致丢 key」 |
| v0.7–v1.x（旧编号） | 主菜单字幕、选项菜单 41 项说明、判定文字、Modifiers |
| v2.x | 安装 4 个剧情 DLC：Lovers Together、Taste of Revenge、Chillin' & Thrillin'、Masters of the Craft（新增 15 个文件，含 Restless 64 句歌词） |
| v2.6 | 4 个 Alt Announcer + 人物档案入口，全库覆盖复查归零 |
| v3.0–v3.4 | 修复结算规则冲突；人名/地名统一（酸橙/酸果酱/藏红花/芥末/托加拉希等 20+ 变体） |
| v3.5–v3.6 | 人工重绘剧情字条回填；saff 片头 Lua 字幕 |
| v3.7–v4.1 | Restless 前段字幕、船歌信件字幕 + 时间轴校正、Home Brew 结束图、修复误删显隐代码块 |
