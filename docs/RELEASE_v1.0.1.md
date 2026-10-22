# v1.0.1 — 补全全部死亡台词

> 修正 v1.0.0 的一个整块遗漏：**所有角色的 GAME OVER 语音字幕此前未翻译**。
> 适用游戏版本仍是 **FNF: Flavor Rave V2.5.2 FULLY BREWED!**

---

## 🩹 这个版本修了什么

### 1. 死亡台词全部中文化（33 个角色 / 74 句）

之前整个 GAME OVER 界面的角色语音字幕都是英文——因为文本存放在 `characters/gameover/*.json` 的 `goSound` 字段里，不在常规的 `data/` 目录，第一版抽取时整块漏掉了。

本版已全部补上，**包含所有 DLC 的死亡台词**：

| 范围 | 角色 |
|---|---|
| 基础游戏（16） | Sour / Sweet / Spicy / Smoky / Savory / Umami / Sun-Dried / Nikki / Rika / Daisy / Troubleshootin / Togarashi / Showman 等 |
| DLC1（5） | Ace / Bitter / Funkin / Salty / Tangy |
| Lovers Together（3） | Cerulean / Eclipsin / SynSun |
| Taste of Revenge（2） | Bree / Tabi |
| Chillin' & Thrillin'（2） | Onion / Pure |
| Masters of the Craft（2） | Crispy / Oil |
| Younger Generation（2） | Gummy / Saff |
| Double-Stacked（1） | Rhythmrobo（含 Tioda / Pyroller 对话） |

细节：
- **每一句的语音计时（`:dur:`）与原版完全一致**，多句台词按原节奏分段显示
- Savory 的西班牙语原台词按中文习惯处理，故障拟声（Synthetic）、长段暴走台词（Oil / Saff）也逐句还原语气
- 群像台词保留说话人前缀（Macy / Zuki、Sekaiya / Luna…）

### 2. 修复「酸莓」→「Sour」

timeshock 章节有一句把 Sour 误译成「酸莓」，已修正并加入全局术语规则。

---

## 📦 下载

| 文件 | 说明 |
|---|---|
| `FR_CN_patch_v1.0.1.zip` | 补丁本体（316 个文件，487 KB） |
| `FR_CN_patch_v1.0.1.zip.sha256` | 校验文件 |

```
SHA256: 09a1264596c90d8f8b3df0fa030e719e4a938a106e26cbf7c32e4c0ee9e9bed6
```

校验方法（文件所在目录打开 cmd）：

```cmd
certutil -hashfile FR_CN_patch_v1.0.1.zip SHA256
```

输出与上方一致即为完整下载。

---

## 🔧 升级方法

**直接覆盖即可**，不需要卸载旧版、不影响存档：

```
把 FR_CN_patch_v1.0.1.zip 内的文件按相同路径覆盖到游戏根目录
```

> 如果你还没装过本补丁，直接按上面的方式覆盖也行（无需先装 v1.0.0）。

---

## 🤖 关于 AI

本补丁译文由 AI 批量生成 + 人工校对与修订。发现错译欢迎提 [译误反馈](https://github.com/lovebabapapa/flavor-rave-ai-cn-patch/issues/new?template=translation-error.yml)。

## 🔗 原作

- 游戏页面（GameBanana）：https://gamebanana.com/mods/410436
- 上游公开源码：https://github.com/Jorge-SunSpirit/Flavor-Rave-Public

> 本补丁不含游戏本体，请支持正版。
