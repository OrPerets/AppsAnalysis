const express = require('express')
const { connectToDb,getAllItems, getFirstTen} = require('./db');
const cors = require("cors");
const { searchGoogle,getCountriesList }= require('./fetchData.js');
const app = express();
app.use(express.json());
app.use(cors());

// SERVER URL - https://appsanalysis.vercel.app
/**
 * Table = AppsAnalysis
 * Collections = App, Installs, Rating, Reviews
 *  */ 

app.get('/', (req, res) => {
  res.send("Apps Server.")
});

// Getting the data from a collection
app.get('/getItems/:collectionId',async (req,res) => {
  let collection = req.params.collectionId
  await connectToDb('AppsAnalysis',collection)
  getAllItems((err,value) => {
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
  // usage example: http://127.0.0.1:8000/getItems/7/100   --> return 100 items from apps_7
  let collection = req.params.collectionId
  let totalItems = Number(req.params.k)
  await connectToDb('Applications', collection)
  getFirstKElements(totalItems, (err,values) => {
    if (err) {
      res.send(err)
    } 
    else {
      console.log('Success');
      res.send(values)
    }
})
})

// Searching google
app.get('/search/:value' , async (req,res) => {
  // usage example: http://127.0.0.1:8000/search/spotify country
  const data = await searchGoogle(`https://google-search3.p.rapidapi.com/api/v1/search/q=${req.params.value}`)
  console.log(data)
  res.send(data)
})

// get all countries
app.get('/countries',async (req,res) => {
  const data = await getCountriesList(`https://restcountries.com/v3.1/all`)
  res.send(data)
})


// Handling false requests
app.all('*',(req,res) => {
  res.status(404).send('resource not found')
})

app.listen(3030, () => console.log('server running on port', 3030));
