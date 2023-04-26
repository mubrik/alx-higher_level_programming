#!/home/mubrik/.nvm/versions/node/v19.2.0/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode} ${response.statusMessage}`);
    return;
  }
  const todos = JSON.parse(body);
  const count = todos.reduce((prev, todo) => {
    if (todo.completed) {
      prev[`${todo.userId}`] = `${todo.userId}` in prev ? prev[`${todo.userId}`] + 1 : 1;
      return prev;
    }
    return prev;
  }, {});
  console.log(count);
});
