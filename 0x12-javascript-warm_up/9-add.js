#!/usr/bin/node
const args = process.argv.slice(2);

function add (a, b) {
  console.log(a + b);
}

add(parseInt(args[0]), parseInt(args[1]));
