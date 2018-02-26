<template>
    <div id="index">
        <div class="content">
            <h1>Index</h1>      
        </div>        
    </div>
</template>
<script>
    // https://www.nytimes.com/2017/09/08/us/hurricane-irma-florida.html

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