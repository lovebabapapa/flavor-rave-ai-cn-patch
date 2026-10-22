# -*- coding: utf-8 -*-
"""收尾修订：对译文/成品做少量字面替换（专名、固定术语）。
用法: python postfix.py <目标目录> [--apply]"""
import json, os, sys, glob

REPL = {
    "甜（Sweet）": "Sweet",
    "酸（Sour）": "Sour",
    "待定团队": "Team TBD",
    # 亲属称谓性别修正：Sour 是 Umami 的表弟，Umami 是 Sour 的表姐
    "冷静点，表妹": "冷静点，表弟",
    "打住，表妹": "打住，表弟",
    "我这个小表妹可担心坏了": "我这个小表弟可担心坏了",
    "回头见，表妹": "回头见，表姐",
    "我表哥打工的那家汉堡店": "我表姐打工的那家汉堡店",
    # 台词修正
    "这姑娘真是特别得紧": "这姑娘可真是与众不同",
    "格林尼": "Greeny",
    "灰云": "烟云",
    "为其增色添彩的灰云": "为其增色添彩的烟云",
    # 间章4 场景时间标记
    "[Saturday]": "[星期六]",
    "[Sunday]": "[星期日]",
    "[The Next Saturday...]": "[下一个星期六……]",
    # 台词润色
    "我是不是打扰到你街头发脾气了？": "我是不是打扰到你在街头发脾气了？",
    "——街头发脾气？！": "——在街头发脾气？！",
    "你在“展销室”一举成名": "你在“Showman 展厅”一举成名",
    "你居然 STILL 能靠自己那 STUPID 至极的言行全身而退": "你居然还是能靠那套蠢到家的言行全身而退",
    # 间章6：酸小子 = Sour（英文 "Sour me boy" / "[Sour begins...]"）
    "我的酸小子！": "我的 Sour 小子！",
    "[酸小子开始穿行于科里安达镇……]": "[Sour 开始在科里安达镇穿行……]",
    "酸小子无法判断": "Sour 无法判断",
    "酸小子": "Sour",
    # 间章7：单字/意译人名改回英文
    "甜……原来如此。": "Sweet……原来如此。",
    "我没事，酸糖。": "我没事，Sour。",
    "酸……Sour！": "S——Sour！",
    # 酸小子保留为海盗对 Sour 的专属称呼（用户要求）
    "我的 Sour 小子！": "我的酸小子！",
    # 联动1：GlazeCorp 公司名与 Glaze the 11th 人名保留英文；Enzync 统一为恩辛克城
    "首席执行官官格莱兹十一世": "首席执行官 Glaze the 11th",
    "格莱兹集团（GlazeCorp）": "GlazeCorp",
    "格莱兹集团": "GlazeCorp",
    "格莱兹十一世": "Glaze the 11th",
    "恩赞克市": "恩辛克城",
    "恩赞克": "恩辛克",
    "恩赞电视台（EnZ-TV）": "EnZ 电视台",
    "恩赞电视台": "EnZ 电视台",
    # 半英半中台词修正
    "你什么时候 ready，我就什么时候 ready！": "你什么时候准备好，我就什么时候准备好！",
    "你们啥时候 ready，我们就啥时候开干！": "你们什么时候准备好，我们就什么时候开干！",
    "见鬼地——超 ready！": "见鬼——太准备好了！",
    "跟鬼魂们一起 vibe": "跟鬼魂们一起嗨",
    "“夜之 crew”": "“Night Crew”",
    # 特别奖励篇：人名保留英文；BF 穿越前不会说人话，其台词不译
    "“男友”和“女友”": "Boyfriend 和 Girlfriend",
    "表演大师先生": "Showman 先生",
    "表演大师": "Showman",
    "我是芬奇，我身边的这位美女就是我的女孩索西！": "我是 Funky，这位是我的女孩 Saucy！",
    "芬奇和索西！": "Funky 和 Saucy！",
    "芬奇": "Funky",
    "索西": "Saucy",
    "斯奇·德普。": "Skee dep.",
    "布普·迪？": "Boop dee?",
    "贝普。": "Bep.",
    # 工作职员表：人名一律还原英文
    "达特戴维": "DatDavi",
    "诺伊奇": "Noichi",
    "可可帕夫斯": "Cocopuffs",
    "里克斯FX": "RixFX",
    "克雷加托": "Kreagato",
    "吉恩奇普": "Genechip",
    "泽罗": "Zeroh",
    "卡梅克斯": "Kamex",
    "托尼·阿斯特罗": "Tony Astro",
    "甜酸配音": "Sweet & Tangy 配音",
    "湍流配音": "Torrent 配音",
    "尼特罗配音": "Nitro 配音",
    "TBD酱配音": "TBD-tan 配音",
    "萨鲁基与药剂与香料团队": "Saruky & The Potions n' Spices Team",
    "萨鲁基": "Saruky",
    "星尘": "Space Dust",
    "梅洛迪": "Mellodi",
    "莉莲": "Lillian",
    "暗影马里奥": "Shadow Mario",
    "阿呜": "Awoo",
    "宾普基": "Binpuki",
    "科德克斯": "Codexes",
    "辛-桑组合主菜单歌曲": "SynSun 主菜单歌曲",
    # 角色介绍里的「中文（English）」人名注释 → 只留英文；地名则只留中文
    "甜味（Sweet）": "Sweet",
    "甜糖（Sweet）": "Sweet",
    "酸糖（Sour）": "Sour",
    "桑妮（Sunny）": "Sunny",
    "SynSun（辛桑）": "SynSun",
    "辛桑": "SynSun",
    "桑妮": "Sunny",
    "桑妮（Syn）": "Syn",
    "合成君（Syn）": "Syn",
    "洪流（Torrent）": "Torrent",
    "洪流：": "Torrent：",
    "，桑妮。": "，Sunny。",
    "尼特罗（Nitro）": "Nitro",
    "侣麸皮酱（Furikake）": "Furikake",
    "芳萝尔（Floral）": "Floral",
    "男友（Boyfriend）": "Boyfriend",
    "女友（Girlfriend）": "Girlfriend",
    "酸甜组合（Sweet and Sour）": "Sweet and Sour",
    "是酸与甜（Sour and Sweet）": "Sour and Sweet",
    "恩辛克市（Enzync City）": "恩辛克城",
    "恩辛克城（Enzync City）": "恩辛克城",
    "唐辛子镇（Togarashi Town）": "唐辛子镇",
    "辛克码头（Enzync Dock）": "恩辛克码头",
    # Rhythm Robo（Tioda & Pyroller）姓名还原 / 去重括号
    "蒂奥迪娅": "Tioda",
    "派罗勒": "Pyroller",
    "Showman（Showman）": "Showman",
    "Sweet（Sweet）": "Sweet",
    '"text": "solr_powr.ogg"': '"text": "Solr Powr"',
    # Rhythm Robo（Tioda & Pyroller）姓名还原 / 去重括号
    "蒂奥迪娅": "Tioda",
    "派罗勒": "Pyroller",
    "Showman（Showman）": "Showman",
    "Sweet（Sweet）": "Sweet",
    '"text": "solr_powr.ogg"': '"text": "Solr Powr"',
    # —— 用户校对反馈（10-22）——
    "Sweet & Sour 夏日混音": "酸甜夏日混音",
    "彻底放任自己？": "彻底放开自己？",
    "“放任自己”……真的就这么简单？": "“放开自己”……真的就这么简单？",
    "放任自己……？": "放开自己……？",
    "普通服务器上的散兵游勇": "普通服务器上随处可见的闲散玩家",
    "嘿，恩辛克城的各位！": "嘿，恩辛克！",
    "让我们一起律动起来，恩辛克城！": "让我们一起律动起来，恩辛克！",
    "如此 spectacularly（大获成功）地收场了": "居然如此漂亮地收场了",
    "但 showroom 外面": "但展厅外面",
    "Sweet & Sour（Sweet and Sour）": "Sweet & Sour",
    "酸糖": "Sour",
    "辣妹": "Spicy",
    "Sunny、桑桑、SD": "Sunny、SD",
    "全都离开了恩辛克……": "全都离开了恩辛克地区……",
    "corporate suit guys（公司西装男）": "西装革履的公司人",
    "赫蒂叔叔餐厅": "哈蒂大叔快餐店",
    "这是Enzync新手说唱歌手": "这是恩辛克地区的新手说唱歌手",
    "想 soon 和 Syn 一起": "想尽快和 Syn 一起",
    "[Monday]": "[星期一]",
    "[Tuesday]": "[星期二]",
    # 名称变体统一：恩兹尼克 / 豪蒂大叔 / Showman 表演厅
    "恩兹尼克市": "恩辛克城",
    "恩兹尼克": "恩辛克",
    "豪蒂大叔": "哈蒂大叔",
    " hearty叔叔餐厅": "哈蒂大叔快餐店",
    "hearty叔叔餐厅": "哈蒂大叔快餐店",
    "Showman 表演厅": "Showman 展厅",
    # 台词修正（校对第二轮）
    "咱们得再即兴 jam 一段！": "咱们得再即兴合奏一段！",
    "也想特别 spotlight（ spotlight：聚光灯/聚焦）一下": "也想特别推荐一下",
    "一项VERY重要的任务": "一项非常重要的任务",
    "Gummy 的“任务”fffphhh…… weeeghhh…… f-failed了……妈妈和爸爸一定会s-so伤心的……":
        "Gummy 的“任务”呃呃呃…… 呜呃…… 失、失败了……妈妈和爸爸一定会超、超伤心的……",
    # 名称变体统一：恩兹尼克 / 豪蒂大叔 / Showman 表演厅
    "恩兹尼克市": "恩辛克城",
    "恩兹尼克": "恩辛克",
    "豪蒂大叔": "哈蒂大叔",
    " hearty叔叔餐厅": "哈蒂大叔快餐店",
    "hearty叔叔餐厅": "哈蒂大叔快餐店",
    "Showman 表演厅": "Showman 展厅",
    # 台词修正（校对第二轮）
    "咱们得再即兴 jam 一段！": "咱们得再即兴合奏一段！",
    "也想特别 spotlight（ spotlight：聚光灯/聚焦）一下": "也想特别推荐一下",
    "一项VERY重要的任务": "一项非常重要的任务",
    "Gummy 的“任务”fffphhh…… weeeghhh…… f-failed了……妈妈和爸爸一定会s-so伤心的……":
        "Gummy 的“任务”呃呃呃…… 呜呃…… 失、失败了……妈妈和爸爸一定会超、超伤心的……",
    # 播报员/百科里的意译人名
    "酸酱": "Sour",
    "甜酱": "Sweet",
    "辣酱": "Spicy",
    # 播报员/百科里的意译人名
    "酸酱": "Sour",
    "甜酱": "Sweet",
    "辣酱": "Spicy",
    # Saffron 人名被意译
    "藏红花配音": "Saffron 配音",
    "—藏红花！": "——Saffron！",
    "藏红花": "Saffron",
    # Sour 被意译成「酸橙」
    "酸橙": "Sour",
    # 画廊标题里的角色名被意译
    "CG图 - 芥末": "CG图 - Wasabi",
    # 画廊标题里的角色名被意译
    "CG图 - 芥末": "CG图 - Wasabi",
    # Sour 被意译成「酸果酱」
    "酸果酱": "Sour",
    # Sour 被意译成「酸果酱」
    "酸果酱": "Sour",
    # 周目分组名统一（原作者笔误：DLC Collab Stories）
    "DLC 联动故事": "联动故事",
    # 周目分组名统一（原作者笔误：DLC Collab Stories）
    "DLC 联动故事": "联动故事",
    # Togarashi Town 译名统一（唐辛子=日语辣椒，与 Tangy 双关一致）
    "托加拉希": "唐辛子",
    # Togarashi Town 译名统一（唐辛子=日语辣椒，与 Tangy 双关一致）
    "托加拉希": "唐辛子",
    # 地名统一
    "恩津克": "恩辛克",
    "爱恩辛克": "恩辛克",
    "唐辛镇": "唐辛子镇",
    "普雷希特": "普雷希茨",
}

# 需要正则处理的地名（避免「科里安达」被二次替换）
import re as _re
REGEX_REPL = [
    (r"科里安(?!达)", "科里安达"),
    # 专名前后补空格（中英混排可读性）
    (r"GlazeCorp(?=[\u4e00-\u9fff])", "GlazeCorp "),
    (r"(?<=[\u4e00-\u9fff])GlazeCorp", " GlazeCorp"),
    (r"Glaze the 11th(?=[\u4e00-\u9fff])", "Glaze the 11th "),
    (r"(?<=[\u4e00-\u9fff])Glaze the 11th", " Glaze the 11th"),
    (r"(?<=[\u4e00-\u9fff])EnZ", " EnZ"),
    # 角色名前后补空格（避免「不再是Boyfriend了」这种粘连）
    (r"(?<=[\u4e00-\u9fff])(?=(?:Boyfriend|Girlfriend|Funky|Saucy|Showman|Sweet|Sour|Spicy|Smoky|Savory|Umami|Salty|Tangy|Bitter|Saffron|Sun-Dried|Synthetic|Tioda|Pyroller)(?![A-Za-z]))", " "),
    (r"((?:Boyfriend|Girlfriend|Funky|Saucy|Showman|Sweet|Sour|Spicy|Smoky|Savory|Umami|Salty|Tangy|Bitter|Saffron|Sun-Dried|Synthetic|Tioda|Pyroller))(?=[\u4e00-\u9fff])", r"\1 "),
    (r"[ \t]{2,}", " "),
]
target = sys.argv[1]
apply = "--apply" in sys.argv
hits = 0; files = 0
for f in glob.glob(os.path.join(target, "**", "*.json"), recursive=True):
    try:
        raw = open(f, encoding="utf-8-sig").read()
    except Exception:
        continue
    new = raw
    for pat, rep in REGEX_REPL:
        new = _re.sub(pat, rep, new)
    for a, b in REPL.items():
        if a in new:
            hits += new.count(a)
            new = new.replace(a, b)
    if new != raw:
        files += 1
        if apply:
            open(f, "w", encoding="utf-8").write(new)
print(f"{'已写' if apply else '预览'}：{hits} 处替换，涉及 {files} 个文件 ({target})")
