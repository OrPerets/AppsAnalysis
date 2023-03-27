const express = require('express')
const { connectToDb,getAllItems, getNdata} = require('./db');
const cors = require("cors");
const { searchGoogle,getCountriesList }= require('./fetchData.js');
const app = express();
app.use(express.json());
app.use(cors());

// SERVER_URL: "https://app-server-three.vercel.app"

app.get('/', (req, res) => {
  res.send("Apps Server.")
});

// Getting the data from a collection
app.get('/getItems/:collectionId',async (req,res) => {
  let collection = req.params.collectionId
  await connectToDb('AppsAnalysis',collection)
  get((err,value) => {
    if (err) {
      res.send(err)
    } 
    else {
      console.log('Success');
      res.send(value)
    }
  })
})

// Getting from the big collection with selected number of data
app.get('/getItems/:collectionId/:k' , async (req,res) => {
  let collection = req.params.collectionId
  let totalItems = Number(req.params.k)
  await connectToDb('AppsAnalysis', collection)
  getNdata(totalItems, (err,values) => {
    if (err) {
      res.send(err)
    } 
    else {
      console.log('Success');
      res.send(values)
    }
})
})

// Handling false requests
app.all('*',(req,res) => {
  res.status(404).send('resource not found')
})

app.listen(3030, () => console.log('server running on port', 3030));
