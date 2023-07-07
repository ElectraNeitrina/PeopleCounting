var transportData = require("./transportData.json");
var offlineSimulatedData = {"transportData": JSON.parse(JSON.stringify(transportData)), "simulated": true};
const express = require('express')
const app = express()
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine','ejs');
app.locals.data = {"transportData": transportData, "simulated": true};

app.get('/', function(req, res) {
  console.log("Stored json:", JSON.stringify(app.locals.data));
  console.log("Transport data:", JSON.stringify(transportData));
  console.log("People counter value: ", app.locals.data.peoplecounter);
  if (req.app.locals.data.simulated) {
    res.render('index', {data: offlineSimulatedData});
  } else {
    res.render('index', {data: req.app.locals.data});
  }
});

app.post('/api', function(req, res) {
    var post_body = req.body;
       if (!post_body.hasOwnProperty("vehicle_id")) {
      console.log("ERROR: vehicle_id missing from the POST data");
      res.send({"ERROR": "vehicle_id missing from the POST data"});
      return;
    }
    if (!post_body.hasOwnProperty("people_counter")) {
      console.log("ERROR: people_counter missing from the POST data");
      res.send({"ERROR": "people_counter missing from the POST data"});
      return;
    }
   console.log("Received json:", post_body);
   req.app.locals.data.transportData.vehicles[post_body.vehicle_id].peopleCounter = post_body.people_counter;
    res.send(post_body);
});

app.post('/internal', function(req, res) {
    var post_body = req.body;
    console.log(post_body);
    req.app.locals.data.simulated = post_body.simulated;
    res.send(post_body);
});

app.listen(8080, function () {
  console.log('Example app listening on port 8080!')
});
