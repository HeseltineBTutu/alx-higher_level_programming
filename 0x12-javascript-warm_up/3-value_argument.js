#!/usr/bin/node
const { argv } = require('node:process');

const firstArgument = argv[2];
if (firstArgument) {
  console.log(firstArgument);
} else {
  console.log('No argument');
}
