#!/usr/bin/node

const dict = require('./101-data.js').dict;

console.log(
  Object.entries(dict).reduce((prev, curr) => {
    const [key, val] = curr;
    if (prev[val]) {
      prev[val].push(key);
    } else {
      prev[val] = [key];
    }
    return prev;
  }, {})
);
