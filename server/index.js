const express = require('express')
const { connectToDb,getFirstFiveThousand,getAllItems, } = require('./db');
const cors = require("cors");
const { searchGoogle,getCountriesList }= require('./fetchData.js');
const app = express();
app.use(express.json());
app.use(cors());

// SERVER URL - https://appsanalysis.vercel.app 
/**
 * Every change in the server:
 * terminal -- run "vercel --prod"
 */

app.get('/', (req, res) => {
  res.send("Apps Server.")
});


app.get('/search/:value' , async (req,res) => {
  // usage example: http://127.0.0.1:8000/search/spotify country
  const data = await searchGoogle(`https://google-search3.p.rapidapi.com/api/v1/search/q=${req.params.value}`)
  console.log(data)
  res.send(data)
})


app.get('/getItems/:collectionId/:k' , async (req,res) => {
  // usage example: http://127.0.0.1:8000/getItems/7/100   --> return 100 items from apps_7
  let collection = "apps_" + req.params.collectionId
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


// get all countries
app.get('/countries',async (req,res) => {
  const data = await getCountriesList(`https://restcountries.com/v3.1/all`)
  res.send(data)
})


app.all('*',(req,res) => {
  res.status(404).send('resource not found')
})

app.listen(8000, () => console.log('server running on port', 8000));
