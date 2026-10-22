# -*- coding: utf-8 -*-
"""菜单/选项界面中文翻译，合并进 汉化底稿/language*-底稿.json。
key 已按游戏 Language.formatKey 归一化（小写、空格转下划线、去冒号等）。"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
UI = os.path.abspath(os.path.join(HERE, "..", "汉化底稿"))

OPTION = {
    # 玩法设置
    "setting_controller_mode": "手柄模式",
    "description_controller_mode": "勾选后可用手柄游玩，\n无需使用键盘。",
    "setting_downscroll": "下落式",
    "description_downscroll": "勾选后音符改为下落式（自上而下），\n简单易懂。",
    "setting_middlescroll": "中置滚动",
    "description_middlescroll": "勾选后你的音符会居中显示。",
    "setting_opponent_notes": "对手音符",
    "description_opponent_notes": "取消勾选后，游玩时会隐藏对手的音符。",
    "setting_ghost_tapping": "空击保护",
    "description_ghost_tapping": "勾选后，在没有可击打音符时按键\n不会判定为失误。",
    "setting_auto_pause": "自动暂停",
    "description_auto_pause": "勾选后，游戏窗口失去焦点时会自动暂停。",
    "setting_results_screen": "结算画面",
    "description_results_screen": "勾选后，完成一周目或自由模式\n每首歌曲后都会显示结算画面。",
    "setting_disable_reset_button": "禁用重置键",
    "description_disable_reset_button": "勾选后，按下重置键不会有任何反应。",
    "setting_hitsound_volume": "打击音音量",
    "description_hitsound_volume": "击中音符时会播放的「咔！」音效。",
    "setting_rating_offset": "判定偏移",
    "description_rating_offset": "调整打出「Sick!」所需的时机偏移，\n数值越高需要打得越晚。",
    "setting_marvelous_hit_window": "Marvelous!! 判定窗口",
    # 打包版里该项名称可能带尾随空格，追加别名键兜底
    "setting_marvelous_hit_window_": "Marvelous!! 判定窗口",
    "setting_marvelous__hit_window": "Marvelous!! 判定窗口",
    "setting_marvelous_hit window": "Marvelous!! 判定窗口",
    # 打包版可能只去掉第一个感叹号
    "setting_marvelous!_hit_window": "Marvelous!! 判定窗口",
    "setting_marvelous!!_hit_window": "Marvelous!! 判定窗口",
    "setting_marvelous_hit\u00a0window": "Marvelous!! 判定窗口",
    # 打包版可能只去掉第一个感叹号
    "setting_marvelous!_hit_window": "Marvelous!! 判定窗口",
    "setting_marvelous!!_hit_window": "Marvelous!! 判定窗口",
    "setting_sick_hit_window_": "Sick! 判定窗口",
    "setting_good_hit_window_": "Good 判定窗口",
    "setting_bad_hit_window_": "Bad 判定窗口",
    "setting_shit_hit_window_": "Shit 判定窗口",
    "description_marvelous_hit_window": "调整打出「Marvelous!!」的时间窗口\n（毫秒）。",
    "description_marvelous_hit_window_": "调整打出「Marvelous!!」的时间窗口\n（毫秒）。",
    "description_marvelous__hit_window": "调整打出「Marvelous!!」的时间窗口\n（毫秒）。",
    "description_marvelous_hit\u00a0window": "调整打出「Marvelous!!」的时间窗口\n（毫秒）。",
    "description_marvelous!_hit_window": "调整打出「Marvelous!!」的时间窗口\n（毫秒）。",
    "description_marvelous!!_hit_window": "调整打出「Marvelous!!」的时间窗口\n（毫秒）。",
    "description_sick_hit_window_": "调整打出「Sick!」的时间窗口（毫秒）。",
    "description_good_hit_window_": "调整打出「Good」的时间窗口（毫秒）。",
    "description_bad_hit_window_": "调整打出「Bad」的时间窗口（毫秒）。",
    "description_shit_hit_window_": "调整打出「Shit」的时间窗口（毫秒）。",
    "setting_sick_hit_window": "Sick! 判定窗口",
    "description_sick_hit_window": "调整打出「Sick!」的时间窗口（毫秒）。",
    "setting_good_hit_window": "Good 判定窗口",
    "description_good_hit_window": "调整打出「Good」的时间窗口（毫秒）。",
    "setting_bad_hit_window": "Bad 判定窗口",
    "description_bad_hit_window": "调整打出「Bad」的时间窗口（毫秒）。",
    "setting_shit_hit_window": "Shit 判定窗口",
    "description_shit_hit_window": "调整打出「Shit」的时间窗口（毫秒）。",
    "setting_safe_frames": "安全帧",
    "description_safe_frames": "调整提前或延后击打音符时\n可容许的帧数。",
    "setting_playback_rate": "播放速度",
    "description_playback_rate": "调整歌曲播放速度（练习与回放用）。",
    "setting_practice_mode": "练习模式",
    "description_practice_mode": "开启练习模式，可自定义起始时间。",
    # 画面设置
    "setting_low_quality": "低画质",
    "description_low_quality": "勾选后关闭部分背景细节，\n缩短读取时间并提升性能。",
    "setting_anti-aliasing": "抗锯齿",
    "description_anti-aliasing": "取消勾选将关闭抗锯齿，\n提升性能但画面更锐利。",
    "setting_shaders": "着色器",
    "description_shaders": "取消勾选将关闭着色器，\n可提升性能但会失去部分视觉效果。",
    "setting_gpu_textures": "GPU 纹理",
    "description_gpu_textures": "勾选后纹理会载入显存，\n减少内存占用。",
    "setting_framerate": "帧率上限",
    "description_framerate": "顾名思义，不用多解释吧？",
    # 界面与视觉
    "setting_note_skins": "音符皮肤：",
    "description_note_skins": "选择你喜欢的音符皮肤。",
    "setting_note_splashes": "打击特效",
    "description_note_splashes": "取消勾选后，击中「Sick!」音符时\n不再显示粒子特效。",
    "setting_hide_hud": "隐藏 HUD",
    "description_hide_hud": "勾选后隐藏大部分界面元素。",
    "setting_subtitles": "字幕",
    "description_subtitles": "开启或关闭本模组的字幕。",
    "setting_flashing_lights": "闪烁光效",
    "description_flashing_lights": "如果你对闪烁光敏感，请取消勾选！",
    "setting_score_text_zoom_on_hit": "得分文字缩放",
    "description_score_text_zoom_on_hit": "取消勾选后，击中音符时\n得分文字不再缩放。",
    "setting_health_bar_transparency": "血条透明度",
    "description_health_bar_transparency": "血条与角色图标的透明程度。",
    "setting_lane_transparency": "轨道透明度：",
    "description_lane_transparency": "音符轨道的透明程度。",
    "setting_timing_indicator": "判定指示：",
    "description_timing_indicator": "显示音符的击打时机。\n简易：非 Marvelous 时显示 EARLY / LATE\n精确：以毫秒显示击打偏差",
    "setting_nps_display": "NPS 显示",
    "description_nps_display": "在信息栏显示当前每秒音符数。",
    "setting_judgement_counter": "判定计数",
    "description_judgement_counter": "显示本曲中各判定的次数。",
    "setting_fps_counter": "FPS 计数器",
    "description_fps_counter": "在信息栏显示当前帧率。",
    "setting_memory_counter": "内存计数器",
    "description_memory_counter": "显示当前内存占用。",
    "setting_peak_counter": "峰值计数器",
    "description_peak_counter": "取消勾选可隐藏峰值计数器。",
    "setting_counter_border": "计数器边框",
    "description_counter_border": "取消勾选可关闭计数器边框，\n略微提升性能。",
    "setting_watermarks": "水印",
    "description_watermarks": "开启或关闭引擎的所有水印。",
    "setting_mouse_navigation": "鼠标导航",
    "description_mouse_navigation": "勾选后可以用鼠标在菜单中导航。",
    # 暂停菜单
    "pause_resume": "继续游戏",
    "pause_restart_song": "重新开始",
    "pause_change_difficulty": "切换难度",
    "pause_options": "选项",
    "pause_exit_to_menu": "退出到菜单",
    "pause_leave_charting_mode": "退出谱面编辑模式",
    "pause_skip_time": "跳过时间",
    "pause_playback_rate": "播放速度",
    "pause_end_song": "结束本曲",
    "pause_toggle_practice_mode": "切换练习模式",
    "pause_toggle_botplay": "切换自动演奏",
    # Modifiers（自由模式修改器）菜单项
    "setting_scroll_type": "滚动类型",
    "setting_scroll_speed": "滚动速度",
    "setting_health_gain": "生命回复",
    "setting_health_loss": "生命损失",
    "setting_instakill_on_miss": "失误即死",
    "setting_randomized_notes": "随机音符",
    "setting_mirrored_notes": "镜像音符",
    "setting_botplay": "自动演奏",
    # Modifiers（自由模式修改器）菜单项
    "setting_scroll_type": "滚动类型",
    "setting_scroll_speed": "滚动速度",
    "setting_health_gain": "生命回复",
    "setting_health_loss": "生命损失",
    "setting_instakill_on_miss": "失误即死",
    "setting_randomized_notes": "随机音符",
    "setting_mirrored_notes": "镜像音符",
    "setting_botplay": "自动演奏",
    # 选项主页菜单项（OptionsState 分发标签）
    "options_controls": "按键设置",
    "options_gameplay": "玩法设置",
    "options_graphics": "画面设置",
    "options_visuals_and_ui": "画面与界面",
    "options_adjust_delay_and_combo": "调整延迟与连击",
    "options_mods_and_dlc": "模组与 DLC",
    # 其他
    "gameplay_menu": "玩法",
    "graphics_menu": "画面",
    "visuals_menu": "画面与界面",
    "delay_beat_hit": "拍点！",
    "combo_rating_offset": "判定偏移",
    "combo_numbers_offset": "数字偏移",
    "delay_current_offset": "当前偏移",
    "combo_offset": "连击偏移",
    "note_delay": "音符/拍点延迟",
    "switch_on_accept": "按确认键切换",
}

GAMEPLAY = {
    "setting_scrolltype-multiplicative": "多重叠加",
    "setting_scrolltype-constant": "恒定",
    "setting_scrolltype-multiplicative": "多重叠加",
    "setting_scrolltype-constant": "恒定",
    "select_personal_best": "个人最佳",
    "select_rank": "排名",
    "score_rating": "评级",
    "player_indicator": "您",
    "botplay": "自动演奏",
    "score_score": "得分",
    "score_misses": "失误",
    "results_highest_combo": "最高连击",
}

FLAVOR = {
    "achievement_awarded": "已解锁！",
    "achievement_desclocked": "此项尚未解锁。达成相应条件后再来看看吧！",
    "achievement_namelocked": "未知",
    "close_game": "确定要关闭游戏吗？",
    "flavorpediaside_blank": "空白",
    "flavorpediaside_notfound": "未找到",
    "freeplay_resetscore_desc": "重置以下曲目的得分：",
}

# 注意：键要再走一次 formatKey，防止手写 key 与游戏侧不一致
import re


def fmt_key(k):
    k = k.replace(" ", "_")
    k = re.sub(r"[~&\\;:<>#]", "", k)
    k = re.sub("[.,'\"%?!\u00a1]", "", k)
    return k.lower().strip()


def merge(cat, mapping):
    p = os.path.join(UI, f"language{cat}-底稿.json")
    d = json.load(open(p, encoding="utf-8"))
    cur = {it["key"]: it["value"] for it in d["map"]}
    for k, v in mapping.items():
        cur[fmt_key(k)] = v
    d["map"] = [{"key": k, "value": v} for k, v in sorted(cur.items())]
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"language{cat}: {len(d['map'])} keys")


merge("Option", OPTION)
merge("Gameplay", GAMEPLAY)
merge("Flavor", FLAVOR)
