// Created by iWeb 3.0.4 local-build-20160125

function createMediaStream_id3()
{return IWCreatePhotocast("http://www.bryanczibesz.com/Bryan_Czibesz/Portfolio/Pages/Operations_files/rss.xml",false);}
function initializeMediaStream_id3()
{createMediaStream_id3().load('http://www.bryanczibesz.com/Bryan_Czibesz/Portfolio/Pages',function(imageStream)
{var entryCount=imageStream.length;var headerView=widgets['widget1'];headerView.setPreferenceForKey(imageStream.length,'entryCount');NotificationCenter.postNotification(new IWNotification('SetPage','id3',{pageIndex:0}));});}
function layoutMediaGrid_id3(range)
{createMediaStream_id3().load('http://www.bryanczibesz.com/Bryan_Czibesz/Portfolio/Pages',function(imageStream)
{if(range==null)
{range=new IWRange(0,imageStream.length);}
IWLayoutPhotoGrid('id3',new IWPhotoGridLayout(4,new IWSize(179,179),new IWSize(179,112),new IWSize(184,306),27,27,0,new IWSize(0,0)),new IWStrokeParts([{rect:new IWRect(-1,1,2,177),url:'Operations_files/stroke.png'},{rect:new IWRect(-1,-1,2,2),url:'Operations_files/stroke_1.png'},{rect:new IWRect(1,-1,177,2),url:'Operations_files/stroke_2.png'},{rect:new IWRect(178,-1,2,2),url:'Operations_files/stroke_3.png'},{rect:new IWRect(178,1,2,177),url:'Operations_files/stroke_4.png'},{rect:new IWRect(178,178,2,2),url:'Operations_files/stroke_5.png'},{rect:new IWRect(1,178,177,2),url:'Operations_files/stroke_6.png'},{rect:new IWRect(-1,178,2,2),url:'Operations_files/stroke_7.png'}],new IWSize(179,179)),imageStream,range,null,null,1.000000,{backgroundColor:'rgb(192, 192, 192)',reflectionHeight:0,reflectionOffset:2,captionHeight:100,fullScreen:1,transitionIndex:2},'../../Media/slideshow.html','widget1','widget2','widget3')});}
function relayoutMediaGrid_id3(notification)
{var userInfo=notification.userInfo();var range=userInfo['range'];layoutMediaGrid_id3(range);}
function onStubPage()
{var args=window.location.href.toQueryParams();parent.IWMediaStreamPhotoPageSetMediaStream(createMediaStream_id3(),args.id);}
if(window.stubPage)
{onStubPage();}
setTransparentGifURL('../../Media/transparent.gif');function applyEffects()
{var registry=IWCreateEffectRegistry();registry.registerEffects({stroke_0:new IWEmptyStroke()});registry.applyEffects();}
function hostedOnDM()
{return false;}
function onPageLoad()
{IWRegisterNamedImage('comment overlay','../../Media/Photo-Overlay-Comment.png')
IWRegisterNamedImage('movie overlay','../../Media/Photo-Overlay-Movie.png')
loadMozillaCSS('Operations_files/OperationsMoz.css')
adjustLineHeightIfTooBig('id1');adjustFontSizeIfTooBig('id1');adjustLineHeightIfTooBig('id2');adjustFontSizeIfTooBig('id2');NotificationCenter.addObserver(null,relayoutMediaGrid_id3,'RangeChanged','id3')
adjustLineHeightIfTooBig('id4');adjustFontSizeIfTooBig('id4');adjustLineHeightIfTooBig('id5');adjustFontSizeIfTooBig('id5');Widget.onload();fixAllIEPNGs('../../Media/transparent.gif');applyEffects()
initializeMediaStream_id3()}
function onPageUnload()
{Widget.onunload();}
