#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(`${apiUrl}?format=json`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode} ${response.statusMessage}`);
    return;
  }
  const films = JSON.parse(body).results;
  const count = films.reduce((prev, film) => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${18}/`)) {
      return prev + 1;
    } else {
      return prev;
    }
  }, 0);
  console.log(count);
});
