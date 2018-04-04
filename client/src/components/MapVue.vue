<template>
    <div id="leafletcontainer" style="height:100%"></div>
</template>
<script>

import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
const TILE_LAYER_URL = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
const TILE_LAYER_ATTR = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';

// Weird webpack related leaflet configuration...
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

import axios from 'axios';

export default {
    mqtt: {
        'telemetry': function(val) {
            var telemetry = JSON.parse(val.toString());
            this.updatePosition(telemetry.latitude, telemetry.longitude);
        }
    },
    data: function() {
        return {
            center: [28.542644, -81.212693],
            zoom: 11,
            markers: [],
            poiMarkerGroup: null,
            vehicleMarkerGroup: null,
            vehicleMarker: null,
            map: null
        }
    },
    mounted: function() {
        this.buildMap();
        this.getMarkers();
    },
    beforeDestroy: function() {
        console.log('destroying map...');
        this.map.off();
        this.map.remove();
        // var leafletmap = document.getElementById('leafletmap');
        // leafletmap.parentNode.removeChild(leafletmap);
    },
    methods: {
        buildMap: function() {
            var vm = this;
            // For some reason, it is suggested to dynamically create the map div if working between multiple views containing a leaflet map.
            // In our case, the 'map' tab and the 'cockpit' tab.
            //var mapdiv = document.createElement('div');
            //mapdiv.setAttribute('id', 'leafletmap');
            //document.getElementById('leafletcontainer').appendChild(mapdiv);
            //
            this.map = L.map('leafletcontainer').setView(this.center, this.zoom);
            //this.map = L.map('leafletmap').setView(this.center, this.zoom);
            this.map.on('click', function(event) {
                vm.addMarker(event);
            });
            L.tileLayer(TILE_LAYER_URL, { attribution: TILE_LAYER_ATTR }).addTo(this.map);
            this.poiMarkerGroup = L.layerGroup().addTo(this.map);
            this.vehicleMarkerGroup = L.layerGroup().addTo(this.map);
        },
        addMarker: function(event) {
            var vm = this;
            var marker = L.marker(event.latlng, {})
                .addTo(this.poiMarkerGroup)
                .bindPopup('<h1>sample text</h1>')
                .bindTooltip('tooltip')
                .on('contextmenu', function(event) {
                    vm.removeMarker(event.target._leaflet_id, event.target._latlng.lat, event.target._latlng.lng);
                });
            axios.post('api/points', {
                description: "pointdesc",
                markerId: marker._leaflet_id,
                latitude: marker._latlng.lat,
                longitude: marker._latlng.lng,
            }).then((res) => {
                console.log(res);
            })
            .catch((err) => {

            });
        },
        getMarkers: function() {
            var vm = this;
            axios.get('api/points').then((res) => {
                res.data.forEach(function(point) {
                    var latlng = {
                        lat: point.latitude,
                        lng: point.longitude
                    }
                L.marker(latlng, {})
                    .addTo(vm.poiMarkerGroup)
                    .bindPopup('Point of Interest')
                    //.bindTooltip('tooltip')
                    .on('contextmenu', function(event) {
                        vm.removeMarker(event.target._leaflet_id, event.target._latlng.lat, event.target._latlng.lng);
                    });
                });
            }).catch((err) => {

            });
        },
        removeMarker: function(markerId, lat, lng) {
            this.poiMarkerGroup.removeLayer(markerId);
            axios.delete('api/points?latitude='+lat+'&longitude='+lng).then((res) => {
                console.log(res);
            }).catch((err) => {

            });
        },
        updatePosition: function(latitude, longitude) {
            console.log('mapvue new quadcopter position: ' + latitude + ', ' + longitude);
            var vm = this;
            var pos = new L.LatLng(latitude, longitude);
            if (this.vehicleMarker == null) {
                this.vehicleMarker = L.marker(pos).bindTooltip('Current position').addTo(vm.vehicleMarkerGroup);
            } else {
                this.vehicleMarker.setLatLng(pos).update();
            }
        }
    }
}

</script>
<style>
#leafletmap {
    height: 100%;
}
</style>