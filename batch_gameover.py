# -*- coding: utf-8 -*-
"""gameover（死亡台词）批次：为 characters/gameover/*.json 生成
source_files 底板 + AiNiee输入 骨架 + out 译文 + _dur_map 计时条目。

用法：python batch_gameover.py
之后跑 python pipeline.py reinject
"""
import json, os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
GAME = r"P:\FNF\Flavor.Rave"
SRC = os.path.join(HERE, "source_files")
IN = os.path.join(HERE, "AiNiee输入")
OUT = os.path.join(HERE, "out")
DUR = os.path.join(HERE, "_dur_map.json")

# 译文表：键 = (模组目录名 或 'base', 角色文件名)，值 = 按 goSound 顺序的中文（None 表示留空跳过）
T = {
 ("base","daisy"): ["哦……好惨……", "太可惜了……"],
 ("base","flavorrave"): ["喂，搞什么！？", "这也太蠢了吧！", "拜托！再给一次机会！", "咱们再来一次。", "谢幕……"],
 ("base","nikku"): ["这令人极度不安"],
 ("base","rika"): ["呃……这破信号，全是 bug。", "气氛全被你搞没了。"],
 ("base","savory"): ["空着肚子我可唱不出来……", "我把感觉弄丢了……"],
 ("base","smoky"): ["哼……／还得多练……", "呃……／下次吧。"],
 ("base","sour"): ["喂，搞什么！？", "这也太蠢了吧！"],
 ("base","spicy"): ["喂，呃……什么？", "啊啊，不公平！"],
 ("base","sundried"): ["这也太丢人了", "呜哇呜哇 :("],
 ("base","sweet"): ["拜托！再给一次机会！", "谢幕……"],
 ("base","synthetic"): ["呃……／Sunny……／救一下？", "*错误*／*啦啦*／错啦错啦／*滋啦*／*滋噗 扎噗*／*扎噗 嘶嘟 噗噗*"],
 ("base","togarashi"): ["哼……／还得多练……", "呃……／下次吧。", "喂，呃……什么？", "啊啊，不公平！"],
 ("base","troubleshootin"): ["糟了。", "别慌，我总有条后门留着。"],
 ("base","umami"): ["小事别较真！"],

 ("Archive - Double-Stacked","rhythmrobo"): [
   "Tioda：呜，我的汉堡……／Pyroller：不就是汉堡嘛，别那么认真。",
   "Pyroller：我们大老远跑来就为这个！？／Tioda：那些宣传都是白吹的？"],

 ("DLC1","ace"): ["*叹气* 哈哈……闹着玩嘛，对吧？", "哇！太烫了！"],
 ("DLC1","bitter"): ["街边垃圾……", "少来这套怜悯。"],
 ("DLC1","funkin"): ["你别告诉我这就是你们最强的对手？！／跟上！",
                     "好了你们俩，趁没人发现，我送你们回去。",
                     "开什么玩笑！／*喘气*／叶／呃／什么！？"],
 ("DLC1","salty"): ["呀啊——／海水进我好眼睛了！", "可不能现在丢了水手腿啊。／我就剩一条了。"],
 ("DLC1","tangy"): ["我……讨厌你。", "唱歌见鬼去吧，我要揍你！"],

 ("Official Collab DLC- Lovers Together","cerulean"): [
   "Macy：我以为……高峰期……已经过去了？／Zuki：它来了……高峰期……2。／Macy：还有续集？？？",
   "Zuki：你也看到了……对吧，Mace？／Macy：客人多到爆炸了！／Zuki：……救命。"],
 ("Official Collab DLC- Lovers Together","eclipsin"): [
   "Sekaiya：天亡我也，亲爱的——！／呃。／Luna：噗，哈哈，也没那么糟啦，戏精！",
   "Sekaiya：*倒吸气* 实在太过分了——！／Sekaiya：抱——住——我——！！！哈啊……／Luna：……嗯，要不再来一次。"],
 ("Official Collab DLC- Lovers Together","synsun"): [
   "Sun-Dried：这也太丢人了……",
   "Synthetic：呃……／Synthetic：Sunny……／Synthetic：救一下？"],

 ("Official Collab DLC- Taste of Revenge","bree"): ["我差一点就要把整座城市电成灰了！", "呃呃呃——！／——随便啦！！！"],
 ("Official Collab DLC- Taste of Revenge","tabi"): ["我需要……更多时间计划……", "这场输了，但整场战争我会赢！"],

 ("Official DLC - Chillin' & Thrillin'","onion"): [
   "扫兴。", "如果我的音乐连我自己都听哭了，那说明我做对了，不是吗？", "……／怎么？还在等什么吗？"],
 ("Official DLC - Chillin' & Thrillin'","pure"): [
   "天啊……拜托，就当没看见吧。", "换别人来做肯定好得多……唔……"],

 ("Official DLC - Masters of the Craft","crispy"): [
   "我还没老到那份上吧……？", "伤口上撒盐也没意义了……"],
 ("Official DLC - Masters of the Craft","oil"): [
   "唔……这一路可真够颠的……",
   "*咳 咳* 呃啊——！／我好像把垫片烧穿了……",
   "哇啊啊啊！！！你个——／——开他妈卡车、油老虎、烧柴油、越野摔沟、一堆废铁——！／我……没事。"],

 ("Official DLC - Younger Generation","gummy"): ["呃……这集得重拍！呜哇……", "呕呃呃呃呃……"],
 ("Official DLC - Younger Generation","saff"): [
   "爸————！／叫屏幕后面那些蠢货别再让我丢脸了！",
   "呃，Sour 明明就在旁边，结果你让我显得更丢人了！",
   "呃，什么——呃呃呃！／真的假的？这就是我——／这就是我得到的感谢？／呃，到底怎么回事？这些人都什么毛病？／啊啊啊啊！！呃——！咳——！啊——！呃——！／我气到连话都说不出来了。／不行，说不出话——！啊，呃——！／呃啊呜哇啦吧啦呼噜噜——／啊啊啊！！！"],
}


def flat(src_key):
    return src_key.replace("/", "__")


def main():
    files = []
    for f in sorted(os.listdir(os.path.join(GAME, "assets", "characters", "gameover"))):
        if f.endswith(".json"):
            files.append(("base", "assets/characters/gameover/" + f,
                          os.path.join(GAME, "assets", "characters", "gameover", f)))
    for mod in sorted(os.listdir(os.path.join(GAME, "mods"))):
        d = os.path.join(GAME, "mods", mod, "characters", "gameover")
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith(".json"):
                files.append((mod, f"mods/{mod}/characters/gameover/{f}", os.path.join(d, f)))

    dur = json.load(open(DUR, encoding="utf-8")) if os.path.exists(DUR) else {}
    n_files = n_lines = 0
    missing = []
    bad = []
    for mod, src_key, p in files:
        char = os.path.splitext(os.path.basename(p))[0]
        data = json.load(open(p, encoding="utf-8-sig"))
        gs = data.get("goSound") or []
        if not gs:
            continue
        # 底板
        sp = os.path.join(SRC, src_key.replace("/", os.sep))
        os.makedirs(os.path.dirname(sp), exist_ok=True)
        shutil.copy2(p, sp)
        # 骨架
        skel = {"goSound": {str(i): {"subtitles": {"0": ""}} for i in range(len(gs))}}
        ip = os.path.join(IN, flat(src_key) + ".i18n.json")
        json.dump(skel, open(ip, "w", encoding="utf-8"), ensure_ascii=False, indent="\t")
        # 译文
        zh = T.get((mod, char))
        out = {"goSound": {}}
        for i, g in enumerate(gs):
            sub = g.get("subtitles", "")
            segs = sub.split("[NL]")
            durs = []
            for seg in segs:
                m = re.search(r":dur:([0-9.]+)$", seg)
                durs.append(m.group(1) if m else None)
            line_zh = zh[i] if zh and i < len(zh) and zh[i] else None
            if line_zh:
                chunks = line_zh.split("／")
                if len(chunks) != len(segs):
                    bad.append(f"{mod}/{char}#{i}: 中文 {len(chunks)} 段 vs 原文 {len(segs)} 段")
                    chunks = chunks + [""] * (len(segs) - len(chunks))
                    chunks = chunks[:len(segs)]
            else:
                chunks = [re.sub(r":dur:[0-9.]+$", "", x) for x in segs]
            subdict = {}
            for j, txt in enumerate(chunks):
                subdict[str(j)] = txt
                if durs[j]:
                    dur[f"{src_key}|goSound/{i}/subtitles/{j}"] = float(durs[j])
                if txt.strip():
                    n_lines += 1
            out["goSound"][str(i)] = {"subtitles": subdict}
        if zh is None and any((g.get("subtitles") or "").strip() for g in gs):
            missing.append(f"{mod}/{char}")
        op = os.path.join(OUT, flat(src_key) + ".i18n_translated.json")
        json.dump(out, open(op, "w", encoding="utf-8"), ensure_ascii=False, indent="\t")
        n_files += 1

    json.dump(dur, open(DUR, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"生成 {n_files} 个文件 / {n_lines} 句译文 / dur 条目 {len(dur)}")
    if missing:
        print("⚠ 未提供译文（保留英文）:", ", ".join(missing))
    if bad:
        print("⚠ 分句数不匹配（已截断/补空）:")
        for b in bad:
            print("   ", b)


if __name__ == "__main__":
    main()
