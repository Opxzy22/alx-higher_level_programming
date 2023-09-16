#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

function add (a, b) {
  const num1 = parseFloat(a);
  const num2 = parseFloat(b);
  return num1 + num2;
}

const result = add(arg1, arg2);
console.log(result);
