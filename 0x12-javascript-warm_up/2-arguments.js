#!/usr/bin/node

const arg_number = process.argv.length;
if (arg_number === 2) {
  console.log('No argument');
} else if (arg_number === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
