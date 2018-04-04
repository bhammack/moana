<template>
    <radial-gauge v-model="heading" v-bind:options="gaugeOptions"></radial-gauge>
</template>
<script>
    import RadialGauge from 'vue-canvas-gauges/src/RadialGauge';
    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                this.heading = telemetry.heading;
            }
        },
        data: function() {
            return {
                heading: 0,
                gaugeOptions: {
                    title: 'Heading',
                    units: 'degrees',
                    height: 300,
                    width: 300,
                    minValue: 0,
                    maxValue: 360,
                    majorTicks: [
                        "N",
                        "NE",
                        "E",
                        "SE",
                        "S",
                        "SW",
                        "W",
                        "NW",
                        "N"
                    ],
                    minorTicks: 22,
                    ticksAngle: 360,
                    startAngle: 180,

                    needleType: 'line',
                    needleStart: 75,
                    needleEnd: 99,
                    needleWidth: 3,

                    highlights: [{}],
                    strokeTicks: false,
                    valueTextShadow: false,

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


                    animation: true,
                    animationTarget: 'plate',
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
