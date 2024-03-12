#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  // Increment the number
  number++;

  // Call the given function with the incremented number as argument
  theFunction(number);
}
module.exports.addMeMaybe = addMeMaybe;
