<template>
     <div>
        <div id="controls">
            <button type="button" class="btn btn-primary btn-sm" data-toggle="modal" data-target="#authModal"><i class="fa fa-unlock"></i> Enable Controls</button>
            <button type="button" :disabled="!controlsEnabled" class="btn btn-danger"><i class="fa fa-power-off"></i> Emergency Power Off</button>
            <button type="button" :disabled="!controlsEnabled" class="btn btn-info"><i class="fa fa-medkit"></i> Release Payload</button>
            <button type="button" :disabled="!controlsEnabled" class="btn btn-info"><i class="fa fa-crosshairs"></i> Calibrate Position</button>
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

    export default {
        mqtt: {
            'telemetry': function(val) {
                var telemetry = JSON.parse(val.toString());
                //this.power = telemetry.power;
            }
        },
        data: function() {
            return {
                username: 'userx',
                password: '',
                controlsEnabled: false
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
            }
        }
    }
</script>
