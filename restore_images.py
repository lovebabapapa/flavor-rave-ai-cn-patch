# -*- coding: utf-8 -*-
"""
把人工修好的帧图还原回 sprite atlas 并写入补丁目录。
用法:
  python restore_images.py            # 只还原「汉化素材_图片_修改后」里改过的帧
  python restore_images.py --sync     # 还原后自动同步补丁到游戏目录
约定:
  修改后的 PNG 放在  汉化素材_图片_修改后/<与提取时相同的子文件夹>/<同名>.png
  只放改过的帧即可，未修改的帧保持原样。
"""
from PIL import Image
import xml.etree.ElementTree as ET
import os, shutil, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
GAME = r"P:\FNF\Flavor.Rave"
PATCH = os.path.join(HERE, "汉化输出", "FR_CN_补丁")
SRC_DIR = os.path.join(HERE, "汉化素材_图片")
EDIT_DIR = os.path.join(HERE, "汉化素材_图片_修改后")

ATLAS = {  # 提取子目录 -> (图集 png 不带扩展名, patch 内目标路径)
 "titlecard_Ignatius":        (r"assets\tbd\images\titlecard\Ignatius",
                               r"assets\tbd\images\titlecard\Ignatius.png"),
 "titlecard_Restless":        (r"mods\Official DLC - Chillin' & Thrillin'\images\titlecard\Restless",
                               r"mods\Official DLC - Chillin' & Thrillin'\images\titlecard\Restless.png"),
 "titlecard_saff":            (r"mods\Official DLC - Younger Generation\images\titlecard\saff",
                               r"mods\Official DLC - Younger Generation\images\titlecard\saff.png"),
 "titlecard_Lodestar_Shanty": (r"mods\DLC1\images\titlecard\Lodestar Shanty",
                               r"mods\DLC1\images\titlecard\Lodestar Shanty.png"),
 "titlecard_Home_Brew":       (r"mods\Official Collab DLC- Lovers Together\images\titlecard\Home Brew",
                               r"mods\Official Collab DLC- Lovers Together\images\titlecard\Home Brew.png"),
 "SaffIntro":                 (r"mods\Official DLC - Younger Generation\images\stages\greenhouse\intro\SaffIntro",
                               r"mods\Official DLC - Younger Generation\images\stages\greenhouse\intro\SaffIntro.png"),
 "Restless_introtext":        (r"mods\Official DLC - Chillin' & Thrillin'\images\stages\brandy\introtext",
                               r"mods\Official DLC - Chillin' & Thrillin'\images\stages\brandy\introtext.png"),
 "Restless_midsongtext":      (r"mods\Official DLC - Chillin' & Thrillin'\images\stages\brandy\midsongtext",
                               r"mods\Official DLC - Chillin' & Thrillin'\images\stages\brandy\midsongtext.png"),
}
STRIPS = {  # 独立字条 -> patch 内目标路径
 "introtext1.png": r"assets\tbd\images\togarashi\introtext1.png",
 "introtext2.png": r"assets\tbd\images\togarashi\introtext2.png",
 "introtext3.png": r"assets\tbd\images\togarashi\introtext3.png",
 "introtext4.png": r"assets\tbd\images\togarashi\introtext4.png",
}


def restore():
    if not os.path.isdir(EDIT_DIR):
        print(f"未找到修改目录: {EDIT_DIR}\n把修好的图按原目录结构放进去后再运行。")
        return 0
    applied = 0
    for sub, (base, dest_rel) in ATLAS.items():
        edir = os.path.join(EDIT_DIR, sub)
        if not os.path.isdir(edir):
            continue
        edited = glob.glob(os.path.join(edir, "*.png"))
        if not edited:
            continue
        # 以游戏目录的原始图集为底
        atlas = Image.open(os.path.join(GAME, base + ".png")).convert("RGBA")
        xmlp = os.path.join(GAME, base + ".xml")
        root = ET.parse(xmlp).getroot()
        coord = {s.get("name"): (int(s.get("x")), int(s.get("y")),
                                 int(s.get("width")), int(s.get("height")))
                 for s in root.iter("SubTexture")}
        for fp in edited:
            nm = os.path.splitext(os.path.basename(fp))[0]
            if nm not in coord:
                print(f"  [跳过] {sub}/{nm}: 在 xml 中找不到该帧名")
                continue
            x, y, w, h = coord[nm]
            im = Image.open(fp).convert("RGBA")
            if im.size != (w, h):
                print(f"  [警告] {sub}/{nm}: 尺寸 {im.size} != 原 {w}x{h}，已强制缩放")
                im = im.resize((w, h))
            atlas.paste(im, (x, y))
            applied += 1
        # 写入补丁（png + 原始 xml 一起，保证 mod 目录完整）
        dest_png = os.path.join(PATCH, dest_rel.replace("\\", os.sep))
        os.makedirs(os.path.dirname(dest_png), exist_ok=True)
        atlas.save(dest_png)
        shutil.copy2(xmlp, os.path.join(PATCH, dest_rel.replace("\\", os.sep)).replace(".png", ".xml"))
        print(f"  图集已回填: {dest_rel}  (本组 {len(edited)} 帧修改)")
    # 独立字条
    strip_dir = os.path.join(EDIT_DIR, "剧情字条_introtext")
    if os.path.isdir(strip_dir):
        for fp in glob.glob(os.path.join(strip_dir, "*.png")):
            fn = os.path.basename(fp)
            if fn in STRIPS:
                dest = os.path.join(PATCH, STRIPS[fn].replace("\\", os.sep))
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy2(fp, dest)
                applied += 1
                print(f"  字条已回填: {fn}")
    print(f"共回填 {applied} 张")
    return applied


if __name__ == "__main__":
    restore()
    if "--sync" in sys.argv:
        n = 0
        for r, _, fs in os.walk(PATCH):
            for f in fs:
                s = os.path.join(r, f)
                rel = os.path.relpath(s, PATCH).replace(os.sep, "/")
                if rel == "汉化说明.txt":
                    continue
                d = os.path.join(GAME, rel.replace("/", os.sep))
                os.makedirs(os.path.dirname(d), exist_ok=True)
                shutil.copy2(s, d)
                n += 1
        print(f"已同步 {n} 个文件到游戏目录")
