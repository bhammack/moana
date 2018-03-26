<template>
    <div id="leafletmap" style="height: 100%"></div>
</template>
<script>

import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
// Weird webpack related leaflet configuration...
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

import axios from 'axios';

export default {
    data: function() {
        return {
            center: [28.542644, -81.212693],
            zoom: 13,
            markers: [],
            markerGroup: null,
            map: null
        }
    },
    mounted: function() {
        this.buildMap();
        this.getMarkers();
    },
    methods: {
        buildMap: function() {
            var vm = this;
            this.map = L.map('leafletmap').setView(this.center, this.zoom);
            this.map.on('click', function(event) {
                vm.addMarker(event);
            });
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(this.map);
            this.markerGroup = L.layerGroup().addTo(this.map);
        },
        addMarker: function(event) {
            var vm = this;
            var marker = L.marker(event.latlng, {})
                .addTo(this.markerGroup)
                .bindPopup('<h1>sample text</h1>')
                .bindTooltip('tooltip')
                .on('contextmenu', function(event) {
                    vm.removeMarker(event.target._leaflet_id);
                });
            axios.post('api/points', {
                name: "pointname",
                description: "pointdesc",
                markerId: marker._leaflet_id,
                latitude: marker._latlng.lat,
                longitude: marker._latlng.lng,
                altitude: 0
            }).then((res) => {
                console.log(res);
            })
            .catch((err) => {

            });
        },
        getMarkers: function() {
            var vm = this;
            // axios.get('api/points').then((res) => {
            //     res.data.forEach(function(point) {
            //         var latlng = {
            //             lat: point.latitude,
            //             lng: point.longitude
            //         }
            //     L.marker(latlng, {})
            //         .addTo(vm.markerGroup)
            //         .bindPopup('<h1>sample text</h1>')
            //         .bindTooltip('tooltip')
            //         .on('contextmenu', function(event) {
            //             vm.removeMarker(event.target._leaflet_id);
            //         });
            //     });
            // }).catch((err) => {

            // });
        },
        removeMarker: function(markerId) {
            this.markerGroup.removeLayer(markerId);
            axios.delete('api/points/'+markerId).then((res) => {
                console.log(res);
            }).catch((err) => {

            });
        }
    }
}

</script>
<style>
    
</style>