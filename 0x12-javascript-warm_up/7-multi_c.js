#!/usr/bin/node
const args = process.argv.slice(2);

if (Number.isNaN(parseInt(args[0]))) {
  console.log("Missing number of occurrences");
  return;
}
const num = parseInt(args[0]);
let index = 0;
if (num > 0) {
  while (index < num) {
    console.log("C is fun");
    index++;
  }
}
