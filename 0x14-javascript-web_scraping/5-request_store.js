#!/home/mubrik/.nvm/versions/node/v19.2.0/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode} ${response.statusMessage}`);
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    }
  });
});
