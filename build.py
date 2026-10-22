#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""发布打包：校验手工资源 → 统计 → 生成 zip + sha256

用法:
    python build.py            # 只打包
    python build.py --sync     # 打包后同步到游戏目录（本地自测用）
"""
import os, sys, json, zipfile, hashlib, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
PATCH = os.path.join(HERE, "汉化输出", "FR_CN_补丁")
OUTDIR = os.path.join(HERE, "汉化输出")
GAME = r"P:\FNF\Flavor.Rave"


def version():
    p = os.path.join(HERE, "VERSION")
    if os.path.exists(p):
        return open(p, encoding="utf-8").read().strip()
    return "0.0.0"


def check_manual():
    lst = os.path.join(HERE, "manual_files.txt")
    if not os.path.exists(lst):
        return []
    miss = []
    for line in open(lst, encoding="utf-8"):
        rel = line.strip()
        if rel and not os.path.exists(os.path.join(PATCH, rel.replace("/", os.sep))):
            miss.append(rel)
    return miss


def stats():
    n_json = n_lua = n_png = 0
    entries = 0
    for r, _, fs in os.walk(PATCH):
        for f in fs:
            if f.endswith(".json"):
                n_json += 1
                try:
                    d = json.load(open(os.path.join(r, f), encoding="utf-8"))
                except Exception:
                    continue
                if isinstance(d, dict):
                    if "dialogue" in d:
                        entries += len(d["dialogue"])
                    else:
                        for k in ("character", "place", "things", "artwork", "peeps", "achievements"):
                            entries += len(d.get(k, []))
            elif f.endswith(".lua"):
                n_lua += 1
            elif f.endswith(".png"):
                n_png += 1
    total = sum(len(fs) for _, _, fs in os.walk(PATCH))
    return total, n_json, n_lua, n_png, entries


def main():
    ver = version()
    if not os.path.isdir(PATCH):
        raise SystemExit("补丁目录不存在，请先运行: python pipeline.py reinject")
    miss = check_manual()
    if miss:
        print("❌ manual_files 缺失，先运行 reinject 或补齐文件：")
        for m in miss:
            print("   -", m)
        raise SystemExit(1)
    total, n_json, n_lua, n_png, entries = stats()
    print(f"版本 {ver} | 文件 {total}（json {n_json} / lua {n_lua} / png {n_png}）| 条目 {entries}")

    zip_path = os.path.join(OUTDIR, f"FR_CN_补丁_v{ver}.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for r, _, fs in os.walk(PATCH):
            for f in fs:
                q = os.path.join(r, f)
                z.write(q, os.path.relpath(q, PATCH))
    size = os.path.getsize(zip_path)
    h = hashlib.sha256(open(zip_path, "rb").read()).hexdigest()
    sha_path = zip_path + ".sha256"
    open(sha_path, "w", encoding="utf-8").write(f"{h}  {os.path.basename(zip_path)}\n")
    print(f"✅ {zip_path}  ({size/1024:.0f} KB)")
    print(f"   sha256: {h}")

    if "--sync" in sys.argv:
        n = 0
        for r, _, fs in os.walk(PATCH):
            for f in fs:
                s = os.path.join(r, f)
                rel = os.path.relpath(s, PATCH).replace(os.sep, "/")
                d = os.path.join(GAME, rel.replace("/", os.sep))
                os.makedirs(os.path.dirname(d), exist_ok=True)
                shutil.copy2(s, d)
                n += 1
        print(f"已同步 {n} 个文件到游戏目录")


if __name__ == "__main__":
    main()
