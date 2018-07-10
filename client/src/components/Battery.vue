<template>
    <radial-gauge v-model="battery" v-bind:options="gaugeOptions"></radial-gauge>
</template>
<script>
    import RadialGauge from 'vue-canvas-gauges/src/RadialGauge';
    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                this.battery = this.calculateLife(telemetry.voltage, telemetry.altitude) * 100;
            }
        },
        data: function() {
            return {
                battery: 0,
                gaugeOptions: {
                    title: 'Battery Life',
                    colorTitle: '#eee',
                    colorNumbers: '#eee',
                    colorUnits: '#eee',
                    height: 290,
                    width: 290,
                    minValue: 0,
                    maxValue: 100,
                    barBeginCircle: false,
                    colorPlate: '#222',
                    units: '%',
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
        methods: {
            // Based on the voltage curves that Seaver provided, calculate the remaining power.
            // Consider whether we're flying or landed, and the current voltage draw.
            calculateLife: function(voltage, altitude) {
                var voltage_cell = voltage / 4;
                var lifeRemaining; // value from 0 to 1 of percent battery remaining.
                if (altitude < 1) {
                    if (voltage_cell > 3.57) {
                        lifeRemaining = 5.73 * Math.pow(voltage_cell, 3) - 69.114 * Math.pow(voltage_cell, 2) + 278.35 * voltage_cell - 373.41;
                    } else {
                        lifeRemaining = 0.2112 * voltage_cell - 0.5751;
                    }
                } else {
                    if (voltage_cell > 3.62) {
                        lifeRemaining = 2.9785 * Math.pow(voltage_cell, 3) - 37.052 * Math.pow(voltage_cell, 2) + 154.47 * voltage_cell - 214.82;
                    } else {
                        lifeRemaining = 0.1804 * voltage_cell - 0.5175;
                    }
                }

                // Force the life remaining to be between 0 and 1.
                if (lifeRemaining < 0) {
                    lifeRemaining = 0;
                } else if (lifeRemaining > 1) {
                    lifeRemaining = 1;
                }

                return lifeRemaining;
            }
        },
        components: {
            'radial-gauge': RadialGauge
        }
    }
</script>
