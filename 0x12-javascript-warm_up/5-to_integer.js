#!/usr/bin/node
const { argv } = require('node:process');
const arg1 = argv[2];
const parsedArg = parseInt(arg1);

if (!isNaN(parsedArg)) {
  console.log('My number:', parsedArg);
} else {
  console.log('Not a number');
}
