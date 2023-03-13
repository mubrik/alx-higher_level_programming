#!/usr/bin/node
const args = process.argv.slice(2);

if (Number.isNaN(parseInt(args[0]))) {
  console.log('Missing size');
} else {
  const num = parseInt(args[0]);
  let col = 0;
  if (num > 0) {
    while (col < num) {
      console.log('X'.repeat(num));
      col++;
    }
  }
}
