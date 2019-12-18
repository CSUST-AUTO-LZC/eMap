//UMap.js文件 自定义控件
window.UMap = window.UMap || {};
(function() {
    function ScaleControl() {
        this.defaultAnchor = BMAP_ANCHOR_TOP_LEFT;
        this.defaultOffset = new BMap.Size(50, 50);	//控件区域大小（即边距设定）
    }
    ScaleControl.prototype = new BMap.Control();
    ScaleControl.prototype.initialize = function(map) {
        //创建button按钮
        var container = document.createElement("div");
        var maxButton = document.createElement('button');
        var minButton = document.createElement('button');
        maxButton.textContent='+';
        minButton.textContent='-';
        container.appendChild(maxButton);
        container.appendChild(minButton);
        maxButton.style.cssText = "font-size:30px;padding:5px 5px";
		minButton.style.cssText = "font-size:30px;padding:5px 8px";
        //点击地图放大或缩小
        maxButton.onclick=minButton.onclick=function(){
            this.textContent=='+'?map.zoomIn():map.zoomOut();
        };
        map.getContainer().appendChild(container);
        return container;
    };
    UMap.ScaleControl = ScaleControl;
})();