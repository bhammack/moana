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
                        <th>...</th>
                    </tr>
                </thead>
            </table>
        </div>

    </div>
</template>
<script>

export default {
    mounted: function() {
        $('#recordsTable').DataTable();
    }
}

</script>
