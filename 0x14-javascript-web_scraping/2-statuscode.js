#!/home/mubrik/.nvm/versions/node/v19.2.0/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
