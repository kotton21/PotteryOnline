// Created by iWeb 3.0.4 local-build-20160125

setTransparentGifURL('Media/transparent.gif');function applyEffects()
{var registry=IWCreateEffectRegistry();registry.registerEffects({stroke_0:new IWEmptyStroke(),stroke_1:new IWStrokeParts([{rect:new IWRect(-1,1,2,278),url:'CV_files/stroke.png'},{rect:new IWRect(-1,-1,2,2),url:'CV_files/stroke_1.png'},{rect:new IWRect(1,-1,418,2),url:'CV_files/stroke_2.png'},{rect:new IWRect(419,-1,2,2),url:'CV_files/stroke_3.png'},{rect:new IWRect(419,1,2,278),url:'CV_files/stroke_4.png'},{rect:new IWRect(419,279,2,2),url:'CV_files/stroke_5.png'},{rect:new IWRect(1,279,418,2),url:'CV_files/stroke_6.png'},{rect:new IWRect(-1,279,2,2),url:'CV_files/stroke_7.png'}],new IWSize(420,280))});registry.applyEffects();}
function hostedOnDM()
{return false;}
function onPageLoad()
{loadMozillaCSS('CV_files/CVMoz.css')
adjustLineHeightIfTooBig('id1');adjustFontSizeIfTooBig('id1');adjustLineHeightIfTooBig('id2');adjustFontSizeIfTooBig('id2');adjustLineHeightIfTooBig('id3');adjustFontSizeIfTooBig('id3');adjustLineHeightIfTooBig('id4');adjustFontSizeIfTooBig('id4');adjustLineHeightIfTooBig('id5');adjustFontSizeIfTooBig('id5');Widget.onload();fixAllIEPNGs('Media/transparent.gif');applyEffects()}
function onPageUnload()
{Widget.onunload();}
