#!/usr/bin/node

const first_arg = process.argv[2];

if first_arg.length === undefined {
	console.log('No argument');
} else {
	console.log(first_arg);
}
