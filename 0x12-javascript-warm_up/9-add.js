#!/usr/bin/node

const { argv } = require('node:process');
const arg1 = argv[2];
const arg2 = argv[3];

function add (a, b) {
  return a + b;
}
console.log(add(parseInt(arg1), parseInt(arg2)));
