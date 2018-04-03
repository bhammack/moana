<template>
    <linear-gauge v-model="power" v-bind:options="gaugeOptions"></linear-gauge>
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
                power: 0,
                gaugeOptions: {
                    title: 'Power',
                    colorTitle: '#eee',
                    colorNumbers: '#eee',
                    colorUnits: '#eee',
                    minValue: 0,
                    maxValue: 100,
                    barBeginCircle: false,
                    colorPlate: '#222',
                    needleType: 'line',
                    numberSide: 'left',
                    needleSide: 'left',
                    tickSide: 'left',
                    units: 'Voltage',
                    width: 150,
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
                    ]
                }
            }
        },
        components: {
            'linear-gauge': LinearGauge
        }
    }
</script>
