<template>
    <div id="leafletmap" style="height: 100%">
       <v-map ref="map" :zoom="zoom" :center="center">
            <v-tilelayer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></v-tilelayer>
            <v-marker :lat-lng="center"></v-marker>
            <!-- <v-marker v-for="point in points" :lat-lng="[47.413220, -1.219482]"></v-marker> -->
        </v-map>
   </div>
</template>
<script>

import 'leaflet/dist/leaflet.css';
import Vue2Leaflet from 'vue2-leaflet';
import axios from 'axios';

export default {
    components: {
        'v-map': Vue2Leaflet.Map,
        'v-tilelayer': Vue2Leaflet.TileLayer,
        'v-marker': Vue2Leaflet.Marker
    },
    data: function() {
        return {
            center: [28.542644, -81.212693],
            zoom: 13,
            markers: []




        }
    },
    created: function() {
        axios.get('api/points').then((res) => {
            console.log(res);
        }).catch((err) => {

        });
    }
}

</script>
<style>
    
</style>