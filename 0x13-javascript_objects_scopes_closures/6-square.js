#!/usr/bin/node

const SquareA = require('./5-square');

class Square extends SquareA {
  constructor (size) {
    super(size, size);
  }

  charPrint (char) {
    const _char = char ?? 'X';
    for (let index = 0; index < this.height; index++) {
      console.log(_char.repeat(this.width));
    }
  }
}

module.exports = Square;
