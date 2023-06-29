
const express = require('express')
const app = express()
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.locals.data = {};

app.get('/', function(req, res) {
  console.log("Stored json:", JSON.stringify(app.locals.data));
  console.log("People counter value: ", app.locals.data.peoplecounter);
  res.send('People counter: ' + app.locals.data.peoplecounter);
});

app.post('/api', function(req, res) {
    var post_body = req.body;
    req.app.locals.data = post_body;
    console.log("Received json:", post_body);
    res.send(post_body);
});

app.listen(8080, function () {
  console.log('Example app listening on port 8080!')
});
