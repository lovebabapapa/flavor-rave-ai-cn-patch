# -*- coding: utf-8 -*-
"""
Flavor Rave <-> AiNiee 管线 (v2)

extract  : 源JSON -> AiNiee输入/*.json (i18next格式, 字符串叶子, 句段拆分)
reinject : AiNiee输出(译文叶子) + 源JSON -> 汉化translation mod 完整目录

换行/特殊标记保真策略:
  - 普通文本: \n -> <br> (AiNiee换行标签, 输出自动还原为\n)
  - subtitles 字段 "文本:dur:秒[NL]文本:dur:秒": 拆成独立叶子, dur 记录在 _dur_map.json
  - ￙(U+FFD9) 等特殊字形保留原样
"""
import json, os, re, sys, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(HERE, "source_files")
OUT_DIR = os.path.join(HERE, "AiNiee输入")
TRANS_DIR = os.path.join(HERE, "汉化输出")
DUR_MAP = os.path.join(HERE, "_dur_map.json")

FILE_RULES = [
    (lambda p: p.endswith("/dreamcast.json") or p.endswith("/saturn.json"), "dreamcast"),
    # 注意：results 必须先于 synsun 判断——角色名恰好叫 "synsun" 时会命中 /character/synsun/
    (lambda p: "/images/results/character/" in p and p.endswith("/dialogue.json"), "results"),
    (lambda p: "/synsun/" in p and p.endswith(".json"), "synsun"),
    (lambda p: p.endswith("/creditsData.json"), "credits"),
    (lambda p: p.endswith("/achievements.json"), "achievements"),
    (lambda p: p.endswith("/galleryData.json") or p.endswith("/galleryCGData.json"), "gallery"),
    (lambda p: p.endswith("/flavorpediaData.json") or p.endswith("/flavorpediaSideData.json"), "flavorpedia"),
    (lambda p: "/weeks/" in p and p.endswith(".json"), "weeks"),
    (lambda p: p.endswith("/meta.json") and "/data/" in p, "meta"),
]

# 白名单: 抽取器 -> [(字段路径, 处理方式)]
# 处理方式: plain=常规  subtitle=带dur计时  nameable=保留占位符
EXTRACTORS = {
    "dreamcast":    [("dialogue.*.text", "plain"), ("dialogue.*.choices.*.text", "plain")],
    "synsun":       [("dialogue.*.text", "plain"), ("dialogue.*.choices.*.text", "plain")],
    "results":      [("dialogue.*.name", "plain")],
    "credits":      [("peeps.*.description", "plain"), ("peeps.*.whichrole", "plain")],
    "achievements": [("achievements.*.fancyName", "plain"),
                     ("achievements.*.unlockCondition", "plain"),
                     ("achievements.*.showmanDialogue", "plain")],
    "gallery":      [("artwork.*.caption", "plain")],
    "flavorpedia":  [("character.*.flavorText", "plain"), ("character.*.subtitles", "subtitle"),
                     ("character.*.design", "plain"), ("character.*.desc", "plain"),
                     ("character.*.place", "plain"),
                     ("character.*.place", "plain"),
                     ("place.*.flavorText", "plain"), ("place.*.desc", "plain"),
                     ("things.*.flavorText", "plain"), ("things.*.desc", "plain")],
    "weeks":        [("weekName", "plain"), ("storyName", "plain"), ("location", "plain")],
    "meta":         [("song.name", "plain")],
}

NL_TAG = "<br>"


def enc_plain(s):
    return s.replace("\r\n", NL_TAG).replace("\n", NL_TAG)


def dec_plain(s):
    return s.replace(NL_TAG, "\n")


def pick_paths():
    d = json.load(open(os.path.join(HERE, "fr_tree.json"), encoding="utf-8"))
    out = []
    for t in d["tree"]:
        p = t["path"]
        if t["type"] != "blob" or p.startswith("art/"):
            continue
        for pred, kind in FILE_RULES:
            if pred(p):
                out.append((p, kind))
                break
    return out


# ---------------- 抽取 ----------------
def extract():
    dur_map = {}
    files_out = 0; lines = 0
    os.makedirs(OUT_DIR, exist_ok=True)
    for p, kind in pick_paths():
        local = os.path.join(SRC_DIR, p.replace("/", os.sep))
        if not os.path.exists(local):
            continue
        try:
            data = json.load(open(local, encoding="utf-8-sig"))
        except Exception as e:
            print(f"! 跳过 {p}: {e}"); continue
        sink = {}
        for path_pat, mode in EXTRACTORS[kind]:
            _collect(data, path_pat.split("."), [], sink, p, mode, dur_map)
        if not sink:
            continue
        fn = os.path.join(OUT_DIR, p.replace("/", "__") + ".i18n.json")
        json.dump(sink, open(fn, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        files_out += 1
        lines += _leaf_count(sink)
    json.dump(dur_map, open(DUR_MAP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"抽取完成: {files_out} 个文件, {lines} 个句段; dur映射 {len(dur_map)} 条")


def _collect(node, segs, prefix, sink, filekey, mode, dur_map):
    if not segs:
        return
    head, rest = segs[0], segs[1:]
    if head == "*":
        if isinstance(node, list):
            for i, it in enumerate(node):
                _collect(it, rest, prefix + [str(i)], sink, filekey, mode, dur_map)
        elif isinstance(node, dict):
            for k, v in node.items():
                _collect(v, rest, prefix + [k], sink, filekey, mode, dur_map)
        return
    if isinstance(node, dict) and head in node:
        val = node[head]
        if not rest and isinstance(val, str) and val.strip():
            pathkey = filekey + "|" + "/".join(prefix + [head])
            if mode == "subtitle":
                parts = val.split("[NL]")
                sub = {}
                for i, seg in enumerate(parts):
                    m = re.match(r"^(.*?)(:dur:(\d+(?:\.\d+)?))?$", seg, re.S)
                    text, dur = m.group(1), m.group(3)
                    sub[str(i)] = enc_plain(text) if text.strip() else ""
                    if dur is not None:
                        dur_map[pathkey + "/" + str(i)] = dur
                    elif text.strip():
                        dur_map[pathkey + "/" + str(i)] = None
                sink.setdefault("/".join(prefix) or "_", {})
                cur = sink
                for k in prefix + [head]:
                    cur = cur.setdefault(k, {}) if isinstance(cur, dict) else cur
                # 直接放置（prefix+head 唯一）
                _setpath(sink, prefix + [head], sub)
            else:
                _setpath(sink, prefix + [head], enc_plain(val))
        elif rest:
            _collect(val, rest, prefix + [head], sink, filekey, mode, dur_map)


def _setpath(sink, keys, value):
    cur = sink
    for k in keys[:-1]:
        if k not in cur or not isinstance(cur[k], dict):
            cur[k] = {}
        cur = cur[k]
    cur[keys[-1]] = value


def _leaf_count(d):
    n = 0
    for v in d.values():
        if isinstance(v, str):
            if v: n += 1
        elif isinstance(v, dict):
            n += _leaf_count(v)
    return n


# ---------------- 回填 ----------------
def _trans_dir():
    """AiNiee 输出目录：优先 out/（新版带 _translated 后缀），兼容 AiNiee输出/"""
    for d in ("out", "AiNiee输出"):
        p = os.path.join(HERE, d)
        if os.path.isdir(p) and any(f.endswith(".json") for f in os.listdir(p)):
            return p
    return os.path.join(HERE, "AiNiee输出")


def _match_trans_file(trans_dir, base):
    """在译文目录里找到与输入文件对应的译文文件（兼容 _translated 后缀）"""
    for cand in (base + ".i18n_translated.json", base + ".i18n.json",
                 base + ".json", base + "_translated.json"):
        p = os.path.join(trans_dir, cand)
        if os.path.exists(p):
            return p
    return None


def reinject(mod_name="FR_CN_补丁"):
    """
    读 AiNiee输出目录(与 AiNiee输入 同名同构的译文文件)，
    生成 汉化输出/<mod_name>/ —— 镜像 repo 原始路径结构的补丁目录。
    用法：备份游戏安装目录后，把补丁内的文件按同名路径覆盖进去。
    (不用 translation mod 是因为 creditsData/flavorpediaData 等 6 个文件
     在基础游戏与各 DLC 包共用同一运行时 key，mod 无法按上下文区分内容)
    """
    trans_in = _trans_dir()
    if not os.path.isdir(trans_in):
        print(f"译文目录不存在: {trans_in}\n请先完成 AiNiee 翻译，把输出文件放到该目录。")
        return
    print(f"译文来源: {trans_in}")
    mod_root = os.path.join(TRANS_DIR, mod_name)
    if os.path.exists(mod_root):
        shutil.rmtree(mod_root)
    os.makedirs(mod_root)

    done = miss = 0
    for fn in sorted(os.listdir(OUT_DIR)):
        if not fn.endswith(".i18n.json") or fn.startswith("__ui__"):
            continue
        base = fn[:-len(".i18n.json")]
        src_key = base.replace("__", "/")
        orig = os.path.join(SRC_DIR, src_key.replace("/", os.sep))
        tpath = _match_trans_file(trans_in, base)
        if tpath is None or not os.path.exists(orig):
            print(f"! 缺少译文或源文件: {base}"); miss += 1; continue
        try:
            data = json.load(open(orig, encoding="utf-8-sig"))
            trans = json.load(open(tpath, encoding="utf-8"))
        except Exception as e:
            print(f"! {fn}: {e}"); miss += 1; continue
        kind = _kind_of(src_key)
        dur_map = json.load(open(DUR_MAP, encoding="utf-8")) if os.path.exists(DUR_MAP) else {}
        for path_pat, mode in EXTRACTORS.get(kind, []):
            _restore(data, path_pat.split("."), [], trans, src_key, mode, dur_map)
        outp = os.path.join(mod_root, _ship_path(src_key).replace("/", os.sep))
        os.makedirs(os.path.dirname(outp), exist_ok=True)
        json.dump(data, open(outp, "w", encoding="utf-8"), ensure_ascii=False, indent="\t")
        done += 1
    print(f"回填完成: {done} 个文件 -> {mod_root}  (跳过 {miss})")
    _write_langfont(mod_root)
    _write_readme(mod_root)


def _write_langfont(mod_root):
    """字体映射：把 5 个字体档位全部指向已内嵌的全 CJK 字体，缺了它中文会渲染成空白"""
    d = {"map": [{"key": k, "value": "GoNotoCurrent.ttf"}
                 for k in ["carat", "despair", "krungthep", "pixel", "vcr"]]}
    p = os.path.join(mod_root, "assets", "data", "languageFont.json")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def _ship_path(src_key):
    """仓库路径 -> 游戏安装目录实际路径。
    构建时 assets/preload/ 这层被拍平：assets/preload/data/x -> assets/data/x
    mods/ 下的包路径保持原样。"""
    if src_key.startswith("assets/preload/"):
        return "assets/" + src_key[len("assets/preload/"):]
    return src_key


def _write_readme(mod_root):
    ver = "1.0.0"
    vp = os.path.join(HERE, "VERSION")
    if os.path.exists(vp):
        ver = open(vp, encoding="utf-8").read().strip()
    txt = f"""Flavor Rave 简体中文补丁 v{ver}
================================================

【这是什么】
面向《Flavor Rave》及其全部官方 / 联动 DLC 的简体中文数据补丁。
仅替换文本与少量带字图片、注入三段 Lua 字幕，不改动游戏程序本体。

★ 适用游戏版本：FNF: Flavor Rave V2.5.2 FULLY BREWED!
   补丁的路径与字段结构按该版本校准。若游戏更新到更高版本，
   可能出现文件缺失或结构不一致，请等待对应补丁更新。

★★ 重要声明：本补丁的初版译文由 AI（大语言模型）批量生成，
   之后经过人工校对与 AI 二次修订。译文可能存在语气偏差、
   双关处理不当或漏译，欢迎在项目页提交修订建议。
   本项目与游戏原作者无关，不含任何游戏本体资源。

【安装步骤】
1. 备份：把游戏安装目录整个复制一份（出问题可直接还原）。
2. 覆盖：把本目录内所有文件按相同相对路径覆盖到游戏根目录。
   例如本补丁 assets/data/x.json → 游戏目录的 assets/data/x.json
       本补丁 mods/&lt;DLC名&gt;/... → 游戏目录的 mods/&lt;DLC名&gt;/...
3. 启动游戏，界面与剧情即为中文。

【升级 / 重装（重要）】
· 本补丁按「文件覆盖」方式工作，重新覆盖即可升级，不会影响存档。
· 若你【新安装了某个 DLC】，请在本补丁更新后重新覆盖一次；
  否则新 DLC 的内容会显示英文（补丁里没有它的文件）。
· 覆盖顺序：先装 DLC，再覆盖本补丁。
· 汉化补丁之间不要混装，会互相覆盖 language*.json。

【已覆盖内容】
· 剧情过场对话（37 个文件）：主线、DLC1、联动 DLC、剧情 DLC 全部
· SynSun 电视百科 / 人物档案 / 曲目介绍（78 个文件）
· 结算画面台词（30 个文件，含各角色 S~D 评价）
· Flavorpedia 图鉴（角色 / 地点 / 物品 / 侧栏人物）
· 成就（名称、条件、Showman 台词）、职员表、画廊说明
· 周目定义（周目名 / 章节分组 / 地点名）、曲名（英文（中文）格式）
· UI 语言表 289 项：选项菜单、Modifiers 修改器、暂停菜单、
  主菜单字幕、判定文字、两首带歌词歌曲的实时歌词
· 选项菜单全部条目与每项说明（41 项）
· 图片类：4 张剧情字条（Introtext，人工重绘）
· Lua 中文字幕：saff 电影片头 8 句、Restless 前段歌词 4 句、
  Lodestar Shanty 羊皮纸信件台词 6 句、Home Brew 结束画面

【未覆盖内容（及原因）】
· DLC 下载菜单：列表与文案是运行时从作者服务器拉取的远程 JSON，
  本地无缓存，且该界面字体不含中文字形 —— 需改源码才能汉化
· 歌曲标题卡动画：内容仅为歌名艺术字，属美术风格，未译
· 评分（Sick/Good…）、主菜单 logo、Kablooie 轮盘彩蛋等美术字：
  属界面/美术范畴，未译
· 成就列表中未解锁项显示「未知」：游戏刻意隐藏，非漏译
· 对话中的语气音效：英文短词，保留原音

【译名约定】
· 角色名一律保留英文：Sweet / Sour / Spicy / Smoky / Savory / Umami /
  Salty / Tangy / Bitter / Saffron / Showman / Sun-Dried / Synthetic 等，
  昵称同样保留。
· 地名用中文意译：恩辛克（地区）/ 恩辛克城 / 唐辛子镇 / 新唐辛子 /
  剩饭区 / 薰衣草公园 / 普雷希茨 / 科里安达。
· 双关优先保留笑点：如「我的歌声现在打八折……啊不，是走调（off-key）」。

【常见问题】
Q1 进游戏还是英文？
   确认覆盖到了「游戏根目录」而不是子文件夹；确认 assets/data 层级正确。
   本补丁不含 assets/preload 这一层，若之前放过请删除该残留目录。

Q2 新装 DLC 后新内容变英文？
   正常现象。等待补丁更新后重新覆盖；或先用英文玩，文本不影响存档。

Q3 中文显示为方块 / 空白？
   assets/data/languageFont.json 未正确覆盖。本补丁会把它指向游戏内嵌的
   全 CJK 字体（GoNotoCurrent），请确认该文件已覆盖。

Q4 某句话很奇怪 / 人名被翻译了？
   属 AI 初译残留。欢迎到项目页提交「文件 + 行号 + 建议译法」，
   我们会合入并发布新版本。

Q5 能和别的汉化 / MOD 一起用吗？
   和其它汉化补丁会互相覆盖，不建议混装。
   普通谱面 MOD 一般不冲突；若它也带 language*.json 则以后覆盖者为准。

Q6 会改存档或判定数据吗？
   不会。补丁只替换文本资源与三段 Lua 字幕脚本，不触碰判定、分数与存档。

【回滚】
用备份目录覆盖回去，或删除本补丁覆盖进去的文件即可。

【反馈】
请附：截图 + 所在文件（本补丁同路径）+ 行号/序号，便于定位。
"""
    open(os.path.join(mod_root, "汉化说明.txt"), "w", encoding="utf-8").write(txt)
    _restore_manual(mod_root)


def _restore_manual(mod_root):
    """把手工维护的资源（Lua 脚本、重绘图片等）回填进补丁目录。
    reinject 每次会清空重建 mod_root，因此这些文件必须在此重新拷入。"""
    man_dir = os.path.join(HERE, "manual_files")
    man_list = os.path.join(HERE, "manual_files.txt")
    if not (os.path.isdir(man_dir) and os.path.exists(man_list)):
        return
    n = 0
    for line in open(man_list, encoding="utf-8"):
        rel = line.strip().replace(chr(92), "/")
        if not rel:
            continue
        src = os.path.join(man_dir, rel.replace("/", os.sep))
        if not os.path.exists(src):
            print(f"  [警告] manual_files 缺少: {rel}")
            continue
        dst = os.path.join(mod_root, rel.replace("/", os.sep))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        n += 1
    print(f"手工资源回填: {n} 个文件")


def _kind_of(p):
    for pred, kind in FILE_RULES:
        if pred(p) and not p.startswith("art/"):
            return kind
    return None


def _restore(node, segs, prefix, trans, filekey, mode, dur_map):
    if not segs or not isinstance(node, (dict, list)) or not isinstance(trans, dict):
        return
    head, rest = segs[0], segs[1:]
    if head == "*":
        items = enumerate(node) if isinstance(node, list) else node.items()
        tkeys = trans  # 数字索引以字符串key存
        for i, it in items:
            k = str(i)
            if isinstance(node, list):
                _restore(it, rest, prefix + [k], tkeys.get(k, {}), filekey, mode, dur_map)
            else:
                _restore(it, rest, prefix + [k], tkeys.get(i, {}), filekey, mode, dur_map)
        return
    if isinstance(node, dict) and head in node:
        val = node[head]
        tval = trans.get(head)
        if not rest:
            if tval is None:
                return
            pathkey = filekey + "|" + "/".join(prefix + [head])
            if mode == "subtitle" and isinstance(tval, dict):
                parts = []
                for i in range(len(tval)):
                    txt = tval.get(str(i))
                    if txt is None:
                        break
                    dur = dur_map.get(pathkey + "/" + str(i))
                    seg = dec_plain(txt)
                    parts.append(seg + (f":dur:{dur}" if dur else ""))
                node[head] = "[NL]".join(parts)
            elif isinstance(tval, str):
                node[head] = dec_plain(tval)
        else:
            _restore(val, rest, prefix + [head], tval if isinstance(tval, dict) else {}, filekey, mode, dur_map)


# ---------------- UI 语言表 (languageGameplay/Option/Flavor) ----------------
UI_DIR = os.path.join(os.path.dirname(HERE), "汉化底稿")  # P:/FNF/FR/汉化底稿
UI_CATS = ["Gameplay", "Option", "Flavor"]

def ui_extract():
    """把 UI 底稿 {map:[{key,value}]} 转成 i18next 叶子，放进 AiNiee输入/ui__*"""
    n = 0
    for cat in UI_CATS:
        f = os.path.join(UI_DIR, f"language{cat}-底稿.json")
        if not os.path.exists(f):
            continue
        data = json.load(open(f, encoding="utf-8"))
        sink = {item["key"]: enc_plain(item["value"]) for item in data["map"]}
        out = os.path.join(OUT_DIR, f"__ui__language{cat}.i18n.json")
        json.dump(sink, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        n += len(sink)
    print(f"UI 抽取: {n} 个 key -> {OUT_DIR}/__ui__language*.i18n.json")


def ui_reinject(mod_name="FR_CN_补丁"):
    """从译文目录的 __ui__language*.json 生成补丁内 assets/preload/data/language*.json
    合并策略：以源底稿 key 全集为准，有译文用译文，缺失/空值回落源英文，
    并把未翻译的 key 列出来（AiNiee 对短词会过滤，导致 key 丢失）。"""
    trans_in = _trans_dir()
    mod_root = os.path.join(TRANS_DIR, mod_name, "assets", "data")
    os.makedirs(mod_root, exist_ok=True)
    done = 0
    for cat in UI_CATS:
        srcf = os.path.join(UI_DIR, f"language{cat}-底稿.json")
        if not os.path.exists(srcf):
            continue
        src = {it["key"]: it["value"] for it in json.load(open(srcf, encoding="utf-8"))["map"]}
        tf = _match_trans_file(trans_in, f"__ui__language{cat}")
        trans = json.load(open(tf, encoding="utf-8")) if tf else {}
        rows, missing = [], []
        for k, en in src.items():
            zh = trans.get(k)
            if zh and isinstance(zh, str) and zh.strip() and zh.strip() != en:
                rows.append({"key": k, "value": dec_plain(zh)})
            else:
                rows.append({"key": k, "value": en})
                missing.append(k)
        json.dump({"map": rows}, open(os.path.join(mod_root, f"language{cat}.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        done += len(rows)
        if missing:
            print(f"  UI[{cat}] 回落英文 {len(missing)}/{len(rows)}: {missing[:6]}")
    print(f"UI 回填: {done} 个 key -> {mod_root}/language*.json")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "extract"
    if cmd == "extract":
        extract(); ui_extract()
    elif cmd == "reinject":
        reinject(); ui_reinject()
    elif cmd == "ui":
        ui_extract()
    else:
        print(__doc__)
