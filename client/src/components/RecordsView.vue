<template>
    <div id="records">

        <div class="container-fluid">
            <div class="row">
                <div class="col-12">
                <h3>Telemetry Records</h3>
                </div>
            </div>
            <table id="recordsTable" class="table table-striped">
                <thead>
                    <tr>
                        <th>Timestamp</th>
                        <th>Latitude</th>
                        <th>Longitude</th>
                        <th>Altitude</th>
                        <th>Temperature</th>
                        <th>Voltage</th>
                        <th>Speed</th>
                    </tr>
                </thead>
            </table>
        </div>
    </div>
</template>
<script>

import $ from 'jquery';
import 'datatables.net-bs4/css/dataTables.bootstrap4.css';
import 'datatables.net-bs4';
$.fn.dataTable.ext.errMode = 'throw';

export default {
    mounted: function() {
        this.dt = $('#recordsTable').DataTable({
            ajax: {
                url: '/api/telemetry',
                dataSrc: ''
            },
            columns: [
                { data: 'dateReceived' },
                { data: 'latitude' },
                { data: 'longitude' },
                { data: 'altitude' },
                { data: 'temperature' },
                { data: 'voltage' },
                { data: 'speed' }
            ]
        })
        .on('error.dt', function(e, settings, techNote, message) {
            // $.fn.dataTable.ext.errMode = none. This method handles dt errors.
            //console.log( 'An error has been reported by DataTables: ', message );
        });
    },
    data: function() {
        return {
            dt: null
        }
    },
    methods: {
        updateTable: function() {
            // update the records table with new data.
            console.log('Updating table...');
            dt.ajax.reload();
        }
    }
}

</script>
