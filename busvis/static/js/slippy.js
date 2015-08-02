!function() {
    function addSlippyLayer(canvas, options)
    {
        var obj = {
            options : {
                minZoom: 10,
                maxZoom: 14,
                tms: false,
                bounds: canvas.bounds,
            },
            layer: null,
            grid: null,
        };
        L.Util.setOptions(obj, options);
        if (!obj.options.url) {
            console.error("No URL specified.");
            return;
        }
        obj.layer = L.tileLayer(obj.options.url, obj.options);
        canvas.map.addLayer(obj.layer);

        if (obj.options.gridUrl) {
            obj.grid = new L.UtfGrid(obj.options.gridUrl, {
			    resolution: 4,
                minZoom: obj.options.minZoom,
			    maxZoom: obj.options.maxZoom,
                bounds: obj.options.bounds,
                useJsonP: false,
		    });
            obj.grid.on('click', function(e){
                if (e.data)
                    canvas.map.openPopup("Speed: " + e.data.speed + '<br />' + 'Shape: ' + e.data.shape_id, e.latlng);
            });
            canvas.map.addLayer(obj.grid);
        }
        return obj;
    }
    busvis.addSlippyLayer = addSlippyLayer;
}();
