<template>
    <div id="cockpit" class="cockpit-grid">
        <div style="display:none;">Icons made from <a href="http://www.onlinewebfonts.com/icon">Icon Fonts</a> is licensed by CC BY 3.0</div> 
        <div class="sensor-grid-left">
            <div class="sensor sensor1"><altimeter></altimeter></div>
            <div class="sensor sensor2"><compass></compass></div>
            <div class="sensor sensor3"><speedometer></speedometer></div>
        </div>
        <div class="control-grid">
            <div class="status"><annunciator-panel></annunciator-panel></div>
            <div class="map"><map-vue></map-vue></div>
            <div class="control"><control-panel></control-panel></div>
        </div>
        <div class="sensor-grid-right">
            <div class="sensor sensor4"><thermometer></thermometer></div>
            <div class="sensor sensor5"><power></power></div>
            <div class="sensor sensor6"><lux></lux></div>
        </div>
    </div>
</template>
<script>
    // https://en.wikipedia.org/wiki/Flight_instruments
    import Altimeter from './Altimeter';
    import Thermometer from './Thermometer';
    import AnnunciatorPanel from './AnnunciatorPanel';
    import ControlPanel from './ControlPanel';
    import Power from './Power';
    import Compass from './Compass';
    import MapVue from './MapVue';
    import Speedometer from './Speedometer';
    import Lux from './Lux';

    export default {
        components: {
            MapVue,
            Altimeter,
            Thermometer,
            Power,
            Compass,
            AnnunciatorPanel,
            ControlPanel,
            Speedometer,
            Lux
        }
    }
</script>
<style>
    .cockpit-grid {
        background-color: black;
        height: 100%;
        display: grid;
        grid-template-columns: min-content auto min-content;
        grid-template-areas:
            "sensor-grid-left control-grid sensor-grid-right"
    }

    .sensor-grid-left {
        display: grid;
        justify-items: start;
        grid-area: sensor-grid-left;
        grid-template-rows: repeat(3, min-content);
        grid-template-areas:
            "sensor1"
            "sensor2"
            "sensor3";
    }

    .sensor-grid-right {
        display: grid;
        justify-items: end;
        grid-area: sensor-grid-right;
        grid-template-rows: repeat(3, min-content);
        grid-template-areas:
            "sensor4"
            "sensor5"
            "sensor6";
    }

    .control-grid {
        display: grid;
        grid-area: control-grid;
        grid-template-rows: min-content auto min-content;
        grid-template-areas:
            "status"
            "map"
            "control";
    }

    .map {
        grid-area: map;
    }

    .sensor {
        background-color: #111;
    }

    .status {
        grid-area: status;
        background-color: #333;
    }

    .control {
        height: 50px;
        grid-area: control;
        background-color: #333;
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

    .sensor5 {
        grid-area: sensor5;
    }

    .sensor6 {
        grid-area: sensor6;
    }
</style>
