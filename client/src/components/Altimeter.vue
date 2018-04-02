<template>
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
</template>
<script>
    import RadialGauge from 'vue-canvas-gauges/src/RadialGauge';
    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                this.altitude = telemetry.altitude;
            }
        },
        data: function() {
            return {
                altitude: 0
            }
        },
        components: {
            'radial-gauge': RadialGauge
        }
    }
</script>
