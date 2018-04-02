<template>
    <div id="cockpit">
        <div class="status">

        </div>
        <div class="map">
            <map-vue></map-vue>
        </div>
        <div class="sensor sensor1">
            <radial-gauge v-model="altitude" 
            v-bind:options="{
                title: 'Altitude',
                units: 'feet',
                minValue: 0,
                maxValue: 100,
                animation: true,
                animationRule: 'linear',
                animationDuration: 200,
                animationValue: true
                }"></radial-gauge>
        </div>
        <div class="sensor sensor2">
            <radial-gauge v-model="temperature" 
            v-bind:options="{
                title: 'Temperature',
                units: 'degrees',
                minValue: 0,
                maxValue: 100,
                animationRule: 'linear',
                animationDuration: 200,
                animationValue: true
            }"></radial-gauge>
        </div>
        <div class="sensor sensor3">
            <linear-gauge v-model="power"
            v-bind:options="{
                title: 'Power',
                minValue: 0,
                maxValue: 100,
                barBeginCircle: 0
            }"></linear-gauge>
        </div>
        <div class="sensor sensor4">
            <!-- <h1>annunciator panel</h1> -->
            <button type="button" class="btn btn-primary" v-on:click="testme()">Test Telemetry Widgets</button>
            <!-- <img src="./../svg/quadcopter_basic.svg"> -->
        </div>
        <div class="control">
        </div>


        
    </div>
</template>
<script>
    import LinearGauge from 'vue-canvas-gauges/src/LinearGauge';
    import RadialGauge from 'vue-canvas-gauges/src/RadialGauge';
    import MapVue from './MapVue';

    import 'leaflet/dist/leaflet.css';
    import Vue2Leaflet from 'vue2-leaflet';

    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                console.log(telemetry);
                this.update(telemetry);
            },
        },
        data: function() {
            return {
                altitude: 0,
                temperature: 0,
                power: 0,
                speed: 0
            }
        },
        components: {
            'linear-gauge': LinearGauge,
            'radial-gauge': RadialGauge,
            'map-vue': MapVue
        },
        mounted: function() {
            console.log('mounted');
            this.$mqtt.subscribe('telemetry');
        },


        methods: {
            testme: function() {
                console.log('attempting to publish');
                var testobj = {
                    altitude: Math.floor(Math.random() * 101),        // [0-100]
                    temperature: Math.floor(Math.random() * 101),     // [0-100]
                    power: Math.floor(Math.random() * 101),           // [0-100]
                    latitude: 0,
                    longitude: 0,
                    eventCode: 0
                }
                this.$mqtt.publish('telemetry', JSON.stringify(testobj), {
                    retain: true
                });
            },
            update: function(telemetry) {
                this.altitude = telemetry.altitude;
                this.temperature = telemetry.temperature;
                this.power = telemetry.power;
            }
        }
    }

</script>
<style>
    #cockpit {
        height: 100%;
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        grid-template-rows: 30px repeat(2, 1fr);
        grid-template-areas:
            "status status status status status"
            "sensor1 map map map sensor2"
            "sensor3 control control control sensor4";
    }

    .map {
        grid-area: map;
    }

    .sensor {
        background-color: black;
    }

    .status {
        grid-area: status;
    }

    .sensor1 {
        grid-area: sensor1;
    }

    .sensor2 {
        grid-area: sensor2;
    }

    .sensor3 {
        grid-area: sensor3;
    }

    .sensor4 {
        grid-area: sensor4;
    }

    .control {
        grid-area: control;
    }
</style>
