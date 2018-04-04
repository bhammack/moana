<template>
    <div id="cockpit" class="cockpit-grid">
        <div style="display:none;">Icons made from <a href="http://www.onlinewebfonts.com/icon">Icon Fonts</a> is licensed by CC BY 3.0</div> 
        <div class="status">
            <annunciator-panel></annunciator-panel>           
        </div>
        <div class="map">
            <map-vue></map-vue>
        </div>
        <div class="sensor-grid">
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
                <compass></compass>
            </div>
        </div>
        <div class="control">
            <control-panel></control-panel>
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

    export default {
        components: {
            MapVue,
            Altimeter,
            Thermometer,
            Power,
            Compass,
            AnnunciatorPanel,
            ControlPanel
        }
    }
</script>
<style>
    .cockpit-grid {
        height: 100%;
        display: grid;
        grid-template-columns: auto min-content;
        grid-template-rows: 100px min-content auto;
        /* grid-column-gap: 10px; */
        /* grid-row-gap:  */
        grid-template-areas:
            "map status"
            "map sensor-grid"
            "map control";
    }

    .sensor-grid {
        display: grid;
        grid-area: sensor-grid;
        grid-template-columns: auto auto;
        grid-template-rows: auto auto;
        grid-template-areas:
            "sensor1 sensor2"
            "sensor3 sensor4";
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

    .card {
        background-color: slategray;
    }

    .card-inactive {
        background-color: slategray;
    }

    .card-active {
        background-color: gold;
    }
</style>
