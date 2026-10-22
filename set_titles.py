# -*- coding: utf-8 -*-
"""曲名显示格式：英文名（中文名）- 曲作者英文名
写入 out/ 的 meta 译文 + 游戏目录的 meta.json。
用法: python set_titles.py [--apply]"""
import json, os, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "source_files")
GAME = "P:/FNF/Flavor.Rave"
apply = "--apply" in sys.argv

# 个别曲名过长会顶出 freeplay 的 604px 文本框，单独给短版中文名
SHORT_OVERRIDES = {
    "Tres Leches (HQ)": "三奶蛋糕",
}

zh_map = {en: zh for en, zh in json.load(open(os.path.join(HERE, "_song_titles.json"), encoding="utf-8"))}

FULL_ARTIST = "--full" in sys.argv

def primary_artist(a):
    """取主作者：去掉 & / ft. / , 后面的合作者，避免自由模式列表溢出"""
    if not a: return ""
    for sep in [" ft.", " feat.", "&", "/", ","]:
        a = a.split(sep)[0]
    return a.strip()

def display(en, artist):
    """默认格式「英文名（中文名）」。
    原因：FlavorHUD 与暂停界面本来就会自己拼『曲名 - 作者』，
    曲名里再带作者会重复；且自由模式列表只有 604px 宽，带作者会溢出。
    --with-artist 可强制带上作者（会重复/溢出，仅供测试）。"""
    zh = SHORT_OVERRIDES.get(en) or zh_map.get(en)
    name = f"{en}（{zh}）" if (zh and zh != en) else en
    if "--with-artist" in sys.argv:
        a = artist if FULL_ARTIST else primary_artist(artist)
        if a: name += f" - {a}"
    return name

rows = []
for f in sorted(glob.glob(os.path.join(SRC, "**/meta.json"), recursive=True)):
    rel = os.path.relpath(f, SRC).replace(os.sep, "/")     # assets/preload/data/x/meta.json | mods/.../meta.json
    try:
        src = json.load(open(f, encoding="utf-8-sig"))
    except Exception:
        continue
    en = src.get("song", {}).get("name", "")
    artist = src.get("song", {}).get("artist", "")
    if not en:
        continue
    newname = display(en, artist)
    rows.append((rel, en, newname))

for rel, en, newname in rows:
    print(f"{en:22} -> {newname}")

if apply:
    # 1) 写 out/ 的 i18n 译文
    for rel, en, newname in rows:
        base = rel.replace("/", "__")
        tp = os.path.join(HERE, "out", base + ".i18n_translated.json")
        if not os.path.exists(tp):
            tp = os.path.join(HERE, "out", rel.replace("/", "__").replace(".json", "") + ".i18n_translated.json")
        if os.path.exists(tp):
            d = json.load(open(tp, encoding="utf-8"))
            d.setdefault("song", {})["name"] = newname
            json.dump(d, open(tp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # 2) 写游戏目录（路径拍平）
    n = 0
    for rel, en, newname in rows:
        ship = rel[len("assets/preload/"):] and ("assets/" + rel[len("assets/preload/"):]) if rel.startswith("assets/preload/") else rel
        gp = os.path.join(GAME, ship.replace("/", os.sep))
        if os.path.exists(gp):
            d = json.load(open(gp, encoding="utf-8-sig"))
            d["song"]["name"] = newname
            json.dump(d, open(gp, "w", encoding="utf-8"), ensure_ascii=False, indent="\t")
            n += 1
    print(f"\n已写入 out/ 与游戏目录（{n} 个 meta.json）")
