<template>
    <div id="cockpit">
        <div class="status">

        </div>
        <div class="map">
            <map-vue></map-vue>
        </div>
        <div class="sensor sensor1">
            <altimeter></altimeter>
        </div>
        <div class="sensor sensor2">
            <thermometer></thermometer>
        </div>
        <div class="sensor sensor3">
            <power></power>
        </div>
        <div class="sensor sensor4">
            <compass></compass>
        </div>
        <div class="control">
            <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#authModal">Enable Controls</button>
        </div>  
        <div id="authModal" class="modal" tabindex="-1">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Operator Authorization</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                </div>
                <div class="modal-body">
                    <div class="col-12">
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"><i class="fa fa-unlock"></i></span>
                            </div>
                            <input v-model="password" type="password" class="form-control" placeholder="Operator password">
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" v-on:click="authorize">Submit</button>
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                </div>
                </div>
            </div>
            </div>      
    </div>
</template>
<script>
    // https://en.wikipedia.org/wiki/Flight_instruments
    import Altimeter from './Altimeter';
    import Thermometer from './Thermometer';
    import Power from './Power';
    import Compass from './Compass';
    import MapVue from './MapVue';
    import axios from 'axios';

    export default {
        data: function() {
            return {
                controlsEnabled: false,
                username: 'userx',
                password: null
            }
        },
        components: {
            'map-vue': MapVue,
            'altimeter': Altimeter,
            'thermometer': Thermometer,
            'power': Power,
            'compass': Compass
        },
        mounted: function() {
            console.log('mounted');
            this.$mqtt.subscribe('telemetry');
        },
        methods: {
            authorize: function() {
                var vm = this;
                console.log(this.password);
                axios.post('api/auth', { username: this.username, password: this.password}).then((res) => {
                    vm.password = '';
                    vm.controlsEnabled = true;
                }).catch((err) => {

                });
            }
        }
    }

</script>
<style>
    #cockpit {
        height: 100%;
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: 100px repeat(2, 1fr) 100px;
        grid-template-areas:
            "map map status status"
            "map map sensor1 sensor2"
            "map map sensor3 sensor4"
            "map map control control";
    }

    .map {
        grid-area: map;
    }

    .sensor {
        background-color: #111;
    }

    .status {
        grid-area: status;
    }

    .control {
        grid-area: control;
    }

    .sensor1 {
        grid-area: sensor1;
    }

    .sensor2 {
        grid-area: sensor2;
    }

    .sensor3 {
        grid-area: sensor3;
    }

    .sensor4 {
        grid-area: sensor4;
    }
</style>
