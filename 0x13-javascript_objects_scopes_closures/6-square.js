#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (char) {
    const _char = char ? char : "X";
    for (let index = 0; index < this.height; index++) {
      console.log(_char.repeat(this.width));
    }
  }
}

module.exports = Square;
