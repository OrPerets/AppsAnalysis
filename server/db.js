var MongoClient = require('mongodb').MongoClient;
require('dotenv').config()

const connectionString = `mongodb+srv://${process.env.dbUserName}:${process.env.dbPassword}@apps.3mt9h.mongodb.net/?retryWrites=true&w=majority`
var _db;
var _items;


module.exports = {
    connectToDb: async (table, collection) => {
        try {
            const client = new MongoClient(connectionString, { useUnifiedTopology: true });
            await client.connect();
            _db = client.db(table);
            _items = _db.collection(collection);
            console.log('Connected to mongo!!!');

        } catch (err) {
            console.log(`Could not connect to MongoDB (err) => ${err}`);
        }
    },

    connection: connectionString,
    getDb: () => {return _db;},

    getNdata: (n,callback) => {
        return _items.find({}).limit(n).toArray(callback);
    },
    
};

