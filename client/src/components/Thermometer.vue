<template>
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
</template>
<script>
    import RadialGauge from 'vue-canvas-gauges/src/RadialGauge';
    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                this.temperature = telemetry.temperature;
            }
        },
        data: function() {
            return {
                temperature: 0
            }
        },
        components: {
            'radial-gauge': RadialGauge
        }
    }
</script>
