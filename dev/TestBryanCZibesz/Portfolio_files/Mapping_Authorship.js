// Created by iWeb 3.0.4 local-build-20160125

function createMediaStream_id2()
{return IWCreatePhotocast("http://www.bryanczibesz.com/Bryan_Czibesz/Portfolio/Pages/Mapping_Authorship_files/rss.xml",false);}
function initializeMediaStream_id2()
{createMediaStream_id2().load('http://www.bryanczibesz.com/Bryan_Czibesz/Portfolio/Pages',function(imageStream)
{var entryCount=imageStream.length;var headerView=widgets['widget1'];headerView.setPreferenceForKey(imageStream.length,'entryCount');NotificationCenter.postNotification(new IWNotification('SetPage','id2',{pageIndex:0}));});}
function layoutMediaGrid_id2(range)
{createMediaStream_id2().load('http://www.bryanczibesz.com/Bryan_Czibesz/Portfolio/Pages',function(imageStream)
{if(range==null)
{range=new IWRange(0,imageStream.length);}
IWLayoutPhotoGrid('id2',new IWPhotoGridLayout(3,new IWSize(239,239),new IWSize(239,112),new IWSize(248,366),27,27,0,new IWSize(0,0)),new IWStrokeParts([{rect:new IWRect(-1,1,2,236),url:'Mapping_Authorship_files/stroke.png'},{rect:new IWRect(-1,-1,2,2),url:'Mapping_Authorship_files/stroke_1.png'},{rect:new IWRect(1,-1,236,2),url:'Mapping_Authorship_files/stroke_2.png'},{rect:new IWRect(237,-1,2,2),url:'Mapping_Authorship_files/stroke_3.png'},{rect:new IWRect(237,1,2,236),url:'Mapping_Authorship_files/stroke_4.png'},{rect:new IWRect(237,237,2,2),url:'Mapping_Authorship_files/stroke_5.png'},{rect:new IWRect(1,237,236,2),url:'Mapping_Authorship_files/stroke_6.png'},{rect:new IWRect(-1,237,2,2),url:'Mapping_Authorship_files/stroke_7.png'}],new IWSize(238,238)),imageStream,range,null,null,1.000000,{backgroundColor:'rgb(192, 192, 192)',reflectionHeight:0,reflectionOffset:2,captionHeight:100,fullScreen:1,transitionIndex:2},'../../Media/slideshow.html','widget1','widget2','widget3')});}
function relayoutMediaGrid_id2(notification)
{var userInfo=notification.userInfo();var range=userInfo['range'];layoutMediaGrid_id2(range);}
function onStubPage()
{var args=window.location.href.toQueryParams();parent.IWMediaStreamPhotoPageSetMediaStream(createMediaStream_id2(),args.id);}
if(window.stubPage)
{onStubPage();}
setTransparentGifURL('../../Media/transparent.gif');function applyEffects()
{var registry=IWCreateEffectRegistry();registry.registerEffects({stroke_0:new IWEmptyStroke()});registry.applyEffects();}
function hostedOnDM()
{return false;}
function onPageLoad()
{IWRegisterNamedImage('comment overlay','../../Media/Photo-Overlay-Comment.png')
IWRegisterNamedImage('movie overlay','../../Media/Photo-Overlay-Movie.png')
loadMozillaCSS('Mapping_Authorship_files/Mapping_AuthorshipMoz.css')
adjustLineHeightIfTooBig('id1');adjustFontSizeIfTooBig('id1');NotificationCenter.addObserver(null,relayoutMediaGrid_id2,'RangeChanged','id2')
adjustLineHeightIfTooBig('id3');adjustFontSizeIfTooBig('id3');adjustLineHeightIfTooBig('id4');adjustFontSizeIfTooBig('id4');adjustLineHeightIfTooBig('id5');adjustFontSizeIfTooBig('id5');adjustLineHeightIfTooBig('id6');adjustFontSizeIfTooBig('id6');adjustLineHeightIfTooBig('id7');adjustFontSizeIfTooBig('id7');Widget.onload();fixAllIEPNGs('../../Media/transparent.gif');applyEffects()
initializeMediaStream_id2()}
function onPageUnload()
{Widget.onunload();}
