# -*- coding: utf-8 -*-
"""DLC: Official Collab DLC- Lovers Together 全量汉化"""
import json, os, shutil

MOD = "Official Collab DLC- Lovers Together"
GAME = r"P:\FNF\Flavor.Rave"
HERE = os.path.dirname(os.path.abspath(__file__))

HOME = [
 "我们已经走了好久了，Sunny。还在恩辛克吗？我现在没网，没法查。",
 "哦，其实我们压根儿不在恩辛克了！我在网上看到这座城市里有家小店，想着咱俩一起去会很有意思。",
 "「咱俩」这说法我爱听，嘿。那儿有像唐辛子镇那样的甜甜街机厅吗？噢，要不然有电竞馆！",
 "听起来挺好玩，不过其实我们要去的是家咖啡馆。",
 "咖啡馆？不是我抬杠啊 Sunny，可我是台机器，所以……我……你懂的。",
 "这家咖啡馆跟咱们路过那些有啥不一样？是那种网咖吗？还是说要跟人碰头？说嘛 Sunny！到底啥情况？",
 "嘿，严格来说也能叫它「赛博」咖啡馆，只是不是你想的那个意思。这家店是机器人开的！还是超高档的那种！",
 "好家伙，这下我可来劲了！快带我去见见这位高级咖啡机器人！",
 "[咖啡馆内……]",
 "刚看了下手机。天呐 Zuki，现在所有人都在问我另一颗痣在哪儿……",
 "对不起对不起！我就是觉得，你知道的，这点小八卦多好玩啊，嘿嘿嘿——",
 "我没那么生气啦，但这属于私事，只告诉你一个人。不过你要是请我一杯大杯拿铁，我倒是可以考虑原谅你~",
 "好嘛 Mace，就算你不说我也照做，嘿。",
 "早上好呀各位！我们是来见识你们那台了不起的机器做的咖啡的！",
 "……",
 "……Sunny，咱们来对地方了吗？这看着就是家很普通的咖啡馆啊。要不问问那位咖啡师女士，酷咖啡机器人在哪儿？",
 "咖啡机器人……？Mace，那台像电脑一样的东西是在说我吗……？",
 "她是有名字的，小方块。她叫 Zuki。",
 "等等，那……哦！我的天！她是台机器！Sunny，你看！我现在看见了！一台完全人形的机器人，就大摇大摆站在公众场合！",
 "Syn——！真是太抱歉了，他就是……对新事物特别来劲。",
 "不过话说回来……我的天，你、你好！我也没想到……啊……我有点不好意思。",
 "很高兴见到你。我的外表很奇怪吗？",
 "不、不是……其实你非常漂亮。我只是更习惯像……嗯，像我身边这位这样的机器。",
 "她真的是最可爱的存在。那张脸就是为惊艳全场而生的。每次看到都让我惊艳，嘿嘿。",
 "啊，你们俩嘴真甜。小姐，需要来点什么吗？",
 "我还没想好……得先看看菜单。",
 "你最好快点决定。Zuki，你知道快到什么时间了吧。",
 "高峰期……一到那个点就总是忙得不可开交。",
 "唉，我还想问你所有关于成为真正人形机器人的事呢！像我这种没有四肢的机器，太渴望答案了……",
 "如果你们不介意等高峰期过去，之后会变得很清静。到时候我不介意多聊聊我自己。",
 "当然！我不介意！",
 "等待的时候也可以随便问我。那台萌机器人我可是熟得不能再熟了。",
]

STAR = [
 "慢点啦宝贝！你找的约会地点也不是每一个都得跑着去啊！",
 "这个重要！最最最重要的那种。大概……排名前三的重要地点！信我！",
 "我信！你老说要带我去所有地方，那这个肯定是榜首咯？",
 "没错！这里就是咱们能到的、最「全方位」的地方！你看你看！",
 "当当！",
 "哇哦，凉亭。挺好。",
 "……",
 "……就这？",
 "你感觉不到吗，Lu？感觉不到那种「全方位」吗？",
 "恕我没感觉到。",
 "好吧，那么！！！这可不是普通的凉亭——凝视亭——随便你怎么叫它啦！它简直在往外渗出异世界的能量！就像……一座地标。",
 "我妈以前跟我讲过一个诗啊歌啊故事之类的东西，说的就是这座庆典场地连接的世界。咳嗯……",
 "「很久以前，有两位歌之精灵。一位甜，一位酸，他们整日争斗不休。」",
 "「直到某个夜晚，有人逼着他们同台。合奏一曲，仇恨便散去了。从宿敌成了恋人，如同昼与夜。他们的音乐响亮，带来欢乐与喜悦。」",
 "「时光流转，两位早已远去，他们的歌声仍在传唱，他们的爱仍在延续。所以据说，只要你仔细聆听——在月亮能与太阳相遇、不再为敌的时刻……」",
 "「你会听见他们仍在歌唱，把故事重新唱起；也许有一天，他们也会听见你。」",
 "我、呃……信息量好大，嘿嘿。不过……是那种很酷的「大」。",
 "咱们的朋友都在这儿，那他们肯定对这块「地标」知道点什么。",
 "对对！只要我们把这儿搞得够热闹，就能听见另一个世界的声音！",
 "那你打算怎么弄，宝贝？照老规矩来？又唱又跳？",
 "那当然啦，我的 Luey-Loo！这事儿简单得很，小菜一碟！",
 "[与此同时，在另一个世界……]",
 "嚯，凉亭。不错。",
 "这地方算是我们这儿最接近薰衣草公园的一处了。去那儿对我意义重大，所以我……真的很想在这儿也找到一处那样的地方。一个我们也能一起唱歌的地方。",
 "这我懂。这地方感觉正合适。",
 "我听说这地方很特别。没人知道是谁建的……而且在特殊的时刻，人们能听见庆典的声音。",
 "可一旦有人靠近，声音就消失了。只有一个人声称亲眼见过这里发生的事。那人形容说，就像踏入了另一个世界！",
 "我的好奇心简直要飞到天上去了！嘿嘿！所以……我知道我必须带你来。说不定我们运气好，能亲眼见到。",
 "你还真是找「最异世界」地点的冠军啊。跟你做什么我都乐意，Sweet。再多这一件一起探索的疯狂事又何妨？",
 "嘿宝贝，你听见什么了吗？",
 "听见了！人声！已经生效了，Lu！",
 "喂——！哟呼——！",
 "呃，喂？外面有人吗？",
 "我现在也有感觉了。是天黑了吗，还是白天？",
 "月亮变得越来越亮了！抓住我的手，Sour！我觉得就是现在！",
]

CREDITS = [
 "作曲：HighPoweredKeyz 与 K-Man\n混音：Starbreak 与 Faceless",
 "过场曲目\n作曲：SkyHighProductions",
 "作曲：SkyHighProductions 与 HighPoweredKeyz",
 "背景画师",
 "暂停菜单画师",
 "作曲家",
 "Macy 配音",
 "Kazuki 配音",
 "Sekaiya 配音",
 "Luna 配音",
 "Cerulean Symphony\n（ItIsIWeeg、K-Man、Cerulean Symphony 团队）",
 "Friday Night Eclipsin'\n（SkyHighProductions、MrArtz、Eclipsin' 团队）",
]

CERU_TEXT = (
 "在 Ringola 有一家小巧别致的咖啡店，名叫 The Cerulean，由一对奇特的伴侣经营。"
 "穿绿衣的女孩是 Mackenzie，不过大多数人只知道她的昵称 Macy。她是个业余词曲作者，对咖啡因有着极强的执念，"
 "常在网上发布自己的作品，也不断寻找合作者。\n\n"
 "穿蓝衣的机器人是 Kazuki，多数人也只叫她的昵称 Zuki。虽然她如今在经营这家咖啡馆，"
 "但她最初被制造出来的目的是成为世界上第一台完全自主的偶像机器人。对音乐的热爱仍深深嵌在她的程序里，"
 "而有了 Macy 在身边，她们把这间 The Cerulean 变成了城中一处热闹的小角落。"
)
ECLI_TEXT = (
 "她们的故事属于恶魔与天使。Sekaiya DelFuego 是半人类、半魅魔，可她并不理会魅魔的常规职责，"
 "比起一时的欲望，她更痴迷于真爱与长久关系的理念。Sekaiya 爱上了 Luna Amchou——一位来自地球本土的半人类、半天使女性；"
 "在 Sekaiya 把她的世界彻底翻过来之前，Luna 一直以为自己只是个普通人。一个活泼冒失，一个低调随性。\n\n"
 "Sekaiya 与 Luna 是形影不离、彼此互补的一对。在这个超自然势力彼此倾轧的世界里，"
 "她们的爱让两人始终相连、保持平衡，如同一轮炽热的太阳与一轮安宁的月亮。"
)

RESULTS = {
 "cerulean": {
  1: "我现在咖啡因上头还没退！Zuki，咱们去吃晚饭吧！然后去看电影！再然后，一起过夜、抱抱，明天再来一遍！",
  2: "真是太棒了！啊……真让我想起当偶像的那些日子……",
  3: "今天玩得真开心！下周同一时间再来？",
  4: "我可能有点生疏了……不、不过只是唱歌生疏！不过你也可以顺便检查检查我身上还有没有别的地方生锈，Mace？嘿嘿……",
  5: "Zuki……咖啡……现在就要……我整首歌都快撑不住了……！",
 },
 "eclipsin": {
  1: "哇哦哦哦——！不管是天堂、地狱，还是跨次元的旅——程，都比不上我们的日蚀！",
  2: "我从不知道这座凉亭这么重要。能尽情释放、还能见识我们世界之外的新天地，真是无比愉快。",
  3: "耶——！我们做到了！我们熬过了那场跨次元的、稀奇古怪的太空玩意儿！不过那两位到底是谁啊？",
  4: "呼，我快喘不上气了，嘿。算不上我们最棒的合声，但总算撑过来了！真好奇这凉亭还藏着什么秘密。",
  5: "呃啊……我头好晕。大概在第 45 秒左右我就迷路了。这地方对我来说可能太刺激了，我得躺一下——",
 },
 "synsun": {
  1: "哦，这局咱们稳了，Sunny！整个恩辛克没人比咱们更同步！",
  2: "呜呼！我真的开始觉得这事有多好玩了！",
  3: "对我这种一盒字节来说已经不错了。你也干得漂亮，Sunny！",
  4: "我不能再通宵了……早上的精气神全没了。",
  5: "呃，等等……我的缓存满了……没剩多少空间留给好好唱歌了……",
 },
}


def add(rel, zh, en):
    gp = os.path.join(GAME, "mods", MOD, rel.replace("/", os.sep))
    src = os.path.join(HERE, "source_files", "mods", MOD, rel.replace("/", os.sep))
    os.makedirs(os.path.dirname(src), exist_ok=True)
    shutil.copy2(gp, src)
    base = ("mods/" + MOD + "/" + rel).replace("/", "__")
    json.dump(en, open(os.path.join(HERE, "AiNiee输入", base + ".i18n.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump(zh, open(os.path.join(HERE, "out", base + ".i18n_translated.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("  +", rel)


def dialogue(rel, texts):
    gp = os.path.join(GAME, "mods", MOD, rel.replace("/", os.sep))
    raw = json.load(open(gp, encoding="utf-8-sig"))
    items = raw.get("dialogue", [])
    assert len(items) == len(texts), f"{rel}: {len(items)} vs {len(texts)}"
    en = {"dialogue": {str(i): {"text": it.get("text", "")} for i, it in enumerate(items)}}
    zh = {"dialogue": {str(i): {"text": texts[i]} for i in range(len(texts))}}
    add(rel, zh, en)


print("Lovers Together:")
dialogue("data/home-brew/dreamcast.json", HOME)
dialogue("data/starburst-special/dreamcast.json", STAR)

# 成就
add("data/achievements.json",
    {"achievements": {
        "0": {"fancyName": "我们 Tomodachi", "unlockCondition": "在《Home Brew》中达成全连",
              "showmanDialogue": "你可能以为我喜欢那种精心冲泡、花里胡哨的咖啡，可我其实就爱一杯朴素的好咖啡。"
                                 "那台手动磨豆机我用了四十年，到现在还好使得很！"},
        "1": {"fancyName": "相反相吸", "unlockCondition": "在《Starburst Special》中达成全连",
              "showmanDialogue": "虽说我不信童话和那些古老的奇幻摇篮曲，但它们给一场活动添的神秘感是无可否认的！"
                                 "也许等下次日蚀来的时候，我该在自己的展厅安排个时段，看看会发生什么……"}}},
    {"achievements": {str(i): {"fancyName": a.get("fancyName", ""), "unlockCondition": a.get("unlockCondition", ""),
                               "showmanDialogue": a.get("showmanDialogue", "")}
                      for i, a in enumerate(json.load(open(os.path.join(GAME, "mods", MOD, "data/achievements.json"),
                                                            encoding="utf-8-sig"))["achievements"])}})

# 画廊
cg = json.load(open(os.path.join(GAME, "mods", MOD, "data/galleryCGData.json"), encoding="utf-8-sig"))["artwork"]
add("data/galleryCGData.json",
    {"artwork": {str(i): {"caption": a["caption"].replace("CGs - ", "CG图 - ")} for i, a in enumerate(cg)}},
    {"artwork": {str(i): {"caption": a["caption"]} for i, a in enumerate(cg)}})

gd = json.load(open(os.path.join(GAME, "mods", MOD, "data/galleryData.json"), encoding="utf-8-sig"))["artwork"]
GD_ZH = {"eclipsesour": "LOVERS DLC - 蚀化 Sour 概念图", "eclipsesweet": "LOVERS DLC - 蚀化 Sweet 概念图"}
add("data/galleryData.json",
    {"artwork": {str(i): {"caption": GD_ZH.get(a["image"], a["caption"])} for i, a in enumerate(gd)}},
    {"artwork": {str(i): {"caption": a["caption"]} for i, a in enumerate(gd)}})

# 职员表
peeps = json.load(open(os.path.join(GAME, "mods", MOD, "data/creditsData.json"), encoding="utf-8-sig"))["peeps"]
add("data/creditsData.json",
    {"peeps": {str(i): {"description": CREDITS[i]} for i in range(len(peeps))}},
    {"peeps": {str(i): {"description": p.get("description", "")} for i, p in enumerate(peeps)}})

# 周目
add("weeks/xcollab_cerulean.json",
    {"weekName": "高峰期", "storyName": "联动故事", "location": "蔚蓝咖啡馆"},
    {"weekName": "Rush Hour", "storyName": "Collab Stories", "location": "The Cerulean"})
add("weeks/xcollab_eclipsin.json",
    {"weekName": "日月追逐", "storyName": "联动故事", "location": "落日庆典凉亭"},
    {"weekName": "Sun Chase Moon", "storyName": "Collab Stories", "location": "Sunset Fest Pavillion"})

# 曲名
add("data/home-brew/meta.json", {"song": {"name": "Home Brew（家酿）"}}, {"song": {"name": "Home Brew"}})
add("data/starburst-special/meta.json", {"song": {"name": "Starburst Special（星爆特调）"}},
    {"song": {"name": "Starburst Special"}})

# 图鉴正文
add("data/flavorpediaData.json",
    {"character": {"0": {"flavorText": CERU_TEXT, "subtitles": "Zuki：来喽！:dur:1.09[NL]Macy：Mace 闪亮登场！:dur:1.85"},
                   "1": {"flavorText": ECLI_TEXT, "subtitles": "Sekaiya：让我上！:dur:1.16[NL]Luna：好啦好啦。:dur:1.01"}}},
    {"character": {"0": {"flavorText": json.load(open(os.path.join(GAME, "mods", MOD, "data/flavorpediaData.json"),
                                                      encoding="utf-8-sig"))["character"][0].get("flavorText", ""),
                         "subtitles": "Zuki: Order up!:dur:1.09[NL]Macy: Mace in your face!:dur:1.85"},
                   "1": {"flavorText": "", "subtitles": "Sekaiya: Let me at 'em!:dur:1.16[NL]Luna: Sure, sure.:dur:1.01"}}})

# 侧栏
side = json.load(open(os.path.join(GAME, "mods", MOD, "data/flavorpediaSideData.json"), encoding="utf-8-sig"))["character"]
def side_zh(c):
    place = "蔚蓝咖啡馆" if c.get("place") == "The Cerulean" else "落日庆典凉亭"
    desc = c.get("desc", "")
    if desc.startswith("A cafe patron"):
        desc_zh = "高峰期人群中的咖啡店顾客！"
    elif desc.startswith("A friend"):
        desc_zh = "在凉亭里悠闲待着的朋友！"
    elif desc.startswith("A strange visitor"):
        desc_zh = "夜里神秘现身的奇怪访客！"
    else:
        desc_zh = desc
    design = c.get("design", "")
    dmap = {"Team TBD Dev": "Team TBD 开发者", "Team TBD Dev OC": "Team TBD 开发者原创角色",
            "Developer Mutual OC": "开发者联动原创角色", "Unknown Origin": "来历不明"}
    return {"design": dmap.get(design, design), "desc": desc_zh, "place": place}

add("data/flavorpediaSideData.json",
    {"character": {str(i): side_zh(c) for i, c in enumerate(side)}},
    {"character": {str(i): {k: c.get(k, "") for k in ("design", "desc", "place")} for i, c in enumerate(side)}})

# 结算台词
for name, mapping in RESULTS.items():
    rel = f"images/results/character/{name}/dialogue.json"
    gp = os.path.join(GAME, "mods", MOD, rel.replace("/", os.sep))
    d = json.load(open(gp, encoding="utf-8-sig"))["dialogue"]
    ranks = [it.get("rank") for it in d]
    texts = []
    for idx, r in enumerate(ranks):
        if r == "...":
            texts.append("...")
        else:
            # rank 顺序 S,A,B,C,D
            order = {"S": 1, "A": 2, "B": 3, "C": 4, "D": 5}
            texts.append(mapping.get(order.get(r, 0), it if False else d[idx].get("name", "")))
    add(rel, {"dialogue": {str(i): {"name": texts[i]} for i in range(len(texts))}},
        {"dialogue": {str(i): {"name": it.get("name", "")} for i, it in enumerate(d)}})

print("完成")
