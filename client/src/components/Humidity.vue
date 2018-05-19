<template>
    <radial-gauge v-model="humidity" v-bind:options="gaugeOptions"></radial-gauge>
</template>
<script>
    import RadialGauge from 'vue-canvas-gauges/src/RadialGauge';
    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                this.humidity = telemetry.humidity;
            }
        },
        data: function() {
            return {
                humidity: 0,
                gaugeOptions: {
                    title: 'Humidity',
                    units: '%',
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
                            to: 35,
                            color: 'brown'
                        },
                        {
                            from: 35,
                            to: 65,
                            color: 'grey'
                        },
                        {
                            from: 65,
                            to: 100,
                            color: 'navy'
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
