<template>
    <div id="about">
        <h3>About</h3>
        <div class="container">
            <div class="jumbotron">
                <div class="row">
                    <div class="col-6">
                        <h1>MOANA</h1>
                        <small>Mobile Operational Assistance for Navigation Appropriations</small>
                        
                    </div>
                    <div class="col-6">
                        <ul>
                            <li v-bind:key="name" v-for="name in names">
                                <h6>{{name}}</h6>
                            </li>
                        </ul>
                    </div>
                </div>
            
            </div>
            
        </div>
    </div>
</template>
<script>
    export default {
        data: function() {
            return {
                names: [
                    'Ray Sanzi III',
                    'Seaver Wrisley',
                    'Matt Jean',
                    'Ben Hammack',
                    'Phillip Bent',
                    'Mark Shipps',
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
