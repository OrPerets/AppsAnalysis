const express = require('express')
var dbModule = require('./db');
var cors = require("cors");

// OR: run the server and navigate to http://127.0.0.1:8000, there check your routes,
// for example: http://127.0.0.1:8000/getFirstTen
// OR: if you want to connect more collection - change the connectToDb function
dbModule.connectToDb("Applications", "apps_2")

const collectionNames = ['apps_1' , 'apps_2' , 'apps_3' , 'apps_4' , 'apps_5' , 'apps_6' , 'apps_7']

const app = express();
app.use(express.json());
app.use(cors());

app.get('/', function(req, res) {
  res.send("Apps Server.")
});

// OR: the server must have a route to perform an action, so for every action we create a route and then 
// activate the relevant function

// const createConnection = (name) => {
//   dbModule.connectToDb('applications' , name)
// }

app.get('/checkConnection', (req, res) => {
  try {
    dbModule.connectToDb('Applications' , "apps_2")
    res.send("Connected!")
  } catch {
    res.send("Error.")
  }
})

app.get("/getFirstTen", (req, res) => {
  dbModule.getFirstTen((err, val) => {
    if (err) res.send(err)
    else {
      res.send(val)
    }
  })
})
// const createPath =  (name) => {
//   createConnection(name)
//   app.get(`/${name}`,(req,res) => {
//     dbModule.getFirstTen((err,values) => {
//       if (err) {
//         res.send(err)
//       } else {
//         console.log('Success');
//         res.send(values)
//       }
//   })
// })
// }


app.listen(8000, () => console.log('server running on port', 8000));
