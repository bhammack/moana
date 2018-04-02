<template>
    <div id="cockpit">
        <div class="status">
        </div>
        <div class="map">
            <map-vue></map-vue>
        </div>
        <div class="sensor sensor1">
            <altimeter></altimeter>
        </div>
        <div class="sensor sensor2">
            <thermometer></thermometer>
        </div>
        <div class="sensor sensor3">
            <power></power>
        </div>
        <div class="sensor sensor4">

        </div>
        <div class="control">
        </div>        
    </div>
</template>
<script>
    // https://en.wikipedia.org/wiki/Flight_instruments
    import Altimeter from './Altimeter';
    import Thermometer from './Thermometer';
    import Power from './Power';
    import MapVue from './MapVue';

    export default {
        data: function() {
            return {
                controlsEnabled: false
            }
        },
        components: {
            'map-vue': MapVue,
            'altimeter': Altimeter,
            'thermometer': Thermometer,
            'power': Power
        },
        mounted: function() {
            console.log('mounted');
            this.$mqtt.subscribe('telemetry');
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
            "sensor3 map map map sensor4";
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
