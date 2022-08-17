const {dbPassword , dbUserName} = require('./config');
const mongoose = require('mongoose');

const connectionString = `mongodb+srv://${dbUserName}:${dbPassword}@apps.3mt9h.mongodb.net/?retryWrites=true&w=majority`


const connectDB = () => {
    return mongoose.connect(
        connectionString,
        () => {
            console.log('connected...');
        }),
        e => console.log(e);

}



module.exports = connectDB
