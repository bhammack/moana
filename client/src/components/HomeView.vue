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
                <p>Foursite Engineering presents...</p>
                <hr>
                <h1>MOANA</h1>
                <h2>Mobile Operational Assistance for Navigation Appropriations</h2>
                <hr>
                <div>
                <a href="/#/cockpit" class="btn btn-lg btn-primary float-left" data-toggle="tooltip" data-placement="bottom" 
                    title="The operator view provides the ability for the user to send control signals to the quadcopter">
                    <i class="fa fa-fighter-jet"></i>
                    Operator Cockpit
                </a>
                <a href="/#/cockpit" class="btn btn-lg btn-primary float-right" data-toggle="tooltip" data-placement="bottom" 
                    title="The spectator view provides a read-only interface for viewing quadcopter telemetry data">
                    <i class="fa fa-eye"></i>
                    Spectator Cockpit
                </a>
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