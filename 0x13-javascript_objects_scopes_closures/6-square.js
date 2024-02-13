#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let ch = '';
      for (let j = 0; j < this.width; j++) {
        if (c) {
          ch += c;
        } else {
          ch += 'X';
        }
      }
      console.log(ch);
    }
  }
}
module.exports = Square;
