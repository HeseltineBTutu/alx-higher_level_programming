#!/usr/bin/node

const list = require('./100-data.js').list;
console.log(list);
const newList = list.map(function (element, index) {
  return element * index;
});
console.log(newList);
