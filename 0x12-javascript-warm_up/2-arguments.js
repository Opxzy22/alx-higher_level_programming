#!/usr/bin/node

const arg_number = process.argv.length;
if (arg_number === 0) {
  console.log('No argument');
} else if (arg_number === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
