#!/usr/bin/node

const Sq = require('./5-square.js');
class Square extends Sq {
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
