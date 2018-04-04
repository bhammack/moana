<template>
     <div class="card-group" style="height: 100%">
        <div class="card card-inactive"><img class="card-img" src="./../svg/quadcopter_liftoff.svg"></div>
        <div class="card card-active"><img class="card-img" src="./../svg/quadcopter_landing.svg"></div>
        <div class="card"><img class="card-img" src="./../svg/quadcopter_load.svg"></div>
        <div class="card"><img class="card-img" src="./../svg/quadcopter_unload.svg"></div>
        <div class="card"><img class="card-img" src="./../svg/quadcopter_lumination.svg"></div>
        <div class="card"><img class="card-img" src="./../svg/quadcopter_payload.svg"></div>
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
