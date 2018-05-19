<template>
    <div id="about">
        <h1>About</h1>
<<<<<<< HEAD
        <!-- <h6 v-for="name in names">{{name}}</h6> -->






=======
        <div class="container">
            <div class="jumbotron">
                <div class="row">
                    <div class="col-6">
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
>>>>>>> bfc5bc80206287d1e63186f1f1e504b8bec85d10
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
