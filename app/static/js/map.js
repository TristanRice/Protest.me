function constructMap(position) {
    const latitude = position.coords.latitude
    const longitude = position.coords.longitude
    //[latitude, longitude] = [position.coords.latitude, position.coords.longitude]
    var map = new ol.Map({
        target: 'map',
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ],
        view: new ol.View({
            center: ol.proj.fromLonLat([longitude, latitude]),
            zoom: 12
        })
    });
    prev_layer = null;
    map.on("click", function (event) {
        var layer = new ol.layer.Vector({
            source: new ol.source.Vector({
                features: [
                    new ol.Feature({
                        geometry: new ol.geom.Point(event.coordinate)
                    })
                ]
            })
        });
        map.removeLayer(prev_layer);
        prev_layer = layer;
        map.addLayer(layer)
    });

}

function handleGeoLocationRejection(error) {
    return error;
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(constructMap, handleGeoLocationRejection)
    }
}