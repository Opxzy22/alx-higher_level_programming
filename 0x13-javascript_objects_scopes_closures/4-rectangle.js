#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
  }

  rotate () {
    const b = this.width;
    this.width = this.height;
    this.height = b;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
};
