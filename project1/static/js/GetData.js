// Echart初始化
var ST = "No RTU ,WaitConnect...";
var RTUname = document.getElementById("RTUname").value; 
var RTU_Name ="RTU_Name",state = 0,height = 0.00,speed=0.00,direction=0.00,temp=0.00,light=0.00;

function randomData() {
    var now = new Date();
    valuef = 30 + Math.random()*10 - 5;
    return {
        value: [
            [now.getHours(), now.getMinutes(), now.getSeconds()].join(':'),
            Math.round(valuef)
        ]
    }
}

//RTU终端切换
function RTUShift(){
	RTUname=document.getElementById("RTUname").value; 
	document.getElementById("RTUinfo").innerHTML = RTUname;
}

//数据获取
function GetData(Rtu_name,URLdata) {
	var now = new Date();	//时间记录
	var Time = "Null";
	
	//Jquery发起GET请求
	$.get("http://120.77.155.195/getdata/"+Rtu_name,function(data,status){
		
		jsonObj = JSON.parse(data);
		RTU_Name = jsonObj.name;
		state = parseInt(jsonObj.state);
		longitude = parseFloat(jsonObj.longitude);
		latitude = parseFloat(jsonObj.latitude);
		height = parseFloat(jsonObj.height);
		speed = parseFloat(jsonObj.speed);
		direction = parseFloat(jsonObj.direction);
		temp = parseFloat(jsonObj.temp);
		light = parseFloat(jsonObj.light);
		
		});

	Time = [now.getHours(), now.getMinutes(), now.getSeconds()].join(':');
	Data_Obj = { name: RTU_Name, state: state,longitude: longitude,latitude: latitude,height: height,speed: speed,direction: direction,temp: temp,light: light};
    return Data_Obj;
}

var timer1 = null;
//自动跟踪 （定时循环程序）
function Autofollow() {
	
	if( timer2 == null && timer1 == null ){
		
		timer1 = setInterval(function () {
		
		document.getElementById("LocationMode").innerHTML = "自动跟踪" ;
		var RTUData = GetData(RTUname,0);
		var date = new Date();

		document.getElementById("realtime").innerHTML = date.toLocaleTimeString();
		document.getElementById("name").innerHTML = RTUData.name;
		document.getElementById("longitude").innerHTML = RTUData.longitude;
		document.getElementById("latitude").innerHTML = RTUData.latitude;
		document.getElementById("height").innerHTML = RTUData.height;
		document.getElementById("speed").innerHTML = RTUData.speed;
		document.getElementById("direction").innerHTML = RTUData.direction;
		document.getElementById("temp").innerHTML = RTUData.temp;
		document.getElementById("light").innerHTML = RTUData.light;
		document.getElementById("data1").innerHTML = "null";
		document.getElementById("data2").innerHTML = "null";
		document.getElementById("data3").innerHTML = "null";
		theLocation(longitude,latitude);

		}, 1000);
	}
}

var timer2 = null;
//自动定位 （定时循环程序）
function AutoLocation(){
	
	if( timer2 == null && timer1 == null ){
		timer2 = setInterval(function () {
		document.getElementById("LocationMode").innerHTML = "自动定位" ;
		var RTUData = GetData(RTUname,0);
		var date = new Date();
		var time = date.toLocaleTimeString();
		
		document.getElementById("realtime").innerHTML = date.toLocaleTimeString();
		document.getElementById("name").innerHTML = RTUData.name;
		document.getElementById("longitude").innerHTML = RTUData.longitude;
		document.getElementById("latitude").innerHTML = RTUData.latitude;
		document.getElementById("height").innerHTML = RTUData.height;
		document.getElementById("speed").innerHTML = RTUData.speed;
		document.getElementById("direction").innerHTML = RTUData.direction;
		document.getElementById("temp").innerHTML = RTUData.temp;
		document.getElementById("light").innerHTML = RTUData.light;
		document.getElementById("data1").innerHTML = "null";
		document.getElementById("data2").innerHTML = "null";
		document.getElementById("data3").innerHTML = "null";
		map.clearOverlays();
		theLocation(longitude,latitude);

		}, 1000);
	}
}

//手动定位
function ManuelLocation() {

		if( timer2 == null && timer1 == null ){
		document.getElementById("LocationMode").innerHTML = "手动定位" ;
		var RTUData = GetData(RTUname,0);
		var date = new Date();
		var time = date.toLocaleTimeString();
		
		document.getElementById("realtime").innerHTML = date.toLocaleTimeString();
		document.getElementById("name").innerHTML = RTUData.name;
		document.getElementById("longitude").innerHTML = RTUData.longitude;
		document.getElementById("latitude").innerHTML = RTUData.latitude;
		document.getElementById("height").innerHTML = RTUData.height;
		document.getElementById("speed").innerHTML = RTUData.speed;
		document.getElementById("direction").innerHTML = RTUData.direction;
		document.getElementById("temp").innerHTML = RTUData.temp;
		document.getElementById("light").innerHTML = RTUData.light;
		document.getElementById("data1").innerHTML = "null";
		document.getElementById("data2").innerHTML = "null";
		document.getElementById("data3").innerHTML = "null";
		map.clearOverlays();
		theLocation(longitude,latitude);
		}
}

//定时停止函数
function StopTimer() {
	
	document.getElementById("LocationMode").innerHTML = "定位停止" ;
    clearInterval(timer1);
	timer1=null;
	clearInterval(timer2);
	timer2=null;
}

// 用经纬度设置地图中心点
function theLocation(longitudeValue,latitudeValue){
	
	if(longitude != "" && latitude != ""){
		//map.clearOverlays();
		var new_point = new BMap.Point(longitudeValue,latitudeValue);
		var marker = new BMap.Marker(new_point);  // 创建标注
		map.addOverlay(marker);              // 将标注添加到地图中
		map.panTo(new_point);
	}
}