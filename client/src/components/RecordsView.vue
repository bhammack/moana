<template>
    <div id="records">
        <h1>Records</h1>
        <div class="container-fluid">
            <table id="recordsTable" class="table table-striped">
                <thead>
                    <tr>
                        <th>Timestamp</th>
                        <th>Latitude</th>
                        <th>Longitude</th>
                        <th>Altitude</th>
                        <th>Temperature</th>
                        <th>Power</th>
                        <th>Event Code</th>
                        <!-- <th>...</th> -->
                    </tr>
                </thead>
            </table>
        </div>

    </div>
</template>
<script>

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
                { data: 'power' },
                { data: 'eventCode' }
            ]
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
