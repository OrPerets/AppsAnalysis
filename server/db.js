var MongoClient = require('mongodb').MongoClient;
var { dbUserName, dbPassword } = require('./config');


const connectionString = `mongodb+srv://${dbUserName}:${dbPassword}@apps.3mt9h.mongodb.net/?retryWrites=true&w=majority`
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
    addItem: (item) => {
        _items.insertOne(item, {}, function (err, doc) {
            if (err) {
                return 500
            }
        });
        return 200
    },
    addManyItems: (items) => {
        _items.insertMany(items, {}, function (err, docs) {
            if (err) {
                return 500
            }
        });
        return 200
    },
    getAllItems: (callback) => {
        return _items.find({}).toArray(callback);
    },

    getFirstTen: (callback) => {
        return _items.find({}).limit(10).toArray(callback);
    },
    
};

