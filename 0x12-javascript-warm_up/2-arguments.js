#!/usr/bin/node

const argNumber = process.argv.length;
if (argNumber === 2) {
  console.log('No argument');
} else if (argNumber === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
