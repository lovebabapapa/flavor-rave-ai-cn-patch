# -*- coding: utf-8 -*-
"""DLC: Official Collab DLC- Taste of Revenge 全量汉化"""
import json, os, shutil

MOD = "Official Collab DLC- Taste of Revenge"
GAME = r"P:\FNF\Flavor.Rave"
HERE = os.path.dirname(os.path.abspath(__file__))

FEST = [
 "[某天深夜，距离「剧毒磨难」还有一周，在 The Leftovers 区一条不起眼的小巷里……]",
 "……",
 "[Tangy 怒气难平，抱着双臂靠在冰冷的砖墙上。她脑子里全是翻涌的负面情绪，却一个字也组织不出来。]",
 "[至少周围安静、无人，她还能借此稍微宽慰自己……可这份宽慰很快就被打破了。]",
 "……",
 "喂，你想干嘛？",
 "……呃。",
 "没话说就让开。我需要自己的空间。",
 "……",
 "……这条破巷子是你的？你也是那种爬进来的老鼠，把这儿当自己的地盘？别烦我。",
 "你说什么？！",
 "啧……行吧，随便你。你继续在那儿闷着吧。但我是不会离开我这个位置的。",
 "……",
 "……",
 "……没人会无缘无故甘愿待在这种地方。你的理由是什么？",
 "我没必要告诉你任何事。",
 "那就别说！",
 "……",
 "*长叹一口气* ……这是我知道的最安静的地方。而且……这儿够冷漠。在家里我没法像自己想的那样发泄，只会更火大。",
 "……嘿，那我们的理由正好对上了。",
 "我以前从没在这片街区见过你。那你肯定不是本地人。要是本地人，我早该撞见你了。",
 "这就更奇怪了——不是本地人，却猫在巷子里。你到底什么情况？",
 "连我家乡的巷子都满载着我的烦闷。我想找个不一样的地方。",
 "这座城市和我熟悉的地方差得远……在我那儿，连巷子都塞满了噪音和灯光……只有这一条例外。",
 "欢迎来到全城最烂的地段。你要是又穷又满腔怒火与怨气，在这儿正合适。",
 "驱使我来这儿的不是怨气。",
 "那是什么？",
 "……复仇。不……是审判。对，我想要的就是这个。",
 "你也是啊？有个人一辈子都在惹我发火。只要能看他输一次，我什么都愿意干。还有……让我也赢一次。",
 "我心里也有个人……告诉我，你打算怎么结束你的烦恼？",
]

SAT = [
 "你……你不是认真的吧……",
 "炸弹？！你他妈疯了吗？！",
 "我的计划能确保她死……一场烈火之死，正配得上那个满口谎言的伪善恶魔。",
 "你……你疯了。你怎么可能觉得这是对的。",
 "别装得比这高尚！你希望伤害你的那个人遭殃，这可是你自己说的。还是为了一场幼稚的单方面较量……",
 "要是你知道心和身体被撕成碎片的痛苦，你就会明白，玷污过你的人唯一配得上的惩罚，远超一时的疼痛……",
 "……那是永久的。",
 "不，这不对！我不管你经历过什么烂事，我都不会听一个人为谋杀找借口……而、而且我这事也不是什么幼稚的较量！",
 "啊啊啊——去你的！我走了！你也给我滚出这座城市！",
 "蠢丫头！你不会明白的！",
 "你不……懂……没人……懂……",
 "[那家伙到底是谁啊？唉……让他当别人的麻烦去吧。我可没那个心力去阻止一桩他妈的重罪。]",
 "……至少我该报警……",
 "[我暴露了自己……要是那丫头到处乱说，我努力的一切就全完了！我必须快点行动。]",
 "[那么……就这么定了。我离开这座城市，明晚……一切都会实现。]",
 "必须这样结束……这是唯一的办法……可是……",
 "我心底……涌起一股渴望……渴望另一种结局。要是……我曾经的挚爱……要是她……",
 "——不……不……不！！！",
]

KAB = [
 "嘿，Spicy！你还好吧？",
 "嘿嘿！我好得不得了！嘿嘿嘿，谢谢你关心！",
 "哎哟看啊！是「香料大师」！",
 "哦，香料大师！这个称呼新鲜！我喜欢！！！",
 "啊，唐辛子镇之焰大驾光临我们的重张开业！请问有何吩咐？",
 "拉面碗，堆得高高的！一直上到我吃不下为止！",
 "[太疯狂了……最近大家都对我这么好。我和 Smoki-doki 真的一飞冲天了，对吧？]",
 "[这……哇。我还不习惯。现在大家都这么开心见到我。这正是我长久以来梦寐以求的！]",
 "耶——！！！再见，过去的 Spicy！你好，全新的 Spicy！唐辛子镇之——",
 "",
 "[轰——！]",
 "把唐辛子镇之焰给我带来！！！",
 "呃——",
 "嘿嘿嘿，我猜这是在叫我？",
 "呃……嘿嘿！你想找我，直接走过来问一声就行了嘛，你知道的？不用——",
 "我的天，是你！",
 "哦……是你。那个蠢兮兮的人类歌唱比赛里的红头发傻丫头……",
 "雷霆使者！好久不见！",
 "我叫 Bree，不是你刚才说的什么「雷霆丁格」！现在，让开。我没空搭理你这种低等人类！",
 "……那你刚才为什么叫我的名字？",
 "我没有！我是来找——",
 "不……天啊，别告诉我。",
 "你就是唐辛子镇之焰？？？你他妈怎么会是我感应到的那股力量波动的源头？！",
 "我靠金属的力量得到的！哦，还有友谊！我「觉得」是这么运作的，嘿嘿嘿。现在我也能 RAVE 了，跟你一样！",
 "……RAVE 是什么鬼？[天啊，你真是土得没边……]",
 "你知道的……RAVE！就是那个能让你从眼睛里射出闪电的东西。就像我们第一次见面时你那样！",
 "我完全不知道你在说什么。",
 "知道我为什么有力量吗？因为我是神。我是宙斯的女儿！众神之神！别告诉我这都没让你想起点什么。",
 "宙斯？没听过。他是那种「天气兽」吗？",
 "……",
 "……呃，他倒不是真的「兽」那种兽，但他很擅长，比如，扔雷电之类的，而那跟天气有关，我猜……",
 "呃，我干嘛要陪你扯这些你瞎编的人类词汇？！",
 "我生来就该用雷电管束像你这样的人类。那些扰乱神圣平衡的人类。",
 "我是平衡之神。而像你这样的人类拥有神一般的火焰之力，会破坏平衡！",
 "嘿，有酷炫力量的人类可不止我一个，这城里都不止我一个！",
 "唉，我懂了。你肯定还在为那场比赛不高兴。那都是图个乐子嘛，对吧？我玩得可开心了，而且那时候我还没使出全力呢！",
 "才、才没有！我才没有为那场比赛不高兴！那种愚蠢的凡人游戏对我来说毫无意义！",
 "再说了……那场比赛根本就是胡闹，你自己也知道！我当时只是……在压制自己的力量。要是我「真的」认真，整个舞台都会被轰成瓦砾！",
 "听起来是有人想再打一场！这次咱们就全力以赴！",
 "这可不是什么幼稚的复赛！这是生死之战！我不会允许你这种混乱的爪牙继续四处游荡、破坏平衡！",
 "别这样嘛，放轻松，享受一下乐趣！你知道的，身为「平衡之神」，你现在可真是相当失衡啊，哈哈哈。",
 "呃啊，闭上你的嘴，开打吧！！！",
]

CREDITS = [
 "作曲：Ascenti 与 Legogodzilla",
 "过场歌曲\n作曲：Ascenti",
 "过场歌曲\n作曲：Legogodzilla",
 "作曲：Mochoco",
 "美术", "美术", "作曲家", "作曲家", "作曲家", "谱面制作人",
 "Bree 配音", "Tabi 配音",
 "Vs. Tabi\n（Ascenti、LegoGodzilla702、Vs. Tabi 团队）",
 "Characteristic Disparity\n（Team Shatterdisk）",
]

TABI_TEXT = (
 "他本是个过着平凡生活的普通人，直到深深爱上一位他以为会是终身伴侣的女性，人生从此改变。"
 "这段感情为他招来悲剧——原本的形体被毁，沦为一具蹒跚的骨架空壳。而这场悲剧也让他的挚爱离他而去，"
 "只留给 Tabi 一具冰冷、空洞的躯壳。那具躯壳很快就被愤怒与仇恨填满。\n\n"
 "Tabi 要向旧爱复仇，因为她「夺走了他的一切」。他坚信自己的极端手段是正当的，"
 "会不顾一切地执行他的审判——在狂怒之中，也对抗着根深蒂固的悔意。"
)
BREE_TEXT = (
 "她是全能的宙斯本人之女。Bree 以自封的「平衡之神」身份守望地球，力图维持秩序、消除这星球上的差异。"
 "可她好斗的性情与对「秩序」的扭曲理解，常使她违背自身职责，因此在同族神祇中排名最低。\n\n"
 "Bree 对任何阻挡她「秩序」的人都毫不客气，还很容易结下幼稚的旧怨。她会毫不犹豫地用神之雷电将人击倒。"
)

RESULTS = {
 "bree": {
  1: "再一次，我证明了自己是宇宙中最强的存在！有没有力量都一样，你们这些凡人根本没法跟神相比！",
  2: "好了，你该吸取教训了。最好别再让我看到那些恶心的 RAVE 力量。",
  3: "真正的平衡回归了……我的在意与不在意恰好各占一半。想让我更在意？那就变成更大的威胁。",
  4: "喂，我根本没认真！要是我真在意，会把你打得多惨你自己想象一下！",
  5: "不，我们不会把这又变成一场愚蠢的歌唱比赛。我要让拳头说话了！",
 },
 "tabi": {
  1: "我的死亡炼狱中不会留下任何东西。我将在火焰中沉醉……终于在这具冰冷的躯壳上感到温暖。",
  2: "别挡我的路，丫头。我的事与你无关。",
  3: "我已准备好……迎接任何麻烦。我的目标终将达成。",
  4: "这个计划会证明……很困难。",
  5: "我感觉……停滞不前。不……我不会允许自己有这种软弱！",
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


print("Taste of Revenge:")
dialogue("data/festering/dreamcast.json", FEST)
dialogue("data/festering/saturn.json", SAT)
dialogue("data/kablooie/dreamcast.json", KAB)

ach = json.load(open(os.path.join(GAME, "mods", MOD, "data/achievements.json"), encoding="utf-8-sig"))["achievements"]
add("data/achievements.json",
    {"achievements": {
        "0": {"fancyName": "痛苦的前奏", "unlockCondition": "在《Festering》中达成全连",
              "showmanDialogue": "远方某家餐厅发生恐怖爆炸的消息到处都是。凶手至今没找到。真令人不安……"
                                 "希望别有可疑人物跑来恩辛克的地盘。"},
        "1": {"fancyName": "接着宙斯就来了", "unlockCondition": "在《Kablooie》中达成全连",
              "showmanDialogue": "先是反常的暴风雪，现在又是损毁财产的落雷？唐辛子镇到底是怎么回事，"
                                 "总招来这种危险天气？！我怀疑那地区近期 RAVE 使用的激增可能是原因之一……"}}},
    {"achievements": {str(i): {"fancyName": a.get("fancyName", ""), "unlockCondition": a.get("unlockCondition", ""),
                               "showmanDialogue": a.get("showmanDialogue", "")} for i, a in enumerate(ach)}})

cg = json.load(open(os.path.join(GAME, "mods", MOD, "data/galleryCGData.json"), encoding="utf-8-sig"))["artwork"]
add("data/galleryCGData.json",
    {"artwork": {str(i): {"caption": a["caption"].replace("CGs - ", "CG图 - ")} for i, a in enumerate(cg)}},
    {"artwork": {str(i): {"caption": a["caption"]} for i, a in enumerate(cg)}})

peeps = json.load(open(os.path.join(GAME, "mods", MOD, "data/creditsData.json"), encoding="utf-8-sig"))["peeps"]
add("data/creditsData.json",
    {"peeps": {str(i): {"description": CREDITS[i]} for i in range(len(peeps))}},
    {"peeps": {str(i): {"description": p.get("description", "")} for i, p in enumerate(peeps)}})

add("weeks/xcollab_tabi.json",
    {"weekName": "内心算计", "storyName": "DLC 联动故事", "location": "剩饭区小巷"},
    {"weekName": "Inner Machinations", "storyName": "DLC Collab Stories", "location": "Leftovers Alleyway"})
add("weeks/xcollab_chardisp.json",
    {"weekName": "雷霆再战", "storyName": "DLC 联动故事", "location": "唐辛子镇"},
    {"weekName": "Rumbling Rematch", "storyName": "DLC Collab Stories", "location": "Togarashi Town"})

add("data/festering/meta.json", {"song": {"name": "Festering（溃烂）"}}, {"song": {"name": "Festering"}})
add("data/kablooie/meta.json", {"song": {"name": "Kablooie（轰然引爆）"}}, {"song": {"name": "Kablooie"}})

add("data/flavorpediaData.json",
    {"character": {"0": {"flavorText": TABI_TEXT, "subtitles": "我受够了！:dur:1.36"},
                   "1": {"flavorText": BREE_TEXT, "subtitles": "吃我一记雷劈吧，混账！:dur:2.2"}}},
    {"character": {"0": {"flavorText": "", "subtitles": "I've had enough!:dur:1.36"},
                   "1": {"flavorText": "", "subtitles": "Get struck down, bitch!:dur:2.2"}}})

side = json.load(open(os.path.join(GAME, "mods", MOD, "data/flavorpediaSideData.json"), encoding="utf-8-sig"))["character"]
add("data/flavorpediaSideData.json",
    {"character": {str(i): {"design": c.get("design", ""),
                            "desc": "激战期间到访唐辛子镇的访客。" if "Togarashi" in c.get("place", "") else c.get("desc", ""),
                            "place": "唐辛子镇" if "Togarashi" in c.get("place", "") else c.get("place", "")}
                   for i, c in enumerate(side)}},
    {"character": {str(i): {k: c.get(k, "") for k in ("design", "desc", "place")} for i, c in enumerate(side)}})

for name, mapping in RESULTS.items():
    rel = f"images/results/character/{name}/dialogue.json"
    d = json.load(open(os.path.join(GAME, "mods", MOD, rel.replace("/", os.sep)), encoding="utf-8-sig"))["dialogue"]
    order = {"S": 1, "A": 2, "B": 3, "C": 4, "D": 5}
    texts = ["..." if it.get("rank") not in order else mapping[order[it["rank"]]] for it in d]
    add(rel, {"dialogue": {str(i): {"name": texts[i]} for i in range(len(texts))}},
        {"dialogue": {str(i): {"name": it.get("name", "")} for i, it in enumerate(d)}})

print("完成")
