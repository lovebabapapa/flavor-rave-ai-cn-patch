function onCreate()
	makeAnimatedLuaSprite('DramaBG', 'stages/brandy/DramaBG', 0, 0);
	addAnimationByPrefix('DramaBG', 'idle', 'OnionBG_', 4, true);
	playAnim('DramaBG', 'idle');
	setObjectCamera('DramaBG', 'effect');
	setProperty('DramaBG.alpha', 1);
    screenCenter('DramaBG');
	addLuaSprite('DramaBG', false);
	
	makeAnimatedLuaSprite('onyosketch', 'stages/brandy/onyosketch', 400, 30);
	addAnimationByPrefix('onyosketch', 'idle', 'onyo', 4, true);
	playAnim('onyosketch', 'idle');
	scaleObject('onyosketch', 1, 1);
	addLuaSprite('onyosketch', false);
	setObjectCamera('onyosketch', 'effect');
	setProperty('onyosketch.alpha', 0.0001);
	
	makeAnimatedLuaSprite('7sketch', 'stages/brandy/7sketch', 300, 0);
	addAnimationByPrefix('7sketch', 'idle', '7s', 4, true);
	playAnim('7sketch', 'idle');
	scaleObject('7sketch', 1, 1);
	addLuaSprite('7sketch', false);
	setObjectCamera('7sketch', 'effect');
	setProperty('7sketch.alpha', 0.0001);

	makeAnimatedLuaSprite('introdramatext', 'stages/brandy/introtext', 0, 0);
	addAnimationByPrefix('introdramatext', 'idle', 'RestlessIntroText_', 24, false);
	addLuaSprite('introdramatext', false);
	setObjectCamera('introdramatext', 'effect');
	setProperty('introdramatext.alpha', 0.0001);
    screenCenter('introdramatext');
	
	makeAnimatedLuaSprite('dramatext', 'stages/brandy/midsongtext', 0, 0);
	addAnimationByPrefix('dramatext', 'idle', 'RestlessMidSongText_', 24, false);
	addLuaSprite('dramatext', false);
	setObjectCamera('dramatext', 'effect');
	setProperty('dramatext.alpha', 0.0001);
    screenCenter('dramatext');

	makeAnimatedLuaSprite('hands', 'stages/brandy/hands', 0, 0);
	addAnimationByPrefix('hands', 'idle', 'hands', 4, true);
	playAnim('hands', 'idle');
	setObjectCamera('hands', 'effect');
	setProperty('hands.alpha', 1);
    screenCenter('hands');
	setProperty('hands.alpha', 0.0001);
	addLuaSprite('hands', false);

	makeAnimatedLuaSprite('gritover', 'stages/brandy/gritover', 0, 0);
	addAnimationByPrefix('gritover', 'idle', 'gritoverlay', 4, true);
	playAnim('gritover', 'idle');
	setObjectCamera('gritover', 'effect');
	setProperty('gritover.alpha', 1);
    screenCenter('gritover');
	setProperty('gritover.alpha', 0.0001);
	addLuaSprite('gritover', false);

	makeLuaSprite('vin', 'stages/brandy/vingette', -0, -0);
	setScrollFactor('vin', 1, 1);
	scaleObject('vin', 1, 1);
	addLuaSprite('vin', false);
	setObjectCamera('vin', 'effect');
    screenCenter('vin');
	
	makeLuaSprite('blackmaskly', '', -100, -100);
    makeGraphic('blackmaskly', 1280*2, 720*2, '000000');
    setScrollFactor('blackmaskly', 0, 0);
    screenCenter('blackmaskly');
	setObjectCamera('blackmaskly', 'effect')
	addLuaSprite('blackmaskly', true);
	
	makeAnimatedLuaSprite('embers2', 'stages/brandy/embers', posX, posY);
	addAnimationByPrefix('embers2', 'idle', 'Embers_', 22, true);
	playAnim('embers2', 'idle');
	setObjectCamera('embers2', 'effect')
	addLuaSprite('embers2', true);
	scaleObject('embers2', 2, 2);
	setProperty('embers2.alpha', 0.0001);
    screenCenter('embers2');

	-- 中文歌词字幕（前段 flavorHUD 移出屏幕期间使用）
	makeLuaText('cnSub', '', 1280, 0, 600);
	setTextSize('cnSub', 26);
	setTextColor('cnSub', 'FFFFFF');
	setTextBorder('cnSub', 2, '000000');
	setTextAlignment('cnSub', 'center');
	setProperty('cnSub.alpha', 0.0001);
	addLuaText('cnSub');
end

function dramalights(num)
	if num == '1' then
		doTweenAlpha('blackmaskly', 'blackmaskly', 0.15, 0.3);
	end
	if num == '2' then
		doTweenAlpha('blackmaskly', 'blackmaskly', 1, 1.4);
	end
	if num == '3' then
		doTweenAlpha('blackmaskly', 'blackmaskly', 0.7, 0.3);
	end
end

function onStepHit()
	if curStep == 12 then
	barY = 1280;
        if downscroll then    barY = -200;    end
		doTweenY("flavorBar", "flavorHUD", barY, 1.2, "circinout")
		doTweenAlpha('embers2', 'embers2', 1, 4);
	end
	if curStep == 116 then
		doTweenAlpha('embers2', 'embers2', 0.0001, 6);
		doTweenAlpha('blackmaskly', 'blackmaskly', 0.0001, 4);
	end
	if curStep == 148 then
		playAnim('introdramatext', 'idle');
		setProperty('introdramatext.alpha', 1);
		doTweenAlpha('onyosketch', 'onyosketch', 1, 2);
		setTextString('cnSub', '仇恨生自如此古老的地方……');
		setProperty('cnSub.alpha', 1);
	end
	if curStep == 180 then
		setTextString('cnSub', '被枷锁锁住，我等得已经累了……');
	end
	if curStep == 212 then
		setTextString('cnSub', '等你亲口说，我……');
	end
	if curStep == 248 then
		doTweenAlpha('onyosketch', 'onyosketch', 0.0001, 3);
	end
	if curStep == 262 then
		setTextString('cnSub', '……够了。');
	end
	if curStep == 272 then
		doTweenAlpha('introdramatext', 'introdramatext', 0.0001, 2);
		doTweenAlpha('blackmaskly', 'blackmaskly', 1, 3);
		setProperty('cnSub.alpha', 0.0001);
	end
	if curStep == 310 then
		setProperty('camFollow.x', 1102);
		setProperty('camFollow.y', 250);
		setProperty('isCameraOnForcedPos', true);
	end
	if curStep == 320 then
		setProperty('DramaBG.alpha', 0.0001);
		setProperty('blackmaskly.alpha', 0.0001);
	end
	if curStep == 350 then
		setProperty('camFollow.x', 172);
		setProperty('camFollow.y', 140);
	end
	if curStep == 382 then
		setProperty('camFollow.x', 1042);
		setProperty('camFollow.y', 600);
	end
	if curStep == 416 then
		setProperty('isCameraOnForcedPos', false);
	end
	if curStep == 440 then
		barYeee = 626.4;
		if downscroll then	barYeee = 21.6;	end
		doTweenY("flavorBar", "flavorHUD", barYeee, 0.8, "circinout")
	end
	if curStep == 690 then
		doTweenAlpha('blackmaskly', 'blackmaskly', 1, 1.5);
	end
	if curStep == 706 then
		doTweenColor('bg', 'bg', '4D2727', '0.0001', 'linear')
		doTweenColor('maindesk', 'maindesk', '4D2727', '0.0001', 'linear')
	end
	if curStep == 832 then
		doTweenAlpha('embers', 'embers', 1, 4);
		setProperty('aura.alpha', 1);
	end
	if curStep == 960 then
		doTweenAlpha('embers', 'embers', 0.0001, 1);
		setProperty('aura.alpha', 0.0001);
		doTweenColor('bg', 'bg', 'FFFFFF', '0.0001', 'linear')
		doTweenColor('maindesk', 'maindesk', 'FFFFFF', '0.0001', 'linear')
	end
	if curStep == 1164 then
		doTweenAlpha('blackmaskly', 'blackmaskly', 1, 1);
	end
	if curStep == 1184 then
		setProperty('DramaBG.alpha', 1);
		doTweenAlpha('blackmaskly', 'blackmaskly', 0.0001, 2);
	end
	if curStep == 1200 then
		doTweenAlpha('onyosketch', 'onyosketch', 1, 2);
	end
	if curStep == 1248 then
		doTweenX('xonyosketch', 'onyosketch', 650, 8, "circout");
		doTweenX('x7sketch', '7sketch', 50, 8, "circout");
	end
	if curStep == 1260 then
		doTweenAlpha('7sketch', '7sketch', 1, 4);
	end
	if curStep == 1368 then
		doTweenAlpha('7sketch', '7sketch', 0.0001, 2);
		doTweenAlpha('onyosketch', 'onyosketch', 0.0001, 2);
	end
	if curStep == 1383 then
		playAnim('dramatext', 'idle');
		setProperty('dramatext.alpha', 1);
	end
	if curStep == 1424 then
		doTweenAlpha('blackmaskly', 'blackmaskly', 1, 1.4);
		doTweenAlpha('dramatext', 'dramatext', 0.0001, 1);
	end
	if curStep == 1440 then
		setProperty('DramaBG.alpha', 0.0001);
		setProperty('blackmaskly.alpha', 0.0001);
		setProperty('firebg.alpha', 1);
		setProperty('embers.alpha', 1);
		setProperty('gritover.alpha', 1);
		setProperty('maindesk.alpha', 0.0001);
		setProperty('maindeskblack.alpha', 1);
	end
	if curStep == 1592 then
		doTweenAlpha('hands', 'hands', 1, 3);
	end
	if curStep == 1614 then
		doTweenAlpha('7sbig', '7sbig', 1, 3);
	end
	if curStep == 1696 then
		setProperty('gritover.alpha', 0.0001);
		setProperty('blackmaskly.alpha', 1);
		setProperty('firebg.alpha', 0.0001);
		setProperty('hands.alpha', 0.0001);
		setProperty('7sbig.alpha', 0.0001);
		setProperty('maindesk.alpha', 1);
		setProperty('maindeskblack.alpha', 0.0001);
		doTweenColor('bg', 'bg', '4D2727', '0.0001', 'linear')
		doTweenColor('maindesk', 'maindesk', '4D2727', '0.0001', 'linear')
	end
	if curStep == 1840 then
		doTweenAlpha('blackmaskly', 'blackmaskly', 1, 4);
	end
end

