<template>
    <radial-gauge v-model="temperature" v-bind:options="gaugeOptions"></radial-gauge>
</template>
<script>
    import RadialGauge from 'vue-canvas-gauges/src/RadialGauge';
    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                //var fahrenheit = telemetry.temperature * 1.8 + 32;
                this.temperature = telemetry.temperature;
            }
        },
        data: function() {
            return {
                temperature: 0,
                gaugeOptions: {
                    title: 'Temperature',
                    units: '°F',
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
                    highlights: [
                        {
                            from: 0,
                            to: 32,
                            color: 'blue'
                        },
                        {
                            from: 32,
                            to: 70,
                            color: 'grey'
                        },
                        {
                            from: 70,
                            to: 100,
                            color: 'green'
                        }
                    ],
                    animationRule: 'linear',
                    animationDuration: 200,
                    animationValue: true,
                }
            }
        },
        components: {
            'radial-gauge': RadialGauge
        }
    }
</script>
