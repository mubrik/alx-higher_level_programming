#!/usr/bin/node
let counter = 0;

function logMe (item) {
  console.log(`${counter}: ${item}`);
  ++counter;
}

module.exports = {
  logMe
};
