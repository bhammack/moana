<template>
     <div class="card-deck" style="height: 100%">
        <div class="card text-white text-center" :class="[propsLocked ? 'bg-warning border-dark' : 'bg-dark border-light']"><h4 class="card-title m-0">PROPS LOCKED</h4></div>
        <div class="card text-white text-center" :class="[heatDetected ? 'bg-danger border-light' : 'bg-dark border-light']"><h4 class="card-title m-0">HEAT DETECTED</h4></div>
        <div class="card text-white text-center" :class="[grounded ? 'bg-success border-light' : 'bg-dark border-light']"><h4 class="card-title m-0">GROUNDED</h4></div>
        <div class="card text-white text-center" :class="[hatchOpen ? 'bg-warning border-dark' : 'bg-dark border-light']"><h4 class="card-title m-0">HATCH OPEN</h4></div>
    </div>
</template>
<script>
    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());

                this.heatDetected = (telemetry.lux > this.luxThreshold);
                this.grounded = !(telemetry.altitude > 0);
                // TODO: parse the status codes
            },
            'lux': function(val) {
                var lux = JSON.parse(val.toString());
                this.luxThreshold = lux.luxThreshold;
            }
        },
        data: function() {
            return {
                luxThreshold: 0,
                heatDetected: false,
                propsLocked: false,
                grounded: false,
                hatchOpen: false
            }
        }
    }
</script>
<style>
</style>
