const fetch = require('node-fetch');

const options = {
	method: 'GET',
	headers: {
		'X-User-Agent': 'desktop',
		'X-Proxy-Location': 'US',
		'X-RapidAPI-Key': 'efded72d34mshf6bf2c499d188d7p1fd487jsnf7fa12714b48',
		'X-RapidAPI-Host': 'google-search3.p.rapidapi.com'
	}
};

// Google search
const getData = async (url) => {
    try {
        const data = await fetch(url,options)
        return data.json();
    } catch (err) {
        console.log(err);
    }
}

// Wikipedia search


module.exports = getData