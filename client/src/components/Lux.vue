<template>
    <radial-gauge v-model="lux" v-bind:options="gaugeOptions"></radial-gauge>
</template>
<script>
    import RadialGauge from 'vue-canvas-gauges/src/RadialGauge';
    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                this.lux = telemetry.lux;
            }
        },
        data: function() {
            return {
                lux: 0,
                gaugeOptions: {
                    title: 'Lux',
                    units: 'lux',
                    minValue: 0,
                    maxValue: 100,
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
