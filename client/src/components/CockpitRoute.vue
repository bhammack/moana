<template>
    <div id="cockpit">
        
        <div class="video">
            <iframe 
                src="https://www.youtube.com/embed/tgbNymZ7vqY" 
                frameborder="1" 
                style="display: block; width: 100%; height: 100%;">
            </iframe>
        </div>
        <div class="map">
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m10!1m8!1m3!1d14019.203099096716!2d-81.21332595000001!3d28.54570735!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1519679998787" 
                frameborder="1" 
                style="display: block; width: 100%; height: 100%;">
            </iframe>
        </div>
        <div class="sensor">
            <linear-gauge :value="377"></linear-gauge>
        </div>
        <div class="sensor"></div>
        <div class="sensor"></div>
        <div class="status"></div>


        
    </div>
</template>
<script>
    import LinearGauge from 'vue-canvas-gauges/src/LinearGauge';
    import RadialGauge from 'vue-canvas-gauges/src/RadialGauge';

    export default {
        components: {
            LinearGauge,
            RadialGauge
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
    }

    .map {
        grid-area: map;
    }

    .sensor {
        grid-area: sensor1;
    }

    .status {
        grid-area: status;
    }


</style>
