/**
 * cd server
 * npm install express
 * npm install cors
 * npm install mongodb
 * 
 * 
 * Collections: apps_1, ...., apps_7
 * Check mongodb how to read part of collection
 */

const express = require('express')
var dbModule = require('./db');
var cors = require("cors");

dbModule.connectToDb("Applications", "apps_7");

const app = express();
app.use(express.json());
app.use(cors());

app.get('/', function(req, res) {
  res.send("Apps Server.")
});

app.get('/getAll', function(req, res) {
  dbModule.getAllItems((err, values) => {
    if (err) {
      res.send(err)
    } else {
      res.send(values)
    }
  })
});

app.listen(8000, () => console.log('server running on port', 8000));
