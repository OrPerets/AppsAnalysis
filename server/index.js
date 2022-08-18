const express = require('express')
const { connectToDb,getFirstTen,getAllItems } = require('./db');
const cors = require("cors");
const getData = require('./fetch.js');


const app = express();
app.use(express.json());
app.use(cors());

app.get('/', (req, res) => {
  res.send("Apps Server.")
});


// Lotan: Right now for the testing, I am using the function that return only the first ten, to get all the data simply change to getAllItems. each route is getting the data of specific collection.

app.get('/app7' , async (req,res) => {
    await connectToDb('Applications', 'apps_7')
    getFirstTen((err,values) => {
      if (err) {
        res.send(err)
      } 
      else {
        console.log('Success');
        res.send(values)
      }
})
})

app.get('/app6' , async (req,res) => {
  await connectToDb('Applications', 'apps_6')
  getFirstTen((err,values) => {
    if (err) {
      res.send(err)
    } 
    else {
      console.log('Success');
      res.send(values)
    }
})
})

app.get('/app5' , async (req,res) => {
  await connectToDb('Applications', 'apps_5')
  getFirstTen((err,values) => {
    if (err) {
      res.send(err)
    } 
    else {
      console.log('Success');
      res.send(values)
    }
})
})

app.get('/app4' , async (req,res) => {
  await connectToDb('Applications', 'apps_4')
  getFirstTen((err,values) => {
    if (err) {
      res.send(err)
    } 
    else {
      console.log('Success');
      res.send(values)
    }
})
})

app.get('/app3' , async (req,res) => {
  await connectToDb('Applications', 'apps_3')
  getFirstTen((err,values) => {
    if (err) {
      res.send(err)
    } 
    else {
      console.log('Success');
      res.send(values)
    }
})
})

app.get('/app2' , async (req,res) => {
  await connectToDb('Applications', 'apps_2')
  getFirstTen((err,values) => {
    if (err) {
      res.send(err)
    } 
    else {
      console.log('Success');
      res.send(values)
    }
})
})

app.get('/app1' , async (req,res) => {
  await connectToDb('Applications', 'apps_1')
  getFirstTen((err,values) => {
    if (err) {
      res.send(err)
    } 
    else {
      console.log('Success');
      res.send(values)
    }
})
})

// the fetch code start here, x will be the developer name.
const x = 'spotify developer country'

app.get('/search' , async (req,res) => {
  const data = await getData(`https://google-search3.p.rapidapi.com/api/v1/search/q=${x}`)
  res.send(data)
})
// 



app.all('*',(req,res) => {
  res.status(404).send('resource not found')
})

app.listen(8000, () => console.log('server running on port', 8000));
