#!/usr/bin/node

const { argv } = require('node:process');
const arg1 = argv[2];
const arg2 = argv[3];

function add (a, b) {
  return a + b;
}

const parsedArg1 = parseInt(arg1);
const parsedArg2 = parseInt(arg2);

if (!isNaN(parsedArg1) && !isNaN(parsedArg2)) {
  console.log(add(parsedArg1, parsedArg2));
} else {
  console.log('Arguments are not integers');
}
