#!/usr/bin/node

const { argv } = require('node:process');
const arg1 = argv[2];
const parsedArg = parseInt(arg1);
const string1 = 'C is fun';
let newString = '';

if (!isNaN(parsedArg)) {
  if (parsedArg > 0) {
    for (let i = 0; i < parsedArg; i++) {
      newString += string1 + '\n';
    }
    console.log(newString.trim());
  } else {
    console.log('Missing number of occurrences');
  }
}
