<template>
    <div id="cockpit">
        
        <div class="video">
            <iframe 
                src="https://www.youtube.com/embed/nutJCBPEwIg" 
                frameborder="1" 
                style="display: block; width: 100%; height: 100%;">
            </iframe>
        </div>
        <div class="map">
            <div id="map">
                
            </div>
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m10!1m8!1m3!1d14019.203099096716!2d-81.21332595000001!3d28.54570735!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1519679998787" 
                frameborder="1" 
                style="display: block; width: 100%; height: 100%;">
            </iframe>
        </div>
        <div class="sensor sensor1">
            <radial-gauge v-model="altitude" 
            v-bind:options="{
                title: 'Altitude',
                units: 'feet',
                minValue: 0,
                maxValue: 100,
                }"></radial-gauge>
        </div>
        <div class="sensor sensor2">
            <radial-gauge v-model="temperature" 
            v-bind:options="{
                title: 'Temperature',
                units: 'degrees',
                minValue: 0,
                maxValue: 100
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
        <div class="status">
            <!-- <h1>annunciator panel</h1> -->
            <button type="button" class="btn btn-primary" v-on:click="testme()">Test Telemetry Widgets</button>
            <!-- <img src="./../svg/quadcopter_basic.svg"> -->
        </div>


        
    </div>
</template>
<script>
    import LinearGauge from 'vue-canvas-gauges/src/LinearGauge';
    import RadialGauge from 'vue-canvas-gauges/src/RadialGauge';

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
                temperature: 75,
                power: 100,
                speed: 0
            }
        },
        components: {
            LinearGauge,
            RadialGauge
        },
        mounted: function() {
            console.log('mounted');
            this.$mqtt.subscribe('telemetry');
        },


        methods: {
            testme: function() {
                this.altitude = Math.floor(Math.random() * 101);        // [0-100]
                this.temperature = Math.floor(Math.random() * 101);     // [0-100]
                this.power = Math.floor(Math.random() * 101);           // [0-100]
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
        grid-template-rows: 2fr 1fr;
        grid-template-areas:
            "video video video map map"
            "sensor1 sensor2 sensor3 status status";
    }

    .video {
        grid-area: video;
        background-color: grey;
    }

    .map {
        grid-area: map;
    }

    .sensor {
        background-color: black;
    }


    .sensor.sensor1 {
        grid-area: sensor1;
    }

    .sensor.sensor2 {
        grid-area: sensor2;
    }

    .sensor.sensor3 {
        grid-area: sensor3;
    }

    .status {
        grid-area: status;
    }


</style>
