# MOANA
> Mobile Operational Assistance for Navigation & Appropriations (MOANA) System
> An ELDP Project for the class of 2020

## Setup

In order to setup the project environment, please enter the commands below:

``` bash
$ git clone https://www.github.com/bhammack/moana.git
$ cd moana
$ npm install
$ npm run build 
$ npm start
```

### Notes
Some final comments as I wrap up the project
* Used PM2 as a Node-driven process manager for starting/stopping/updating the server on ec2
* Used Nginx as a reverse proxy