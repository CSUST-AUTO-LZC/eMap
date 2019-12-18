//baidu.js文件
var longitude = 113.01455;
var latitude = 28.075959;
    //设置地图的显示类型 及缩放最小值
var opt={mapType:BMAP_NORMAL_MAP,minZoom:4};
var map=new BMap.Map('map',opt);
var myDistanceTool = new BMapLib.DistanceTool(map, {lineStroke : 2});

function init(){

    //初始化地图
    map.centerAndZoom("长沙理工大学");
    var center=new BMap.Point(longitude,latitude);
    map.centerAndZoom(center,15);
    //禁止拖拽
    map.disableDragging();
    //禁用双击放大
    map.disableDoubleClickZoom();
    //启用滚轮放大缩小
    map.enableScrollWheelZoom();
    //右键启用地图拖拽
    map.addEventListener('rightclick',function(){
        map.enableDragging();
    });
    //创建定位控件 img/icon.jpg定位图片
    var location=new BMap.GeolocationControl({
        locationIcon:new BMap.Icon('/static/img/icon.png',new BMap.Size(50,50))
    });
    //控件位置右上角
    location.setAnchor(BMAP_ANCHOR_TOP_RIGHT);
    //控件偏移
    location.setOffset(new BMap.Size(100,50));
    map.addControl(location);
    //右键双击隐藏/开启控件
    map.addEventListener("rightdblclick",function () {
        location.isVisible()?location.hide():location.show();
   });
   //返回当前的定位信息，若当前还未定位，则返回null
   setTimeout(function(){
     location.location();
     console.log(location.getAddressComponent());
   },3*1000);
   //定位成功触发事件
   map.addEventListener("locationSuccess",function (result) {
       console.log(result);
   });
   //地图类型控件可选项
   var mapTypeControl=new BMap.MapTypeControl({
      type:BMAP_MAPTYPE_CONTROL_MAP,
      mapTypes:[BMAP_NORMAL_MAP,BMAP_PERSPECTIVE_MAP,BMAP_SATELLITE_MAP,BMAP_HYBRID_MAP],
      offset:new BMap.Size(5,80)
   });
   map.addControl(mapTypeControl);
   //设置版权控件位置
   var CopyrightControl = new BMap.CopyrightControl({
    anchor: BMAP_ANCHOR_TOP_RIGHT,
    offset:new BMap.Size(100,20)
   });
    //添加版权控件
    map.addControl(CopyrightControl); 
    //返回地图可视区域
    var getBounds= map.getBounds();   
    //Copyright(id,content,bounds)类作为CopyrightControl.addCopyright()方法的参数
    CopyrightControl.addCopyright({
        id: 1, 
        content: "<a href='/echartindex' style='font-size:20px;background:0;color:black'>TestMap@长沙理工大学-Geeks</a>",
        bounds: getBounds
    });
    //全景控件
    var PanoramaControl=new BMap.PanoramaControl()
    map.addControl(PanoramaControl);
    //实例化新创建的控件放到map上
    var ScaleControl= new UMap.ScaleControl();
    map.addControl(ScaleControl);
    //创建自定义图标代替大头针
    var icon = new BMap.Icon('/static/img/robot.png',new BMap.Size(40,40));
    icon.setImageSize(new BMap.Size(40,40));
    //创建大头针标注
    var marker = new BMap.Marker(center,{
        icon:icon,
        //微调大头针箭头指向误差
        offset:new BMap.Size(0,0)
    });
    map.addOverlay(marker);
    //坠落动画
    marker.setAnimation(BMAP_ANIMATION_DROP);
    //双击创建大头针 像素坐标 经纬度坐标 互相转换
    map.addEventListener("dblclick",function (event) {
       var icon = new BMap.Icon('/static/img/addAnchor.png',new BMap.Size(40,40));
        icon.setImageSize(new BMap.Size(40,40));
        var marker = new BMap.Marker(event.point,{
            icon:icon
        });
       //将setAnimation放到addOverlay后 创建大头针跳动效果
        map.addOverlay(marker);
        marker.setAnimation(BMAP_ANIMATION_BOUNCE);
   });
}
init();