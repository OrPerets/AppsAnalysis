// var MongoClient = require('mongodb').MongoClient;
// var {dbPassword , dbUserName} = require('./config');

// const connectionString = `mongodb+srv://${dbUserName}:${dbPassword}@apps.3mt9h.mongodb.net/?retryWrites=true&w=majority`
// var _db;
// var _items;

//  module.exports = {
//     connectToDb: async (table, collection) => {
//         try {
//             const client = new MongoClient(connectionString, { useUnifiedTopology: true });
//             await client.connect();
//             _db = client.db(table);
//             _items = _db.collection(collection);
//             console.log('Connected to mongo!!!');

//         } catch (err) {
//             console.log(`Could not connect to MongoDB (err) => ${err}`);
//         }
//     },

//     getAllItems: (callback) => {
//         return _items.find({}).toArray(callback);
//     },


//     getFirstTen: (callback) => {
//         return _items.find({}).limit(10).toArray(callback);
//     },

//     collectionNames : ['apps_1' , 'apps_2' , 'apps_3' , 'apps_4' , 'apps_5' , 'apps_6' , 'apps_7']
// };

