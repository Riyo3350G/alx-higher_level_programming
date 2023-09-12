#!/usr/bin/node

const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let idx = 0; idx < this.height; idx++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
