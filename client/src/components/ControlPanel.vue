<template>
     <div>
        <div id="controls" v-on:keyup.space="console.log('test');">
            <div class="row">
                <div class="col-2">
                    <button type="button" :disabled="controlsEnabled" class="btn btn-primary btn-block" data-toggle="modal" data-target="#authModal"><i class="fa fa-unlock"></i> Enable Controls</button>
                </div>
                <div class="col-6">
                    <div class="row">
                        <div class="col-6">
                            <button type="button" :disabled="!controlsEnabled" v-on:click="lockProps" class="btn btn-warning btn-block"><i class="fa fa-ban"></i> Lock Propellers</button>
                        </div>
                        <div class="col-6">
                            <button type="button" :disabled="!controlsEnabled" v-on:click="unlockProps" class="btn btn-success btn-block"><i class="fa fa-ban"></i> Unlock Propellers</button>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-6">
                            <button type="button" :disabled="!controlsEnabled" v-on:click="emergencyLand" class="btn btn-danger btn-block"><i class="fa fa-arrow-circle-o-down"></i> Emergency Land</button>
                        </div>
                        <div class="col-6">
                            <button type="button" :disabled="!controlsEnabled" v-on:click="releasePayload" class="btn btn-info btn-block"><i class="fa fa-medkit"></i> Release Payload</button>
                        </div>
                    </div>
                    
                    
                </div>
                <div class="col-4">
                    <div class="row">
                        <div class="col-12">
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <button type="button" :disabled="!controlsEnabled" class="btn btn-info" v-on:click="calibratePosition"><i class="fa fa-crosshairs"></i> Calibrate Position</button>
                                </div>
                                <input v-model.number="latitude" type="text" maxlength="10" class="form-control" placeholder="Latitude">
                                <input v-model.number="longitude" type="text" maxlength="10" class="form-control" placeholder="Longitude">
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-12">
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <button type="button" :disabled="!controlsEnabled" class="btn btn-warning" v-on:click="luxThreshold"><i class="fa fa-lightbulb-o"></i> Lux Threshold</button>
                                </div>
                                <input v-model.number="lux" type="number" min="0" max="10000" step="10" class="form-control" placeholder="Lux Threshold">
                            </div>
                        </div>
                    </div>
                    
                </div>
            </div>
        </div>
        <div id="authModal" class="modal fade" tabindex="-1">
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
    import axios from 'axios';
    const SPACE = 32;
    const BACKSPACE = 8;

    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                //this.power = telemetry.power;
            },
            'calibration': function(val) {
                var position = JSON.parse(val.toString());
                this.latitude = position.latitude;
                this.longitude = position.longitude;
            },
            'lux': function(val) {
                var lux = JSON.parse(val.toString());
                this.lux = lux.luxThreshold;
                console.log(lux.luxThreshold);
            }
        },
        data: function() {
            return {
                username: 'userx',
                password: '',
                controlsEnabled: process.env.NODE_ENV == "development",
                latitude: 0,
                longitude: 0,
                lux: 10
            }
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
            },
            releasePayload: function() {
                console.log('Payload released...');
                this.$mqtt.publish('control', JSON.stringify({
                    command: 'DROP'
                }));
            },
            lockProps: function() {
                console.log('Locking propellers...');
                this.$mqtt.publish('control', JSON.stringify({
                    command: 'LOCK'
                }));
            },
            unlockProps: function() {
                console.log('Unlocking propellers...');
                this.$mqtt.publish('control', JSON.stringify({
                    command: 'UNLK'
                }));
            },
            emergencyLand: function() {
                console.log('Emergency Land initiated...');
                this.$mqtt.publish('control', JSON.stringify({
                    command: 'LAND'
                }));
            },
            calibratePosition: function() {
                var vm = this;
                console.log('Calibrating position...');
                this.$mqtt.publish('calibration', JSON.stringify({
                    latitude: vm.latitude,
                    longitude: vm.longitude
                }), 2, true);
            },
            luxThreshold: function() {
                var vm = this;
                console.log('Setting lux threshold...');
                this.$mqtt.publish('lux', JSON.stringify({
                    luxThreshold: vm.lux
                }), 2, true);
            }
        },
        mounted: function() {
            var vm = this;
            window.addEventListener('keyup', function(event) {
                if (vm.controlsEnabled) {
                    if (event.keyCode == SPACE) {
                        vm.releasePayload();
                    } else if (event.keyCode == BACKSPACE) {
                        vm.emergencyLand();
                    }
                }
            });
        }
    }
</script>
