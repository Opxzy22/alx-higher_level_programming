#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      i += 1;
      for (let j = 0; j < this.width; j++) {
        row += 'x';
        j += 1;
      }
      console.log(row);
    }
  }
};
