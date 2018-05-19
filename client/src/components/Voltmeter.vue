<template>
    <radial-gauge v-model="voltage" v-bind:options="gaugeOptions"></radial-gauge>
</template>
<script>
    import RadialGauge from 'vue-canvas-gauges/src/RadialGauge';
    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                this.voltage = telemetry.voltage;
            }
        },
        data: function() {
            return {
                voltage: 0,
                gaugeOptions: {
                    title: 'Power',
                    colorTitle: '#eee',
                    colorNumbers: '#eee',
                    colorUnits: '#eee',
                    height: 290,
                    width: 290,
                    minValue: 0,
                    maxValue: 100,
                    barBeginCircle: false,
                    colorPlate: '#222',

                    //numberSide: 'left',
                    //needleSide: 'left',
                    //tickSide: 'left',
                    units: 'Voltage',
                    //width: 150,
                    borders: true,
                    highlights: [
                        {
                            from: 0,
                            to: 30,
                            color: 'red'
                        },
                        {
                            from: 30,
                            to: 60,
                            color: 'yellow'
                        },
                        {
                            from: 60,
                            to: 100,
                            color: 'green'
                        }
                    ],
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
                    colorBorderInnerEnd: '#333'
                }
            }
        },
        components: {
            'radial-gauge': RadialGauge
        }
    }
</script>
