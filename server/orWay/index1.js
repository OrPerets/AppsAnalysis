// const express = require('express')
// var dbModule = require('./db');
// var cors = require("cors");
// const app = express();
// app.use(express.json());
// app.use(cors());


// app.get('/', function(req, res) {
//   res.send("Apps Server.")
// });


// app.get('/checkConnection', (req, res) => {
//   try {
//     dbModule.connectToDb('Applications', 'apps_7')
//     res.send("Connected!")
//   } catch {
//     res.send("Error.")
//   }
// })

// app.get("/getFirstTen", (req, res) => {
//   dbModule.getFirstTen((err, val) => {
//     if (err) res.send(err)
//     else {
//       res.send(val)
//     }
//   })
// })

// // const createPath =  (name) => {
// //   createConnection(name)
// //   app.get(`/${name}`,(req,res) => {
// //     dbModule.getFirstTen((err,values) => {
// //       if (err) {
// //         res.send(err)
// //       } else {
// //         console.log('Success');
// //         res.send(values)
// //       }
// //   })
// // })
// // }


// app.listen(8000, () => console.log('server running on port', 8000));
