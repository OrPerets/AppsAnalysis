const express = require('express')
var dbModule = require('./db');
var cors = require("cors");
const { application } = require('express');

const collectionNames = ['apps_1' , 'apps_2' , 'apps_3' , 'apps_4' , 'apps_5' , 'apps_6' , 'apps_7']

const app = express();
app.use(express.json());
app.use(cors());

app.get('/', function(req, res) {
  res.send("Apps Server.")
});

const createConnection = (name) => {
  dbModule.connectToDb('applications' , name)
}

const createPath =  (name) => {
  createConnection(name)
  app.get(`/${name}`,(req,res) => {
    dbModule.getFirstTen((err,values) => {
      if (err) {
        res.send(err)
      } else {
        console.log('Success');
        res.send(values)
      }
  })
})
}

createPath('apps_7')


// const data = collectionNames.map((collection) => {
//   dbModule.connectToDb('applications' , collection)
//   return app.get(`/${collection}`, (req, res) => {
//     dbModule.getFirstTen((err,values) => {
      
//       if (err) {
//         res.send(err)
//       } else {
//         console.log('Success');
//         res.send(values)
//       }
//     })
//   });
// })

// app.get('/getAll', function(req, res) {
//   dbModule.getAllItems((err,values) => {
//     if (err) {
//       res.send(err)
//     } else {
//       res.send(values)
//     }
//   })
// });

app.all('*',(req,res) => {
  res.status(404).send('resource not found')
})

app.listen(8000, () => console.log('server running on port', 8000));
