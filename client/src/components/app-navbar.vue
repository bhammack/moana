<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  	<a class="navbar-brand" href="/#/">MOANA</a>
	  <!-- Todo: put foursite logo here -->
  	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
		<span class="navbar-toggler-icon"></span>
  	</button>
	<div class="collapse navbar-collapse" id="navbarSupportedContent">
		<ul class="navbar-nav mr-auto">
			<li class="nav-item"><a class="nav-link" href="/#/home">Home</a></li>      
			<li class="nav-item"><a class="nav-link" href="/#/cockpit">Cockpit</a></li>
			<li class="nav-item"><a class="nav-link" href="/#/records">Records</a></li>
			<li class="nav-item"><a class="nav-link" href="/#/map">Map</a></li>
			<li class="nav-item"><a class="nav-link" href="/#/about">About</a></li>
		</ul>
		<p class="nav navbar-text">Last updated: {{ lastReceived }} <span v-bind:class="{ 'badge-success': isConnected, 'badge-danger': !isConnected }" class="badge">{{ statusMessage }}</span></p>
		
	</div>
</nav>
</template>
<script>
	export default {
		mqtt: {
			'telemetry': function(val) {
				this.updateLastReceived();
			}
		},
		data: function() {
			return {
				isConnected: false,
				statusMessage: 'Disconnected',
				lastReceived: null
			}
		},
		mounted: function() {
			var vm = this;
			this.$mqtt.on('connect', vm.onConnect());
			this.$mqtt.on('reconnect', vm.onConnect());
			this.$mqtt.on('close', vm.onDisconnect());
			this.$mqtt.on('offline', vm.onDisconnect());
			this.$mqtt.on('error', vm.onError(error));
			this.$mqtt.on('end', vm.onDisconnect());
		},
		methods: {
			onConnect: function() {
				this.statusMessage = 'Connected';
				this.isConnected = true;
				this.updateLastReceived();
			},
			onDisconnect: function() {
				this.statusMessage = 'Disconnected';
				this.isConnected = false;
				this.updateLastReceived();
			},
			onError: function(error) {
				this.statusMessage = 'Error';
				console.log(error);
				this.isConnected = false;
				this.updateLastReceived();
			},
			updateLastReceived: function() {
				this.lastReceived = new Date().toString();
			}
		}
	}
</script>
