const express = require('express')
var { connectToDb,getFirstTen,getAllItems } = require('./db');
var cors = require("cors");


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


app.all('*',(req,res) => {
  res.status(404).send('resource not found')
})

app.listen(8000, () => console.log('server running on port', 8000));
