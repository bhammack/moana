<template>
    <div id="about">
        <h1>About</h1>
        <h6 v-for="name in names">{{name}}</h6>






    </div>
</template>
<script>
    export default {
        data: function() {
            return {
                names: [
                    'Ben Hammack',
                    'Phillip Bent',
                    'Mark Shipps',
                    'Ray Sanzi III',
                    'Seaver Wrisley',
                    'Matt Jean',
                    'Ayo Duyile',
                    'Chris Parmentier',
                    'Jill Sharkley',
                    'Xavier Johnson',
                    'Paul La Rosa'
                ]
            }
        }
    }
</script>
