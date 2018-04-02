<template>
    <div id="index">
        <div class="content container">

            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>

            <div class="jumbotron">
                <!-- Todo: Two column layout. One side a big image, the other the moana system, description, and buttons -->
                <img src="./../images/foursite.png"> presents...
                <hr>
                <h1>MOANA</h1>
                <h2>Mobile Operational Assistance for Navigation Appropriations</h2>
                <hr>
                <div>
                    <a href="/#/cockpit" class="btn btn-lg btn-outline-primary float-left"><i class="fa fa-fighter-jet"></i> Enter Cockpit</a>
                    <a href="/#/records" class="btn btn-lg btn-outline-primary float-right"><i class="fa fa-eye"></i> View Records</a>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    // https://www.nytimes.com/2017/09/08/us/hurricane-irma-florida.html

export default {
  mounted: function() {
    $('[data-toggle="tooltip"]').tooltip();
  }
}

</script>
<style>
    .content:before {
        content: "";
        position: fixed;

        left: 0;
        right: 0;
        z-index: -1;

        display: block;
        height: 100%;
        background-image: url('./../images/hurricane.jpg');
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;

        -webkit-filter: blur(5px);
        -moz-filter: blur(5px);
        -o-filter: blur(5px);
        -ms-filter: blur(5px);
        filter: blur(5px);
    }

    .content {
        position: fixed;
        left: 0;
        right: 0;
        z-index: 0;
    }
</style>