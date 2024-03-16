#!/usr/bin/node

const { argv } = require('node:process');
const arg1 = argv[2];
const parsedArg = parseInt(arg1);

if (!isNaN(parsedArg)) {
  if (parsedArg > 0) {
    let output = '';
    for (let i = 0; i < parsedArg; i++) {
      for (let j = 0; j < parsedArg; j++) {
        output += 'X';
      }
      output += '\n';
    }
    console.log(output.trim());
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
