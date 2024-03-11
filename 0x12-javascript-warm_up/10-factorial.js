#!/usr/bin/node

const { argv } = require('node:process');
const arg1 = argv[2];
const parsedArg = parseInt(arg1);

function factorial (parsedArg) {
  if (isNaN(parsedArg)) {
    return 1;
  }
  if (parsedArg === 0) {
    return 1;
  } else {
    return parsedArg * factorial(parsedArg - 1);
  }
}
console.log(factorial(parsedArg));
