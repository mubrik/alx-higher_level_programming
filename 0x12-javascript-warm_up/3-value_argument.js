#!/usr/bin/node
const args = process.argv.slice(2);

if (!args.some(elem =>  elem)) {
  console.log("No argument");
} else {
  console.log(args[0]);
}
