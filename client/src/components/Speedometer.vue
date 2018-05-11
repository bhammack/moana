<template>
    <radial-gauge v-model="speed" v-bind:options="gaugeOptions"></radial-gauge>
</template>
<script>
    import RadialGauge from 'vue-canvas-gauges/src/RadialGauge';
    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                this.speed = telemetry.speed;
            }
        },
        data: function() {
            return {
                speed: 0,
                gaugeOptions: {
                    title: 'Ground Speed',
                    units: 'm/s',
                    minValue: 0,
                    maxValue: 30,
                    height: 290,
                    width: 290,
                    colorMajorTicks: '#dddddd',
                    colorMinorTicks: '#dddddd',
                    colorTitle: '#eeeeee',
                    colorPlate: '#222222',
                    borders: true,
                    colorUnits: '#cccccc',
                    colorNumbers: '#eeeeee',
                    colorBorderOuter: '#333333',
                    colorBorderOuterEnd: '#111111',
                    colorBorderMiddle: '#222222',
                    colorBorderMiddleEnd: '#111',
                    colorBorderInner: '#111',
                    colorBorderInnerEnd: '#333',
                    highlights: false,
                    animation: true,
                    animationRule: 'linear',
                    animationDuration: 200,
                    animationValue: true
                }
            }
        },
        components: {
            'radial-gauge': RadialGauge
        }
    }
</script>
