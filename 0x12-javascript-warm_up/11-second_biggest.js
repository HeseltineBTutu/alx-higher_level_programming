#!/usr/bin/node

const { argv } = require('node:process');
const numbers = argv.slice(2).map(Number);

if (numbers.length < 2) {
  console.log('0');
} else {
  let firstBiggest = Number.NEGATIVE_INFINITY;
  let secondBiggest = Number.NEGATIVE_INFINITY;
  for (const num of numbers) {
    if (num > firstBiggest) {
      secondBiggest = firstBiggest;
      firstBiggest = num;
    } else if (num > secondBiggest && num !== firstBiggest) {
      secondBiggest = num;
    }
  }
  console.log(secondBiggest);
}
