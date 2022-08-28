const express = require('express')
const { connectToDb,getFirstFiveThousand,getAllItems } = require('./db');
const cors = require("cors");
const getData = require('./fetchData.js');
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


app.get('/app7' , async (req,res) => {
    await connectToDb('Applications', 'apps_7')
    getFirstFiveThousand((err,values) => {
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
  getFirstFiveThousand((err,values) => {
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
  getFirstFiveThousand((err,values) => {
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
  getFirstFiveThousand((err,values) => {
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
  getFirstFiveThousand((err,values) => {
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
  getFirstFiveThousand((err,values) => {
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
  getFirstFiveThousand((err,values) => {
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
/**
 * OR: move constant variable to other file, such as "consts.js"
 */
const x = 'spotify developer country'

app.get('/search' , async (req,res) => {
  const data = await getData(`https://google-search3.p.rapidapi.com/api/v1/search/q=${x}`)
  res.send(data)
})

app.all('*',(req,res) => {
  res.status(404).send('resource not found')
})

app.listen(8000, () => console.log('server running on port', 8000));
