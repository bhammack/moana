<template>
     <div class="card-deck" style="height: 100%">
        <div class="card text-white text-center bg-dark border border-light"><h4 class="card-title m-0">PROPS LOCKED</h4></div>
        <div class="card text-white text-center bg-dark border border-light"><h4 class="card-title m-0">HEAT DETECTED</h4></div>
        <div class="card text-white text-center bg-dark border border-light"><h4 class="card-title m-0">GROUNDED</h4></div>
        <div class="card text-white text-center bg-dark border border-light"><h4 class="card-title m-0">HATCH OPEN</h4></div>
        <div class="card text-white text-center bg-dark border border-light"><h4 class="card-title m-0">CONNECTED</h4></div>
    </div>
</template>
<script>
    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                //this.power = telemetry.power;
            }
        },
        data: function() {
            return {
                //power: 0
            }
        }
    }
</script>
