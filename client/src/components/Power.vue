<template>
    <linear-gauge v-model="power"
    v-bind:options="{
        title: 'Power',
        minValue: 0,
        maxValue: 100,
        barBeginCircle: 0
    }"></linear-gauge>
</template>
<script>
    import LinearGauge from 'vue-canvas-gauges/src/LinearGauge';
    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                this.power = telemetry.power;
            }
        },
        data: function() {
            return {
                power: 0
            }
        },
        components: {
            'linear-gauge': LinearGauge
        }
    }
</script>
