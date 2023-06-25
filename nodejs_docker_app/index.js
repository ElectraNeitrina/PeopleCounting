var express = require('express');

// Constants
var DEFAULT_PORT = 8080;
var PORT = process.env.PORT || DEFAULT_PORT;

// App
var app = express();
app.locals.data = {};
app.get('/', function (req, res) {
  var toDisplay = app.locals.data
  res.send("People counter feedback:" + toDisplay + "; thanks\n");
});

app.post('/', function(req, res) {
  app.locals.data = req.body;
  res.send(req.body); // echo the result back
});

app.listen(PORT)
console.log('Running on http://localhost:' + PORT);
