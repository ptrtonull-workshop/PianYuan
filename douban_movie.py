
from bs4 import BeautifulSoup
import requests
import bs4
import re

mainWeb ="""
 '<html class="ua-windows ua-ff69" lang="zh-cmn-Hans"><head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw">
    <title>
        昨日奇迹 (豆瓣)
</tit   le>
    
    <meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    
    <link rel="apple-touch-icon" href="https://img3.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png">
    <link href="https://img3.doubanio.com/f/shire/52c9997d6d42db58eab418e976a14d5f3eff981e/css/douban.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/shire/ae3f5a3e3085968370b1fc63afcecb22d3284848/css/separation/_all.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/movie/8864d3756094f5272d3c93e30ee2e324665855b0/css/movie/base/init.css" rel="stylesheet">
    <link type="text/css" rel="stylesheet" href="https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css"><script src="//vidstat.taboola.com/vpaid/ds/176/dsm.js"></script><script charset="UTF-8" type="text/javascript" async="async" src="https://cdn.taboola.com/libtrc/userx.20190919-3-RELEASE.es6.js"></script><script async="" src="https://sb.scorecardresearch.com/beacon.js"></script><script charset="UTF-8" type="text/javascript" src="https://cdn.taboola.com/libtrc/impl.20190919-3-RELEASE.js"></script><script async="" src="//cdn.taboola.com.cn/libtrc/douban-cn-web/loader.js" id="tb_loader_script"></script><script type="text/javascript" src="https://img3.doubanio.com/f/movie/3d4f8e4a8918718256450eb6e57ec8e1f7a2e14b/js/movie/lib/handlebars.current.js" async="true"></script><script type="text/javascript" defer="" async="" src="https://img3.doubanio.com/dae/fundin/piwik.js"></script><script type="text/javascript" src="//img1.doubanio.com/dDY0Zjl6NS9mL2FkanMvNGQ1MjFiYTY2ZGE0MjE4OTc4YmYyOWZhODVjZDA2ZDdmODAyMTlkMy9hZC5yZWxlYXNlLmpz" async="true"></script><script type="text/javascript" src="https://img3.doubanio.com/f/movie/c4ab132ff4d3d64a83854c875ea79b8b541faf12/js/movie/lib/qrcode.min.js" async="true"></script><script type="text/javascript" src="https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js" async="true"></script><script type="text/javascript">var _head_start = new Date();</script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/1316664523258f7b8b536e4ce45afc9cb37b8963/js/douban.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/0efdc63b77f895eaf85281fb0e44d435c6239a3f/js/separation/_all.js"></script>
    
    <meta name="keywords" content="昨日奇迹,Yesterday,昨日奇迹影评,剧情介绍,电影图片,预告片,影讯,在线购票,论坛">
    <meta name="description" content="昨日奇迹电影简介和剧情介绍,昨日奇迹影评、图片、预告片、影讯、论坛、在线购票">
    <meta name="mobile-agent" content="format=html5; url=http://m.douban.com/movie/subject/30165034/">
    <link rel="alternate" href="android-app://com.douban.movie/doubanmovie/subject/30165034/">
    <link rel="stylesheet" href="https://img3.doubanio.com/dae/cdnlib/libs/LikeButton/1.0.5/style.min.css">
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
    <script type="text/javascript">
      Do.add('dialog', {path: 'https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js', type: 'js'});
      Do.add('dialog-css', {path: 'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css', type: 'css'});
      Do.add('handlebarsjs', {path: 'https://img3.doubanio.com/f/movie/3d4f8e4a8918718256450eb6e57ec8e1f7a2e14b/js/movie/lib/handlebars.current.js', type: 'js'});
    </script>
    
  <script type="text/javascript">
  var _vwo_code = (function() {
    var account_id = 249272,
      settings_tolerance = 0,
      library_tolerance = 2500,
      use_existing_jquery = false,
      // DO NOT EDIT BELOW THIS LINE
      f=false,d=document;return{use_existing_jquery:function(){return use_existing_jquery;},library_tolerance:function(){return library_tolerance;},finish:function(){if(!f){f=true;var a=d.getElementById('_vis_opt_path_hides');if(a)a.parentNode.removeChild(a);}},finished:function(){return f;},load:function(a){var b=d.createElement('script');b.src=a;b.type='text/javascript';b.innerText;b.onerror=function(){_vwo_code.finish();};d.getElementsByTagName('head')[0].appendChild(b);},init:function(){settings_timer=setTimeout('_vwo_code.finish()',settings_tolerance);var a=d.createElement('style'),b='body{opacity:0 !important;filter:alpha(opacity=0) !important;background:none !important;}',h=d.getElementsByTagName('head')[0];a.setAttribute('id','_vis_opt_path_hides');a.setAttribute('type','text/css');if(a.styleSheet)a.styleSheet.cssText=b;else a.appendChild(d.createTextNode(b));h.appendChild(a);this.load('//dev.visualwebsiteoptimizer.com/j.php?a='+account_id+'&u='+encodeURIComponent(d.URL)+'&r='+Math.random());return settings_timer;}};}());

  +function () {
    var bindEvent = function (el, type, handler) {
        var $ = window.jQuery || window.Zepto || window.$
       if ($ && $.fn && $.fn.on) {
           $(el).on(type, handler)
       } else if($ && $.fn && $.fn.bind) {
           $(el).bind(type, handler)
       } else if (el.addEventListener){
         el.addEventListener(type, handler, false);
       } else if (el.attachEvent){
         el.attachEvent("on" + type, handler);
       } else {
         el["on" + type] = handler;
       }
     }

    var _origin_load = _vwo_code.load
    _vwo_code.load = function () {
      var args = [].slice.call(arguments)
      bindEvent(window, 'load', function () {
        _origin_load.apply(_vwo_code, args)
      })
    }
  }()

  _vwo_settings_timer = _vwo_code.init();
  </script>
  
     
    


<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "name": "昨日奇迹 Yesterday",
  "url": "/subject/30165034/",
  "image": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2561245949.jpg",
  "director": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1054404/",
      "name": "丹尼·博伊尔 Danny Boyle"
    }
  ]
,
  "author": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1410722/",
      "name": "杰克·巴斯 Jack Barth"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1040673/",
      "name": "理查德·柯蒂斯 Richard Curtis"
    }
  ]
,
  "actor": 
  [
    {
      "@type": "Person",
      "url": "/celebrity/1391915/",
      "name": "希米什·帕特尔 Himesh Patel"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1318674/",
      "name": "莉莉·詹姆斯 Lily James"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1355940/",
      "name": "艾德·希兰 Ed Sheeran"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1319532/",
      "name": "凯特·麦克金农 Kate McKinnon"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1327567/",
      "name": "阿历克斯·阿诺 Alexander Arnold"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1352741/",
      "name": "乔尔·弗莱 Joel Fry"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1017966/",
      "name": "詹姆斯·柯登 James Corden"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1071717/",
      "name": "卡米利·陈 Camille Chen"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1324073/",
      "name": "拉蒙尼·莫里斯 Lamorne Morris"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1202935/",
      "name": "索菲娅·迪·马蒂诺 Sophia Di Martino"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1050009/",
      "name": "卡米拉·拉瑟福德 Camilla Rutherford"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1400644/",
      "name": "艾利斯·查普尔 Ellise Chappell"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1027525/",
      "name": "莎拉·兰卡夏尔 Sarah Lancashire"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1327058/",
      "name": "多米尼克·科尔曼 Dominic Coleman"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1383566/",
      "name": "玛丽安娜·斯皮瓦克 Maryana Spivak"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1173092/",
      "name": "詹妮弗·阿尔莫 Jennifer Armour"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1045259/",
      "name": "安娜·德·阿玛斯 Ana de Armas"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1392995/",
      "name": "哈廷·帕特尔 Hiten Patel"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1397360/",
      "name": "阿图尔·夏尔马 Atul Sharma"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1395012/",
      "name": "马诺伊·阿南德 Manoj Anand"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1221389/",
      "name": "哈里·米歇尔 Harry Michell"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1355273/",
      "name": "珊妮·姚 Sunny Yeo"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1273387/",
      "name": "乔希·特雷特 Josh Trett"
    }
    ,
    {
      "@type": "Person",
      "url": "/celebrity/1270161/",
      "name": "西蒙·P·爱德华兹 Simon P Edwards"
    }
  ]
,
  "datePublished": "2019-05-05",
  "genre": ["\u559c\u5267", "\u5947\u5e7b", "\u97f3\u4e50"],
  "duration": "PT1H56M",
  "description": "杰克（希米什·帕特尔 饰）是英国一个海滨小镇上苦苦挣扎的创作型歌手，有着好友艾莉（莉莉·詹姆斯 饰）的一直支持。在一次神秘的全球大停电中发生了一起奇怪的公交车事故，杰克醒来后发现披头士乐队根本从未存在...",
  "@type": "Movie",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingCount": "5466",
    "bestRating": "10",
    "worstRating": "2",
    "ratingValue": "6.6"
  }
}
</script>


    <style type="text/css">
  
</style>
    <style type="text/css">img { max-width: 100%; }</style>
    <script type="text/javascript"></script>
    <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/72714049fc2fddc3.css">

    <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
<style type="text/css" id="css-share-button">.bn-sharing{padding-right:10px;background-image:url(//img3.doubanio.com/pics/a1.png) !important;background-repeat:no-repeat !important;background-position:100% -19px !important;*display:inline-block;}a.bn-sharing:hover{text-decoration:underline;}.bn-sharing-on{background-position:100% 4px !important;position:relative !important;z-index:1 !important;}#db-div-sharing{position:absolute;width:100px;*margin-top:-2px;}#db-div-sharing .bd{border:1px solid #aaa;background:#fff;padding:10px 0 0 10px;}#db-div-sharing .bd li{line-height:20px;margin-bottom:5px;}#db-div-sharing .hd{position:absolute;height:24px;*line-height:21px;overflow:hidden;right:0;top:-24px;padding:0 5px;border:1px solid #aaa;border-bottom:none;background:#fff;}.rec-ren,.rec-sin,.rec-douban,.rec-tx,.rec-sohu,.rec-qqim,.rec-wechat{padding-left:23px;background:url(//img3.doubanio.com/img/files/file-1395904010.png) no-repeat 0 0;}.rec-wechat{background-position:0 0;}.rec-sin{background-position:0 -20px;}.rec-qqim{background-position:0 -40px;}.rec-tx{background-position:0 -60px;}.rec-ren{background-position:0 -80px;}.rec-douban{background-position:0 -100px;}</style><script src="https://ssl.google-analytics.com/ga.js" async="true"></script><style type="text/css">.trc_rbox_container{direction:ltr;text-align:left}.trc_multi_widget_container{display:-ms-flexbox;display:flex;-ms-flex-pack:justify;justify-content:space-between}.trc_multi_widget_container .trc_rbox_div{margin:0}.trc_rbox_header{border:0 solid;overflow:hidden;vertical-align:middle}.trc_rbox_container .trc_img{display:inline-block!important}.trc_rbox_header_icon_div{display:table-cell;vertical-align:baseline}.trc_rbox_header .trc_rbox_header_icon_div .trc_rbox_header_icon_img{vertical-align:middle;width:auto}.trc_rbox_header_icon_span{display:inline-table}.in_trc_header{position:relative!important;float:right;margin:0}#trc_rbox_css_loaded{overflow:hidden;width:0;height:0}.trc_rbox{margin-top:0}.trc_rbox_div{margin:0 0 3px;direction:ltr;padding:0;box-sizing:border-box;-moz-box-sizing:border-box;-ms-box-sizing:border-box;-webkit-box-sizing:border-box;overflow:auto;position:relative;width:auto;border:solid #ccc 1px}.loading-animation span{display:block}.videoCube{zoom:1;cursor:pointer;float:none;overflow:hidden;box-sizing:border-box;-moz-box-sizing:border-box;-ms-box-sizing:border-box;-webkit-box-sizing:border-box}.videoCube_hover,div.videoCube:hover{cursor:pointer}.videoCube span.video-title:hover,.videoCube_hover span.video-title{text-decoration:underline}.videoCube a{text-decoration:none;border:0;color:#000;cursor:pointer}.videoCube a,.videoCube a:hover,.videoCube a:link,.videoCube_hover a{text-decoration:none!important;outline:0}.videoCube a .thumbBlock{float:left;display:block;overflow:hidden!important}.videoCube a img,.videoCube img{border:0;display:block;margin:0;height:auto;width:auto}.videoCube .video-label{display:block;overflow:hidden}.videoCube .video-label{width:auto!important;white-space:pre-wrap;white-space:-moz-pre-wrap;white-space:-o-pre-wrap;word-wrap:break-word}.videoCube .video-label-box.label-box-with-title-icon{display:table}.video-icon-container{float:left;display:table-cell;vertical-align:baseline}.video-icon-img{vertical-align:middle}.videoCube .video-duration{height:0;float:left;position:relative;color:#fff;font-size:11px}.videoCube .video-duration dt{border-radius:4px;-moz-border-radius:4px;-webkit-border-radius:4px;background-color:#000;opacity:.6}.videoCube span.video-label.trc_ellipsis{position:relative;overflow:hidden;display:-webkit-box;-webkit-box-orient:vertical}.videoCube span.video-label.trc-smart-ellipsis{position:relative;overflow:hidden}.videoCube span.video-label.trc-smart-ellipsis ins{display:inline-block;text-decoration:inherit}.videoCube span.video-label.trc-smart-ellipsis ins.lastLineEllipsis{display:block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;word-wrap:normal}.video-duration.video-duration-detail div{color:#fff}.trc_rbox .sponsored{position:relative;display:block;overflow:visible;height:auto;width:auto;padding-right:0;text-align:right;font-size:9px}.trc_rbox_div{height:410px}.videoCube{direction:ltr;font-size:11px;margin:0;color:#000;border-width:0}.videoCube.vertical:first-child{border-top:0;margin-top:0}.videoCube.horizontal:first-child{border-left:0;margin-left:0}.videoCube_hover,div.videoCube:hover{background-color:#ebf0ff;color:#000}.videoCube .thumbBlock{margin-right:5px;margin-left:1px;border-style:solid}.videoCube a img,.videoCube img{border-color:#ececec}.videoCube .video-label-box{margin-left:81px}.videoCube .video-label dt{font-weight:700}.videoCube .video-title{height:auto;margin-bottom:3px;white-space:normal}.videoCube .trc_inline_detail_spacer{display:inline-block;white-space:pre}.loading-animation{font-family:sans;font-size:1.5em;text-align:center;color:gray;height:100%}.trc_rbox_header{font-family:Arial,Helvetica,sans-serif;font-size:12px;font-weight:700;text-decoration:none;color:#000}.trc_header_right_part{position:absolute;left:50%;top:0}.branding_div{overflow:visible;float:right}.branding_div img{height:20px}.videoCube .branding .logoDiv{font-size:inherit;line-height:inherit;background:0 0;margin:0;padding:0}.videoCube .branding .logoDiv a{vertical-align:inherit;color:inherit;line-height:inherit}.videoCube .branding .logoDiv a span{vertical-align:inherit}.trc_related_container .videoCube .branding .attribution-disclosure-link-sponsored{display:inline-block;float:none}.trc_related_container .videoCube .branding .attribution-disclosure-link-sponsored.align-disclosure-right{float:right;margin-left:auto;padding-left:2px}.videoCube .video-label-box .branding.composite-branding{display:-webkit-box;display:-ms-flexbox;display:flex}.branding.composite-branding>*{display:inline-block;vertical-align:bottom}.branding .branding-separator{margin:0 2px;font-weight:400}.branding .branding-inner{text-overflow:ellipsis;overflow:hidden;white-space:nowrap}.trc_related_container div.horizontal{float:left;box-sizing:border-box;-moz-box-sizing:border-box;-ms-box-sizing:border-box;-webkit-box-sizing:border-box}.trc_related_container DIV.videoCube.thumbnail_bottom .thumbBlock,.trc_related_container DIV.videoCube.thumbnail_top .thumbBlock{float:none}.vidiscovery-note{display:none}.videoCube .thumbBlock .trc_sponsored_overlay_base{display:block;width:auto;margin-left:0;position:absolute;color:#fff!important}.videoCube .thumbBlock .trc_sponsored_overlay{opacity:.6;display:block;position:absolute}.videoCube .thumbBlock .trc_sponsored_overlay_base .sponsored{position:relative;display:block;overflow:visible;width:auto;text-align:center;padding:0 5px;margin-top:0}.videoCube .thumbBlock .trc_sponsored_overlay_base.round .trc_sponsored_overlay{border-radius:4px;-moz-border-radius:4px;-webkit-border-radius:4px}.videoCube .thumbBlock .trc_sponsored_overlay_base.round{margin-left:4px}.thumbnail-emblem,.videoCube .thumbnail-overlay,.videoCube:hover .thumbnail-overlay,.videoCube_hover .thumbnail-overlay{position:absolute;background:transparent no-repeat;z-index:50}.thumbnail_bottom{padding-bottom:8px}.trc_related_container .logoDiv{font-family:Arial,Helvetica,sans-serif;white-space:nowrap;font-size:9px}.trc_related_container .logoDiv a{font-size:9px;text-decoration:none!important;color:#000;margin-right:1px;vertical-align:text-bottom}.logoDiv a span:hover{text-decoration:underline}.trc_rbox_header .logoDiv{font-size:1em}.trc_rbox_container.trc_expandable{overflow:hidden;max-height:0;transition-property:max-height;-webkit-transition-property:max-height;-moz-transition-property:max-height;-o-transition-property:max-height;-webkit-transform:translateZ(0);-moz-transform:translateZ(0);-ms-transform:translateZ(0);-o-transform:translateZ(0);transform:translateZ(0)}.trc_related_container .static-text.bottom-right{bottom:0;right:0}.trc_related_container .static-text.top-right{top:0;right:0}.trc_related_container .static-text.bottom-left{bottom:0;left:0}.trc_related_container .static-text.top-left{top:0;left:0}.trc_related_container .videoCube .thumbBlock .branding{position:absolute;bottom:0;z-index:1;width:100%;margin:0;padding:5px 0;text-align:center}.syndicatedItem .branding{margin:0}.trc_related_container .videoCube .thumbBlock .static-text{position:absolute;z-index:1;margin:0;padding:5px;background-color:#000;color:#fff;display:block;font-family:Arial,Helvetica,sans-serif;font-size:10px;font-weight:400;text-align:left;text-decoration:none;opacity:.7}.trc_related_container .static-text.top{width:100%;top:0;padding:5px 0}.trc_related_container .static-text.bottom{width:100%;bottom:0;padding:2px 0}.trc-inplayer-rbox{background:#333;background:rgba(30,30,30,.9);bottom:0;position:absolute;height:300px;text-align:center}.trc-inplayer-rbox .trc_rbox_container{margin:50px auto 0;width:640px}.trc_rbox.trc-auto-size{width:100%;height:100%}.videoCube.thumbnail_under .thumbBlock{margin-left:0;margin-right:0}.videoCube.thumbnail_under .label-box-overlay{width:100%;height:100%;position:absolute;background:#000;opacity:.75;top:0}.videoCube.thumbnail_under .video-labels-anchor{width:100%;height:auto;position:absolute;z-index:1;left:0;bottom:0;min-height:2.58em;max-height:2.58em;padding-top:2px;padding-bottom:2px;-webkit-transition:all .2s linear;-moz-transition:all .2s linear;-ms-transition:all .2s linear;-o-transition:all .2s linear;transition:all .2s linear;line-height:1.25em}.videoCube.thumbnail_under .video-labels-anchor span.branding,.videoCube.thumbnail_under .video-labels-anchor span.video-title{position:relative;z-index:1;padding:0 3px;margin:0}.videoCube.thumbnail_under .video-title{min-height:2.58em}.videoCube.thumbnail_under:hover .video-labels-anchor{opacity:1;max-height:6.45em}.trc-auto-size .trc_rbox_outer .trc_rbox_div{height:auto;width:auto}.trc-auto-size .trc_rbox_div .videoCube{height:auto}.trc-auto-size .trc_rbox_div .videoCube.trc-first-recommendation{margin-top:0}.trc_rbox .trc_rbox_outer .trc_rbox_div .videoCube.trc-first-in-row{margin-left:0}.trc_elastic .trc_rbox{width:auto}.trc_elastic .videoCube{overflow:hidden}.trc_elastic .videoCube .thumbBlock{background:transparent no-repeat center center;background-size:cover;position:absolute;display:inline-block;top:0;right:0;bottom:0;left:0;margin-left:0;margin-right:0}.trc_elastic .thumbBlock_holder{position:relative;width:100%}.trc_elastic .thumbnail_start .thumbBlock_holder{float:left;margin-right:10px}.trc_elastic .thumbnail_start.item-has-pre-label .thumbBlock_holder{margin-right:0}.trc_elastic .videoCube_aspect{width:1px}.trc_elastic .trc_rbox .trc_rbox_div{height:auto}.trc_elastic .thumbnail_start .trc-pre-label{float:left;padding-right:10px}.trc_elastic .thumbnail_start.trc-split-label .trc-main-label{float:left;padding-left:10px}.trc_elastic .video-label-box{display:block}.trc_elastic .thumbnail_start .video-label-box{box-sizing:border-box}.trc_user_adChoice_btn{background:url(//cdn.taboola.com/static/c5/c5ef96bc-30ab-456a-b3d5-a84f367c6a46.svg) no-repeat scroll 0 0 rgba(255,255,255,1);border-radius:0 0 0 5px;width:16px;height:16px;position:absolute;right:0;top:0;z-index:9000;cursor:pointer;border-width:2px 0 2px 4px;border-style:solid;border-color:#fff;opacity:.7;background-size:contain;visibility:hidden}.videoCube:hover .trc_user_adChoice_btn,.videoCube_hover .trc_user_adChoice_btn{visibility:visible}.videoCube .trc_user_adChoice_btn_static{visibility:visible}.p-video-overlay-container{position:absolute;width:100%;height:100%;top:0;left:0;background-color:transparent}.p-video-overlay.p-video-overlay-show{display:flex}.p-video-overlay{display:none;background-color:#000;opacity:.7;width:100%;height:100%;flex-direction:column}.p-video-overlay-action{color:#fff;width:100%;direction:ltr;text-align:center;display:flex;justify-content:center;flex-direction:column}.p-video-overlay-action.p-video-back-action{height:34%}.p-video-back-action-label{font-family:Helvetica Neue,serif;font-size:14px;font-weight:200;letter-spacing:1px}.p-video-overlay-action.p-video-goto-action{height:66%}.p-video-goto-action-url{font-family:Helvetica Neue,serif;font-size:24px;font-weight:400;text-decoration:underline;margin-top:5px}.p-video-goto-action-label{font-family:Helvetica Neue,serif;font-size:14px;font-weight:100;letter-spacing:1px}.trc_related_container .trc_clearer{clear:both;height:0;overflow:hidden;font-size:0;line-height:0;visibility:hidden}.link-adc{float:right!important}.trc-widget-footer .logoDiv{line-height:normal;padding-bottom:5px}.trc-widget-footer .link-adc a .trc_adc_wrapper,.trc_header_ext .link-adc a .trc_adc_wrapper{height:12px;width:18px;display:inline-block;padding-left:1px;margin-bottom:2px}.trc-widget-footer .link-adc a .trc_adc_b_logo,.trc-widget-footer .link-adc a .trc_adc_s_logo,.trc_header_ext .link-adc a .trc_adc_b_logo,.trc_header_ext .link-adc a .trc_adc_s_logo{vertical-align:middle;height:15px;display:inline-block;margin-top:-1px}.trc-widget-footer .link-adc a .trc_adc_s_logo,.trc_header_ext .link-adc a .trc_adc_s_logo{width:12px;height:14px;background:url(//cdn.taboola.com/static/c5/c5ef96bc-30ab-456a-b3d5-a84f367c6a46.svg) no-repeat;background-size:contain;vertical-align:middle}.trc-widget-footer .link-adc a .trc_adc_b_logo,.trc_header_ext .link-adc a .trc_adc_b_logo{width:77px;background:#fff url(//cdn.taboola.com/libtrc/static/thumbnails/0781f9c5a8637d1e162874f157460048.png) no-repeat!important;right:-1px;display:none;position:absolute}.logoDiv .trc_mobile_adc_link,.logoDiv .trc_mobile_attribution_link,.logoDiv .trc_mobile_disclosure_link{display:none}.logoDiv .trc_desktop_adc_link,.logoDiv .trc_desktop_attribution_link,.logoDiv .trc_desktop_disclosure_link{display:inline}@media screen and (max-width:767px){.logoDiv .trc_mobile_disclosure_link{display:inline}.logoDiv .trc_mobile_attribution_link{display:inline}.logoDiv .trc_mobile_adc_link{display:inline}.logoDiv .trc_desktop_disclosure_link{display:none}.logoDiv .trc_desktop_attribution_link{display:none}.logoDiv .trc_desktop_adc_link{display:none}}.trc_in_iframe .logoDiv .trc_mobile_attribution_link,.trc_in_iframe .logoDiv .trc_mobile_disclosure_link{display:inline}.trc_in_iframe .logoDiv .trc_desktop_attribution_link,.trc_in_iframe .logoDiv .trc_desktop_disclosure_link{display:none}.trc_related_container .logoDiv,.trc_related_container .trc_header_ext .logoDiv{float:right}.trc_related_container .logoDiv+.logoDiv{margin-right:2px}.trc_related_container .attribution-disclosure-link-hybrid,.trc_related_container .attribution-disclosure-link-sponsored{display:none}.trc-w2f.trc-content-sponsored .attribution-disclosure-link-sponsored,.trc_related_container .trc-content-sponsored .attribution-disclosure-link-sponsored{display:block}.trc-w2f.trc-content-hybrid .attribution-disclosure-link-hybrid,.trc_related_container .trc-content-hybrid .attribution-disclosure-link-hybrid{display:block}.trc_related_container .trc-widget-footer:hover a span,.trc_related_container .trc_header_ext:hover a span{text-decoration:underline!important}.logoDiv a span.trc_logos_v_align{display:inline-block!important;font-size:15px!important;line-height:1em!important;width:0!important}.trc_related_container .trc-widget-footer:hover a span.trc_adc_wrapper,.trc_related_container .trc-widget-footer:hover a span.trc_logos_v_align,.trc_related_container .trc_header_ext:hover a span.trc_adc_wrapper,.trc_related_container .trc_header_ext:hover a span.trc_logos_v_align{text-decoration:none!important}.trc_related_container{clear:both}.tbl-loading-spinner{width:100%;height:40px;background:url(//cdn.taboola.com/static/91/91a25024-792d-4b52-84e6-ad1478c3f552.gif) center center no-repeat;background-size:40px}.tbl-hidden{display:none!important}.tbl-batch-anchor{width:100%;height:1px}.iw_video_frame .trc_rbox_div{overflow:hidden}.trc-w2f .trc_rbox .trc-widget-footer,.trc-w2f .trc_rbox .trc_rbox_header{display:none!important}.rbox-blended .video-title{font-family:Arial, Helvetica, sans-serif;font-size:14px;line-height:17.5px;font-weight:bold;max-height:2.58em;*height:2.58em;color:black;text-decoration:none;}.rbox-blended .video-description{font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:11px;font-weight:normal;max-height:2.2em;*height:2.2em;color:black;text-decoration:none;}.rbox-blended .trc_rbox_div{width:auto;_width:99%;height:410px;border-width:1px;padding:0;}.rbox-blended .videoCube .video-duration{left:36px;display:block;}.rbox-blended .videoCube .video-label-box{margin-left:81px;margin-right:0px;}.rbox-blended .video-label,.rbox-blended .sponsored,.rbox-blended .sponsored-url{font-family:Arial, Helvetica, sans-serif;}.rbox-blended .trc_rbox_header{font-family:Arial, Helvetica, sans-serif;font-size:16px;font-weight:bold;text-decoration:none;color:black;border-width:0;background:transparent;border-style:none none solid none;border-color:#D6D5D3;padding:0;}.rbox-blended .sponsored-url{font-size:9px;font-weight:bold;text-decoration:underline;color:green;}.rbox-blended .sponsored{font-size:9px;font-weight:normal;text-decoration:none;color:#9C9A9C;}.rbox-blended .video-category{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .video-duration-detail{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .video-rating{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .video-uploader{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .video-views{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .video-published-date{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .sponsored-default .video-title{max-height:2.58em;*height:2.58em;}.rbox-blended .sponsored-default .video-description{max-height:2.2em;*height:2.2em;}.rbox-blended .videoCube{width:auto;_width:auto;background-color:transparent;border-width:1px;border-color:#D6D5D3;padding:3px;height:auto;margin-left:0px;margin-top:0px;border-radius:0px;-moz-border-radius:0px;-webkit-border-radius:0px;border-style:none;}.rbox-blended div.videoCube:hover,.rbox-blended  div.videoCube_hover{background-color:transparent;}.rbox-blended .sponsored-default{background-color:#F7F6C6;}.rbox-blended div.sponsored-default:hover,.rbox-blended  div.sponsored-default.videoCube_hover{background-color:inherit;}.rbox-blended .videoCube .thumbnail-overlay{background-image:null;background-position:5% 5%;}.rbox-blended .videoCube:hover .thumbnail-overlay,.rbox-blended  .videoCube_hover .thumbnail-overlay{background-image:null;}.rbox-blended .trc_rbox_border_elm{border-color:darkgray;}.rbox-blended .videoCube .thumbBlock{border-width:0px;border-color:darkgray;}.rbox-blended div.videoCube:hover .thumbBlock{border-color:inherit;}.rbox-blended .pager_enabled{color:#0056b3;}.rbox-blended .trc_pager_counter{color:#000000;}.rbox-blended .pager_disabled{color:#7d898f;}.rbox-blended .trc_pager_prev:hover,.rbox-blended  .trc_pager_next:hover{color:#6497ED;}.rbox-blended .trc_pager_selected{color:#0056b3;}.rbox-blended .trc_pager_unselected{color:#7d898f;}.rbox-blended div.trc_pager_pages div:hover{color:#6497ED;}.rbox-blended .trc_lightbox_overlay{background-color:#000000;opacity:0.70;filter:alpha(opacity=70);}.rbox-blended .video-label-box{text-align:left;}.rbox-blended .trc_sponsored_overlay{background-color:black;}.rbox-blended .thumbnail-emblem{background-position:5% 5%;}.rbox-blended .videoCube .sponsored{margin-top:-7px;}.rbox-blended {width:300px;_width:300px;border-width:0px;border-style:solid solid solid solid;border-color:#000000;padding:0;border-radius:0;-moz-border-radius:0;-webkit-border-radius:0;box-shadow:none;}.rbox-blended .videoCube.vertical{border-style:solid none none none;}.rbox-blended .videoCube.horizontal{border-style:none none none solid;}.rbox-blended .trc_pager_prev,.rbox-blended .trc_pager_next{font-size:12px;font-weight:normal;text-decoration:none;}.rbox-blended .trc_pager_pages div{font-size:12px;font-weight:normal;text-decoration:none;}.rbox-blended .video-external-data{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .trc_pager div{font-family:serif;}.rbox-blended .playerCube .thumbnail-overlay{background-image:null;background-position:5% 5%;}.rbox-blended .playerCube:hover .thumbnail-overlay,.rbox-blended  .playerCube_hover .thumbnail-overlay{background-image:null;}.rbox-blended .playerCube .videoCube{background-color:transparent;border-color:#D6D5D3;border-width:1px;border-radius:0px;-moz-border-radius:0px;-webkit-border-radius:0px;margin-left:0px;margin-top:0px;padding:3px;}.rbox-blended .playerCube .videoCube.horizontal{border-style:none none none none;}.rbox-blended .playerCube .videoCube .video-label-box{margin-left:81px;margin-right:0px;}.rbox-blended .playerCube .video-duration-detail{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .playerCube .video-external-data{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .playerCube .video-label-box{text-align:left;}.rbox-blended .playerCube .video-published-date{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .playerCube .video-category{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .playerCube .video-description{font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:11px;font-weight:normal;text-decoration:none;max-height:2.2em;*height:2.2em;color:black;}.rbox-blended .playerCube .videoCube .video-duration{display:block;left:36px;}.rbox-blended .playerCube .videoCube .thumbBlock{border-width:0px;border-color:darkgray;}.rbox-blended .playerCube .video-rating{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .playerCube .video-uploader{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .playerCube .video-views{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.rbox-blended .playerCube .video-title{font-family:Arial, Helvetica, sans-serif;text-decoration:none;font-size:14px;line-height:17.5px;font-weight:bold;max-height:2.58em;*height:2.58em;color:black;}.rbox-blended .playerCube div.videoCube:hover,.rbox-blended  div.videoCube_hover{background-color:transparent;}.rbox-blended .whatsThisSyndicated{font-family:Arial, Verdana, sans-serif;font-size:9px;font-weight:normal;color:black;text-decoration:none;padding:0;}.rbox-blended div.syndicatedItem:hover,.rbox-blended  div.syndicatedItem.videoCube_hover{background-color:transparent;}.rbox-blended div.syndicatedItem:hover .thumbBlock{border-color:inherit;}.rbox-blended .videoCube.syndicatedItem{background-color:transparent;border-color:#D6D5D3;border-radius:0px;-moz-border-radius:0px;-webkit-border-radius:0px;border-width:1px;border-style:none;}.rbox-blended .videoCube.syndicatedItem.horizontal{border-style:none none none solid;}.rbox-blended .videoCube.syndicatedItem .thumbBlock{border-color:darkgray;border-width:0px;}.rbox-blended .videoCube.syndicatedItem .thumbnail-overlay{background-image:null;background-position:5% 5%;}.rbox-blended .videoCube.syndicatedItem.vertical{border-style:solid none none none;}.rbox-blended .videoCube.syndicatedItem .video-duration{display:block;left:36px;}.rbox-blended .videoCube.syndicatedItem .video-label-box{margin-left:0px;}.rbox-blended .syndicatedItem{background-color:transparent;}.rbox-blended .syndicatedItem .video-description{max-height:2.2em;*height:2.2em;color:black;font-family:Arial, Helvetica, sans-serif;font-size:10px;font-weight:normal;line-height:11px;text-decoration:none;}.rbox-blended .syndicatedItem .video-title{max-height:2.58em;*height:2.58em;color:black;font-family:Arial, Helvetica, sans-serif;font-size:14px;line-height:17.5px;font-weight:bold;text-decoration:none;}.rbox-blended .syndicatedItem .sponsored{color:#9C9A9C;font-size:9px;font-weight:normal;text-decoration:none;}.rbox-blended .syndicatedItem .sponsored-url{color:green;font-size:9px;font-weight:bold;text-decoration:underline;}.rbox-blended .syndicatedItem .video-category{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.rbox-blended .syndicatedItem .video-duration-detail{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.rbox-blended .syndicatedItem .video-external-data{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.rbox-blended .syndicatedItem .video-published-date{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.rbox-blended .syndicatedItem .video-rating{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.rbox-blended .syndicatedItem .video-uploader{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.rbox-blended .syndicatedItem .video-views{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.rbox-blended .syndicatedItem .branding{color:black;font-size:10px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;background-image:null;text-align:left;}.rbox-blended .videoCube.syndicatedItem .thumbBlock .branding{text-align:left;background-color:transparent;display:block;left:0px;color:black;font-size:10px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;background-image:null;}.rbox-blended .videoCube.syndicatedItem .thumbBlock .static-text{text-align:left;background-color:black;display:block;color:white;font-size:10px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;}.rbox-blended .videoCube.thumbnail_start .thumbBlock_holder{width:40%;_width:40%;}.rbox-blended .trc_rbox_header_icon_img{margin:0px;height:18px;}.rbox-blended .video-icon-img{margin:0px;height:18px;}.rbox-blended .video-label-box.trc-pre-label{height:auto;}.rbox-blended .syndicatedItem .video-label-box.trc-pre-label{height:auto;}.rbox-blended .videoCube.thumbnail_start .trc-pre-label{width:60%;_width:60%;}.rbox-blended .videoCube.thumbnail_start.trc-split-label .trc-main-label{width:30%;_width:30%;}.rbox-blended .videoCube.thumbnail_start.trc-split-label .trc-pre-label{width:30%;_width:30%;}.rbox-blended .videoCube .video-label-box.trc-pre-label{margin:0;}.rbox-blended .branding{color:black;font-size:10px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;background-image:null;text-align:left;}.rbox-blended .branding .logoDiv a span{color:inherit;font-size:inherit;}.rbox-blended .branding div.logoDiv{font-family:inherit;}.thumbnails-a .video-title{font-family:Arial, Helvetica, sans-serif;font-size:14.0px;line-height:20.0px;font-weight:normal;max-height:38.0px;*height:38.0px;color:#111;text-decoration:none;}.thumbnails-a .video-description{font-family:Arial, Helvetica, sans-serif;font-size:14px;line-height:19.0px;font-weight:normal;max-height:2.2em;*height:2.2em;color:black;text-decoration:none;}.thumbnails-a .trc_rbox_div{width:auto;_width:99%;height:410px;border-width:0;padding:0;}.thumbnails-a .videoCube .video-duration{left:36px;display:none;}.thumbnails-a .videoCube .video-label-box{margin-left:;margin-right:;}.thumbnails-a .video-label,.thumbnails-a .sponsored,.thumbnails-a .sponsored-url{font-family:Arial, Helvetica, sans-serif;}.thumbnails-a .trc_rbox_header{font-family:Arial, Helvetica, sans-serif;font-size:16.0px;font-weight:normal;text-decoration:none;color:#072;border-width:0;background:transparent;border-style:none;border-color:#D6D5D3;padding:0px 0px 0px 0px;}.thumbnails-a .sponsored-url{font-size:9px;font-weight:bold;text-decoration:underline;color:green;}.thumbnails-a .sponsored{font-size:9px;font-weight:normal;text-decoration:none;color:#9C9A9C;}.thumbnails-a .video-category{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .video-duration-detail{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .video-rating{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .video-uploader{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .video-views{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .video-published-date{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .sponsored-default .video-title{max-height:2.58em;*height:2.58em;}.thumbnails-a .sponsored-default .video-description{max-height:2.2em;*height:2.2em;}.thumbnails-a .videoCube{width:auto;_width:auto;background-color:transparent;border-width:0px 0px 0px 0px;border-color:#E4E4E4;padding:0px 0px 0px 0px;height:auto;margin-left:0px;margin-top:0px;border-radius:0px;-moz-border-radius:0px;-webkit-border-radius:0px;border-style:SOLID;}.thumbnails-a div.videoCube:hover,.thumbnails-a  div.videoCube_hover{background-color:transparent;}.thumbnails-a .sponsored-default{background-color:#F7F6C6;}.thumbnails-a div.sponsored-default:hover,.thumbnails-a  div.sponsored-default.videoCube_hover{background-color:inherit;}.thumbnails-a .videoCube .thumbnail-overlay{background-image:null;background-position:5% 5%;}.thumbnails-a .videoCube:hover .thumbnail-overlay,.thumbnails-a  .videoCube_hover .thumbnail-overlay{background-image:null;}.thumbnails-a .trc_rbox_border_elm{border-color:darkgray;}.thumbnails-a .videoCube .thumbBlock{border-width:0px;border-color:darkgray;}.thumbnails-a div.videoCube:hover .thumbBlock{border-color:inherit;}.thumbnails-a .pager_enabled{color:#0056b3;}.thumbnails-a .trc_pager_counter{color:#000000;}.thumbnails-a .pager_disabled{color:#7d898f;}.thumbnails-a .trc_pager_prev:hover,.thumbnails-a  .trc_pager_next:hover{color:#6497ED;}.thumbnails-a .trc_pager_selected{color:#0056b3;}.thumbnails-a .trc_pager_unselected{color:#7d898f;}.thumbnails-a div.trc_pager_pages div:hover{color:#6497ED;}.thumbnails-a .trc_lightbox_overlay{background-color:#000000;opacity:0.70;filter:alpha(opacity=70);}.thumbnails-a .video-label-box{text-align:left;}.thumbnails-a .trc_sponsored_overlay{background-color:black;}.thumbnails-a .thumbnail-emblem{background-position:5% 5%;}.thumbnails-a .videoCube .sponsored{margin-top:-7px;}.thumbnails-a {width:300px;_width:300px;border-width:0px 0px 0px 0px;border-style:solid solid solid solid;border-color:#DFDFDF;padding:0px 0px 0px 0px;border-radius:0;-moz-border-radius:0;-webkit-border-radius:0;box-shadow:none;}.thumbnails-a .videoCube.vertical{border-style:solid none none none;}.thumbnails-a .videoCube.horizontal{border-style:none;}.thumbnails-a .trc_pager_prev,.thumbnails-a .trc_pager_next{font-size:12px;font-weight:normal;text-decoration:none;}.thumbnails-a .trc_pager_pages div{font-size:12px;font-weight:normal;text-decoration:none;}.thumbnails-a .video-external-data{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .trc_pager div{font-family:serif;}.thumbnails-a .playerCube .thumbnail-overlay{background-image:null;background-position:5% 5%;}.thumbnails-a .playerCube:hover .thumbnail-overlay,.thumbnails-a  .playerCube_hover .thumbnail-overlay{background-image:null;}.thumbnails-a .playerCube .videoCube{background-color:transparent;border-color:#D6D5D3;border-width:1px;border-radius:0px;-moz-border-radius:0px;-webkit-border-radius:0px;margin-left:0px;margin-top:0px;padding:3px;}.thumbnails-a .playerCube .videoCube.horizontal{border-style:none none none none;}.thumbnails-a .playerCube .videoCube .video-label-box{margin-left:81px;margin-right:0px;}.thumbnails-a .playerCube .video-duration-detail{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .playerCube .video-external-data{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .playerCube .video-label-box{text-align:left;}.thumbnails-a .playerCube .video-published-date{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .playerCube .video-category{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .playerCube .video-description{font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:11px;font-weight:normal;text-decoration:none;max-height:2.2em;*height:2.2em;color:black;}.thumbnails-a .playerCube .videoCube .video-duration{display:block;left:36px;}.thumbnails-a .playerCube .videoCube .thumbBlock{border-width:0px;border-color:darkgray;}.thumbnails-a .playerCube .video-rating{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .playerCube .video-uploader{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .playerCube .video-views{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-a .playerCube .video-title{font-family:Arial, Helvetica, sans-serif;text-decoration:none;font-size:14px;line-height:17.5px;font-weight:bold;max-height:2.58em;*height:2.58em;color:black;}.thumbnails-a .playerCube div.videoCube:hover,.thumbnails-a  div.videoCube_hover{background-color:transparent;}.thumbnails-a .whatsThisSyndicated{font-family:Arial, Verdana, sans-serif;font-size:9px;font-weight:normal;color:black;text-decoration:none;padding:0;}.thumbnails-a div.syndicatedItem:hover,.thumbnails-a  div.syndicatedItem.videoCube_hover{background-color:transparent;}.thumbnails-a div.syndicatedItem:hover .thumbBlock{border-color:inherit;}.thumbnails-a .videoCube.syndicatedItem{background-color:transparent;border-color:#E4E4E4;border-radius:0px;-moz-border-radius:0px;-webkit-border-radius:0px;border-width:0px 0px 0px 0px;border-style:SOLID;}.thumbnails-a .videoCube.syndicatedItem.horizontal{border-style:none;}.thumbnails-a .videoCube.syndicatedItem .thumbBlock{border-color:darkgray;border-width:0px;}.thumbnails-a .videoCube.syndicatedItem .thumbnail-overlay{background-image:null;background-position:5% 5%;}.thumbnails-a .videoCube.syndicatedItem.vertical{border-style:solid none none none;}.thumbnails-a .videoCube.syndicatedItem .video-duration{display:none;left:36px;}.thumbnails-a .videoCube.syndicatedItem .video-label-box{margin-left:;}.thumbnails-a .syndicatedItem{background-color:transparent;}.thumbnails-a .syndicatedItem .video-description{max-height:2.2em;*height:2.2em;color:black;font-family:Arial, Helvetica, sans-serif;font-size:14px;font-weight:normal;line-height:19.0px;text-decoration:none;}.thumbnails-a .syndicatedItem .video-title{max-height:38.0px;*height:38.0px;color:#111;font-family:Arial, Helvetica, sans-serif;font-size:14.0px;line-height:20.0px;font-weight:normal;text-decoration:none;}.thumbnails-a .syndicatedItem .sponsored{color:#9C9A9C;font-size:9px;font-weight:normal;text-decoration:none;}.thumbnails-a .syndicatedItem .sponsored-url{color:green;font-size:9px;font-weight:bold;text-decoration:underline;}.thumbnails-a .syndicatedItem .video-category{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-a .syndicatedItem .video-duration-detail{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-a .syndicatedItem .video-external-data{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-a .syndicatedItem .video-published-date{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-a .syndicatedItem .video-rating{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-a .syndicatedItem .video-uploader{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-a .syndicatedItem .video-views{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-a .syndicatedItem .branding{color:#999;font-size:12.0px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;background-image:null;text-align:left;}.thumbnails-a .videoCube.syndicatedItem .thumbBlock .branding{text-align:left;background-color:transparent;display:none;left:0px;color:black;font-size:10px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;background-image:null;}.thumbnails-a .videoCube.syndicatedItem .thumbBlock .static-text{text-align:left;background-color:black;display:none;color:white;font-size:10px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;}.thumbnails-a .videoCube.thumbnail_start .thumbBlock_holder{width:40%;_width:40%;}.thumbnails-a .trc_rbox_header_icon_img{margin:0px;height:18px;}.thumbnails-a .video-icon-img{margin:0px;height:18px;}.thumbnails-a .video-label-box.trc-pre-label{height:0px;}.thumbnails-a .syndicatedItem .video-label-box.trc-pre-label{height:0px;}.thumbnails-a .videoCube.thumbnail_start .trc-pre-label{width:60%;_width:60%;}.thumbnails-a .videoCube.thumbnail_start.trc-split-label .trc-main-label{width:30%;_width:30%;}.thumbnails-a .videoCube.thumbnail_start.trc-split-label .trc-pre-label{width:30%;_width:30%;}.thumbnails-a .videoCube .video-label-box.trc-pre-label{margin:0px 0px 5px 0px;}.thumbnails-a .branding{color:#999999;font-size:12.0px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;background-image:null;text-align:left;}.thumbnails-a .branding .logoDiv a span{color:inherit;font-size:inherit;}.thumbnails-a .branding div.logoDiv{font-family:inherit;}.thumbnails-rr .video-title{font-family:Arial, Helvetica, sans-serif;font-size:14.0px;line-height:20.0px;font-weight:bold;max-height:38.0px;*height:38.0px;color:#111;text-decoration:none;}.thumbnails-rr .video-description{font-family:Arial, Helvetica, sans-serif;font-size:14px;line-height:19.0px;font-weight:normal;max-height:2.2em;*height:2.2em;color:black;text-decoration:none;}.thumbnails-rr .trc_rbox_div{width:auto;_width:99%;height:410px;border-width:0;padding:0;}.thumbnails-rr .videoCube .video-duration{left:36px;display:none;}.thumbnails-rr .videoCube .video-label-box{margin-left:;margin-right:;}.thumbnails-rr .video-label,.thumbnails-rr .sponsored,.thumbnails-rr .sponsored-url{font-family:Arial, Helvetica, sans-serif;}.thumbnails-rr .trc_rbox_header{font-family:Arial, Helvetica, sans-serif;font-size:16.0px;font-weight:bold;text-decoration:none;color:#072;border-width:0;background:transparent;border-style:none;border-color:#D6D5D3;padding:0px 0px 6px 0px;}.thumbnails-rr .sponsored-url{font-size:9px;font-weight:bold;text-decoration:underline;color:green;}.thumbnails-rr .sponsored{font-size:9px;font-weight:normal;text-decoration:none;color:#9C9A9C;}.thumbnails-rr .video-category{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .video-duration-detail{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .video-rating{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .video-uploader{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .video-views{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .video-published-date{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .sponsored-default .video-title{max-height:2.58em;*height:2.58em;}.thumbnails-rr .sponsored-default .video-description{max-height:2.2em;*height:2.2em;}.thumbnails-rr .videoCube{width:auto;_width:auto;background-color:transparent;border-width:0px 0px 0px 0px;border-color:#E4E4E4;padding:0px 0px 0px 0px;height:auto;margin-left:0px;margin-top:0px;border-radius:0px;-moz-border-radius:0px;-webkit-border-radius:0px;border-style:SOLID;}.thumbnails-rr div.videoCube:hover,.thumbnails-rr  div.videoCube_hover{background-color:transparent;}.thumbnails-rr .sponsored-default{background-color:#F7F6C6;}.thumbnails-rr div.sponsored-default:hover,.thumbnails-rr  div.sponsored-default.videoCube_hover{background-color:inherit;}.thumbnails-rr .videoCube .thumbnail-overlay{background-image:null;background-position:5% 5%;}.thumbnails-rr .videoCube:hover .thumbnail-overlay,.thumbnails-rr  .videoCube_hover .thumbnail-overlay{background-image:null;}.thumbnails-rr .trc_rbox_border_elm{border-color:darkgray;}.thumbnails-rr .videoCube .thumbBlock{border-width:0px;border-color:darkgray;}.thumbnails-rr div.videoCube:hover .thumbBlock{border-color:inherit;}.thumbnails-rr .pager_enabled{color:#0056b3;}.thumbnails-rr .trc_pager_counter{color:#000000;}.thumbnails-rr .pager_disabled{color:#7d898f;}.thumbnails-rr .trc_pager_prev:hover,.thumbnails-rr  .trc_pager_next:hover{color:#6497ED;}.thumbnails-rr .trc_pager_selected{color:#0056b3;}.thumbnails-rr .trc_pager_unselected{color:#7d898f;}.thumbnails-rr div.trc_pager_pages div:hover{color:#6497ED;}.thumbnails-rr .trc_lightbox_overlay{background-color:#000000;opacity:0.70;filter:alpha(opacity=70);}.thumbnails-rr .video-label-box{text-align:left;}.thumbnails-rr .trc_sponsored_overlay{background-color:black;}.thumbnails-rr .thumbnail-emblem{background-position:5% 5%;}.thumbnails-rr .videoCube .sponsored{margin-top:-7px;}.thumbnails-rr {width:300px;_width:300px;border-width:0px 0px 0px 0px;border-style:solid solid solid solid;border-color:#DFDFDF;padding:0px 0px 0px 0px;border-radius:0;-moz-border-radius:0;-webkit-border-radius:0;box-shadow:none;}.thumbnails-rr .videoCube.vertical{border-style:solid none none none;}.thumbnails-rr .videoCube.horizontal{border-style:none;}.thumbnails-rr .trc_pager_prev,.thumbnails-rr .trc_pager_next{font-size:12px;font-weight:normal;text-decoration:none;}.thumbnails-rr .trc_pager_pages div{font-size:12px;font-weight:normal;text-decoration:none;}.thumbnails-rr .video-external-data{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .trc_pager div{font-family:serif;}.thumbnails-rr .playerCube .thumbnail-overlay{background-image:null;background-position:5% 5%;}.thumbnails-rr .playerCube:hover .thumbnail-overlay,.thumbnails-rr  .playerCube_hover .thumbnail-overlay{background-image:null;}.thumbnails-rr .playerCube .videoCube{background-color:transparent;border-color:#D6D5D3;border-width:1px;border-radius:0px;-moz-border-radius:0px;-webkit-border-radius:0px;margin-left:0px;margin-top:0px;padding:3px;}.thumbnails-rr .playerCube .videoCube.horizontal{border-style:none none none none;}.thumbnails-rr .playerCube .videoCube .video-label-box{margin-left:81px;margin-right:0px;}.thumbnails-rr .playerCube .video-duration-detail{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .playerCube .video-external-data{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .playerCube .video-label-box{text-align:left;}.thumbnails-rr .playerCube .video-published-date{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .playerCube .video-category{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .playerCube .video-description{font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:11px;font-weight:normal;text-decoration:none;max-height:2.2em;*height:2.2em;color:black;}.thumbnails-rr .playerCube .videoCube .video-duration{display:block;left:36px;}.thumbnails-rr .playerCube .videoCube .thumbBlock{border-width:0px;border-color:darkgray;}.thumbnails-rr .playerCube .video-rating{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .playerCube .video-uploader{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .playerCube .video-views{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbnails-rr .playerCube .video-title{font-family:Arial, Helvetica, sans-serif;text-decoration:none;font-size:14px;line-height:17.5px;font-weight:bold;max-height:2.58em;*height:2.58em;color:black;}.thumbnails-rr .playerCube div.videoCube:hover,.thumbnails-rr  div.videoCube_hover{background-color:transparent;}.thumbnails-rr .whatsThisSyndicated{font-family:Arial, Verdana, sans-serif;font-size:9px;font-weight:normal;color:black;text-decoration:none;padding:0;}.thumbnails-rr div.syndicatedItem:hover,.thumbnails-rr  div.syndicatedItem.videoCube_hover{background-color:transparent;}.thumbnails-rr div.syndicatedItem:hover .thumbBlock{border-color:inherit;}.thumbnails-rr .videoCube.syndicatedItem{background-color:transparent;border-color:#E4E4E4;border-radius:0px;-moz-border-radius:0px;-webkit-border-radius:0px;border-width:0px 0px 0px 0px;border-style:SOLID;}.thumbnails-rr .videoCube.syndicatedItem.horizontal{border-style:none;}.thumbnails-rr .videoCube.syndicatedItem .thumbBlock{border-color:darkgray;border-width:0px;}.thumbnails-rr .videoCube.syndicatedItem .thumbnail-overlay{background-image:null;background-position:5% 5%;}.thumbnails-rr .videoCube.syndicatedItem.vertical{border-style:solid none none none;}.thumbnails-rr .videoCube.syndicatedItem .video-duration{display:none;left:36px;}.thumbnails-rr .videoCube.syndicatedItem .video-label-box{margin-left:;}.thumbnails-rr .syndicatedItem{background-color:transparent;}.thumbnails-rr .syndicatedItem .video-description{max-height:2.2em;*height:2.2em;color:black;font-family:Arial, Helvetica, sans-serif;font-size:14px;font-weight:normal;line-height:19.0px;text-decoration:none;}.thumbnails-rr .syndicatedItem .video-title{max-height:38.0px;*height:38.0px;color:#111;font-family:Arial, Helvetica, sans-serif;font-size:14.0px;line-height:20.0px;font-weight:bold;text-decoration:none;}.thumbnails-rr .syndicatedItem .sponsored{color:#9C9A9C;font-size:9px;font-weight:normal;text-decoration:none;}.thumbnails-rr .syndicatedItem .sponsored-url{color:green;font-size:9px;font-weight:bold;text-decoration:underline;}.thumbnails-rr .syndicatedItem .video-category{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-rr .syndicatedItem .video-duration-detail{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-rr .syndicatedItem .video-external-data{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-rr .syndicatedItem .video-published-date{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-rr .syndicatedItem .video-rating{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-rr .syndicatedItem .video-uploader{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-rr .syndicatedItem .video-views{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbnails-rr .syndicatedItem .branding{color:#999999;font-size:10.0px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;background-image:null;text-align:left;}.thumbnails-rr .videoCube.syndicatedItem .thumbBlock .branding{text-align:left;background-color:transparent;display:none;left:0px;color:black;font-size:10px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;background-image:null;}.thumbnails-rr .videoCube.syndicatedItem .thumbBlock .static-text{text-align:left;background-color:black;display:none;color:white;font-size:10px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;}.thumbnails-rr .videoCube.thumbnail_start .thumbBlock_holder{width:40%;_width:40%;}.thumbnails-rr .trc_rbox_header_icon_img{margin:0px;height:18px;}.thumbnails-rr .video-icon-img{margin:0px;height:18px;}.thumbnails-rr .video-label-box.trc-pre-label{height:auto;}.thumbnails-rr .syndicatedItem .video-label-box.trc-pre-label{height:auto;}.thumbnails-rr .videoCube.thumbnail_start .trc-pre-label{width:60%;_width:60%;}.thumbnails-rr .videoCube.thumbnail_start.trc-split-label .trc-main-label{width:30%;_width:30%;}.thumbnails-rr .videoCube.thumbnail_start.trc-split-label .trc-pre-label{width:30%;_width:30%;}.thumbnails-rr .videoCube .video-label-box.trc-pre-label{margin:;}.thumbnails-rr .branding{color:#999999;font-size:10.0px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;background-image:null;text-align:left;}.thumbnails-rr .branding .logoDiv a span{color:inherit;font-size:inherit;}.thumbnails-rr .branding div.logoDiv{font-family:inherit;}.thumbs-feed-01 .video-title{font-family:Arial, Helvetica, sans-serif;font-size:20.0px;line-height:27.0px;font-weight:bold;max-height:81.0px;*height:81.0px;color:#000000;text-decoration:none;}.thumbs-feed-01 .video-description{font-family:Arial, Helvetica, sans-serif;font-size:14px;line-height:19.0px;font-weight:normal;max-height:2.2em;*height:2.2em;color:black;text-decoration:none;}.thumbs-feed-01 .trc_rbox_div{width:auto;_width:99%;height:410px;border-width:0;padding:0;}.thumbs-feed-01 .videoCube .video-duration{left:36px;display:none;}.thumbs-feed-01 .videoCube .video-label-box{margin-left:;margin-right:;}.thumbs-feed-01 .video-label,.thumbs-feed-01 .sponsored,.thumbs-feed-01 .sponsored-url{font-family:Arial, Helvetica, sans-serif;}.thumbs-feed-01 .trc_rbox_header{font-family:Arial, Helvetica, sans-serif;font-size:100%;font-weight:bold;text-decoration:none;color:#000000;border-width:0;background:transparent;border-style:none;border-color:#D6D5D3;padding:0px 0px 2px 0px;}.thumbs-feed-01 .sponsored-url{font-size:9px;font-weight:bold;text-decoration:underline;color:green;}.thumbs-feed-01 .sponsored{font-size:9px;font-weight:normal;text-decoration:none;color:#9C9A9C;}.thumbs-feed-01 .video-category{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .video-duration-detail{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .video-rating{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .video-uploader{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .video-views{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .video-published-date{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .sponsored-default .video-title{max-height:2.58em;*height:2.58em;}.thumbs-feed-01 .sponsored-default .video-description{max-height:2.2em;*height:2.2em;}.thumbs-feed-01 .videoCube{width:auto;_width:auto;background-color:transparent;border-width:0px 0px 0px 0px;border-color:#E4E4E4;padding:0px 0px 0px 0px;height:auto;margin-left:0px;margin-top:0px;border-radius:0px;-moz-border-radius:0px;-webkit-border-radius:0px;border-style:SOLID;}.thumbs-feed-01 div.videoCube:hover,.thumbs-feed-01  div.videoCube_hover{background-color:transparent;}.thumbs-feed-01 .sponsored-default{background-color:#F7F6C6;}.thumbs-feed-01 div.sponsored-default:hover,.thumbs-feed-01  div.sponsored-default.videoCube_hover{background-color:inherit;}.thumbs-feed-01 .videoCube .thumbnail-overlay{background-image:null;background-position:5% 5%;}.thumbs-feed-01 .videoCube:hover .thumbnail-overlay,.thumbs-feed-01  .videoCube_hover .thumbnail-overlay{background-image:null;}.thumbs-feed-01 .trc_rbox_border_elm{border-color:darkgray;}.thumbs-feed-01 .videoCube .thumbBlock{border-width:0px;border-color:darkgray;}.thumbs-feed-01 div.videoCube:hover .thumbBlock{border-color:inherit;}.thumbs-feed-01 .pager_enabled{color:#0056b3;}.thumbs-feed-01 .trc_pager_counter{color:#000000;}.thumbs-feed-01 .pager_disabled{color:#7d898f;}.thumbs-feed-01 .trc_pager_prev:hover,.thumbs-feed-01  .trc_pager_next:hover{color:#6497ED;}.thumbs-feed-01 .trc_pager_selected{color:#0056b3;}.thumbs-feed-01 .trc_pager_unselected{color:#7d898f;}.thumbs-feed-01 div.trc_pager_pages div:hover{color:#6497ED;}.thumbs-feed-01 .trc_lightbox_overlay{background-color:#000000;opacity:0.70;filter:alpha(opacity=70);}.thumbs-feed-01 .video-label-box{text-align:left;}.thumbs-feed-01 .trc_sponsored_overlay{background-color:black;}.thumbs-feed-01 .thumbnail-emblem{background-position:5% 5%;}.thumbs-feed-01 .videoCube .sponsored{margin-top:-7px;}.thumbs-feed-01 {width:300px;_width:300px;border-width:0px 0px 0px 0px;border-style:solid solid solid solid;border-color:#DFDFDF;padding:0px 0px 0px 0px;border-radius:0;-moz-border-radius:0;-webkit-border-radius:0;box-shadow:none;}.thumbs-feed-01 .videoCube.vertical{border-style:solid none none none;}.thumbs-feed-01 .videoCube.horizontal{border-style:none;}.thumbs-feed-01 .trc_pager_prev,.thumbs-feed-01 .trc_pager_next{font-size:12px;font-weight:normal;text-decoration:none;}.thumbs-feed-01 .trc_pager_pages div{font-size:12px;font-weight:normal;text-decoration:none;}.thumbs-feed-01 .video-external-data{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .trc_pager div{font-family:serif;}.thumbs-feed-01 .playerCube .thumbnail-overlay{background-image:null;background-position:5% 5%;}.thumbs-feed-01 .playerCube:hover .thumbnail-overlay,.thumbs-feed-01  .playerCube_hover .thumbnail-overlay{background-image:null;}.thumbs-feed-01 .playerCube .videoCube{background-color:transparent;border-color:#D6D5D3;border-width:1px;border-radius:0px;-moz-border-radius:0px;-webkit-border-radius:0px;margin-left:0px;margin-top:0px;padding:3px;}.thumbs-feed-01 .playerCube .videoCube.horizontal{border-style:none none none none;}.thumbs-feed-01 .playerCube .videoCube .video-label-box{margin-left:81px;margin-right:0px;}.thumbs-feed-01 .playerCube .video-duration-detail{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .playerCube .video-external-data{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .playerCube .video-label-box{text-align:left;}.thumbs-feed-01 .playerCube .video-published-date{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .playerCube .video-category{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .playerCube .video-description{font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:11px;font-weight:normal;text-decoration:none;max-height:2.2em;*height:2.2em;color:black;}.thumbs-feed-01 .playerCube .videoCube .video-duration{display:block;left:36px;}.thumbs-feed-01 .playerCube .videoCube .thumbBlock{border-width:0px;border-color:darkgray;}.thumbs-feed-01 .playerCube .video-rating{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .playerCube .video-uploader{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .playerCube .video-views{font-size:10px;font-weight:normal;text-decoration:none;color:black;}.thumbs-feed-01 .playerCube .video-title{font-family:Arial, Helvetica, sans-serif;text-decoration:none;font-size:14px;line-height:17.5px;font-weight:bold;max-height:2.58em;*height:2.58em;color:black;}.thumbs-feed-01 .playerCube div.videoCube:hover,.thumbs-feed-01  div.videoCube_hover{background-color:transparent;}.thumbs-feed-01 .whatsThisSyndicated{font-family:Arial, Verdana, sans-serif;font-size:9px;font-weight:normal;color:black;text-decoration:none;padding:0;}.thumbs-feed-01 div.syndicatedItem:hover,.thumbs-feed-01  div.syndicatedItem.videoCube_hover{background-color:transparent;}.thumbs-feed-01 div.syndicatedItem:hover .thumbBlock{border-color:inherit;}.thumbs-feed-01 .videoCube.syndicatedItem{background-color:transparent;border-color:#E4E4E4;border-radius:0px;-moz-border-radius:0px;-webkit-border-radius:0px;border-width:0px 0px 0px 0px;border-style:SOLID;}.thumbs-feed-01 .videoCube.syndicatedItem.horizontal{border-style:none;}.thumbs-feed-01 .videoCube.syndicatedItem .thumbBlock{border-color:darkgray;border-width:0px;}.thumbs-feed-01 .videoCube.syndicatedItem .thumbnail-overlay{background-image:null;background-position:5% 5%;}.thumbs-feed-01 .videoCube.syndicatedItem.vertical{border-style:solid none none none;}.thumbs-feed-01 .videoCube.syndicatedItem .video-duration{display:none;left:36px;}.thumbs-feed-01 .videoCube.syndicatedItem .video-label-box{margin-left:;}.thumbs-feed-01 .syndicatedItem{background-color:transparent;}.thumbs-feed-01 .syndicatedItem .video-description{max-height:2.2em;*height:2.2em;color:black;font-family:Arial, Helvetica, sans-serif;font-size:14px;font-weight:normal;line-height:19.0px;text-decoration:none;}.thumbs-feed-01 .syndicatedItem .video-title{max-height:54.0px;*height:54.0px;color:#000000;font-family:Arial, Helvetica, sans-serif;font-size:20.0px;line-height:27.0px;font-weight:bold;text-decoration:none;}.thumbs-feed-01 .syndicatedItem .sponsored{color:#9C9A9C;font-size:9px;font-weight:normal;text-decoration:none;}.thumbs-feed-01 .syndicatedItem .sponsored-url{color:green;font-size:9px;font-weight:bold;text-decoration:underline;}.thumbs-feed-01 .syndicatedItem .video-category{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbs-feed-01 .syndicatedItem .video-duration-detail{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbs-feed-01 .syndicatedItem .video-external-data{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbs-feed-01 .syndicatedItem .video-published-date{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbs-feed-01 .syndicatedItem .video-rating{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbs-feed-01 .syndicatedItem .video-uploader{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbs-feed-01 .syndicatedItem .video-views{color:black;font-size:10px;font-weight:normal;text-decoration:none;}.thumbs-feed-01 .syndicatedItem .branding{color:#999999;font-size:11.0px;font-weight:bold;text-decoration:none;font-family:Arial, Helvetica, sans-serif;background-image:null;text-align:left;}.thumbs-feed-01 .videoCube.syndicatedItem .thumbBlock .branding{text-align:left;background-color:transparent;display:none;left:0px;color:black;font-size:10px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;background-image:null;}.thumbs-feed-01 .videoCube.syndicatedItem .thumbBlock .static-text{text-align:left;background-color:black;display:none;color:white;font-size:10px;font-weight:normal;text-decoration:none;font-family:Arial, Helvetica, sans-serif;}.thumbs-feed-01 .videoCube.thumbnail_start .thumbBlock_holder{width:40%;_width:40%;}.thumbs-feed-01 .trc_rbox_header_icon_img{margin:0px;height:18px;}.thumbs-feed-01 .video-icon-img{margin:0px;height:18px;}.thumbs-feed-01 .video-label-box.trc-pre-label{height:0px;}.thumbs-feed-01 .syndicatedItem .video-label-box.trc-pre-label{height:0px;}.thumbs-feed-01 .videoCube.thumbnail_start .trc-pre-label{width:60%;_width:60%;}.thumbs-feed-01 .videoCube.thumbnail_start.trc-split-label .trc-main-label{width:30%;_width:30%;}.thumbs-feed-01 .videoCube.thumbnail_start.trc-split-label .trc-pre-label{width:30%;_width:30%;}.thumbs-feed-01 .videoCube .video-label-box.trc-pre-label{margin:0px 0px 0px 0px;}.thumbs-feed-01 .branding{color:#999999;font-size:11.0px;font-weight:bold;text-decoration:none;font-family:Arial, Helvetica, sans-serif;background-image:null;text-align:left;}.thumbs-feed-01 .branding .logoDiv a span{color:inherit;font-size:inherit;}.thumbs-feed-01 .branding div.logoDiv{font-family:inherit;}.thumbnails-a img {
max-width: none;
}
/* override bootstrap default span definitions */
.thumbnails-a [class*=span] {
    float:none;
    margin: 0px 0px 0px 0px!important;
}
.thumbnails-a .trc_rbox_header {
    line-height: 1.2em;
    position: relative;
    display: block;
    width: auto;
    margin: 0px 0px 0px 0px;
    background: transparent;
    height: auto;
    background-color: transparent;
    box-sizing: initial;
    margin-left: 0px!important;
    width: 675px!important;
}
.thumbnails-a .trc_rbox_header_span .trc_header_right_column {
    display: none;
    background: transparent;
    height: auto;
}
.thumbnails-a .trc_rbox_header .logoDiv {
    font-size: inherit;
    line-height: normal;
}
.thumbnails-a .logoDiv .trc_desktop_disclosure_link.trc_attribution_position_top {
    display: none;
}
.thumbnails-a .logoDiv a {
    font-size: 100%;
}
.thumbnails-a .logoDiv a span {
    display: inline;
    color: #999;
    font-weight: normal;
    font-size: 12.0px;
}
.thumbnails-a .logoDiv a.trc_mobile_disclosure_link span {
    display: none;
}
.thumbnails-a .logoDiv a span:hover {
    display: inline;
    color: #999; /* changed */
    font-weight: normal;
    font-size: 12.0px;
}
.thumbnails-a .videoCube a {
    width: 210px!important;
    /*height: 208px!important;*/
    margin: 0px 23px 0px 0px!important;
    display: block; /*changed*/
}
.thumbnails-a .videoCube a:hover {
    background: none !important;
}
.thumbnails-a .trc_rbox_header .logoDiv a:hover {
    background: none !important;
}
.thumbnails-a .thumbBlock {
    margin: 0;
}
.thumbnails-a .video-label-box {
    margin: 5px 0px 0px 0px;
    height: 57px;
}
.thumbnails-a .syndicatedItem .video-label-box {
    margin: 5px 0px 0px 0px;
    height: 57px;
}
.thumbnails-a .videoCube .video-label-box .video-title {
    text-decoration: none;
    /*margin-top: -40px;*/
    margin: -20px 0px 5px 0px; /*changed*/
    width: 210px!important;
}
.thumbnails-a .videoCube:hover .video-label-box .video-title,
.thumbnails-a .videoCube:hover .video-label-box .video-description {
    text-decoration: underline;
}
.thumbnails-a .video-label-box .branding {
    display: block;
    line-height: 19.0px;
}
.thumbnails-a .syndicatedItem .branding {
    line-height: 19.0px;
}
.thumbnails-a .trc_header_left_column {
    width: 48%;
    display: inline-block;
    background: transparent;
    height: auto;
}
.thumbnails-a .trc_header_right_part {
    margin-top: 0px;
}
.thumbnails-a .trc_rbox_header .logoDiv a {
    font-size: 100%;
}
.thumbnails-a .trc_rbox_header .trc_header_ext {
    position: relative;
    top: auto;
    right: auto;
}
.thumbnails-a .videoCube.syndicatedItem .thumbBlock {
    width: 210px;
    height: 120px;
    top: 20px;
    padding: 0px 0px 0px 0px;
    margin-top: -22px;
}
.thumbnails-a .videoCube .thumbBlock {
    width: 210px!important;
    height: 120px!important;
    top: 20px!important;
    padding: 0px 0px 0px 0px!important;
    margin-top: -22px;
}
.thumbnails-a .trc_rbox_div{
    padding: 0px 0px 50px 0px;
    width: 700px!important;
    /*margin: 0px 0px 0px 14px!important;*/
    margin: 0px!important;
}
.thumbnails-a .videoCube.syndicatedItem {
    width: 210px!important;
    height: 208px!important;
    margin: 0px 23px 0px 0px!important;
}
.thumbnails-a .videoCube {
    width: 210px!important;
    height: 208px!important;
    margin: 0px 23px 0px 0px!important;
}
.trc_elastic .videoCube_aspect{
    padding: 20px 0px 120px 0px!important;
}
.trc_desktop_disclosure_link.trc_attribution_position_top{
    display: none;
}
.trc_elastic_thumbnails-a .trc_rbox_outer {
    margin-left: 0!important;
    margin-top: 15px;
}
.thumbnails-a .video-title {
    max-height: 40px;
}
.thumbnails-rr img {
max-width: none;
}
/* override bootstrap default span definitions */
.thumbnails-rr [class*=span] {
    float:none;
    margin-left:0;
}
.thumbnails-rr .trc_rbox_div {
    margin-bottom: 0;
    margin-top: -10px;
}
.thumbnails-rr .trc_rbox_header {
    line-height: 1.2em;
    position: relative;
    display: block;
    width: auto;
    margin: 0px 0px 0px 0px;
    background: transparent;
    height: auto;
    background-color: transparent;
    box-sizing: initial;
    font-weight: normal; /*change*/
}
.thumbnails-rr .trc_rbox_header_span .trc_header_right_column {
    display: none;
    background: transparent;
    height: auto;
}
.thumbnails-rr .trc_rbox_header .logoDiv {
    font-size: inherit;
    line-height: normal;
}
.thumbnails-rr .logoDiv a {
    font-size: 100%;
}
.thumbnails-rr .logoDiv a span {
    display: inline;
    color: #999;
    font-weight: normal;
    font-size: 12.0px;
    position: relative;
    /*right: 640px;*/
}
.thumbnails-rr .videoCube a {
    padding: 0;
}
.thumbnails-rr .trc_rbox_outer .videoCube {
    margin-bottom: 0px!important;
    margin-top: 20px;
    height:115px
}
.thumbnails-rr .thumbBlock {
    margin: 0;
    width: 100px;
    height: 115px;
}
.thumbnails-rr .videoCube .video-label-box .video-title {
    text-decoration: none;
    margin-bottom: 0;
    padding: 0px 0px 5px 0px;
    /*height: 38.0px;*/
}
.thumbnails-rr .video-title {
    font-size: 14.0px;
    line-height: 20.0px;
    font-weight: normal;
    max-height: 38.0px;
    color: #111;
    text-decoration: none;
}
.thumbnails-rr .syndicatedItem .video-title {
    font-weight: normal;
}
.thumbnails-rr .videoCube:hover .video-label-box .video-title,
.thumbnails-rr .videoCube:hover .video-label-box .video-description {
    text-decoration: underline;
}
.thumbnails-rr .video-label-box .branding {
    display: block;
    line-height: 19.0px;
    text-overflow: ellipsis;
    height: 19px;
    white-space: nowrap;
    overflow: hidden;
}
.thumbnails-rr .syndicatedItem .branding {
    line-height: 19.0px;
}
.thumbnails-rr .video-label-box {
    margin: 0px 0px 0px 0px;
    height: auto;
}
.thumbnails-rr .syndicatedItem .video-label-box {
    margin: 0px 0px 0px 0px;
    height: auto;
}
.thumbnails-rr .trc_header_left_column {
    width: 48%;
    display: inline-block;
    background: transparent;
    height: auto;
}
.thumbnails-rr .trc_header_right_part {
    margin-top: 0px;
}
.thumbnails-rr .trc_rbox_header .logoDiv a {
    font-size: 100%;
}
.thumbnails-rr .trc_rbox_header .trc_header_ext {
    position: relative;
    top: auto;
    right: auto;
}
.thumbnails-rr .videoCube.thumbnail_start .thumbBlock_holder  {
    width: 100px;
}
.trc_elastic .thumbnail_start .thumbBlock_holder{
    margin-right: 12px;
}
.thumbnails-rr .trc_rbox_div{
    padding: 0px 0px 15px 0px;
    /*width: 500px;*/
}
.thumbnails-rr .videoCube {
    height: 70px;
}
.thumbnails-rr .trc-widget-footer {
    display: inline-block;
}
.thumbnails-rr .trc-widget-footer a:hover {
    background: #fff;
}
.thumbs-feed-01 img {
        max-width: none;
}
/* override bootstrap default span definitions */
.thumbs-feed-01 [class*=span] {
    float:none;
    margin-left:0;
}
.thumbs-feed-01 .trc_rbox_header {
        line-height: 1.2em;
        position: relative;
        display: none;
        width: auto;
	margin: 0px 0px 0px 0px;
	background: transparent;
	height: auto;
	background-color: transparent;
	box-sizing: initial;
}
.thumbs-feed-01 .trc_rbox_header_span .trc_header_right_column {
        display: none;
	background: transparent;
	height: auto;
}
.thumbs-feed-01 .trc_rbox_header .logoDiv {
        font-size: inherit;
        line-height: normal;
}
.thumbs-feed-01 .logoDiv a {
    font-size: 100%;
}
.thumbs-feed-01 .logoDiv a span {
    display: inline;
    color: #999999;
    font-weight: normal;
    font-size: 11.0px;
}
.thumbs-feed-01 .videoCube a {
    padding: 0;
}
.thumbs-feed-01 .thumbBlock {
    margin: 0;
}
.thumbs-feed-01 .video-label-box {
    margin: 5px 0px 0px 0px;
    height: 81px;
}
.thumbs-feed-01 .syndicatedItem .video-label-box {
    margin: 5px 0px 0px 0px;
    height: 81px;
}
.thumbs-feed-01 .videoCube .video-label-box .video-title {
    text-decoration: none;
    margin: 0;
}
.thumbs-feed-01 .videoCube:hover .video-label-box .video-title,
.thumbs-feed-01 .videoCube:hover .video-label-box .video-description {
    text-decoration: underline;
}
.thumbs-feed-01 .video-label-box .branding {
    display: block;
	line-height: 27.0px;
}
.thumbs-feed-01 .syndicatedItem .branding {
    line-height: 27.0px;
}
.thumbs-feed-01 .trc_header_left_column {
	background: transparent;
	height: auto;
}
.thumbs-feed-01 .trc_header_right_part {
	margin-top: 0px;
}
.thumbs-feed-01 .trc_rbox_header .logoDiv a {
	font-size: 100%;
}
.thumbs-feed-01 .trc_rbox_header .trc_header_ext {
	position: relative;
	top: auto;
	right: auto;
}
</style><style type="text/css">@media screen and (min-width: 0px) {.trc_elastic_thumbnails-rr .trc_rbox_outer .videoCube .video-label-box {height:auto;}.trc_elastic_thumbnails-rr .trc_rbox_outer .videoCube {margin-bottom:10px;}.trc_elastic_thumbnails-rr .trc_rbox_outer{margin-left:-2%;}.trc_elastic_thumbnails-rr .videoCube_aspect{padding-bottom:71.42857142857143%; width: 100%;}.trc_elastic_thumbnails-rr .videoCube{width: 97.99%; position: relative; float: left; margin: 0 0 2% 0; margin-left: 2%;}.trc_elastic_thumbnails-rr div.videoCube:nth-of-type(-n+2){display:block;visibility:visible;}.trc_elastic_thumbnails-rr div.videoCube:nth-of-type(n+3){display:none;visibility:hidden;}} </style><style type="text/css">.trc_user_exclude_btn { background: url("//cdn.taboola.com/libtrc/static/thumbnails/f539211219b796ffbb49949997c764f0.png") no-repeat scroll 0 0 transparent; width: 12px; height: 12px; position: absolute; right: 2px; top: 2px; z-index: 9000; cursor: pointer; visibility: hidden; }.trc_undo_btn { font-family: Arial, Helvetica, sans-serif; font-size: 11px; line-height: 14px; font-weight: normal; color: #3366CC; text-decoration: underline; cursor: pointer; position: absolute; right: 2px; top: 2px; padding: 0 1px; z-index: 11000; visibility: hidden; }.videoCube:hover .trc_user_exclude_btn,.videoCube_hover .trc_user_exclude_btn,.trc_user_excluded.videoCube:hover .trc_undo_btn,.trc_user_excluded.videoCube_hover .trc_undo_btn,.trc_undo_btn.trc_anchor { visibility: visible; }.videoCube.trc_user_excluded .trc_user_exclude_btn { visibility: hidden; }.trc_fade { opacity: 0; filter: alpha(opacity=0); visibility: hidden; -webkit-transition: opacity 500ms 0s, visibility 0s 500ms; -moz-transition: opacity 500ms 0s, visibility 0s 500ms; -ms-transition: opacity 500ms 0s, visibility 0s 500ms; -o-transition: opacity 500ms 0s, visibility 0s 500ms; transition: opacity 500ms 0s, visibility 0s 500ms; }.trc_fade.trc_in,.trc_user_excluded .trc_exclude_overlay { visibility: visible; opacity: 1; filter: alpha(opacity=100); -webkit-transition-delay: 0s, 0s; -moz-transition-delay: 0s, 0s; -ms-transition-delay: 0s, 0s; -o-transition-delay: 0s, 0s; transition-delay: 0s, 0s; }.trc_excludable .trc_exclude_overlay { position: absolute; z-index: 10000; top: 0; left: 0; width: 100%; height: 100%; cursor: default; background-color: white; /* this is to make elements from underneath this overlay unclickable in IE */ }.videoCube.trc_excludable .trc_exclude_overlay.trc_fade { filter: alpha(opacity=80) 9; /* fix for IE8 and below - keep opacity the same or else it goes crazy, because we also change the visibility */ }.videoCube.trc_user_excluded .trc_exclude_overlay { visibility: visible; opacity: 0.8; filter: alpha(opacity=80); }.videoCube.trc_user_excluded .thumbBlock { filter: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg'><filter id='grayscale'><feColorMatrix type='matrix' values='0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0.3333 0.3333 0.3333 0 0 0 0 0 1 0' /></filter></svg>#grayscale"); filter: gray; -webkit-filter: grayscale(100%); }.videoCube.trc_user_excluded a .video-label-box .label-box-overlay { background-color: #BBBBBB; -webkit-transition: background-color 500ms 0s; -moz-transition: background-color 500ms 0s; -ms-transition: background-color 500ms 0s; -o-transition: background-color 500ms 0s; transition: background-color 500ms 0s; }.videoCube.trc_user_excluded:hover a .video-label-box .video-title,.videoCube_hover.trc_user_excluded a .video-label-box .video-title { text-decoration: none; }.videoCube.trc_user_excluded a .video-label-box *,.videoCube.trc_user_excluded:hover a .video-label-box *,.videoCube_hover.trc_user_excluded a .video-label-box * { color: #000000; overflow: hidden; /* fixes a bug in IE7 - opacity does not work with overflow: visible */ -webkit-transition: color 500ms 0s; -moz-transition: color 500ms 0s; -ms-transition: color 500ms 0s; -o-transition: color 500ms 0s; transition: color 500ms 0s; }.videoCube.thumbnail_under.trc_user_excluded .video-labels-anchor,.videoCube.thumbnail_under.trc_user_excluded:hover .video-labels-anchor { max-height: none; -webkit-transition: none; -moz-transition: none; -o-transition: none; transition: none; }
                .trc_popover_aug_container { position: static; }#tbl-aug-sazlah #tbl-aug-ewtiqf #tbl-aug-vtnyds .trc_popover { position: absolute; font-family: Arial, Helvetica, sans-serif; font-size: 12px; line-height: 16px; color: #000000; cursor: default; top: 0; right: 0; z-index: 12000; width: 180px; padding: 1px; text-align: left; white-space: normal; background-color: #ffffff; border: 1px solid rgba(0, 0, 0, 0.2); -webkit-border-radius: 6px; -moz-border-radius: 6px; -ms-border-radius: 6px; -o-border-radius: 6px; border-radius: 6px; -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2); -moz-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2); -ms-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2); -o-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2); box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2); -webkit-background-clip: padding-box; -moz-background-clip: padding-box; -ms-background-clip: padding-box; -o-background-clip: padding-box; background-clip: padding-box; -moz-background-clip: padding; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; -ms-box-sizing: content-box; -o-box-sizing: content-box; box-sizing: content-box; } #tbl-aug-sazlah #tbl-aug-ewtiqf #tbl-aug-vtnyds .trc_popover.trc_bottom { margin-top: 10px; } #tbl-aug-sazlah #tbl-aug-ewtiqf #tbl-aug-vtnyds .trc_popover.trc_bottom .trc_popover_arrow { top: -11px; right: 11px; margin-left: -11px; border-bottom-color: #999; border-bottom-color: rgba(0, 0, 0, 0.25); border-top-width: 0; } #tbl-aug-sazlah #tbl-aug-ewtiqf #tbl-aug-vtnyds .trc_popover.trc_bottom .trc_popover_arrow:after { top: 1px; margin-left: -10px; border-bottom-color: #ffffff; border-top-width: 0; } #tbl-aug-sazlah #tbl-aug-ewtiqf #tbl-aug-vtnyds .trc_popover iframe { width: 100%; } #tbl-aug-sazlah #tbl-aug-ewtiqf #tbl-aug-vtnyds .trc_popover .trc_popover_arrow, #tbl-aug-sazlah #tbl-aug-ewtiqf #tbl-aug-vtnyds .trc_popover .trc_popover_arrow:after { position: absolute; display: block; width: 0; height: 0; border: solid transparent; } #tbl-aug-sazlah #tbl-aug-ewtiqf #tbl-aug-vtnyds .trc_popover .trc_popover_arrow { border-width: 11px; } #tbl-aug-sazlah #tbl-aug-ewtiqf #tbl-aug-vtnyds .trc_popover .trc_popover_arrow:after { border-width: 10px; content: ""; }#tbl-aug-sazlah #tbl-aug-ewtiqf #tbl-aug-vtnyds .trc_popover_fade { visibility: hidden; opacity: 0; filter: alpha(opacity=0); -webkit-transition: opacity 500ms 0s, visibility 0s 500ms; -moz-transition: opacity 500ms 0s, visibility 0s 500ms; -ms-transition: opacity 500ms 0s, visibility 0s 500ms; -o-transition: opacity 500ms 0s, visibility 0s 500ms; transition: opacity 500ms 0s, visibility 0s 500ms; } #tbl-aug-sazlah #tbl-aug-ewtiqf #tbl-aug-vtnyds .trc_popover_fade.trc_in { visibility: visible; opacity: 1; filter: alpha(opacity=100); -webkit-transition-delay: 0s, 0s; -moz-transition-delay: 0s, 0s; -ms-transition-delay: 0s, 0s; -o-transition-delay: 0s, 0s; transition-delay: 0s, 0s; }</style><script src="//vidstat.taboola.com/vpaid/units/14_12_0/creatives/creative_js.js"></script><script type="text/javascript" src="//vidstat.taboola.com/vpaid/units/23_14_8/infra/cmTagINLINE_INSTREAM.js"></script><link type="text/css" rel="stylesheet" href="//vidstat.taboola.com/vpaid/units/23_14_8/assets/css/cmOsUnit.css"><script src="//vidstat.taboola.com/content14_10_18m.js"></script><script src="//vidstat.taboola.com/vpaid/vPlayer/player/v10.4.4/OvaMediaPlayer.js"></script><link rel="stylesheet" type="text/css" href="//vidstat.taboola.com/vpaid/vPlayer/player/v10.4.4/assets/player.css"></head>

<body>
  
    <script type="text/javascript">var _body_start = new Date();</script>

    
    



    <link href="//img3.doubanio.com/dae/accounts/resources/2f48733/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <a href="https://accounts.douban.com/passport/login?source=movie" class="nav-login" rel="nofollow">登录/注册</a>
</div>


    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&amp;direct_dl=1&amp;download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&amp;direct_dl=1&amp;download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
    </li>
    <li class="">
      <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
    </li>
    <li class="on">
      <a href="https://movie.douban.com" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com/?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm/?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com/?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com/?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">豆品</a>
    </li>
    <li>
      <a href="#more" class="bn-more"><span>更多</span></a>
      <div class="more-items">
        <table cellspacing="0" cellpadding="0">
          <tbody>
            <tr>
              <td>
                <a href="https://ypy.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-ypy&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣摄影</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/2f48733/shire/bundle.js" defer="defer"></script>




    



    <link href="//img3.doubanio.com/dae/accounts/resources/2f48733/movie/bundle.css" rel="stylesheet" type="text/css">




<div id="db-nav-movie" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https://movie.douban.com">豆瓣电影</a>
    </div>
    <div class="nav-search">
      <form action="https://movie.douban.com/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="搜索电影、电视剧、综艺、影人" value="" autocomplete="off"></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1002">
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">
    

<div class="nav-items">
  <ul>
    <li><a href="https://movie.douban.com/cinema/nowplaying/">影讯&amp;购票</a>
    </li>
    <li><a href="https://movie.douban.com/explore">选电影</a>
    </li>
    <li><a href="https://movie.douban.com/tv/">电视剧</a>
    </li>
    <li><a href="https://movie.douban.com/chart">排行榜</a>
    </li>
    <li><a href="https://movie.douban.com/tag/">分类</a>
    </li>
    <li><a href="https://movie.douban.com/review/best/">影评</a>
    </li>
    <li><a href="https://movie.douban.com/annual/2018?source=navigation">2018年度榜单</a>
    </li>
    <li><a href="https://www.douban.com/standbyme/2018?source=navigation">2018书影音报告</a>
    </li>
  </ul>
</div>

    <a href="https://movie.douban.com/annual/2018?source=movie_navigation" class="movieannual2018"></a>
  </div>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'movie_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= img}}" width="40" />
            <p>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                {{if sub_title}}
                    <br /><span>{{= sub_title}}</span>
                {{/if}}
                {{if address}}
                    <br /><span>{{= address}}</span>
                {{/if}}
                {{if episode}}
                    {{if episode=="unknow"}}
                        <br /><span>集数未知</span>
                    {{else}}
                        <br /><span>共{{= episode}}集</span>
                    {{/if}}
                {{/if}}
            </p>
        </a>
        </li>
  </script>




    <script src="//img3.doubanio.com/dae/accounts/resources/2f48733/movie/bundle.js" defer="defer"></script>





    
    <div id="wrapper">
        

        
    <div id="content">
        

    <div id="dale_movie_subject_top_icon" ad-status="loaded"></div>
    <h1>
        <span property="v:itemreviewed">昨日奇迹 Yesterday</span>
            <span class="year">(2019)</span>
    </h1>

        <div class="grid-16-8 clearfix">
            

            
            <div class="article">
                
    

    





        <div class="indent clearfix">
            <div class="subjectwrap clearfix">
                <div class="subject clearfix">
                    



<div id="mainpic" class="">
    <a class="nbgnbg" href="https://movie.douban.com/subject/30165034/photos?type=R" title="点击看更多海报">
        <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2561245949.jpg" title="点击看更多海报" alt="Yesterday" rel="v:image">
   </a>
</div>

                    


<div id="info">
        <span><span class="pl">导演</span>: <span class="attrs"><a href="/celebrity/1054404/" rel="v:directedBy">丹尼·博伊尔</a></span></span><br>
        <span><span class="pl">编剧</span>: <span class="attrs"><a href="/celebrity/1410722/">杰克·巴斯</a> / <a href="/celebrity/1040673/">理查德·柯蒂斯</a></span></span><br>
        <span class="actor"><span class="pl">主演</span>: <span class="attrs"><span><a href="/celebrity/1391915/" rel="v:starring">希米什·帕特尔</a> / </span><span><a href="/celebrity/1318674/" rel="v:starring">莉莉·詹姆斯</a> / </span><span><a href="/celebrity/1355940/" rel="v:starring">艾德·希兰</a> / </span><span><a href="/celebrity/1319532/" rel="v:starring">凯特·麦克金农</a> / </span><span><a href="/celebrity/1327567/" rel="v:starring">阿历克斯·阿诺</a> / </span><span style="display: none;"><a href="/celebrity/1352741/" rel="v:starring">乔尔·弗莱</a> / </span><span style="display: none;"><a href="/celebrity/1017966/" rel="v:starring">詹姆斯·柯登</a> / </span><span style="display: none;"><a href="/celebrity/1071717/" rel="v:starring">卡米利·陈</a> / </span><span style="display: none;"><a href="/celebrity/1324073/" rel="v:starring">拉蒙尼·莫里斯</a> / </span><span style="display: none;"><a href="/celebrity/1202935/" rel="v:starring">索菲娅·迪·马蒂诺</a> / </span><span style="display: none;"><a href="/celebrity/1050009/" rel="v:starring">卡米拉·拉瑟福德</a> / </span><span style="display: none;"><a href="/celebrity/1400644/" rel="v:starring">艾利斯·查普尔</a> / </span><span style="display: none;"><a href="/celebrity/1027525/" rel="v:starring">莎拉·兰卡夏尔</a> / </span><span style="display: none;"><a href="/celebrity/1327058/" rel="v:starring">多米尼克·科尔曼</a> / </span><span style="display: none;"><a href="/celebrity/1383566/" rel="v:starring">玛丽安娜·斯皮瓦克</a> / </span><span style="display: none;"><a href="/celebrity/1173092/" rel="v:starring">詹妮弗·阿尔莫</a> / </span><span style="display: none;"><a href="/celebrity/1045259/" rel="v:starring">安娜·德·阿玛斯</a> / </span><span style="display: none;"><a href="/celebrity/1392995/" rel="v:starring">哈廷·帕特尔</a> / </span><span style="display: none;"><a href="/celebrity/1397360/" rel="v:starring">阿图尔·夏尔马</a> / </span><span style="display: none;"><a href="/celebrity/1395012/" rel="v:starring">马诺伊·阿南德</a> / </span><span style="display: none;"><a href="/celebrity/1221389/" rel="v:starring">哈里·米歇尔</a> / </span><span style="display: none;"><a href="/celebrity/1355273/" rel="v:starring">珊妮·姚</a> / </span><span style="display: none;"><a href="/celebrity/1273387/" rel="v:starring">乔希·特雷特</a> / </span><span style="display: none;"><a href="/celebrity/1270161/" rel="v:starring">西蒙·P·爱德华兹</a></span><a href="javascript:;" class="more-actor" title="更多主演">更多...</a></span></span><br>
        <span class="pl">类型:</span> <span property="v:genre">喜剧</span> / <span property="v:genre">音乐</span> / <span property="v:genre">奇幻</span><br>
        
        <span class="pl">制片国家/地区:</span> 英国<br>
        <span class="pl">语言:</span> 英语<br>
        <span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="2019-08-16(中国大陆)">2019-08-16(中国大陆)</span> / <span property="v:initialReleaseDate" content="2019-05-05(翠贝卡电影节)">2019-05-05(翠贝卡电影节)</span> / <span property="v:initialReleaseDate" content="2019-06-28(英国)">2019-06-28(英国)</span><br>
        <span class="pl">片长:</span> <span property="v:runtime" content="116">116分钟</span><br>
        <span class="pl">又名:</span> 缘來自昨天(港) / 靠谱歌王(台) / 昨天 / 昨日 / 你需要的只是爱 / All You Need is Love<br>
        <span class="pl">IMDb链接:</span> <a href="http://www.imdb.com/title/tt8079248" target="_blank" rel="nofollow">tt8079248</a><br>

</div>




                </div>
                    


<div id="interest_sectl">
    <div class="rating_wrap clearbox" rel="v:rating">
        <div class="clearfix">
          <div class="rating_logo ll">豆瓣评分</div>
          <div class="output-btn-wrap rr" style="">
            <img src="https://img3.doubanio.com/f/movie/692e86756648f29457847c5cc5e161d6f6b8aaac/pics/movie/reference.png">
            <a class="download-output-image" href="#">引用</a>
          </div>
          
          
        </div>
        



<div class="rating_self clearfix" typeof="v:Rating">
    <strong class="ll rating_num" property="v:average">6.6</strong>
    <span property="v:best" content="10.0"></span>
    <div class="rating_right ">
        <div class="ll bigstar bigstar35"></div>
        <div class="rating_sum">
                <a href="collections" class="rating_people">
                    <span property="v:votes">5470</span>人评价
                </a>
        </div>
    </div>
</div>
<div class="ratings-on-weight">
    
        <div class="item">
        
        <span class="stars5 starstop" title="力荐">
            5星
        </span>
        <div class="power" style="width:8px"></div>
        <span class="rating_per">6.6%</span>
        <br>
        </div>
        <div class="item">
        
        <span class="stars4 starstop" title="推荐">
            4星
        </span>
        <div class="power" style="width:36px"></div>
        <span class="rating_per">29.1%</span>
        <br>
        </div>
        <div class="item">
        
        <span class="stars3 starstop" title="还行">
            3星
        </span>
        <div class="power" style="width:64px"></div>
        <span class="rating_per">51.5%</span>
        <br>
        </div>
        <div class="item">
        
        <span class="stars2 starstop" title="较差">
            2星
        </span>
        <div class="power" style="width:13px"></div>
        <span class="rating_per">11.2%</span>
        <br>
        </div>
        <div class="item">
        
        <span class="stars1 starstop" title="很差">
            1星
        </span>
        <div class="power" style="width:1px"></div>
        <span class="rating_per">1.6%</span>
        <br>
        </div>
</div>

    </div>
        <div class="rating_betterthan">
            好于 <a href="/typerank?type_name=音乐&amp;type=14&amp;interval_id=25:15&amp;action=">20% 音乐片</a><br>
            好于 <a href="/typerank?type_name=喜剧&amp;type=24&amp;interval_id=40:30&amp;action=">39% 喜剧片</a><br>
        </div>
</div>


                
            </div>
                




<div id="interest_sect_level" class="clearfix">
        
            <a href="https://www.douban.com/reason=collectwish&amp;ck=" rel="nofollow" class="j a_show_login colbutt ll" name="pbtn-30165034-wish">
                <span>想看</span>
            </a>
            <a href="https://www.douban.com/reason=collectcollect&amp;ck=" rel="nofollow" class="j a_show_login colbutt ll" name="pbtn-30165034-collect">
                <span>看过</span>
            </a>
        <div class="ll j a_stars">
            
    
    评价:
    <span id="rating"> <span id="stars" data-solid="https://img3.doubanio.com/f/shire/5a2327c04c0c231bced131ddf3f4467eb80c1c86/pics/rating_icons/star_onmouseover.png" data-hollow="https://img3.doubanio.com/f/shire/2520c01967207a1735171056ec588c8c1257e5f8/pics/rating_icons/star_hollow_hover.png" data-solid-2x="https://img3.doubanio.com/f/shire/7258904022439076d57303c3b06ad195bf1dc41a/pics/rating_icons/star_onmouseover@2x.png" data-hollow-2x="https://img3.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png">

            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-30165034-1">
        <img src="https://img3.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png" id="star1" width="16" height="16"></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-30165034-2">
        <img src="https://img3.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png" id="star2" width="16" height="16"></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-30165034-3">
        <img src="https://img3.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png" id="star3" width="16" height="16"></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-30165034-4">
        <img src="https://img3.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png" id="star4" width="16" height="16"></a>
            <a href="https://www.douban.com/register?reason=rate" class="j a_show_login" name="pbtn-30165034-5">
        <img src="https://img3.doubanio.com/f/shire/95cc2fa733221bb8edd28ad56a7145a5ad33383e/pics/rating_icons/star_hollow_hover@2x.png" id="star5" width="16" height="16"></a>
    </span><span id="rateword" class="pl"></span>
    <input id="n_rating" type="hidden" value="">
    </span>

        </div>
    

</div>


            

















<div class="gtleft">
    <ul class="ul_subject_menu bicelink color_gray pt6 clearfix">
        
    
        
                <li> 
    <img src="https://img3.doubanio.com/f/shire/cc03d0fcf32b7ce3af7b160a0b85e5e66b47cc42/pics/short-comment.gif">&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_cmnt_login'})" class="j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow">写短评</a>
 </li>
                    <li> 
    
    <img src="https://img3.doubanio.com/f/shire/5bbf02b7b5ec12b23e214a580b6f9e481108488c/pics/add-review.gif">&nbsp;
        <a onclick="moreurl(this, {from:'mv_sbj_wr_rv_login'})" class="j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow">写影评</a>
 </li>
                <li> 
    



 </li>
                <li> 
   

   
    
    <span class="rec" id="电影-30165034">
    <a href="#" data-type="电影" data-url="https://movie.douban.com/subject/30165034/" data-desc="电影《昨日奇迹 Yesterday》 (来自豆瓣) " data-title="电影《昨日奇迹 Yesterday》 (来自豆瓣) " data-pic="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2561245949.jpeg" class="bn-sharing ">
        分享到
    </a> &nbsp;&nbsp;
    </span>

    <script>
        if (!window.DoubanShareMenuList) {
            window.DoubanShareMenuList = [];
        }
        var __cache_url = __cache_url || {};

        (function(u){
            if(__cache_url[u]) return;
            __cache_url[u] = true;
            window.DoubanShareIcons = 'https://img3.doubanio.com/f/shire/d15ffd71f3f10a7210448fec5a68eaec66e7f7d0/pics/ic_shares.png';

            var initShareButton = function() {
                $.ajax({url:u,dataType:'script',cache:true});
            };

            if (typeof Do == 'function' && 'ready' in Do) {
                Do(
                    'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
                    'https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js',
                    'https://img3.doubanio.com/f/movie/c4ab132ff4d3d64a83854c875ea79b8b541faf12/js/movie/lib/qrcode.min.js',
                    initShareButton
                );
            } else if(typeof Douban == 'object' && 'loader' in Douban) {
                Douban.loader.batch(
                    'https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css',
                    'https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js',
                    'https://img3.doubanio.com/f/movie/c4ab132ff4d3d64a83854c875ea79b8b541faf12/js/movie/lib/qrcode.min.js'
                ).done(initShareButton);
            }

        })('https://img3.doubanio.com/f/movie/32be6727ed3ad8f6c4a417d8a086355c3e7d1d27/js/movie/lib/sharebutton.js');
    </script>


  </li>
            

    </ul>

    <script type="text/javascript">
        $(function(){
            $(".ul_subject_menu li.rec .bn-sharing").bind("click", function(){
                $.get("/blank?sbj_page_click=bn_sharing");
            });
            $(".ul_subject_menu .create_from_menu").bind("click", function(e){
                e.preventDefault();
                var $el = $(this);
                var glRoot = document.getElementById('gallery-topics-selection');
                if (window.has_gallery_topics && glRoot) {
                    // 判断是否有话题
                    glRoot.style.display = 'block';
                } else {
                    location.href = $el.attr('href');
                }
            });
        });
    </script>
</div>




                





<div class="rec-sec">
<span class="rec">
    <script id="movie-share" type="text/x-html-snippet">
        
    <form class="movie-share" action="/j/share" method="POST">
        <div class="clearfix form-bd">
            <div class="input-area">
                <textarea name="text" class="share-text" cols="72" data-mention-api="https://api.douban.com/shuo/in/complete?alt=xd&amp;callback=?"></textarea>
                <input type="hidden" name="target-id" value="30165034">
                <input type="hidden" name="target-type" value="0">
                <input type="hidden" name="title" value="昨日奇迹 Yesterday‎ (2019)">
                <input type="hidden" name="desc" value="导演 丹尼·博伊尔 主演 希米什·帕特尔 / 莉莉·詹姆斯 / 英国 / 6.6分(5470评价)">
                <input type="hidden" name="redir" value=""/>
                <div class="mentioned-highlighter"></div>
            </div>

            <div class="info-area">
                    <img class="media" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2561245949.jpg" />
                <strong>昨日奇迹 Yesterday‎ (2019)</strong>
                <p>导演 丹尼·博伊尔 主演 希米什·帕特尔 / 莉莉·詹姆斯 / 英国 / 6.6分(5470评价)</p>
                <p class="error server-error">&nbsp;</p>
            </div>
        </div>
        <div class="form-ft">
            <div class="form-ft-inner">
                



                <span class="avail-num-indicator">140</span>
                <span class="bn-flat">
                    <input type="submit" value="推荐" />
                </span>
            </div>
        </div>
    </form>
    
    <div id="suggest-mention-tmpl" style="display:none;">
        <ul>
            {{#users}}
            <li id="{{uid}}">
              <img src="{{avatar}}">{{{username}}}&nbsp;<span>({{{uid}}})</span>
            </li>
            {{/users}}
        </ul>
    </div>


    </script>

        
        <a href="/accounts/register?reason=recommend" class="j a_show_login lnk-sharing" share-id="30165034" data-mode="plain" data-name="昨日奇迹 Yesterday‎ (2019)" data-type="movie" data-desc="导演 丹尼·博伊尔 主演 希米什·帕特尔 / 莉莉·詹姆斯 / 英国 / 6.6分(5470评价)" data-href="https://movie.douban.com/subject/30165034/" data-image="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2561245949.jpg" data-properties="{}" data-redir="" data-text="" data-apikey="" data-curl="" data-count="10" data-object_kind="1002" data-object_id="30165034" data-target_type="rec" data-target_action="0" data-action_props="{&quot;subject_url&quot;:&quot;https:\/\/movie.douban.com\/subject\/30165034\/&quot;,&quot;subject_title&quot;:&quot;昨日奇迹 Yesterday‎ (2019)&quot;}">推荐</a>
</span>


</div>






            <script type="text/javascript">
                $(function() {
                    $('.collect_btn', '#interest_sect_level').each(function() {
                        Douban.init_collect_btn(this);
                    });
                    $('html').delegate(".indent .rec-sec .lnk-sharing", "click", function() {
                        moreurl(this, {
                            from : 'mv_sbj_db_share'
                        });
                    });
                });
            </script>
        </div>
            


    <div id="collect_form_30165034"></div>


        



<div class="related-info" style="margin-bottom:-10px;">
    <a name="intro"></a>
    
        
            
            
    <h2>
        <i class="">昨日奇迹的剧情简介</i>
              · · · · · ·
    </h2>

            <div class="indent" id="link-report">
                    
                        <span property="v:summary" class="">
                                　　杰克（希米什·帕特尔 饰）是英国一个海滨小镇上苦苦挣扎的创作型歌手，有着好友艾莉（莉莉·詹姆斯 饰）的一直支持。在一次神秘的全球大停电中发生了一起奇怪的公交车事故，杰克醒来后发现披头士乐队根本从未存在过。他正面临着非常复杂的问题。
                        </span>
                        

            </div>
</div>


    








<div id="celebrities" class="celebrities related-celebrities">

  
    <h2>
        <i class="">昨日奇迹的演职员</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="/subject/30165034/celebrities">全部 27</a>
            )
            </span>
    </h2>


  <ul class="celebrities-list from-subject __oneline">
        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1054404/" title="丹尼·博伊尔 Danny Boyle" class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p571.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1054404/" title="丹尼·博伊尔 Danny Boyle" class="name">丹尼·博伊尔</a></span>

      <span class="role" title="导演">导演</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1391915/" title="希米什·帕特尔 Himesh Patel" class="">
      <div class="avatar" style="background-image: url(https://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1524627472.78.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1391915/" title="希米什·帕特尔 Himesh Patel" class="name">希米什·帕特尔</a></span>

      <span class="role" title="饰 杰克 Jack Malik">饰 杰克 Jack Malik</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1318674/" title="莉莉·詹姆斯 Lily James" class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1426508419.1.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1318674/" title="莉莉·詹姆斯 Lily James" class="name">莉莉·詹姆斯</a></span>

      <span class="role" title="饰 艾莉 Ellie Appleton">饰 艾莉 Ellie Appleton</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1355940/" title="艾德·希兰 Ed Sheeran" class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1470303058.81.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1355940/" title="艾德·希兰 Ed Sheeran" class="name">艾德·希兰</a></span>

      <span class="role" title="饰 艾德·希兰 Ed Sheeran">饰 艾德·希兰 Ed Sheeran</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1319532/" title="凯特·麦克金农 Kate McKinnon" class="">
      <div class="avatar" style="background-image: url(https://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1386531771.86.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1319532/" title="凯特·麦克金农 Kate McKinnon" class="name">凯特·麦克金农</a></span>

      <span class="role" title="饰 黛博拉 Debra Hammer">饰 黛博拉 Debra Hammer</span>

    </div>
  </li>


        
    

    
  
  <li class="celebrity">
    

  <a href="https://movie.douban.com/celebrity/1327567/" title="阿历克斯·阿诺 Alexander Arnold" class="">
      <div class="avatar" style="background-image: url(https://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p57467.jpg)">
    </div>
  </a>

    <div class="info">
      <span class="name"><a href="https://movie.douban.com/celebrity/1327567/" title="阿历克斯·阿诺 Alexander Arnold" class="name">阿历克斯·阿诺</a></span>

      <span class="role" title="饰 盖文 Gavin">饰 盖文 Gavin</span>

    </div>
  </li>


  </ul>
</div>


    


<link rel="stylesheet" href="https://img3.doubanio.com/f/verify/16c7e943aee3b1dc6d65f600fcc0f6d62db7dfb4/entry_creator/dist/author_subject/style.css">
<div id="author_subject" class="author-wrapper"><div data-reactroot="" class="author-subject"></div></div>
<script type="text/javascript">
    var answerObj = {
      ISALL: 'False',
      TYPE: 'movie',
      SUBJECT_ID: '30165034',
      USER_ID: 'None'
    }
</script>
<script type="text/javascript" src="https://img3.doubanio.com/f/movie/61252f2f9b35f08b37f69d17dfe48310dd295347/js/movie/lib/react/15.4/bundle.js"></script>
<script type="text/javascript" src="https://img3.doubanio.com/f/verify/ac140ef86262b845d2be7b859e352d8196f3f6d4/entry_creator/dist/author_subject/index.js"></script>


    









    
    <div id="related-pic" class="related-pic">
        
    
    
    <h2>
        <i class="">昨日奇迹的视频和图片</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/30165034/trailer#trailer">预告片34</a>&nbsp;|&nbsp;<a href="https://movie.douban.com/subject/30165034/trailer#short_video">视频评论1</a>&nbsp;·&nbsp;<a href="/video/create?subject_id=30165034">添加</a>&nbsp;|&nbsp;<a href="https://movie.douban.com/subject/30165034/all_photos">图片208</a>&nbsp;·&nbsp;<a href="https://movie.douban.com/subject/30165034/mupload">添加</a>
            )
            </span>
    </h2>


        <ul class="related-pic-bd  wide_videos">
                <li class="label-trailer">
                    <a class="related-pic-video" href="https://movie.douban.com/trailer/251441/#content" title="预告片" style="background-image:url(https://img3.doubanio.com/img/trailer/medium/2565871791.jpg?)">
                    </a>
                </li>
                
                <li class="label-short-video">
                    <a class="related-pic-video" href="https://movie.douban.com/video/103379/" title="视频评论" style="background-image:url(https://img3.doubanio.com/view/photo/photo/public/p2561264735.jpg?)">
                    </a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2565899520/"><img src="https://img3.doubanio.com/view/photo/sqxs/public/p2565899520.jpg" alt="图片"></a>
                </li>
                <li>
                    <a href="https://movie.douban.com/photos/photo/2564201094/"><img src="https://img3.doubanio.com/view/photo/sqxs/public/p2564201094.jpg" alt="图片"></a>
                </li>
        </ul>
    </div>




    
    



<style type="text/css">
.award li { display: inline; margin-right: 5px }
.awards { margin-bottom: 20px }
.awards h2 { background: none; color: #000; font-size: 14px; padding-bottom: 5px; margin-bottom: 8px; border-bottom: 1px dashed #dddddd }
.awards .year { color: #666666; margin-left: -5px }
.mod { margin-bottom: 25px }
.mod .hd { margin-bottom: 10px }
.mod .hd h2 {margin:24px 0 3px 0}
</style>



    








    <div id="recommendations" class="">
        
        
    <h2>
        <i class="">喜欢这部电影的人也喜欢</i>
              · · · · · ·
    </h2>

        
    
    <div class="recommendations-bd">
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/27594473/?from=subject-page">
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2553591134.jpg" alt="野玫瑰" class="">
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/27594473/?from=subject-page" class="">野玫瑰</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/30200414/?from=subject-page">
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2560410640.jpg" alt="光盲青春" class="">
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/30200414/?from=subject-page" class="">光盲青春</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/30391300/?from=subject-page">
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2541300705.jpg" alt="我们是小僵尸" class="">
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/30391300/?from=subject-page" class="">我们是小僵尸</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/6895950/?from=subject-page">
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2553820571.jpg" alt="火箭人" class="">
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/6895950/?from=subject-page" class="">火箭人</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/27043941/?from=subject-page">
                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2561505888.jpg" alt="疯狂思想" class="">
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/27043941/?from=subject-page" class="">疯狂思想</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/26787585/?from=subject-page">
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2563001946.jpg" alt="猫" class="">
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/26787585/?from=subject-page" class="">猫</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/21354767/?from=subject-page">
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2555983860.jpg" alt="伯纳黛特你去了哪" class="">
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/21354767/?from=subject-page" class="">伯纳黛特你去了哪</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/26752997/?from=subject-page">
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2566486014.jpg" alt="戈梅拉岛" class="">
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/26752997/?from=subject-page" class="">戈梅拉岛</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/1297615/?from=subject-page">
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1882506345.jpg" alt="救命！" class="">
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/1297615/?from=subject-page" class="">救命！</a>
            </dd>
        </dl>
        <dl class="">
            <dt>
                <a href="https://movie.douban.com/subject/5300054/?from=subject-page">
                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2549558913.jpg" alt="波西米亚狂想曲" class="">
                </a>
            </dt>
            <dd>
                <a href="https://movie.douban.com/subject/5300054/?from=subject-page" class="">波西米亚狂想曲</a>
            </dd>
        </dl>
    </div>

    </div>



        


<script type="text/x-handlebar-tmpl" id="comment-tmpl">
    <div class="dummy-fold">
        {{#each comments}}
        <div class="comment-item" data-cid="id">
            <div class="comment">
                <h3>
                    <span class="comment-vote">
                            <span class="votes">{{votes}}</span>
                        <input value="{{id}}" type="hidden"/>
                        <a href="javascript:;" class="j {{#if ../if_logined}}a_vote_comment{{else}}a_show_login{{/if}}">有用</a>
                    </span>
                    <span class="comment-info">
                        <a href="{{user.path}}" class="">{{user.name}}</a>
                        {{#if rating}}
                        <span class="allstar{{rating}}0 rating" title="{{rating_word}}"></span>
                        {{/if}}
                        <span>
                            {{time}}
                        </span>
                        <p> {{content_tmpl content}} </p>
                    </span>
            </div>
        </div>
        {{/each}}
    </div>
</script>












    

    <div id="comments-section">
        <div class="mod-hd">
            
            
        <a class="comment_btn j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow">
            <span>我要写短评</span>
        </a>

            
    <h2>
        <i class="">昨日奇迹的短评</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/30165034/comments?status=P">全部 2354 条</a>
            )
            </span>
    </h2>

            
        </div>
        <div class="mod-bd">
                

    <div class="tab-hd">
        <a id="hot-comments-tab" href="comments" data-id="hot" class="on">热门</a>&nbsp;/&nbsp;
            <a id="new-comments-tab" href="comments?sort=time" data-id="new">最新</a>&nbsp;/&nbsp;
        <a id="following-comments-tab" href="follows_comments" data-id="following" class="j a_show_login">好友</a>
    </div>

    <div class="tab-bd">
        <div id="hot-comments" class="tab">
            
    
        
        <div class="comment-item" data-cid="1777969518">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">212</span>
                <input value="1777969518" type="hidden">
                <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/158276034/" class="">。。。。</a>
                    <span>看过</span>
                    <span class="allstar30 rating" title="还行"></span>
                <span class="comment-time " title="2019-05-06 20:12:18">
                    2019-05-06
                </span>
            </span>
        </h3>
        <p class="">
            
                <span class="short">这不就是套了Beatles皮的夏洛特烦恼吗？!</span>
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1836209661">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">194</span>
                <input value="1836209661" type="hidden">
                <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/3540441/" class="">同志亦凡人中文站</a>
                    <span>看过</span>
                    <span class="allstar30 rating" title="还行"></span>
                <span class="comment-time " title="2019-06-26 18:56:10">
                    2019-06-26
                </span>
            </span>
        </h3>
        <p class="">
            
                <span class="short">不敢想象平静活到78岁的列侬......这个世界可以没有可乐、星巴克和哈利波特，但不能没有披头士和他们的歌。√</span>
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1424721901">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">150</span>
                <input value="1424721901" type="hidden">
                <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/groupiesmm/" class="">门门。</a>
                    <span>看过</span>
                    <span class="allstar40 rating" title="推荐"></span>
                <span class="comment-time " title="2019-04-20 21:19:21">
                    2019-04-20
                </span>
            </span>
        </h3>
        <p class="">
            
                <span class="short">好久没看爱情电影了 以及 列侬如果能活到78岁那真是太美好了。</span>
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1911027103">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">77</span>
                <input value="1911027103" type="hidden">
                <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/75473004/" class="">番茄杀手</a>
                    <span>看过</span>
                    <span class="allstar40 rating" title="推荐"></span>
                <span class="comment-time " title="2019-08-16 15:49:50">
                    2019-08-16
                </span>
            </span>
        </h3>
        <p class="">
            
                <span class="short">披粉过年了（虽说这年过得有点寒酸） 《昨日奇迹》估计是博伊尔拍过最俗气的片子 考虑到编剧是柯蒂斯似乎也合情合理 花了一千万美刀买的beatles版权 但翻唱的编曲实在是太简单了点 男主声音完全撑不起Back in the USSR/Help这些稍微重一点的歌 Let it be感觉翻唱的不错然鹅总被打断 相对用心一点的是停电处音效设计 用了strawberry fields forever那段风琴...</span>
                <span class="hide-item full">披粉过年了（虽说这年过得有点寒酸） 《昨日奇迹》估计是博伊尔拍过最俗气的片子 考虑到编剧是柯蒂斯似乎也合情合理 花了一千万美刀买的beatles版权 但翻唱的编曲实在是太简单了点 男主声音完全撑不起Back in the USSR/Help这些稍微重一点的歌 Let it be感觉翻唱的不错然鹅总被打断 相对用心一点的是停电处音效设计 用了strawberry fields forever那段风琴和sgt.pepper lonely hearts club band音效倒放和A day in the life音墙的一个Mix 当然看到78岁的列侬还是令人泪奔 最后原版Hey Jude出来的时候又一次泪奔惹 保罗的声音全世界最好听 没有披头士的世界真该是糟糕透顶的</span>
                <span class="expand">(<a href="javascript:;">展开</a>)</span>
        </p>
    </div>

        </div>
        
        <div class="comment-item" data-cid="1841781963">
            
    
    <div class="comment">
        <h3>
            <span class="comment-vote">
                <span class="votes">93</span>
                <input value="1841781963" type="hidden">
                <a href="javascript:;" class="j a_show_login" onclick="">有用</a>
            </span>
            <span class="comment-info">
                <a href="https://www.douban.com/people/ILWTFT/" class="">文森特九六</a>
                    <span>看过</span>
                    <span class="allstar30 rating" title="还行"></span>
                <span class="comment-time " title="2019-06-30 23:34:25">
                    2019-06-30
                </span>
            </span>
        </h3>
        <p class="">
            
                <span class="short">披头士在电影中因消失而更加被人铭记，博伊尔却可能因拍摄本片而遭人忘记。</span>
        </p>
    </div>

        </div>



                
                &gt; <a href="comments?sort=new_score&amp;status=P">
                    更多短评
                        2354条
                </a>
        </div>
        <div id="new-comments" class="tab">
            <div id="normal">
            </div>
            <div class="fold-hd hide">
                <a class="qa" href="/help/opinion#t2-q0" target="_blank">为什么被折叠？</a>
                <a class="btn-unfold" href="#">有一些短评被折叠了</a>
                <div class="qa-tip">
                    评论被折叠，是因为发布这条评论的帐号行为异常。评论仍可以被展开阅读，对发布人的账号不造成其他影响。如果认为有问题，可以<a href="https://help.douban.com/help/ask?category=movie">联系</a>豆瓣电影。
                </div>
            </div>
            <div class="fold-bd">
            </div>
            <span id="total-num"></span>
        </div>
        <div id="following-comments" class="tab">
            
    


        <div class="comment-item">
            你关注的人还没写过短评
        </div>

        </div>
    </div>


            
            
        </div>
    </div>



        

<link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/54ebe45c299a020a.css">



<section class="reviews mod movie-content">
    <header>
        <a href="new_review" rel="nofollow" class="create-review comment_btn " data-isverify="False" data-verify-url="https://www.douban.com/accounts/phone/verify?redir=http://movie.douban.com/subject/30165034/new_review">
            <span>我要写影评</span>
        </a>
        <h2>
            昨日奇迹的影评 · · · · · ·
            <span class="pl">( <a href="reviews">全部 37 条</a> )</span>
        </h2>
    </header>

    

<style>
#gallery-topics-selection {
  position: fixed;
  width: 595px;
  padding: 40px 40px 33px 40px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 16px 0 rgba(0, 0, 0, 0.2);
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  z-index: 9999;
}
#gallery-topics-selection h1 {
  font-size: 18px;
  color: #007722;
  margin-bottom: 36px;
  padding: 0;
  line-height: 28px;
  font-weight: normal;
}
#gallery-topics-selection .gl_topics {
  border-bottom: 1px solid #dfdfdf;
  max-height: 298px;
  overflow-y: scroll;
}
#gallery-topics-selection .topic {
  margin-bottom: 24px;
}
#gallery-topics-selection .topic_name {
  font-size: 15px;
  color: #333;
  margin: 0;
  line-height: inherit;
}
#gallery-topics-selection .topic_meta {
  font-size: 13px;
  color: #999;
}
#gallery-topics-selection .topics_skip {
  display: block;
  cursor: pointer;
  font-size: 16px;
  color: #3377AA;
  text-align: center;
  margin-top: 33px;
}
#gallery-topics-selection .topics_skip:hover {
  background: transparent;
}
#gallery-topics-selection .close_selection {
  position: absolute;
  width: 30px;
  height: 20px;
  top: 46px;
  right: 40px;
  background: #fff;
  color: #999;
  text-align: right;
}
#gallery-topics-selection .close_selection:hover{
  background: #fff;
  color: #999;
}
</style>




        <div class="review_filter">
            <a href="javascript:;;" class="cur" data-sort="">热门</a> /
            <a href="javascript:;;" data-sort="time">最新</a> /
            <a href="javascript:;;" data-sort="follow">好友</a>
            
        </div>


        



<div class="review-list  ">
        
    

        
    
    <div data-cid="10417678">
        <div class="main review-item" id="10417678">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/123967271/" class="avator">
            <img src="https://img3.doubanio.com/icon/u123967271-4.jpg" width="24" height="24">
        </a>

        <a href="https://www.douban.com/people/123967271/" class="name">Kenny Saxton</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2019-08-17" class="main-meta">2019-08-17 20:11:04</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10417678/">《昨日奇迹》披头士梗+彩蛋大全（涉嫌严重剧透）</a></h2>

                <div id="review_10417678_short" class="review-short" data-rid="10417678">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        首先要表达一下对这个片子的不满，拍的什么玩意！！！ 男主要情商没情商，要智商没智商，剧情还虎头蛇尾，拿着那么好的歌，全暴殄天物了！！！ 以下正文： 1.大陆版片头被删，就像《波西米亚狂想曲》一样，本片的片头——即环球影业logo的那段旋律——被改编成了披头士风格，很...

                        &nbsp;(<a href="javascript:;" id="toggle-10417678-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10417678_full" class="hidden">
                    <div id="review_10417678_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10417678" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png">
                        <span id="r-useful_count-10417678">
                                125
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10417678" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png">
                        <span id="r-useless_count-10417678">
                                3
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10417678/#comments" class="reply ">46回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10408571">
        <div class="main review-item" id="10408571">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/starren/" class="avator">
            <img src="https://img1.doubanio.com/icon/u1680355-8.jpg" width="24" height="24">
        </a>

        <a href="https://www.douban.com/people/starren/" class="name">谋谋谋</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2019-08-14" class="main-meta">2019-08-14 20:06:37</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10408571/">这应该是我们对待当下糟糕的世界的态度：心存美好、善良、不伪善、乐观、以及勇敢</a></h2>

                <div id="review_10408571_short" class="review-short" data-rid="10408571">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        看了清新小片《昨日奇迹》，还真的蛮喜欢的。 刚开始的时候还以为是拍英国小镇的故事，心里想，导演把英国小镇处理得太美了，但是后面转到莫斯科、转到洛杉矶，发现拍得都很美。导演是想展现披头士歌中的那个充满爱的温暖的世界。尤其在当下，在这个真实的支离破碎的世界，读着...

                        &nbsp;(<a href="javascript:;" id="toggle-10408571-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10408571_full" class="hidden">
                    <div id="review_10408571_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10408571" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png">
                        <span id="r-useful_count-10408571">
                                29
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10408571" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png">
                        <span id="r-useless_count-10408571">
                                3
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10408571/#comments" class="reply ">6回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10311945">
        <div class="main review-item" id="10311945">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/ago223/" class="avator">
            <img src="https://img3.doubanio.com/icon/u60725903-5.jpg" width="24" height="24">
        </a>

        <a href="https://www.douban.com/people/ago223/" class="name">一个响亮的名号</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2019-07-16" class="main-meta">2019-07-16 04:23:38</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10311945/">手拉手唱黄色潜水艇，我感觉就跟过年一样</a></h2>

                <div id="review_10311945_short" class="review-short" data-rid="10311945">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        1. 就是披头士乐队粉丝线下聚会 + 圣地巡礼 + 卡拉OK的一次meetup。 2. 听歌要背歌词啊。很重要。 3. 做音乐真快乐，录着录着音突然随机加了个火车音效自然采样， 也挺美的。 4. John Lennon出现的一瞬间突然就开始真情实感的哭泣。 在电影创造的这个平行世界里他活到了78岁。...

                        &nbsp;(<a href="javascript:;" id="toggle-10311945-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10311945_full" class="hidden">
                    <div id="review_10311945_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10311945" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png">
                        <span id="r-useful_count-10311945">
                                18
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10311945" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png">
                        <span id="r-useless_count-10311945">
                                1
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10311945/#comments" class="reply ">1回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10357139">
        <div class="main review-item" id="10357139">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/76290975/" class="avator">
            <img src="https://img3.doubanio.com/icon/u76290975-2.jpg" width="24" height="24">
        </a>

        <a href="https://www.douban.com/people/76290975/" class="name">再见杀手</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2019-07-31" class="main-meta">2019-07-31 08:35:34</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10357139/">yesterday</a></h2>

                <div id="review_10357139_short" class="review-short" data-rid="10357139">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        在普利茅斯艺术影院，周围都是老爷爷老奶奶诶 拿了红酒杯进来喝酒哈哈哈 1⃣️第一眼看介绍以为是炒披头士热度的商业片，但是比商业片多了一些有趣和诚意。见John那里真的很治愈。拥抱后，“你需要注意心理问题”“再也不需要了”。没有听清这里john给jack说的生活哲理，但...

                        &nbsp;(<a href="javascript:;" id="toggle-10357139-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10357139_full" class="hidden">
                    <div id="review_10357139_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10357139" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png">
                        <span id="r-useful_count-10357139">
                                7
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10357139" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png">
                        <span id="r-useless_count-10357139">
                                1
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10357139/#comments" class="reply ">1回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10431288">
        <div class="main review-item" id="10431288">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/jovie/" class="avator">
            <img src="https://img3.doubanio.com/icon/u1399483-24.jpg" width="24" height="24">
        </a>

        <a href="https://www.douban.com/people/jovie/" class="name">myhardcandy</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2019-08-22" class="main-meta">2019-08-22 19:24:49</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10431288/">浪费了披头士这么多歌的版权费</a></h2>

                <div id="review_10431288_short" class="review-short" data-rid="10431288">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        俗到不能再俗的看了一会儿就能猜出结局的爱情故事，减分； 每个角色都能几乎在《诺丁山》里找到一一对应人物，编剧懒惰到令人发指，减分； 9成喜剧梗都一点儿不好笑，有些甚至尴尬，减分； 全世界只有你记得披头士这个高概念，加分——但据说这个点子早就有作品了，所以还得减...

                        &nbsp;(<a href="javascript:;" id="toggle-10431288-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10431288_full" class="hidden">
                    <div id="review_10431288_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10431288" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png">
                        <span id="r-useful_count-10431288">
                                7
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10431288" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png">
                        <span id="r-useless_count-10431288">
                                1
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10431288/#comments" class="reply ">0回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10415303">
        <div class="main review-item" id="10415303">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/2129082/" class="avator">
            <img src="https://img3.doubanio.com/icon/u2129082-3.jpg" width="24" height="24">
        </a>

        <a href="https://www.douban.com/people/2129082/" class="name">左丘失明</a>

            <span class="allstar40 main-title-rating" title="推荐"></span>

        <span content="2019-08-16" class="main-meta">2019-08-16 23:42:10</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10415303/">小众的约翰列侬</a></h2>

                <div id="review_10415303_short" class="review-short" data-rid="10415303">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        2012年伦敦奥运会前夕，央视的记者向开幕式导演提问：为什么奥运会开幕式要用小众的摇滚乐？ 他问的没有错。 《昨日奇迹》拍片很少。我用淘票票查了一下，整个昆明市只有7家影院上映。除了百老汇影城和嘉美文艺影院，其它每家影院只排了一两场。 在排片如此稀少的情况下，昆明...

                        &nbsp;(<a href="javascript:;" id="toggle-10415303-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10415303_full" class="hidden">
                    <div id="review_10415303_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10415303" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png">
                        <span id="r-useful_count-10415303">
                                27
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10415303" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png">
                        <span id="r-useless_count-10415303">
                                8
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10415303/#comments" class="reply ">11回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10408656">
        <div class="main review-item" id="10408656">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/160987642/" class="avator">
            <img src="https://img3.doubanio.com/icon/u160987642-1.jpg" width="24" height="24">
        </a>

        <a href="https://www.douban.com/people/160987642/" class="name">唐乐</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2019-08-14" class="main-meta">2019-08-14 20:40:37</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10408656/">我们想去Abbey Road</a></h2>

                <div id="review_10408656_short" class="review-short" data-rid="10408656">
                    <div class="short-content">
                            <p class="spoiler-tip">这篇影评可能有剧透</p>

                        在我看来，这是一部献给歌迷的电影，整个电影便是向披头士乐队朝圣之路，除了他们的歌迷外，也许只适合英国人看了，里面充满了一名披头士乐迷所能想到的所有意淫和梦想，也有英国人对美国流行文化的一点点鄙夷。 《昨日奇迹》如果换个通俗易懂的名字，应该叫，《我管你是不是甲...

                        &nbsp;(<a href="javascript:;" id="toggle-10408656-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10408656_full" class="hidden">
                    <div id="review_10408656_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10408656" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png">
                        <span id="r-useful_count-10408656">
                                12
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10408656" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png">
                        <span id="r-useless_count-10408656">
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10408656/#comments" class="reply ">0回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10414712">
        <div class="main review-item" id="10414712">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/57968508/" class="avator">
            <img src="https://img3.doubanio.com/icon/u57968508-2.jpg" width="24" height="24">
        </a>

        <a href="https://www.douban.com/people/57968508/" class="name">人间洗具</a>

            <span class="allstar20 main-title-rating" title="较差"></span>

        <span content="2019-08-16" class="main-meta">2019-08-16 21:33:33</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10414712/">Good music doesn't make good music</a></h2>

                <div id="review_10414712_short" class="review-short" data-rid="10414712">
                    <div class="short-content">

                        本来对这个阵容很期待的，结果评分低还是有原因的。Good music doesn't make good music。一个是没有分清主次，主线到底是靠文抄公成为巨星的苏文，还是爱情线？（虽然电影可能是想说要做真实的自己之类的，但是对事业线表现得不到位，降低了说服力。男主说自己有钱有名了，但...

                        &nbsp;(<a href="javascript:;" id="toggle-10414712-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10414712_full" class="hidden">
                    <div id="review_10414712_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10414712" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png">
                        <span id="r-useful_count-10414712">
                                2
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10414712" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png">
                        <span id="r-useless_count-10414712">
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10414712/#comments" class="reply ">2回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10439450">
        <div class="main review-item" id="10439450">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/157056931/" class="avator">
            <img src="https://img1.doubanio.com/icon/u157056931-9.jpg" width="24" height="24">
        </a>

        <a href="https://www.douban.com/people/157056931/" class="name">Słonecznik</a>

            <span class="allstar50 main-title-rating" title="力荐"></span>

        <span content="2019-08-26" class="main-meta">2019-08-26 00:12:27</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10439450/">一封写给Beatles和英伦摇滚乐迷的情书</a></h2>

                <div id="review_10439450_short" class="review-short" data-rid="10439450">
                    <div class="short-content">

                        虽然是Danny Boyle和Beatles的脑残粉，但我承认在我进电影院之前刷到豆瓣这才6分多是没报什么太大期待的，刚开始看到演技如此浮夸的男主和女主也一度想中途退场，哪知道到后面竟然有大型真香现场，在椅子上哭到完全停不下来 在那个大断片之后，世界上没有了Beatles。我猜想导演...

                        &nbsp;(<a href="javascript:;" id="toggle-10439450-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10439450_full" class="hidden">
                    <div id="review_10439450_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10439450" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png">
                        <span id="r-useful_count-10439450">
                                2
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10439450" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png">
                        <span id="r-useless_count-10439450">
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10439450/#comments" class="reply ">0回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>

        
    
    <div data-cid="10512396">
        <div class="main review-item" id="10512396">

            
    
    <header class="main-hd">
        <a href="https://www.douban.com/people/aurorayuan/" class="avator">
            <img src="https://img3.doubanio.com/icon/u2333788-6.jpg" width="24" height="24">
        </a>

        <a href="https://www.douban.com/people/aurorayuan/" class="name">馆助七小姐</a>

            <span class="allstar30 main-title-rating" title="还行"></span>

        <span content="2019-09-18" class="main-meta">2019-09-18 11:56:29</span>


    </header>


            <div class="main-bd">

                <h2><a href="https://movie.douban.com/review/10512396/">所有的相见恨晚都是久别重逢</a></h2>

                <div id="review_10512396_short" class="review-short" data-rid="10512396">
                    <div class="short-content">

                        对于我自己来说，假如世界没有披头士，大概我不会打开那扇新世界的大门吧。 第一次听披头士的歌是在一部电影里。搬完新校区之后，我一位同学打算去考电影学的研究生，她为了备考，买了很多电影碟片和电影书籍，有时候我们宿舍的人会聚在一起看。有一次大家一起看《美国往事》（...

                        &nbsp;(<a href="javascript:;" id="toggle-10512396-copy" class="unfold" title="展开">展开</a>)
                    </div>
                </div>

                <div id="review_10512396_full" class="hidden">
                    <div id="review_10512396_full_content" class="full-content"></div>
                </div>

                <div class="action">
                    <a href="javascript:;" class="action-btn up" data-rid="10512396" title="有用">
                        <img src="https://img3.doubanio.com/f/zerkalo/536fd337139250b5fb3cf9e79cb65c6193f8b20b/pics/up.png">
                        <span id="r-useful_count-10512396">
                        </span>
                    </a>
                    <a href="javascript:;" class="action-btn down" data-rid="10512396" title="没用">
                        <img src="https://img3.doubanio.com/f/zerkalo/68849027911140623cf338c9845893c4566db851/pics/down.png">
                        <span id="r-useless_count-10512396">
                        </span>
                    </a>
                    <a href="https://movie.douban.com/review/10512396/#comments" class="reply ">0回应</a>

                    <a href="javascript:;;" class="fold hidden">收起</a>
                </div>
            </div>
        </div>
    </div>




    

    

    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/79f3979d74c13441.js"></script>
    <!-- COLLECTED CSS -->
</div>








            <p class="pl">
                &gt;
                <a href="reviews">
                    更多影评
                        37篇
                </a>
            </p>
</section>

<!-- COLLECTED JS -->

    <br>

        <div class="section-discussion">
                
                <div class="mod-hd">
                        <a class="comment_btn j a_show_login" href="https://www.douban.com/register?reason=review" rel="nofollow"><span>添加新讨论</span></a>
                    
    <h2>
        讨论区
         &nbsp; ·&nbsp; ·&nbsp; ·&nbsp; ·&nbsp; ·&nbsp; ·
    </h2>

                </div>
                
  <table class="olt"><tbody><tr><td></td><td></td><td></td><td></td></tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/30165034/discussion/616432423/" title="确定Danny Boyle没看过《夏洛特烦恼》么？？">确定Danny Boyle没看过《夏洛特烦恼》么？？</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/AlohA0407/">荆棘</a></td>
          <td class="pl"><span>6 回应</span></td>
          <td class="pl"><span>2019-09-26</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/30165034/discussion/616397398/" title="lennon活到78?">lennon活到78?</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/186822157/">☔️</a></td>
          <td class="pl"><span>5 回应</span></td>
          <td class="pl"><span>2019-09-26</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/30165034/discussion/616401647/" title="列侬的扮演者是哪个演员啊">列侬的扮演者是哪个演员啊</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/afterbetter29/">蒋烈浓</a></td>
          <td class="pl"><span>5 回应</span></td>
          <td class="pl"><span>2019-09-26</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/30165034/discussion/616433699/" title="披头士是谁啊">披头士是谁啊</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/49027770/">呆呆双鱼女</a></td>
          <td class="pl"><span>9 回应</span></td>
          <td class="pl"><span>2019-09-25</span></td>
        </tr>
        
        <tr>
          <td class="pl"><a href="https://movie.douban.com/subject/30165034/discussion/616397549/" title="好像被删减了～～～">好像被删减了～～～</a></td>
          <td class="pl"><span>来自</span><a href="https://www.douban.com/people/dontgiveurshit/">竽莳</a></td>
          <td class="pl"><span>11 回应</span></td>
          <td class="pl"><span>2019-09-24</span></td>
        </tr>
  </tbody></table>

                <p class="pl" align="right">
                    <a href="/subject/30165034/discussion/" rel="nofollow">
                        &gt; 去这部影片的讨论区（全部32条）
                    </a>
                </p>
        </div>


    <script type="text/javascript">
        $(function(){if($.browser.msie && $.browser.version == 6.0){
            var $info = $('#info'),
                maxWidth = parseInt($info.css('max-width'));
            if($info.width() > maxWidth) {
                $info.width(maxWidth);
            }
        }});
    </script>


            </div>
            <div class="aside" style="left: 851.333px;">
                


    









    <!-- douban ad begin -->
    <div id="dale_movie_subject_top_right" ad-status="appended" data-sell-type="RTB" data-type="GoogleRender" data-version="3.2.13"><div style="position: relative; margin: 0px 0px 20px; display: block; width: 300px; height: 250px; overflow: hidden;"><iframe src="https://ad.doubanio.com" sandbox="allow-forms allow-scripts allow-same-origin allow-popups allow-top-navigation" scrolling="no" style="overflow: hidden; display: block;" name="dale_movie_subject_top_right_frame" id="dale_movie_subject_top_right_frame" __idm_frm__="8589934608" width="300" height="250" frameborder="0"></iframe><div style="line-height: 1; text-align: center; background-color: rgba(0, 0, 0, 0.3); font-size: 12px; position: absolute; right: 0px; bottom: 0px; padding: 4px; color: rgb(255, 255, 255);">由谷歌提供的广告</div></div></div>
    <div id="dale_movie_subject_top_middle" ad-status="loaded"></div>
    <!-- douban ad end -->

    



<style type="text/css">
    .m4 {margin-bottom:8px; padding-bottom:8px;}
    .movieOnline {background:#FFF6ED; padding:10px; margin-bottom:20px;}
    .movieOnline h2 {margin:0 0 5px;}
    .movieOnline .sitename {line-height:2em; width:160px;}
    .movieOnline td,.movieOnline td a:link,.movieOnline td a:visited{color:#666;}
    .movieOnline td a:hover {color:#fff;}
    .link-bt:link,
    .link-bt:visited,
    .link-bt:hover,
    .link-bt:active {margin:5px 0 0; padding:2px 8px; background:#a8c598; color:#fff; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; display:inline-block;}
</style>



    







    
    <div class="tags">
        
        
    <h2>
        <i class="">豆瓣成员常用的标签</i>
              · · · · · ·
    </h2>

        <div class="tags-body">
                <a href="/tag/披头士" class="">披头士</a>
                <a href="/tag/音乐" class="">音乐</a>
                <a href="/tag/英国" class="">英国</a>
                <a href="/tag/喜剧" class="">喜剧</a>
                <a href="/tag/2019" class="">2019</a>
                <a href="/tag/摇滚" class="">摇滚</a>
                <a href="/tag/奇幻" class="">奇幻</a>
                <a href="/tag/平行穿越" class="">平行穿越</a>
        </div>
    </div>


    <div id="dale_movie_review_right_guess_you_like" ad-status="appended" data-sell-type="CPD" data-type="TaboolaRender" data-version="3.2.13"><div style="position: relative; margin: 0px 0px 20px; display: block; overflow: hidden;" id="dale_movie_review_right_guess_you_like_frame"><script>
  window._taboola = window._taboola || [];
  _taboola.push({article:'auto'});
  !function (e, f, u, i) {
    if (!document.getElementById(i)){
      e.async = 1;
      e.src = u;
      e.id = i;
      f.parentNode.insertBefore(e, f);
    }
  }(document.createElement('script'),
  document.getElementsByTagName('script')[0],
  '//cdn.taboola.com.cn/libtrc/douban-cn-web/loader.js',
  'tb_loader_script');
  if(window.performance && typeof window.performance.mark == 'function')
    {window.performance.mark('tbl_ic');}
</script><div id="taboola-right-rail-thumbnails" class=" trc_related_container trc_spotlight_widget trc_elastic trc_elastic_thumbnails-rr " data-placement-name="Right Rail Thumbnails" observeid="tbl-observe-0"><div id="taboola-right-rail-thumbnails-video"><div class="_cm-div" id="_cm-css-reset" data-tracked="true"></div><div class="_cm-single-inline" style="height: 0px; width: 300px;" id="_cm-css-reset"><div class="_cm-ad-title" style="display: none;">ADVERTISEMENT</div> <div class="_cm-inline-video" style=""> <div id="_cm-css-reset" style="text-align: left;"><div class="_cm-video-ad vpaid-player-container" id="_cm-css-reset" style="width: 300px; height: 168px;" width="300" height="168"><div class="_cm-video-ad vpaid-player-container vpaid-handler" id="0__cm-css-reset" style="width: 300px; height: 168px; position: absolute; top: 0px; left: 0px; border: 0px none; z-index: 0;"></div></div><div id="_cm-close-area" class="_cm-close-area _cm-close-ie-fix"><!--?xml version="1.0" encoding="utf-8"?--> <svg version="1.1" id="_x2014_ÎÓÈ_x5F_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 99 99" xml:space="preserve"> <style type="text/css">.st0{fill:#fff}</style> <g> <g stroke="null" id="svg_1"> <g stroke="null" id="svg_2"> <path stroke="null" id="svg_3" d="m82.77256,91.4817c-1.64243,0 -3.25444,-0.644 -4.50148,-1.9964l-65.57555,-69.42328c-2.49406,-2.6404 -2.49406,-6.92301 0,-9.56341c2.49406,-2.6404 6.53931,-2.6404 9.03337,0l65.57555,69.45548c2.49406,2.6404 2.49406,6.92301 0,9.56341c-1.24703,1.3202 -2.88946,1.9642 -4.53189,1.9642z" class="st0"></path> </g> <g stroke="null" id="svg_4"> <path stroke="null" id="svg_5" d="m17.19702,91.4817c-1.64243,0 -3.25444,-0.644 -4.50148,-1.9964c-2.49406,-2.6404 -2.49406,-6.92301 0,-9.56341l65.57555,-69.42328c2.49406,-2.6404 6.53931,-2.6404 9.03337,0c2.49406,2.6404 2.49406,6.92301 0,9.56341l-65.57555,69.45548c-1.24703,1.3202 -2.88946,1.9642 -4.53189,1.9642z" class="st0"></path> </g> </g> </g> </svg></div><div class="_cm-ad-choice"><a class="_cm-ad-choice-text" target="_blank" style="" href="https://popup.taboola.com/en">Ad</a> <a class="_cm-ad-choice-logo" target="_blank" style="background: rgba(0, 0, 0, 0) url(&quot;//cdn.taboola.com/static/c5/c5ef96bc-30ab-456a-b3d5-a84f367c6a46.svg&quot;) no-repeat scroll 0% 0%;" href="https://popup.taboola.com/en"></a></div><div id="_cm-css-reset" class="_cm-volume-area _cm-volume-area-bottom"><div class="_cm-volume-border"> <svg class="_cm-volume-mute" data-name="—ÎÓÈ_1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 351.22 266.75"> <defs> <style>.cls-1{fill:#fff}</style> </defs> <g id="_Group_" data-name="<Group>"> <g id="_Group_2" data-name="<Group>"> <path class="cls-1" d="M338,185.84c-.48-3.15-1.39-6.11-5.31-7.4H330c-3.63.93-6.33,3-8.93,5.29L249.59,246H170.26c-7.93,0-14.35,5.59-14.35,12.5V370.1c0,6.9,6.42,12.5,14.35,12.5h85.1l66.91,58.27a19,19,0,0,0,6,3.71c3.92,1.44,7.13.29,8.73-3.12a14.33,14.33,0,0,0,1.22-6.29V189.22A22.39,22.39,0,0,0,338,185.84Z" transform="translate(-155.91 -178.44)"></path> </g> </g> <path class="cls-1" d="M486.13,381.62a20.93,20.93,0,0,1-14.85-6.15l-97.62-97.62a21,21,0,1,1,29.69-29.7L501,345.77a21,21,0,0,1-14.85,35.85Z" transform="translate(-155.91 -178.44)"></path> <path class="cls-1" d="M388.5,381.62a21,21,0,0,1-14.84-35.85l97.62-97.62a21,21,0,1,1,29.7,29.7l-97.63,97.62A20.93,20.93,0,0,1,388.5,381.62Z" transform="translate(-155.91 -178.44)"></path> </svg> <svg class="_cm-volume-unmute" data-name="—ÎÓÈ_1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 311.81 266.75"> <defs> <style>.cls-1{fill:#fff}</style> </defs> <g id="_Group_" data-name="<Group>"> <path id="_Path_" data-name="<Path>" class="cls-1" d="M465.85,290.12A124.1,124.1,0,0,0,453.19,253a127.55,127.55,0,0,0-21.66-29.51c-3.38-3.47-7.4-5.23-12.25-4.6a13.27,13.27,0,0,0-11.5,9.27c-1.87,5.38-.66,10.26,3.23,14.43,1,1.05,2,2,2.95,3.1a96.67,96.67,0,0,1,25.09,55.19,95.28,95.28,0,0,1-1.17,29.52,96.57,96.57,0,0,1-26.52,50.23,13.74,13.74,0,0,0-4.23,12.12,13.25,13.25,0,0,0,9.2,11.27c5.3,1.85,10.15.74,14.31-3.08.82-.74,1.57-1.56,2.33-2.36a125,125,0,0,0,34.74-87.88A131.18,131.18,0,0,0,465.85,290.12Z" transform="translate(-155.91 -178.44)"></path> <path id="_Path_2" data-name="<Path>" class="cls-1" d="M420.23,307.35a87,87,0,0,0-6.32-28.82A88,88,0,0,0,395,249.69a14,14,0,0,0-24.29,11.22,16.39,16.39,0,0,0,4.73,8.92c13.86,14.79,19.22,32.3,16.05,52.27a58.5,58.5,0,0,1-16.83,32.54A14,14,0,0,0,388.48,378c3.13-.88,5.44-2.88,7.6-5.18,16.05-17.16,23.94-37.57,24.15-61C420.23,310.31,420.29,308.83,420.23,307.35Z" transform="translate(-155.91 -178.44)"></path> <path id="_Path_3" data-name="<Path>" class="cls-1" d="M338,185.84c-.48-3.15-1.39-6.11-5.31-7.4H330c-3.63.93-6.33,3-8.93,5.29L249.59,246H170.26c-7.93,0-14.35,5.59-14.35,12.5V370.1c0,6.9,6.42,12.5,14.35,12.5h85.1l66.91,58.27a19,19,0,0,0,6,3.71c3.92,1.44,7.13.29,8.73-3.12a14.33,14.33,0,0,0,1.22-6.29V189.22A22.39,22.39,0,0,0,338,185.84Z" transform="translate(-155.91 -178.44)"></path> </g> </svg> <div class="_cm-volume-text">Unmute</div> </div> </div></div></div><div id="_cm-css-reset" class="_cm-loading" style="display: none;"><div class="_cm-loading-div"> <img src="//vidstat.taboola.com/assets/loading2.png" class="_cm_loader_img"><div id="_cm-css-reset" class="_cm-repeat-div" style="background-image: url(&quot;//vidstat.taboola.com/assets/blurry-image.png&quot;) !important; display: none;"> <div class="_cm-repeat-view-wrapper"> <div class="_cm-repeat-buttons-wrapper"> <img class="_cm-repeat-button" src="//vidstat.taboola.com/assets/replay-button.svg"> <img class="_cm-repeat-button-hover" src="//vidstat.taboola.com/assets/replay-button-hover.svg"> </div> <div class="_cm-learn-more-buttons-wrapper" style="display: none;"> <img class="_cm-learn-more-button" src="//vidstat.taboola.com/assets/learn-more-button.svg"> <img class="_cm-learn-more-button-hover" src="//vidstat.taboola.com/assets/learn-more-button-hover.svg"> </div> </div> </div></div></div></div></div><div class="trc_rbox_container"><div><div id="trc_wrapper_96697" class="trc_rbox thumbnails-rr trc-content-sponsored " style="overflow: hidden; display: block;"><div id="trc_header_96697" class="trc_rbox_header trc_rbox_border_elm"><div class="trc_header_ext"></div><span class="trc_rbox_header_span">你可能会喜欢· · · · · ·</span></div><div id="outer_96697" class="trc_rbox_outer"><div id="rbox-t2m" class="trc_rbox_div trc_rbox_border_elm"><div id="internal_trc_96697"><div data-item-id="~~V1~~6818759145910177433~~joJuwtTznRW0nEFSyOynF-hPzdZZimEjhSmvpXOnt9TTxvAnL2wqac4MyzR7uD46gj3kUkbS3FhelBtnsiJV6MhkDZRZzzIqDobN6rWmCPBsA_db74Bm8TtTpOXcnHNoZfQKfxi4agJPY1p70aDfniuw7z8kUHpbxvYxOKt7BLYYuZEX4s4n-IxCt1-8kVvKTS8Maux2jWC1gRU3nx5A7kchcA-V62U9N99J9-T6Zbk" data-item-title="这款在线发布的全新“自拍无人机”让大型无人机公司感到担忧" data-item-thumb="http://cdn.taboola.com/libtrc/static/thumbnails/2b85d1c24a2e190a227ceea8ad9226b9.jpg" data-item-syndicated="true" class="videoCube trc_spotlight_item origin-default thumbnail_start syndicatedItem photoItem videoCube_1_child trc-first-recommendation trc-spotlight-first-recommendation  trc_excludable " observeid="tbl-observe-1"><a title="这款在线发布的全新“自拍无人机”让大型无人机公司感到担忧" href="https://dailygadgetreviews.com/cn?utm_source=taboola&amp;utm_medium=referral" rel="nofollow noopener" target="_blank" class=" item-thumbnail-href "><div class="thumbBlock_holder"><span class="thumbBlock" style="background-image: url(&quot;https://images.taboola.com/taboola/image/fetch/f_jpg%2Cq_auto%2Ch_240%2Cw_200%2Cc_fill%2Cg_faces:auto%2Ce_sharpen/http%3A//cdn.taboola.com/libtrc/static/thumbnails/2b85d1c24a2e190a227ceea8ad9226b9.jpg&quot;);"><span class="thumbnail-overlay"></span><span class="branding">DroneXPro</span><span class="static-text top-right"></span></span><div class="videoCube_aspect"></div></div></a><a title="这款在线发布的全新“自拍无人机”让大型无人机公司感到担忧" href="https://dailygadgetreviews.com/cn?utm_source=taboola&amp;utm_medium=referral" rel="nofollow noopener" target="_blank" class=" item-label-href "><span class="video-label-box trc-main-label "><span class="video-label video-title trc_ellipsis " style="-webkit-line-clamp: 2;">这款在线发布的全新“自拍无人机”让大型无人机公司感到担忧</span><span class="branding">DroneXPro | 赞助商</span></span></a><div class=" trc_user_exclude_btn " title="移除此项目"></div><div class=" trc_exclude_overlay trc_fade "></div><div class=" trc_undo_btn ">撤消</div></div><div data-item-id="~~V1~~-2631727839993587157~~sInZMtE-6gTqj0CeaCauRj-7fuZ7SaL1Y5LHLAxcsuDTxvAnL2wqac4MyzR7uD46gj3kUkbS3FhelBtnsiJV6MhkDZRZzzIqDobN6rWmCPAILBuh_RBr0fpf-7936xvE4n4y5xGq0g94Mc8yHOFJVS6n47n796cbgjChUfH7Hm7nfHmjKoHCa2fvMo6npySzP2MYuvc5Q33ihwHgEhojLw" data-item-title="&amp;lt;![CDATA[中国日报网]]&amp;gt;" data-item-thumb="http://www.xinhuanet.com/local/2018-07/23/1123161325_15323025126221n.jpg" data-item-syndicated="true" class="videoCube trc_spotlight_item origin-default thumbnail_start syndicatedItem textItem videoCube_2_child trc_excludable " observeid="tbl-observe-2"><a title="<![CDATA[中国日报网]]>" href="http://ms.chinadaily.com.cn/MSN/53002531/53002531.xml?utm_source=taboola&amp;utm_medium=referral" rel="nofollow noopener" target="_blank" class=" item-thumbnail-href "><div class="thumbBlock_holder"><span class="thumbBlock" style="background-image: url(&quot;https://images.taboola.com/taboola/image/fetch/f_jpg%2Cq_auto%2Ch_240%2Cw_200%2Cc_fill%2Cg_faces:auto%2Ce_sharpen/http%3A//www.xinhuanet.com/local/2018-07/23/1123161325_15323025126221n.jpg&quot;);"><span class="thumbnail-overlay"></span><span class="branding">中国日报</span><span class="static-text top-right"></span></span><div class="videoCube_aspect"></div></div></a><a title="<![CDATA[中国日报网]]>" href="http://ms.chinadaily.com.cn/MSN/53002531/53002531.xml?utm_source=taboola&amp;utm_medium=referral" rel="nofollow noopener" target="_blank" class=" item-label-href "><span class="video-label-box trc-main-label "><span class="video-label video-title trc_ellipsis " style="-webkit-line-clamp: 1;">&lt;![CDATA[中国日报网]]&gt;</span><span class="branding">中国日报 | 赞助商</span></span></a><div class=" trc_user_exclude_btn " title="移除此项目"></div><div class=" trc_exclude_overlay trc_fade "></div><div class=" trc_undo_btn ">撤消</div></div></div></div></div><div class="trc-widget-footer"><div class="logoDiv link-attribution "><a class="trc_desktop_attribution_link trc_attribution_position_bottom" rel="nofollow noopener" href="https://popup.taboola.com/zh-CN/?template=colorbox&amp;utm_source=douban-cn-web&amp;utm_medium=referral&amp;utm_content=thumbnails-rr:Right Rail Thumbnails:" target="_blank"><span>by Taboola</span></a><a class="trc_mobile_attribution_link trc_attribution_position_bottom" rel="nofollow noopener" href="https://popup.taboola.com/zh-CN/?template=colorbox&amp;utm_source=douban-cn-web&amp;utm_medium=referral&amp;utm_content=thumbnails-rr:Right Rail Thumbnails:" target="_blank"><span>by Taboola</span></a></div><div class="logoDiv link-disclosure  attribution-disclosure-link-sponsored"><a class="trc_desktop_disclosure_link trc_attribution_position_bottom" rel="nofollow noopener" href="https://popup.taboola.com/zh-CN/?template=colorbox&amp;utm_source=douban-cn-web&amp;utm_medium=referral&amp;utm_content=thumbnails-rr:Right Rail Thumbnails:" target="_blank"><span>Promoted Links</span></a><a class="trc_mobile_disclosure_link trc_attribution_position_bottom" rel="nofollow noopener" href="https://popup.taboola.com/zh-CN/?template=colorbox&amp;utm_source=douban-cn-web&amp;utm_medium=referral&amp;utm_content=thumbnails-rr:Right Rail Thumbnails:" target="_blank"><span>Promoted Links</span></a></div><div class="logoDiv link-disclosure  attribution-disclosure-link-hybrid"><a class="trc_desktop_disclosure_link trc_attribution_position_bottom" rel="nofollow noopener" href="https://popup.taboola.com/zh-CN/?template=colorbox&amp;utm_source=douban-cn-web&amp;utm_medium=referral&amp;utm_content=thumbnails-rr:Right Rail Thumbnails:" target="_blank"><span>Promoted Links</span></a><a class="trc_mobile_disclosure_link trc_attribution_position_bottom" rel="nofollow noopener" href="https://popup.taboola.com/zh-CN/?template=colorbox&amp;utm_source=douban-cn-web&amp;utm_medium=referral&amp;utm_content=thumbnails-rr:Right Rail Thumbnails:" target="_blank"><span>Promoted Links</span></a></div></div><div class="trc_clearer"></div></div></div></div><script id="taboola-right-rail-thumbnails-v-loader" src="//15.taboola.com/tb?oid=15&amp;pubnm=douban-cn-web&amp;unitType=199&amp;tbloc=1&amp;pageType=text&amp;pstn=Right%20Rail%20Thumbnails%20-%20Video&amp;uuip=&amp;cisrf=http%3A%2F%2Fwww.pianyuan.la%2Fr_ZZdmF9Ec0.html&amp;cirf=https%3A%2F%2Fmovie.douban.com%2Fsubject%2F30165034%2F&amp;encoded=1&amp;uid=a75154db-6f30-4f57-a57e-fc206c335904-tuct48472cd&amp;variant=0|1260359810&amp;callback=TRC.videoTagCallbacks.videoCallback1&amp;cb=1569502749510&amp;tagid=&amp;cntry=CN&amp;platform=1&amp;sesid=fae2c4758321687d35905bf16eebb37d&amp;itemid=/subject/30165034&amp;viewid=1569502748146&amp;geolat=&amp;geoing=&amp;deviceifa=&amp;appid=&amp;sd=v2_fae2c4758321687d35905bf16eebb37d_a75154db-6f30-4f57-a57e-fc206c335904-tuct48472cd_1569502747_1569502747_CKii_xQQ0oFJGPK7ne3WLSABKAQwMDjK_QdAgaEQSKHFH1CcwwlYAGAA&amp;ri=7941467b230e84171fef59918bbc00b2&amp;appname=&amp;cdb=&amp;gdprApplies=&amp;rid=&amp;sii=4483842389808629009"></script></div><script>
  window._taboola = window._taboola || [];
  _taboola.push({
    mode: 'thumbnails-rr',
    container: 'taboola-right-rail-thumbnails',
    placement: 'Right Rail Thumbnails',
    target_type: 'mix'
  });
</script><script>
  window._taboola = window._taboola || [];
  _taboola.push({flush: true});
</script><img src="https://erebor.douban.com/count/?ad=204079&amp;bid=FmJMxw_grHs&amp;chicken=883f70abf371ef7541d1938477d77f2b&amp;crtr=7%3A%E5%AE%89%E5%A8%9C%C2%B7%E5%BE%B7%C2%B7%E9%98%BF%E7%8E%9B%E6%96%AF%7C7%3A%E5%8D%A1%E7%B1%B3%E6%8B%89%C2%B7%E6%8B%89%E7%91%9F%E7%A6%8F%E5%BE%B7%7C7%3A%E8%A9%B9%E5%A6%AE%E5%BC%97%C2%B7%E9%98%BF%E5%B0%94%E8%8E%AB%7C7%3A%E8%8E%89%E8%8E%89%C2%B7%E8%A9%B9%E5%A7%86%E6%96%AF%7C7%3A%E5%B8%8C%E7%B1%B3%E4%BB%80%C2%B7%E5%B8%95%E7%89%B9%E5%B0%94%7C7%3A%E7%8E%9B%E4%B8%BD%E5%AE%89%E5%A8%9C%C2%B7%E6%96%AF%E7%9A%AE%E7%93%A6%E5%85%8B%7C7%3A%E4%B9%94%E5%B0%94%C2%B7%E5%BC%97%E8%8E%B1%7C7%3A%E5%87%AF%E7%89%B9%C2%B7%E9%BA%A6%E5%85%8B%E9%87%91%E5%86%9C%7C7%3A%E5%8D%A1%E7%B1%B3%E5%88%A9%C2%B7%E9%99%88%7C7%3A%E5%89%A7%E6%83%85%7C7%3A%E9%9F%B3%E4%B9%90%7C7%3A%E6%91%87%E6%BB%9A%7C7%3A%E5%A4%9A%E7%B1%B3%E5%B0%BC%E5%85%8B%C2%B7%E7%A7%91%E5%B0%94%E6%9B%BC%7C7%3A2019%7C7%3A%E8%89%BE%E5%88%A9%E6%96%AF%C2%B7%E6%9F%A5%E6%99%AE%E5%B0%94%7C7%3A%E9%A9%AC%E8%AF%BA%E4%BC%8A%C2%B7%E9%98%BF%E5%8D%97%E5%BE%B7%7C7%3A%E8%8E%8E%E6%8B%89%C2%B7%E5%85%B0%E5%8D%A1%E5%A4%8F%E5%B0%94%7C7%3A%E9%98%BF%E5%8E%86%E5%85%8B%E6%96%AF%C2%B7%E9%98%BF%E8%AF%BA%7C7%3A%E7%B4%A2%E8%8F%B2%E5%A8%85%C2%B7%E8%BF%AA%C2%B7%E9%A9%AC%E8%92%82%E8%AF%BA%7C7%3A%E8%89%BE%E5%BE%B7%C2%B7%E5%B8%8C%E5%85%B0%7C7%3A%E7%BE%8E%E5%9B%BD%7C7%3A%E9%98%BF%E5%9B%BE%E5%B0%94%C2%B7%E5%A4%8F%E5%B0%94%E9%A9%AC%7C7%3A%E6%8A%AB%E5%A4%B4%E5%A3%AB%7C7%3A%E8%8B%B1%E5%9B%BD%7C7%3A%E5%A5%87%E5%B9%BB%7C7%3A%E6%8B%89%E8%92%99%E5%B0%BC%C2%B7%E8%8E%AB%E9%87%8C%E6%96%AF%7C7%3A%E5%B9%B3%E8%A1%8C%E7%A9%BF%E8%B6%8A%7C7%3A%E4%B8%B9%E5%B0%BC%C2%B7%E5%8D%9A%E4%BC%8A%E5%B0%94%7C7%3A%E8%A9%B9%E5%A7%86%E6%96%AF%C2%B7%E6%9F%AF%E7%99%BB%7C7%3A%E5%93%88%E5%BB%B7%C2%B7%E5%B8%95%E7%89%B9%E5%B0%94%7C7%3A%E5%96%9C%E5%89%A7%7C3%3A%2Fsubject%2F30165034%2F&amp;device=101&amp;experiment_id=0&amp;fv=&amp;hn=anson81&amp;lat=0.00000&amp;lon=0.00000&amp;mark=&amp;model=&amp;net=&amp;ns=1569502744009988880&amp;os=52&amp;osv=NT+10.0&amp;p=0&amp;pid=debug_60ea6cc5da417670ea884e6cf500883469b179f7&amp;rexxar=0&amp;type=impression&amp;uid=&amp;unit=dale_movie_review_right_guess_you_like&amp;user_variation=&amp;vendor=" style="position:absolute;" width="0" height="0" border="0"></div></div>
    <div id="dale_movie_subject_inner_middle" ad-status="appended" data-sell-type="COMPLEMENT" data-type="DoubanRender" data-version="3.2.13"><iframe src="https://ad.doubanio.com" sandbox="allow-forms allow-scripts allow-same-origin allow-popups allow-top-navigation" style="position: relative; margin: 0px 0px 20px; display: block; width: 300px; height: 100px; overflow: hidden;" scrolling="no" name="dale_movie_subject_inner_middle_frame" id="dale_movie_subject_inner_middle_frame" __idm_frm__="8589934610" width="300" height="100" frameborder="0"></iframe></div>
    <div id="dale_movie_subject_download_middle" ad-status="loaded"></div>
        








<div id="subject-doulist">
    
    
    <h2>
        <i class="">以下豆列推荐</i>
              · · · · · ·
            <span class="pl">
            (
                <a href="https://movie.douban.com/subject/30165034/doulists">全部</a>
            )
            </span>
    </h2>


    
    <ul>
            <li>
                <a href="https://www.douban.com/doulist/1504454/" target="_blank">ღ♩♪生活有这些期待很有动力♫♬ღ</a>
                <span>(freedom♪)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/1593367/" target="_blank">2019—2021值得期待的影片（欧洲日韩）</a>
                <span>(closer)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/799113/" target="_blank">音乐和音乐人电影</a>
                <span>(懒精零)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/1964161/" target="_blank">这些电影，可以期待</a>
                <span>(大波罗霸)</span>
            </li>
            <li>
                <a href="https://www.douban.com/doulist/110953664/" target="_blank">Berlinale2019</a>
                <span>(陀螺凡达可)</span>
            </li>
    </ul>

</div>

            








<div id="subject-others-interests">
    
    
    <h2>
        <i class="">谁在看这部电影</i>
              · · · · · ·
    </h2>

    
    <ul class="">
            
            <li class="">
                <a href="https://www.douban.com/people/196986577/" class="others-interest-avatar">
                    <img src="https://img3.doubanio.com/icon/u196986577-1.jpg" class="pil" alt="               ">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/196986577/" class="">               </a>
                    <div class="">
                        17分钟前
                        看过
                        <span class="allstar50" title="力荐"></span>
                    </div>
                </div>
            </li>
            
            <li class="">
                <a href="https://www.douban.com/people/122939291/" class="others-interest-avatar">
                    <img src="https://img3.doubanio.com/icon/u122939291-1.jpg" class="pil" alt="润帅">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/122939291/" class="">润帅</a>
                    <div class="">
                        28分钟前
                        看过
                        <span class="allstar40" title="推荐"></span>
                    </div>
                </div>
            </li>
            
            <li class="">
                <a href="https://www.douban.com/people/157996246/" class="others-interest-avatar">
                    <img src="https://img3.doubanio.com/icon/u157996246-1.jpg" class="pil" alt="平+">
                </a>
                <div class="others-interest-info">
                    <a href="https://www.douban.com/people/157996246/" class="">平+</a>
                    <div class="">
                        30分钟前
                        看过
                        <span class="allstar20" title="较差"></span>
                    </div>
                </div>
            </li>
    </ul>

    
    <div class="subject-others-interests-ft">
        
            <a href="https://movie.douban.com/subject/30165034/collections">6135人看过</a>
                &nbsp;/&nbsp;
            <a href="https://movie.douban.com/subject/30165034/wishes">8514人想看</a>
    </div>

</div>



    
    

<!-- douban ad begin -->
<div id="dale_movie_subject_middle_right" ad-status="appended" data-sell-type="RTB" data-type="GoogleRender" data-version="3.2.13"><div style="position: relative; margin: 0px 0px 20px; display: block; width: 300px; height: 250px; overflow: hidden;"><iframe src="https://ad.doubanio.com" sandbox="allow-forms allow-scripts allow-same-origin allow-popups allow-top-navigation" scrolling="no" style="overflow: hidden; display: block;" name="dale_movie_subject_middle_right_frame" id="dale_movie_subject_middle_right_frame" __idm_frm__="8589934606" width="300" height="250" frameborder="0"></iframe><div style="line-height: 1; text-align: center; background-color: rgba(0, 0, 0, 0.3); font-size: 12px; position: absolute; right: 0px; bottom: 0px; padding: 4px; color: rgb(255, 255, 255);">由谷歌提供的广告</div></div></div>
<script type="text/javascript">
    (function (global) {
        if(!document.getElementsByClassName) {
            document.getElementsByClassName = function(className) {
                return this.querySelectorAll("." + className);
            };
            Element.prototype.getElementsByClassName = document.getElementsByClassName;

        }
        var articles = global.document.getElementsByClassName('article'),
            asides = global.document.getElementsByClassName('aside');

        if (articles.length > 0 && asides.length > 0 && articles[0].offsetHeight >= asides[0].offsetHeight) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_movie_subject_middle_right');
        }
    })(this);
</script>
<!-- douban ad end -->



    <br>

    
<p class="pl">订阅昨日奇迹的评论: <br><span class="feed">
    <a href="https://movie.douban.com/feed/subject/30165034/reviews"> feed: rss 2.0</a></span></p>


            </div>
            <div class="extra">
                
    
<!-- douban ad begin -->
<div id="dale_movie_subject_bottom_super_banner" ad-status="loaded" data-sell-type="RTB" data-type="YoudaoRender" data-version="3.2.13"></div>
<script type="text/javascript">
    (function (global) {
        var body = global.document.body,
            html = global.document.documentElement;

        var height = Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);
        if (height >= 2000) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_movie_subject_bottom_super_banner');
        }
    })(this);
</script>
<!-- douban ad end -->


            </div>
        </div>
    </div>

        
    <div id="footer">
            <div class="footer-extra"></div>
        
<span id="icp" class="fleft gray-link">
    © 2005－2019 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about/legal">法律声明</a>
    
    · <a href="https://help.douban.com/?app=movie" target="_blank">帮助中心</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

    </div>

    </div>
    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/6fd2f353e26cc080.js"></script>
        
        
    <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css">
    <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/movie/4aca95d66d37ec0712b3d19973b5d8feb75f2f05/css/movie/mod/reg_login_pop.css">
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js"></script>
    <script type="text/javascript">
        var HTTPS_DB='https://www.douban.com';
var account_pop={open:function(o,e){e?referrer="?referrer="+encodeURIComponent(e):referrer="?referrer="+window.location.href;var n="",i="",t=448;n="用户登录",i="https://accounts.douban.com/passport/login_popup?source=movie";var r=document.location.protocol+"//"+document.location.hostname,a=dui.Dialog({width:340,title:n,height:t,cls:"account_pop",isHideTitle:!0,modal:!0,content:"<iframe scrolling='no' frameborder='0' width='340' height='"+t+"' src='"+i+"' name='"+r+"'></iframe>"},!0),c=a.node;if(c.undelegate(),c.delegate(".dui-dialog-close","click",function(){var o=$("body");o.find("#login_msk").hide(),o.find(".account_pop").remove()}),$(window).width()<478){var d="";"reg"===o?d=HTTPS_DB+"/accounts/register"+referrer:"login"===o&&(d=HTTPS_DB+"/accounts/login"+referrer),window.location.href=d}else a.open();$(window).bind("message",function(o){"https://accounts.douban.com"===o.originalEvent.origin&&(c.find("iframe").css("height",o.originalEvent.data),c.height(o.originalEvent.data),a.update())})}};Douban&&Douban.init_show_login&&(Douban.init_show_login=function(o){var e=$(o);e.click(function(){var o=e.data("ref")||"";return account_pop.open("login",o),!1})}),Do(function(){$("body").delegate(".pop_register","click",function(o){o.preventDefault();var e=$(this).data("ref")||"";return account_pop.open("reg",e),!1}),$("body").delegate(".pop_login","click",function(o){o.preventDefault();var e=$(this).data("ref")||"";return account_pop.open("login",e),!1})});
    </script>

    




    
<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '',
            browserId = 'FmJMxw_grHs',
            criteria = '7:安娜·德·阿玛斯|7:卡米拉·拉瑟福德|7:詹妮弗·阿尔莫|7:莉莉·詹姆斯|7:希米什·帕特尔|7:玛丽安娜·斯皮瓦克|7:乔尔·弗莱|7:凯特·麦克金农|7:卡米利·陈|7:剧情|7:音乐|7:摇滚|7:多米尼克·科尔曼|7:2019|7:艾利斯·查普尔|7:马诺伊·阿南德|7:莎拉·兰卡夏尔|7:阿历克斯·阿诺|7:索菲娅·迪·马蒂诺|7:艾德·希兰|7:美国|7:阿图尔·夏尔马|7:披头士|7:英国|7:奇幻|7:拉蒙尼·莫里斯|7:平行穿越|7:丹尼·博伊尔|7:詹姆斯·柯登|7:哈廷·帕特尔|7:喜剧|3:/subject/30165034/',
            preview = '',
            debug = false,
            adSlots = ['dale_movie_subject_top_icon', 'dale_movie_subject_top_right', 'dale_movie_subject_top_middle', 'dale_movie_subject_inner_middle', 'dale_movie_subject_download_middle', 'dale_movie_review_right_guess_you_like'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', '//img1.doubanio.com/dDY0Zjl6NS9mL2FkanMvNGQ1MjFiYTY2ZGE0MjE4OTc4YmYyOWZhODVjZDA2ZDdmODAyMTlkMy9hZC5yZWxlYXNlLmpz');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>







<script type="text/javascript">
var _paq = _paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript';
    g.defer=true;
    g.async=true;
    g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
})();
</script>

<script type="text/javascript">
var setMethodWithNs = function(namespace) {
  var ns = namespace ? namespace + '.' : ''
    , fn = function(string) {
        if(!ns) {return string}
        return ns + string
      }
  return fn
}

var gaWithNamespace = function(fn, namespace) {
  var method = setMethodWithNs(namespace)
  fn.call(this, method)
}

var _gaq = _gaq || []
  , accounts = [
      { id: 'UA-7019765-1', namespace: 'douban' }
    , { id: 'UA-7019765-19', namespace: '' }
    ]
  , gaInit = function(account) {
      gaWithNamespace(function(method) {
        gaInitFn.call(this, method, account)
      }, account.namespace)
    }
  , gaInitFn = function(method, account) {
      _gaq.push([method('_setAccount'), account.id]);
      _gaq.push([method('_setSampleRate'), '5']);

      
  _gaq.push([method('_addOrganic'), 'google', 'q'])
  _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
  _gaq.push([method('_addOrganic'), 'soso', 'w'])
  _gaq.push([method('_addOrganic'), 'youdao', 'q'])
  _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
  _gaq.push([method('_addOrganic'), 'sogou', 'query'])
  if (account.namespace) {
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
    _gaq.push([method('_addIgnoredOrganic'), 'douban'])
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
    _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
  }

      if (account.namespace === 'douban') {
        _gaq.push([method('_setDomainName'), '.douban.com'])
      }

        _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])

        _gaq.push([method('_setCustomVar'), 2, 'login_status', '0', 2]);

      _gaq.push([method('_trackPageview')])
    }

for(var i = 0, l = accounts.length; i < l; i++) {
  var account = accounts[i]
  gaInit(account)
}


;(function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
})()
</script>


    <!-- fram14-docker-->

  <script>_SPLITTEST=''</script>





<div id="search_suggest" style="display: none; top: 78px; left: 273.733px;"><ul></ul></div><span><iframe class="trc-hidden" id="trc-pixel-iframe-4319" name="trc-pixel-iframe-4319" style="display:none" __idm_frm__="8589934637" width="0" height="0"></iframe></span><div id="tbl-aug-sazlah" class="trc_popover_aug_container"><div id="tbl-aug-ewtiqf" class="trc_popover_aug_container"><div id="tbl-aug-vtnyds" class="trc_popover_aug_container"><div class=" trc_popover trc_popover_fade trc_bottom "><div class=" trc_popover_arrow "></div><iframe scrolling="no" src="javascript:void(0)" style="width: 100%;" __idm_frm__="8589934639" frameborder="0"></iframe></div></div></div></div><iframe src="//imprhkmp.taboola.com/st?cipid=66346445&amp;ttype=0&amp;cirid=D58E28C76182559562056631&amp;cicmp=2261215&amp;cijs=1&amp;dast=V7s04CFgPD_e72U5vyrgTD_e72U5vyrgUAAAAGBscHGsQarijDDW-2GE5Wq-VoMdwMhrvZZLmaQoc0fUbTQdJwmg2iouttsTucZs9BLZA1TS6_G1TQdDp8rnu92m97uuwiv-visNs1frdf87pYXR7TXzNYzFaDzWgvBwAAAIAHACrbLIgfQACACAAAAAAJAAAAAIqAin8LgQsAAAAADACEtx4NABYOA3RYLk67PwAAGhRAAAAEMEgACkyLSgA-XEZPAAAAAAAAAABY_v___2MG6LuaZQBEAL9vEHoAHnwAHoQAAAAehuDQnX8hMRmtiUoCixgBAAAAxBFkNhxN6oTKogoAgCDdCuAKACCgre00zDhLd1DiLQwAAEBA7OwMmV5c4TN6bIEeFr_f7LBr_G6XAQAAAAAAAACY_Z_9ownZuCelCfXnYKn9AgIArP0CAgCwaVu4Abi_DcCF3AmaTofrXq_7_e6Cp8PufD3sdrHDL_lXqyW3jbniGOZC09tsugBYnUJMZoPNajlcDGYHAAAAcPf___-Pd3aGTC-u8BmtB2IOl2Vj2q2Gm8liNtyNPKvlYDWxOWYrl8Xi2Y28h6LHz8lRlhzb1yFNn9F0kDScZoOo6Hpb7A6n2XNQC2RNk8tvP4qWLHfL3Wo0WYxGy-VmN9yMBvsTsOUAJ2KwXE4mi8luNVqNNsPdaDZYoEAMJjghw9FmshrtVrvJcjgZjWabyQYpWrWajTaD4Wo2me12q-FguByNkKI1i9lkspiNlrvNYDkZDYaT4RBhwrdarEYji1s28wzWoplrt1a4diu3zGMZzDaezWo5GK1Fr4_pNBztJhuTFwUDGvYiuEgnIr_r4rC7NXa37mWxiCWak0U6kV32NYfLsjHtVsPNZDEb7kae1XKwmtgcs5XLYvHsRv6Gb7VYjUYWt2zmGaxFM9durXDtVm6ZxzKYbTyb1XIwWoteH9NpONpNNiZ_YzVbrgaT3Wi3b6xmy9Vgshvt9h0u0-kvPhqFvY3KI3R5c5dnV-Y0KFwGo_cmUb38RsnBc7gYnS6RRmRsOL7f2dngMRgUsURwukgnopfxdBFLJE-LdKJbjhaj2W5i2QxWxtFit5i5bK7lcjGcWDyGwcQyEUuUpot0ote8LlaXx_TXDBaz1WAzmqj_yBCLzVw0V6w2c8VmlQAAAAAAAAAAljBl3gQAAADgNJjdYDJaLRdAAkh61yfHuTw1rDiiuPHjBvK7Lg67W2N3614WKwNIAEED!&amp;excid=22&amp;tst=1&amp;docw=0" style="display: none;"></iframe><iframe style="width: 0px; height: 0px; visibility: hidden; display: none;" __idm_frm__="8589934644"></iframe></body></html>'
"""



def get_douban_inf():
    #direct:导演  starring:演员  genre：
    #inf = {'direct':'null','starring':'null','genre':'null','loca':'null','lang':'null','time':'null'}
    #response = requests.get(url)
    soup = BeautifulSoup(mainWeb,'html.parser')
    mov_info = soup(id="info")[0]


    #for循环里面的东西不能重复

    comment_info = soup.find_all(class_="comment")
    for child in comment_info:
        com_name_te = child.find_all(name='a',class_="")
        for child1 in com_name_te:
            if child1.string =='展开':
            else
                print(child1.string)
        
    '''
    comment_info = soup.find_all(class_="comment")
    for child in comment_info:
        com_name_te = child.find_all(name='a',class_="")
        for child1 in com_name_te:
            print(child1.string)

        

        com = child.find_all(class_="short")
        if(child.find_all(class_="short"))
        
        
        for child2 in com:
            print(child2.string)
        
        print("")

    '''




'''

    #获取电影简介（以string形式输出）
    intro_te = soup(name='span',attrs={"property":"v:summary"})
    for child in intro_te:
        print(child.string)
 
    #获取主演名称
    star_te = soup(rel="v:starring")
    for child in star_te:
        print(child.string)
  
    #获取类型名称
    cate_te = soup(property="v:genre") 
    for child in cate_te:
        print(child.string)

    #获取上映日期
    date_te = soup(property="v:initialReleaseDate")
    for child in date_te:
        print(child.string)



    #获取其他相关信息
    compil_dire = r'导演<.*?><.*>(.+)</a>'
    compil_writ = r'编剧<.*?><.*>(.+)</a>'
    compil_loca = r'制片国家/地区:<.*?> (.+)<.*>' 
    compil_lang = r'语言:<.*?> (.+)<.*>' 
    compil_runt = r'片长:<.*?>.*<.*?>(.+)</.*>'
    compil_otna = r'又名:<.*?> (.+)<.*>'
    

    dire = re.findall(compil_dire,str(mov_info))
    writ = re.findall(compil_writ,str(mov_info))
    loca = re.findall(compil_loca,str(mov_info))
    lang = re.findall(compil_lang,str(mov_info))
    runt = re.findall(compil_runt,str(mov_info))
    otna = re.findall(compil_otna,str(mov_info))
    
  
    print(dire) 
    print(writ)
    print(loca)
    print(lang)
    print(date)
    print(runt)
    print(otna)

'''



#主程序入口，最后封装请直接删除
if __name__=='__main__':
    get_douban_inf()