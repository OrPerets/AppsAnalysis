const express = require('express')
const cors = require("cors");
const app = express();
const connectDB = require('./connect');
const  app_7 = require('./appSchema');

app.use(express.json());
app.use(cors());


app.get('/', function(req, res) {
  connectDB()
  res.send("Apps Server.")
});
app.get('/table' , (req,res) => {
  res.send(JSON.stringify(app_7.find({App_Name : 'Regain'})));
})



app.listen(8000, () => console.log('server running on port', 8000));
