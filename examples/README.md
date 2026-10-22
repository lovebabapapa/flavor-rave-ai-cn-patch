# 示例：为单个 DLC 建立翻译批次

`batch_*.py` 是 v1.0.0 期间为 4 个剧情 DLC 手写的批量翻译脚本，
它们演示了「新增一个 DLC 后如何一次性产出脚本就能回填的译文」：

1. 从游戏目录读取 `dreamcast.json`（对话）、`synsun/*.json`（电视百科）、
   `achievements.json`、`galleryData.json`、`creditsData.json`、`flavorpediaData.json`
2. 按 AiNiee 的输入格式写出 `AiNiee输入/<压平路径>.i18n.json`（只含 key + 英文原文）
3. 同时写出 `out/<压平路径>.i18n_translated.json`（中文译文）
4. 歌词类写入 `汉化底稿/languageFlavor-底稿.json`
5. 之后统一执行 `python pipeline.py reinject`

要点：
- 中文译文**直接写在脚本里的列表**，方便人工校对与成批修订
- `dialogue` 的 key 是序号字符串，结算画面用 `name` 字段而非 `text`
- Flavorpedia 字幕要保留 `:dur:` / `[NL]` 标记

看完这四个脚本，照着改歌名/文件路径就能给新 DLC 建批次。
