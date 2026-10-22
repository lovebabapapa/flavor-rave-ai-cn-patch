# -*- coding: utf-8 -*-
"""DLC: Official DLC - Masters of the Craft 全量汉化"""
import json, os, shutil

MOD = "Official DLC - Masters of the Craft"
GAME = r"P:\FNF\Flavor.Rave"
HERE = os.path.dirname(os.path.abspath(__file__))

SQUIS = [
 "*拨弦……拨弦……拨弦……铮*",
 "……",
 "*拨弦……铮……铮……铮……*",
 "为什么感觉……比从前难了这么多……我真的失去手感了吗……？",
 "夜复一夜，我的双手几乎凑不出一段旋律。曾经在弦上游刃有余的嗓音，如今只剩呜咽。",
 "想来是没有观众要难得多吧……不……哪怕只是有个能听的人也好。如今再也没有迷路的旅人需要我指引了。",
 "……难道迷路的只剩我自己了吗？",
 "不……还没有。不过……",
 "如果这正是关键呢？对，没错！我需要主动去「迷路」！",
 "我……很少在科里安达之外旅行……所以很好奇……这地方之外还有什么？普雷希茨群山背后的世界，是那么神秘……",
 "对，当然是它！那就是我的钥匙。一刻也不能耽误！现在动身，天亮之前一定能找到我需要的东西。",
 "[Savory 从家乡一路北上，徒步开始了他的漫长旅程。]",
 "[旅程一开始还算顺利，但翻山的上坡和山后一望无际的荒草，哪怕对身手矫健的 Wayfinder 也是极大的消耗。]",
 "[不过辗转跋涉之后，Savory 来到了一座镇子脚下——它的名字让他想起些什么。]",
 "迷迭香山脊……山的那边就是迷迭香山脊？！",
 "妈妈以前总跟我讲她来这里旅行的事……她从这儿带回的那些美妙音乐和美食……没想到竟然这么近——！",
 "呃……能到这儿也算是一种福气吧……我的胃从来没这么瘪过……",
 "嗯……Crispy's……看起来很高档，可是……我感觉撑不到集市了……",
 "[Savory 走进一家气派华丽的大餐厅，井然有序，宾客盈门。]",
 "欢迎光临，欢迎欢迎，buongiorno（早上好）！快请坐！",
 "……Gracias（谢谢），Señor（先生）……",
 "Señor，嗯？Un placer ayudarle hoy, mi buen señor（很高兴今天能为您服务，我的好先生）。",
 "啊？你会说我的语言？你也是科里安达人？",
 "非也，我可是土生土长的迷迭香山脊人。只是当年我去科里安达做过多次宴席，顺手学会了那儿的语言。",
 "原来如此。",
 "……所以我也才能认出，那身神秘斗篷下面是谁——Savory 先生！",
 "还是说，您如今只被人叫「Wayfinder」了？嘁。",
 "啊——？！",
 "起初我也拿不准，可您这个嗓音……一听便知！",
 "您母亲以前常来这里，她把您写的每一首歌都弹给我们听过。要知道，她非常以您为傲。",
 "……希望她老人家现在还安好？",
 "我……想来是的。",
 "这回答可不够笃定。那可是您的母亲啊，Savory！您难道就没停下来问候过她和其他家人吗？",
 "我只是……好久没见她了。好、好久好久。既然你已经认出我，那你也知道——",
 "知道你后来一走极端？那就是你们最后一次说话？二十年过去了，你居然一次都没有跟家人说过话？！",
 "我……我不想争执。我只是来找点吃的……",
 "……",
 "*叹气……*",
 "我从你眼里看得分明。你是真的失去了热情。你现在需要的可不止是食物。听我说，amico（朋友）。",
 "热情从世界万物的各个侧面酿生，而一路热情足以点燃其余所有！在我的屋檐下，热情来自——烹饪！",
 "让我把我们的热情之道教给你，看看它如何同时喂养身体与灵魂！",
]

TUNE = [
 "恩辛克第二季，宝贝！这次我保证，不会再像你上次来那样状况百出了，Sweet。",
 "Sour，我跟你说过多少回了，那些小插曲才让我们的重逢特别！好的坏的，我一样都不想错过。",
 "嘿，我就喜欢一切都在计划内的感觉……毕竟计划嘛。城郊不远处有个超酷的游乐园，所以今天咱们开上「声浪号」兜风去！",
 "你还记得我们初次见面时我那辆房车吧？",
 "记得！上面全是你那套风格的涂装，嘿嘿。特别可爱。",
 "定制喷漆，装满我的演出设备，随时随地想开演就开演！而且你知道，跟朋友出去兜风超开心的。",
 "这家伙这么多年状态一直完美。系好了吗？那我们出发上街！",
 "[噗噗噗——]",
 "……我再试一次。",
 "[噗噗——砰——嘶————]",
 "……出什么问题了吗？",
 "[呜———————！！]",
 "Sour？！",
 "我。真的。不敢。相信。",
 "引擎坏了，哈？真是太好了。我才一天没碰它，它就开始给我罢工。",
 "呃……嗯……我赶紧打个电话……喂，Umami？对，呃……你有 Oil 的号码吗？我们遇到点状况——",
 "嘿！它没修不也撑了这么久嘛！只是……你之前让我去检查的那些话，我都忘了，对吧？",
 "……行行，知道了。多谢，表姐。你也顺心。",
 "Sour……要是你的房车指望不上了，我不介意找点别的活动。",
 "没事，别担心。我表姐会安排拖车和维修。咱们就等一下。",
 "[半小时后……]",
 "哟，今天接的是哪种霓虹涂装的嘻哈大篷车啊？Umami 说得一点没错——你开车又响又张扬！",
 "我完全不知道它哪坏了。我一拧钥匙，它就开始哐哐作响。",
 "我的天，这底下也太乱来了，Sparky（闪电哥）！你试过自己修这玩意儿？",
 "我对修车一窍不通。这是我哥传给我的二手车。多半是他之前动过什么手脚。撑到现在也算够本了。",
 "没有我一小时搞不定的毛病。我给这家伙通通电，再拖过去。",
 "您和 Sour 都提到认识 Umami，女士？",
 "哦，是的！她是我特别好的朋友！当年恩辛克学院同一届毕业的。",
 "她差不多每周都来跟我过女孩之夜。你们两位小情人的事她跟我讲得可多了。",
 "唉，她为这辆房车要我送去维修的事，已经念叨我好多岁了。奇怪她居然没跟你说过——早知道你肯定早就催着我修了，嘿。",
 "哈，你懂的，Sparky！Umami 跟我学到了「座驾保持巅峰状态」有多重要，所以听你表姐的话，下次别再摊上这种事！我店门永远敞开！",
 "再说了，朋友的活儿我永远免费修。这种好事你得抓紧享受，懂吧？",
 "来，上我的拖车，我送你们去店里？车库里有架旧钢琴，我修车的时候你们可以弹琴给工作区加点气氛！",
]

CRISPY_TV = [
 "什么，咱们现在是美食直播了吗？那明明是个大厨，不是作曲家。",
 "我的天，就是他——",
 "嗯？你认识他？",
 "嗯，我倒是没见过 Crispy 本人，但我叔叔好几年来一直想跟他攀上合作。",
 "他是迷迭香山脊的名厨——就是海对面、普雷希茨北边那座很讲究的镇子。",
 "那儿的居民都爱死他了。他每道菜评分都超高，客人等餐时还会为他们奏乐。",
 "哇，一顿晚餐带一场演出，全出自同一人之手。难怪你叔叔想跟这种人物合作。",
 "那个，呃……这大概算个小秘密……我觉得 Crispy 其实嫌弃我叔叔。",
 "什么？快把这八卦的来龙去脉讲给我听！",
 "他是真的不喜欢我叔叔做的食物。就是……我听说他讨厌到有一次差点气到——字面意义——浑身通红。",
 "我知道快餐不算高档……可天呐。这也没能阻止我叔叔继续想跟他称兄道弟……",
 "所以他对「正经烹饪」就是这么有热情吗？这下我可太想亲眼见识了！",
 "快！谁去跟这位大厨搭个话，掰断一根意面！记得开着摄像！我给他免费引流！",
 "求你，千万别那么做！还有，呃……要是我叔叔听到这段……抱歉把细节说漏了……",
]

OIL_TV = [
 "哦，她看着好眼熟！我保证我数据库里存着一段关于她的早期记忆……",
 "没错！她就是恩辛克学院的校友之一，我毕业前每年都会有校友回校参观。",
 "我高三那年她来过，那时我刚被组装完成。",
 "对对。她会，呃……汽修资格证？如果我没记错的话……",
 "嗯，我刚查过。她现在在恩辛克城上城区经营那家汽车修理铺。",
 "她每次来访都超酷的。她会推来那些翻新过的老爷车，给我们上手演示。",
 "我以前觉得汽车特别吓人，现在我理解它们的原理几乎和懂电脑一样自然了。",
 "不过……让我自己开车我还是害怕。我还是坐公共交通吧。",
 "那些汽车知识你还留着吗？",
 "在的吧。问这个干嘛？",
 "那听我说。我超想有一套自己的轮子能到处跑！总比去哪都让人扛着我来强——",
 "那画面是挺搞笑，但我觉得你会不小心让我撞墙的。",
 "那轮子交给我管！你来当巡航控制。",
 "这我真的做不到。你八成会滚到某个再也回不来的地方。比如……楼梯下面。",
 "是啊……至少 idea 很有趣。开车这事还是交给专业人士吧。",
 "不过等你真有了自己的车，你可以找那位 Oil 女士合作，把我改装进仪表盘里！",
 "对，我已经在想象了——集终极音响/导航/电台于一身的伴侣，就是我！公路永不再无聊！",
 "嘿，你现在没装进车里也能干所有这些事啊，Syn。",
]

CRISPY_TEXT = (
 "他是名震一方的大厨，住在科里安达与普雷希茨以北的镇子——迷迭香山脊，一个文化浓郁、尤其以美食著称的地方。"
 "他经营着以自己名字命名的餐厅，客人来自世界各个角落。他对每位客人都会以一句响亮的"
 "「欢迎光临，欢迎欢迎，buongiorno！」和灿烂笑容相迎。\n\n"
 "Crispy 深信热情之道。人人都有自己的热情语言，失去一路热情，往往正是另一簇火苗燃起的契机。"
 "他的厨房完全按他的心意配置，为了通过烹饪把热情表达到底。而想把他的热情好客变成熊熊怒火，最快的方式就是不尊重他的热情之地。"
)
OIL_TEXT = (
 "恩辛克城修车的头号人选。Oil 约十年前从恩辛克学院毕业后上了汽修技校，如今是本地一家汽车修理铺口碑极佳的老板。"
 "她做事高效、脾气稳定又好相处，客户与员工都对她敬重有加。\n\n"
 "Oil 心态年轻，工作之余也纵情于其他爱好，比如打游戏、参加恩辛克的大小活动。她和年轻人格外合得来，"
 "很多人觉得她就是那种「很酷的小姨」——无论是空闲时帮忙带娃，还是回恩辛克学院给新一代汽修人讲课时。"
)

SIDE_ZH = {
 "Charred": "爆红美食博主，用 RAVE 之力展示离谱的烹饪手法。风格与魅力满溢。",
 "Cheesy": "白天是朴实的农家女孩，夜晚登上舞台做喜剧演员。别被她的名字骗了，她超搞笑。",
 "Juice": "生在恩辛克的三岁小孩。话还说不利索，经常对着远处发呆。",
 "Pure": "害羞安静的恩辛克学院毕业生，尚未找到真正的使命。在大多数场合都觉得自己格格不入。",
 "Sorbet": "来迷迭香山脊找对象的居民。他迫切想成为著名摇滚明星，只为撑撑这个肤浅的场面。",
 "Palm": "电动车专家，修理铺的两大台柱之一。听着体育广播干活，特别专注。",
 "Sunflower": "为 Oil 工作的通用汽修工。看着迷迷糊糊，实则是非常可靠的员工，帮衬着住在 The Leftovers 区的家人。",
 "Olive": "修理铺的财务与文书担当。无论客人还是同事惹出乱子，她都会用尽一切办法摆平。",
 "Grilled": "老车迷，Patty 的好丈夫。想在一家搬过海之前，把他最爱的摩托修好。",
 "Patty": "元气厨师，梦想开一家自己的小餐馆。很快将随家人搬离恩辛克去追这个梦。",
}
SIDE_PLACE = {"Crispy's Eatery": "Crispy's 餐厅", "Oil's Auto Repair": "Oil 汽修铺"}

GAL = {
 "Crispy Final Concept": "Crispy 最终概念图", "Crispy Sketches": "Crispy 涂鸦集",
 "A Fine Dish!": "好菜上桌！", "Cheesy Concept": "Cheesy 概念图",
 "Seaside Cheesy!": "海边的 Cheesy！", "Charred Concept": "Charred 概念图",
 "A Fellow Culinary Master": "同行的大厨", "Pure Concept": "Pure 概念图",
 "Juice Concept": "Juice 概念图", "A Fine Dish for All!": "好菜人人有份！",
 "Oil Final Concept": "Oil 最终概念图", "Sunflower, Palm, & Olive Concept": "向日葵、Palm 与 Olive 概念图",
 "Patty and Grilled Concept": "Patty 与 Grilled 概念图", "Always here for repairs!": "修理随时在线！",
 "Tune-Up Event Concepts": "Tune-Up 活动概念图", "Headpat!": "摸摸头！",
 "Endure the Heat!": "顶住高温！", "Training Hard": "魔鬼训练", "Masters at Work!": "大师开工！",
}

RESULTS = {
 "crispy": {
  1: "火候完美！这一餐和这一场演出都是！哦，我妈妈一定会为我骄傲的！",
  2: "Propongo un brindisi（我提议干杯）！干杯，我的朋友们！",
  3: "不算差，不过在 Crispy's，我们追求手艺的极致！但极致这种事急不得。下次再来一起打磨热情啊，amico（朋友）！",
  4: "把每顿饭都做成大秀固然美好，可那……大概让我的老腰有点吃不消。",
  5: "Che noia mortale（无聊透顶）！我们今天心里那股更伟大的热情，一定还在的，对吧？",
 },
 "oil": {
  1: "我全缸点火、状态拉满！来，伙计们上车！带你们兜个风！",
  2: "听见引擎呼噜呼噜的声音了吗……那是我耳边最美的音乐。",
  3: "咱们低挡慢巡，稳得很。",
  4: "路上有几个小颠簸，不过咱们到达目的地了。",
  5: "发动机故障灯亮了。最好再检查一遍……",
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


print("Masters of the Craft:")
dialogue("data/squisito/dreamcast.json", SQUIS)
dialogue("data/tune-up/dreamcast.json", TUNE)
dialogue("synsun/people-crispy.json", CRISPY_TV)
dialogue("synsun/people-oil.json", OIL_TV)

ach = json.load(open(os.path.join(GAME, "mods", MOD, "data/achievements.json"), encoding="utf-8-sig"))["achievements"]
add("data/achievements.json",
    {"achievements": {
        "0": {"fancyName": "我的妈呀！", "unlockCondition": "在《Squisito》中达成全连",
              "showmanDialogue": "早就听说 Crispy 的厨艺举世无双！我觉得该去一趟迷迭香山脊拜会本尊了。"
                                 "我手上正好有一场聚会，急需他这样的掌勺！"},
        "1": {"fancyName": "油脂闪电", "unlockCondition": "在《Tune-Up》中达成全连",
              "showmanDialogue": "我开的也是一套相当有年份的老座驾，而 Oil 是我唯一信任、能让它保持原汁原味光泽的人。"
                                 "可惜她的店只做本地生意，我知道不少同乡外的朋友都用得上这样的手艺。"}}},
    {"achievements": {str(i): {"fancyName": a.get("fancyName", ""), "unlockCondition": a.get("unlockCondition", ""),
                               "showmanDialogue": a.get("showmanDialogue", "")} for i, a in enumerate(ach)}})

cg = json.load(open(os.path.join(GAME, "mods", MOD, "data/galleryCGData.json"), encoding="utf-8-sig"))["artwork"]
add("data/galleryCGData.json",
    {"artwork": {str(i): {"caption": a["caption"].replace("CGs - ", "CG图 - ")} for i, a in enumerate(cg)}},
    {"artwork": {str(i): {"caption": a["caption"]} for i, a in enumerate(cg)}})

gd = json.load(open(os.path.join(GAME, "mods", MOD, "data/galleryData.json"), encoding="utf-8-sig"))["artwork"]
add("data/galleryData.json",
    {"artwork": {str(i): {"caption": "MASTERS DLC - " + GAL.get(a["caption"].replace("MASTERS DLC - ", ""),
                                                                 a["caption"].replace("MASTERS DLC - ", ""))}
                   for i, a in enumerate(gd)}},
    {"artwork": {str(i): {"caption": a["caption"]} for i, a in enumerate(gd)}})

CREDITS = ["作曲：Biddle3", "过场歌曲\n作曲：Millxr",
           "作曲：Juno Songs、Faceless、SkyHighProductions",
           "过场歌曲\n作曲：HighPoweredKeyz 与 Faceless",
           "角色选择画面画师", "作曲家", "作曲家", "作曲家", "Crispy 配音", "Oil 配音"]
peeps = json.load(open(os.path.join(GAME, "mods", MOD, "data/creditsData.json"), encoding="utf-8-sig"))["peeps"]
add("data/creditsData.json",
    {"peeps": {str(i): {"description": CREDITS[i]} for i in range(len(peeps))}},
    {"peeps": {str(i): {"description": p.get("description", "")} for i, p in enumerate(peeps)}})

add("weeks/dlc_aop.json",
    {"weekName": "热情之道", "storyName": "DLC 章节", "location": "Crispy's 餐厅"},
    {"weekName": "The Art of Passion", "storyName": "DLC Chapter", "location": "Crispy's Eatery"})
add("weeks/dlc_viaj.json",
    {"weekName": "房车抛锚", "storyName": "DLC 章节", "location": "恩辛克城主街"},
    {"weekName": "Van in a Jam", "storyName": "DLC Chapter", "location": "Enzync City Main Street"})

add("data/squisito/meta.json", {"song": {"name": "Squisito（美味满分）"}}, {"song": {"name": "Squisito"}})
add("data/tune-up/meta.json", {"song": {"name": "Tune-Up（保养升级）"}}, {"song": {"name": "Tune-Up"}})

add("data/flavorpediaData.json",
    {"character": {"0": {"flavorText": CRISPY_TEXT,
                         "subtitles": "欢迎光临，欢迎欢迎，buongiorno！:dur:3.34[NL]就由我 Crispy，带你领略真正的烹饪魅力！:dur:5.311"},
                   "1": {"flavorText": OIL_TEXT,
                         "subtitles": "从古董到现代，从油老虎到纯电！:dur:4.22[NL]只要它会「嗡」一声，我一下午就给你修好！:dur:3.521[NL]"
                                      "顶级服务，本店出品，我是 Oil！:dur:3.594"}}},
    {"character": {"0": {"flavorText": "", "subtitles": "Welcome, welcome, and buongiorno!:dur:3.34[NL]Allow me, Crispy, to show you true culinary captivation!:dur:5.311"},
                   "1": {"flavorText": "", "subtitles": "From vintage to modern, gas-guzzlers to electric!:dur:4.22[NL]If it goes VROOM, I'll have it fixed up in an afternoon!:dur:3.521[NL]Top notch service from yours truly, Oil!:dur:3.594"}}})

side = json.load(open(os.path.join(GAME, "mods", MOD, "data/flavorpediaSideData.json"), encoding="utf-8-sig"))["character"]
def side_tr(c):
    return {"design": c.get("design", "").replace("Designed by", "设计：").replace("Flavor Rave Original", "Flavor Rave 原创角色"),
            "desc": SIDE_ZH.get(c.get("name", ""), c.get("desc", "")),
            "place": SIDE_PLACE.get(c.get("place", ""), c.get("place", ""))}
add("data/flavorpediaSideData.json",
    {"character": {str(i): side_tr(c) for i, c in enumerate(side)}},
    {"character": {str(i): {k: c.get(k, "") for k in ("design", "desc", "place")} for i, c in enumerate(side)}})

for name, mapping in RESULTS.items():
    rel = f"images/results/character/{name}/dialogue.json"
    d = json.load(open(os.path.join(GAME, "mods", MOD, rel.replace("/", os.sep)), encoding="utf-8-sig"))["dialogue"]
    order = {"S": 1, "A": 2, "B": 3, "C": 4, "D": 5}
    texts = ["..." if it.get("rank") not in order else mapping[order[it["rank"]]] for it in d]
    add(rel, {"dialogue": {str(i): {"name": texts[i]} for i in range(len(texts))}},
        {"dialogue": {str(i): {"name": it.get("name", "")} for i, it in enumerate(d)}})

print("完成")
