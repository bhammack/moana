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
                // TODO: parse the status codes
            }
        },
        data: function() {
            return {
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
