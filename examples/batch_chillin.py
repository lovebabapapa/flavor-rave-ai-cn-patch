# -*- coding: utf-8 -*-
"""DLC: Official DLC - Chillin' & Thrillin' 全量汉化（含 Restless 实时歌词）"""
import json, os, shutil, glob

MOD = "Official DLC - Chillin' & Thrillin'"
GAME = r"P:\FNF\Flavor.Rave"
HERE = os.path.dirname(os.path.abspath(__file__))

FLOW = [
 "[两年前，恩辛克学院的走廊里……]",
 "[毕业日压在高三年级头顶，而恩辛克学院机器人社仅剩的成员，还要面对更沉重的压力。]",
 "……我不喜欢这种感觉。总觉得时间快不够了，这念头甩不掉。",
 "我不想失去这个地方。除了这里，我不知道还能去哪儿……也不知道还有谁……或者……",
 "[Pure 在机器人社门口停下。]",
 "[她习惯了从旧木门后透出的键盘声与金属摩擦声，所以此刻诡异的安静，只让她脆弱的神经更加动摇。]",
 "……",
 "[她朝窗里张望。从她站的角度看不到任何人，但走近时，她听见了细微的声响。]",
 "[压抑的抽泣声。]",
 "*吸鼻子 吸鼻子*",
 "S、Sunny！怎么了？",
 "Pure……？",
 "是我。我在这儿……你为什么在哭……？",
 "我……做不完。",
 "……？",
 "Syn……我没法把他装起来……",
 "我知道他的代码没问题，可是……硬件就是不配合。他的音频传感器不工作，我搞不清哪根线接哪儿，还缺了几个零件……",
 "[Sun-Dried 低下头，又轻轻哭了起来。]",
 "Sunny……等等，其他人呢？",
 "都病了……两个人都被同班的人传染了流感……要到毕业日才能回来。",
 "我以为……你也病了，所以……我就想自己把 Syn 完成。可、可是……",
 "我没事，Sunny。我该早点跟你说的。要是我早知道你一个人扛着这些……我会……*叹气*",
 "[Pure 坐下来陪在朋友身边，安静地陪她把眼泪流完。]",
 "好了……让我看看……我想我能帮忙理清楚。我把我们的笔记调出来，你把 Syn 启动到调试模式，行吗？",
 "嗯嗯，这个我能做。",
 "嗯……哦！这也许比我们想的简单。装配我来，排查你来。",
 "好、好的……好！我们能做到。",
]

REST = [
 "所以，她就在这儿打工？嗯，跟我猜的差不多。",
 "而这真是一处神圣的庇护所啊！~ 角落里一处幽暗的壁龛，秘密在那里避开不配窥视者的目光~",
 "这就是家俗气的 emo 小孩店，不是什么他妈的巫师小屋。我妹妹就在这儿买东西。",
 "相信我。~ 外壳只会欺骗那些没有眼睛、看不见底下藏着什么秘密的人。进来吧，你会找到你要的答案~",
 "行吧行吧。随你。只是求你别再用那种腔调说话。",
 "欢迎光临 Brandy's……今天所有乐队 T 恤买二送一……在我们网站用优惠码「GREEN」，所有 Atherium 周边五折……我叫……*打哈欠*",
 "你不用把整套词儿念完。",
 "谢天谢地。",
 "我不是来买东西的。我想打听一首歌。我朋友说你是……「禁忌」音乐方面的专家？管它是什么意思……",
 "我知道很多事。未发表的曲目、泄露的音乐、从地狱深处直接传来的声音……",
 "……噗。行吧。我要找的没那么蠢。",
 "……那就说具体点。",
 "7Spice。我一直听到传闻，说有人找到了一首没发表的歌……还是什么的。网上什么都搜不到。",
 "——！",
 "……你还好吧？请退后一点。",
 "Restless。那是 7Spice 解散以来，唯一一首从一张从未发行的专辑里被找到的歌。",
 "四天前在一个小号上泄露到网上。没人知道是谁干的。一小时内就被删了。没有二次上传出现。",
 "行，不错，这是我这一周来的第一条线索。你听过吗？",
 "我已经把它收进心里了。从头到尾都记住了。",
 "每一句词、每一个和弦、每一下打击。那是一个明显濒临崩溃的乐队，愤怒、溃烂般的怒火……有力。痛苦。真实。",
 "你赶在被删之前把它下下来了？",
 "嗯，是啊……",
 "那不就得了！那就重新上传啊！",
 "不。",
 "为什么不？你就打算把这份失传的东西压着？你有毛病吧？！",
 "这首歌本来就不该被公众消费。如果你没法自己深入底层找出它的秘密，那你就不配当它的听众。",
 "我大老远跑来就是为了了解它。这还不够吗？",
 "也许吧……我不能把这首歌的数据交给你，因为我无法保证它的神圣性会被你好好守住……所以……",
 "就让我亲自引导乐队的动荡……现在就演奏给你听。仔细听。这将是你第一次、也是最后一次听到这样的秘密旋律。",
]

ONION_TV = [
 "哇哦，那发型才叫一个绝。每天早上光弄那个就得花掉大半个早晨吧……而且还有那一整套妆！",
 "那是 Ensemble 购物中心哥特服饰店的头号收银员。她和那地方的调性简直完美契合。",
 "哦对！Brandy's！就是那家你不敢进去的店！",
 "嘿！我才不是不敢进去！我只是……被他们卖的那些衣服和玩意儿吓到了……比如……那些东西穿在我身上会好看吗？还是……会……",
 "我以前也去过几次，就为了在我 7Spice 时期买点乐队海报。那之后就没怎么有理由再去了……",
 "这位 Onion 说不定就是个再去一趟的好理由。我刚查了下她，听起来她是小众音乐的宗师。",
 "那种你只在快倒闭的老式小唱片店后堆着的、没有标签的旧磁带上才找得到的音乐。",
 "那种就算我在网上翻上好几天也找不到的、没有记录的东西。真正的禁忌货。",
 "听起来挺有意思，不过我的音乐口味没那么冷门。",
 "拓展口味永远不嫌晚！Onion 很可能给你推点改变人生的东西！",
 "或者更妙——推点冷到你会庆幸它一直被禁的东西！这样你反而更能珍惜自己真正喜欢的音乐！哈哈哈！",
 "另外我听说她说话挺逗的。我喜欢逗的人。下次我们逛商场的时候让我跟她聊聊吧，求你了？",
 "也许吧……但前提是我在那儿真能找到想买的东西！希望她在这方面也能给点好建议。",
 "说不定她能成为你一直在找的化妆搭子！毕竟我这方面帮不上你。没手之类的。",
]

PURE_TV = [
 "Pure？！",
 "那个名字我永远不会忘！她在哪儿？她在直播间吗？",
 "我、我想没有，可、可是！有人在聊天室里提到了她，那肯定有人知道她在哪儿！",
 "我的天……我好想她……",
 "我们俩都很想她。我们偶尔试着给她打电话，都没人接……她也不在社交媒体上。",
 "我们从恩辛克学院毕业后，她跟着家人搬离了这个国家。她一直没机会告诉我搬去了哪儿……那之后也没什么消息……",
 "不管她在哪儿，我希望她在自己觉得舒服的地方。我实在不相信她会无缘无故突然断联，所以也许只是搬家的事一直耽误了她……",
 "是啊……可是……她搬走都两年了。一条短信、一个电话，或者……随便什么都好啊。",
 "我不舒服的时候她一直陪着我……所以如果她最近过得艰难，我也希望能陪在她身边。",
 "她……她现在是不是讨厌我了……？",
 "嘿，嘿，她绝不会的，Sunny！她有点善变，但我们在她心里很重要。我知道的。",
 "她特别喜欢待在社办里，和你们一起把我装起来，总是很擅长解决技术问题。",
 "嘿……甚至连把我带去毕业典礼都是她的主意。她还给了我一副备用的学士帽。",
 "哦！还记得有个社团成员想让我恶作剧全场——抢过麦克风，假装威胁说要搞一场机器人暴动吗？",
 "你们俩当时慌得不行，可事后我们一起想到那事笑得多开心，那种感觉很特别。",
 "我虽然只是台机器……但连我都能看出来，那样的日子不会那么轻易从心里离开。",
 "就像电脑数据永远不会真正被清空，哪怕你把它全丢进回收站。我知道她还在想着我们，用她的脑子，或者……",
 "毕业典礼依然是我人生中最快乐的时刻……*吸鼻子*",
 "呃——我不想在直播里太情绪化。不过……也许如果 Pure 看到这个……我只能希望她会再联系我们。",
 "你要是再让我们等下去，我可真要难过了，姑娘！",
 "当然是开玩笑的，不过……你知道的……你也是我最好的朋友之一，Pure。我们想你。",
]

LYRICS = {
 1: "仇恨生自如此古老的地方……",
 2: "被枷锁锁住，我等得已经累了……",
 3: "等你亲口说，我……",
 4: "……够了。",
 5: "我们要把它烧成灰！",
 6: "烧成尘土，",
 7: "任你嘴上嘴下，直到把你这腐败的家伙锈穿，",
 8: "他们永不消停！",
 9: "为了我们的事业，",
 10: "以为我们会甘当齿轮",
 11: "嵌在一台机器里。",
 12: "那些有钱人和贪人正握着这一切，",
 13: "但这不是玩笑，我把你拎起来，",
 14: "然后掐住你的脖子，看着你窒息。",
 15: "你什么时候开始这副模样？现在我们正在崩塌，",
 16: "当他们把你硬塞进去，心脏被卡在外面……",
 17: "不如从我这儿接过去？",
 18: "你能看见的还有更多，足以让你相信……",
 19: "他们把你困住的这座笼子……",
 20: "一处阴森之地，惨淡得很……",
 21: "那不是像你这样的人该待的地方，所以……",
 22: "牵我的手，我带你去看！",
 23: "我们从顶端把它拆下来，",
 24: "自由坠落，绝不停下，",
 25: "对那些听不懂的人，我们永不坠落",
 26: "我们的动机，为了拿下属于我们的胜利",
 27: "这个社会已经无药可救，",
 28: "所以我们把它全烧了！",
 29: "烧成尘土，",
 30: "任你嘴上嘴下，直到把你这腐败的家伙锈穿，",
 31: "他们永不消停！",
 32: "为了我们的事业，",
 33: "以为我们会甘当齿轮",
 34: "嵌在一台机器里。",
 35: "那些有钱人和贪人正握着这一切，",
 36: "不，我们绝不停止。",
 37: "不安分者和弱者没有睡眠，所以我再说一遍：",
 38: "他们永不消停！",
 39: "为了我们的事业，",
 40: "一只从灰烬与尘土中升起的凤凰，我们爆发！",
 41: "一根煤渣与熔渣之柱，压在那腐朽之上，",
 42: "烟与碎片越升越高",
 43: "升到他们从未有过的高度！",
 44: "所以我们就在这里，一次次坠落……",
 45: "地狱深处，朋友，要不要一起来？",
 46: "这些殉道者压在我们后颈上，",
 47: "他们念叨着下一个就是我们。",
 48: "把这些石头埋进土里，",
 49: "我们会爬到顶上，先把他们烧掉。",
 50: "要么你，要么我。",
 51: "我不会再给你一次让我失望的机会。",
 52: "烧了它！",
 53: "把它烧成平地！",
 54: "直到我们唤醒的混乱只剩瓦砾！",
 55: "你把我们锁上镣铐，",
 56: "在一场取代我们的竞赛里，",
 57: "现在我们替自己人把它夺回来！",
 58: "这是为了你从我们身上夺走的那些命！",
 59: "你交易、你殴打、你伤我们伤够了！",
 60: "现在我们正挣脱锁链，所以",
 61: "他妈的看着点路！",
 62: "下一代只建立在你的……",
 63: "……仇恨上。",
 64: "操！",
}

CREDITS = [
 "暂停菜单画师",
 "3D 美术师",
 "作曲：Mochoco",
 "作曲：Noichi、Mochoco、Flootena",
 "作曲：LegoGodzilla 与 Faceless",
 "作曲：Faceless 与 LegoGodzilla\n演唱：Amai Hisa",
 "歌词与混音协助：Juno Songs",
 "Pure 配音",
 "Onion 配音",
]

PURE_TEXT = (
 "她也是恩辛克城的毕业生，曾是 Sun-Dried 组建的机器人社成员。她一向循规蹈矩，凡事照着别人的样子做到位，"
 "安全、标准、毫不起眼。这让她在这座充满怪咖个性的城市里，产生了「自己平淡无味」的不安全感。"
 "她很容易自我贬低、紧张兮兮，可她那种教科书级的学问与过人的聪慧无人能及。\n\n"
 "离开恩辛克上大学之后，她不幸失去了那群体谅她的朋友，又回到了努力想被接纳的状态。"
)
ONION_TEXT = (
 "恩辛克城 Ensemble 购物中心最偏的一个角落，开着一家小型哥特服饰店，名叫 Brandy's。"
 "Onion 是店里资历最老的收银员，总安静地守在柜台后。她维持这份工作，只是为了给自己的哥特时尚爱好攒钱——"
 "靠员工折扣和双周薪水，抢在新衣与配饰上架时第一个拿到手。\n\n"
 "她外表看起来就是标准的阴郁哥特范儿，可一旦聊起小众、未发行或失传的音乐，她的态度就会从安静瞬间变成迷人的热情洋溢。"
)

GAL = {
 "CHILLIN' THRILLIN' DLC - Self-Love": "CHILLIN' THRILLIN' DLC - 自爱",
 "CHILLIN' THRILLIN' DLC - Sitting Pretty": "CHILLIN' THRILLIN' DLC - 坐姿特写",
 "CHILLIN' THRILLIN' DLC - Streamlined": "CHILLIN' THRILLIN' DLC - 流线造型",
 "CHILLIN' THRILLIN' DLC - Congrats, Graduates!": "CHILLIN' THRILLIN' DLC - 恭喜毕业！",
 "CHILLIN' THRILLIN' DLC - Onion Final Concept": "CHILLIN' THRILLIN' DLC - Onion 最终概念图",
 "CHILLIN' THRILLIN' DLC - Onion Hair Breakdown": "CHILLIN' THRILLIN' DLC - Onion 发型拆解",
 "CHILLIN' THRILLIN' DLC - Casual Onion": "CHILLIN' THRILLIN' DLC - 休闲 Onion",
 "CHILLIN' THRILLIN' DLC - Forbidden Knowledge": "CHILLIN' THRILLIN' DLC - 禁忌知识",
 "CHILLIN' THRILLIN' DLC - How Familiar...": "CHILLIN' THRILLIN' DLC - 似曾相识……",
 "CHILLIN' THRILLIN' DLC - Bloomin'": "CHILLIN' THRILLIN' DLC - 绽放",
 "CHILLIN' THRILLIN' DLC - Cry for Me": "CHILLIN' THRILLIN' DLC - 为我哭泣",
 "CHILLIN' THRILLIN' DLC - Artist Swap!": "CHILLIN' THRILLIN' DLC - 画师互换！",
}

RESULTS = {
 "onion": {
  1: "嚯，我玩得还挺开心的。给你个折扣。经理不会喜欢我乱发折扣，不过……随便吧。",
  2: "你要不要，来这儿上班？在这地方你绝对会是个靠谱的同事。",
  3: "我出多少力，就等于我拿多少钱。",
  4: "我的歌声现在打八折……啊不，是走调（off-key）。我太幽默了。笑。",
  5: "经理在监控里抓到我摸鱼了……唉。你至少买点东西，让我业绩还过得去。",
 },
 "pure": {
  1: "一开始上手，一切就……通了！Sunny 看起来也好开心……真高兴我们最后的校园回忆是好的……",
  2: "搞定了！而、而且还提前了！也许我们可以……再一起待一会儿……就这一次？",
  3: "赶出来的活儿……我觉得还不算太差——！",
  4: "我们没时间做 bug 测试——！不过……也许这样也行？",
  5: "这远超我的水平……希望她别因此讨厌我……",
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
    items = json.load(open(gp, encoding="utf-8-sig")).get("dialogue", [])
    assert len(items) == len(texts), f"{rel}: {len(items)} vs {len(texts)}"
    add(rel, {"dialogue": {str(i): {"text": texts[i]} for i in range(len(texts))}},
        {"dialogue": {str(i): {"text": it.get("text", "")} for i, it in enumerate(items)}})


print("Chillin' & Thrillin':")
dialogue("data/flow-state/dreamcast.json", FLOW)
dialogue("data/restless/dreamcast.json", REST)
dialogue("synsun/people-onion.json", ONION_TV)
dialogue("synsun/people-pure.json", PURE_TV)

ach = json.load(open(os.path.join(GAME, "mods", MOD, "data/achievements.json"), encoding="utf-8-sig"))["achievements"]
add("data/achievements.json",
    {"achievements": {
        "0": {"fancyName": "哎呀，Y2K！", "unlockCondition": "在《Flow State》中达成全连",
              "showmanDialogue": "恩辛克学院校友的成就，把它的名声、乃至规模，都推到了前所未有的高度！"
                                 "不过我听说如今入学越来越难了，所以小伙子们，好好表现，去挣到那个录取名额吧！"},
        "1": {"fancyName": "浴火重生", "unlockCondition": "在《Restless》中达成全连",
              "showmanDialogue": "我甚至不知道商场最里面还开着那么一家店。不过我会继续敬而远之。"
                                 "那股青春期的戾气隔着老远就能闻到，而且……呃啊……光想想就让我起鸡皮疙瘩。"}}},
    {"achievements": {str(i): {"fancyName": a.get("fancyName", ""), "unlockCondition": a.get("unlockCondition", ""),
                               "showmanDialogue": a.get("showmanDialogue", "")} for i, a in enumerate(ach)}})

cg = json.load(open(os.path.join(GAME, "mods", MOD, "data/galleryCGData.json"), encoding="utf-8-sig"))["artwork"]
add("data/galleryCGData.json",
    {"artwork": {str(i): {"caption": a["caption"].replace("CGs - ", "CG图 - ")} for i, a in enumerate(cg)}},
    {"artwork": {str(i): {"caption": a["caption"]} for i, a in enumerate(cg)}})

gd = json.load(open(os.path.join(GAME, "mods", MOD, "data/galleryData.json"), encoding="utf-8-sig"))["artwork"]
add("data/galleryData.json",
    {"artwork": {str(i): {"caption": GAL.get(a["caption"], a["caption"])} for i, a in enumerate(gd)}},
    {"artwork": {str(i): {"caption": a["caption"]} for i, a in enumerate(gd)}})

peeps = json.load(open(os.path.join(GAME, "mods", MOD, "data/creditsData.json"), encoding="utf-8-sig"))["peeps"]
add("data/creditsData.json",
    {"peeps": {str(i): {"description": CREDITS[i]} for i in range(len(peeps))}},
    {"peeps": {str(i): {"description": p.get("description", "")} for i, p in enumerate(peeps)}})

add("weeks/cnt-1.json",
    {"weekName": "相信过程", "storyName": "DLC 章节", "location": "恩辛克学院机器人社"},
    {"weekName": "Trust The Process", "storyName": "DLC Chapter", "location": "Enzync Academy Robotics Club"})
add("weeks/cnt-2.json",
    {"weekName": "禁忌之音", "storyName": "DLC 章节", "location": "Brandy's 服饰店"},
    {"weekName": "Forbidden Music", "storyName": "DLC Chapter", "location": "Brandy's Apparel"})

add("data/flow-state/meta.json", {"song": {"name": "Flow State（心流）"}}, {"song": {"name": "Flow State"}})
add("data/restless/meta.json", {"song": {"name": "Restless（不得安宁）"}}, {"song": {"name": "Restless"}})

add("data/flavorpediaData.json",
    {"character": {"0": {"flavorText": PURE_TEXT,
                         "subtitles": "哦！呃……你好。:dur:2.1[NL]呃嗯……我没想到真有人会来看这个，不过……呃……:dur:4.55[NL]"
                                      "我叫 Pure，我……:dur:3.35[NL]呃嗯……呃……:dur:4.01[NL]*叹气* 我没词了，抱歉……:dur:3.1"},
                   "1": {"flavorText": ONION_TEXT,
                         "subtitles": "欢迎光临 Brandy's……我叫 Onion。:dur:3.43[NL]来看看我们的特卖……:dur:1.6[NL]"
                                      "——废话废话废话，随便吧。公司那套词你早听腻了，买点东西就行！:dur:4.2"}}},
    {"character": {"0": {"flavorText": "", "subtitles": "Oh! Uh... hey.:dur:2.1[NL]Uhhhmm...:dur:4.55[NL]My name's Pure, and I...:dur:3.35[NL]Uhmmm... Uhhh...:dur:4.01[NL]*sigh* I got nothing, I'm sorry...:dur:3.1"},
                   "1": {"flavorText": "", "subtitles": "Welcome to Brandy's... My name is Onion.:dur:3.43[NL]Check out our sale on...:dur:1.6[NL]-yadda yadda yadda, whatever.:dur:4.2"}}})

for name, mapping in RESULTS.items():
    rel = f"images/results/character/{name}/dialogue.json"
    d = json.load(open(os.path.join(GAME, "mods", MOD, rel.replace("/", os.sep)), encoding="utf-8-sig"))["dialogue"]
    order = {"S": 1, "A": 2, "B": 3, "C": 4, "D": 5}
    texts = ["..." if it.get("rank") not in order else mapping[order[it["rank"]]] for it in d]
    add(rel, {"dialogue": {str(i): {"name": texts[i]} for i in range(len(texts))}},
        {"dialogue": {str(i): {"name": it.get("name", "")} for i, it in enumerate(d)}})

# 歌词写入 languageFlavor 底稿
lf = os.path.abspath(os.path.join(HERE, "..", "汉化底稿", "languageFlavor-底稿.json"))
data = json.load(open(lf, encoding="utf-8"))
cur = {x["key"]: x["value"] for x in data["map"]}
for i, txt in LYRICS.items():
    cur[f"restlesslyric_{i}"] = txt
data["map"] = [{"key": k, "value": v} for k, v in sorted(cur.items())]
json.dump(data, open(lf, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"  歌词 {len(LYRICS)} 条 -> languageFlavor ({len(data['map'])} keys)")
print("完成")
