#!/usr/bin/node

const { argv } = require('node:process');
const arg1 = argv[2];
const parsedArg = parseInt(arg1);

if (!isNaN(parsedArg)) {
  if (parsedArg > 0) {
    let output = '';
    for (let i = 0; i < parsedArg; i++) {
      output += 'C is fun\n';
    }
    console.log(output.trim());
  }
} else {
  console.log('Missing number of occurrences');
}
