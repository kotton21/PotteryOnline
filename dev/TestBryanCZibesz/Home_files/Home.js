// Created by iWeb 3.0.4 local-build-20160125

setTransparentGifURL('Media/transparent.gif');function applyEffects()
{var registry=IWCreateEffectRegistry();registry.registerEffects({stroke_0:new IWStrokeParts([{rect:new IWRect(-1,1,2,539),url:'Home_files/stroke.png'},{rect:new IWRect(-1,-1,2,2),url:'Home_files/stroke_1.png'},{rect:new IWRect(1,-1,701,2),url:'Home_files/stroke_2.png'},{rect:new IWRect(702,-1,2,2),url:'Home_files/stroke_3.png'},{rect:new IWRect(702,1,2,539),url:'Home_files/stroke_4.png'},{rect:new IWRect(702,540,2,2),url:'Home_files/stroke_5.png'},{rect:new IWRect(1,540,701,2),url:'Home_files/stroke_6.png'},{rect:new IWRect(-1,540,2,2),url:'Home_files/stroke_7.png'}],new IWSize(703,541)),stroke_1:new IWEmptyStroke()});registry.applyEffects();}
function hostedOnDM()
{return false;}
function onPageLoad()
{loadMozillaCSS('Home_files/HomeMoz.css')
detectBrowser();adjustLineHeightIfTooBig('id1');adjustFontSizeIfTooBig('id1');adjustLineHeightIfTooBig('id2');adjustFontSizeIfTooBig('id2');Widget.onload();fixupAllIEPNGBGs();fixAllIEPNGs('Media/transparent.gif');applyEffects()}
function onPageUnload()
{Widget.onunload();}
