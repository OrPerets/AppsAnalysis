const mongoose = require('mongoose');

const appSchema = new mongoose.Schema({
    id: String,
    App_Name: String,
    App_Id: String,
    Category: String,
    Rating: Number,
    Rating_Count: Number,
    Installs: String,
    Minimum_Installs: Number,
    Maximum_Installs: Number,
    Free: Boolean,
    Price: Number,
    Currency: String,
    Size: String,
    Minimum_Android: String,
    Developer_Id: String,
    Developer_Website: String,
    Developer_Email: String,
    Released: String,
    Last_Updated: String,
    Content_Rating: String,
    Privacy_Policy: String,
    Ad_Supported: Boolean,
    In_App_Purchases: Boolean,
    Editors_Choice: Boolean,
    Scraped_Time: String
});


module.exports = mongoose.model('Application',appSchema)


