#!/usr/bin/node

const { dict } = require('./101-data');

const userOccurrences = {};

// Iterate over the keys of the dict object
for (const userId in dict) {
  const occurrences = dict[userId];

  // If the occurrences count is not a key in userOccurrences, initialize it as an empty array
  if (!Object.prototype.hasOwnProperty.call(userOccurrences, occurrences)) {
    userOccurrences[occurrences] = [];
  }

  // Push the user id to the array corresponding to the occurrences count
  userOccurrences[occurrences].push(parseInt(userId));
}

console.log(userOccurrences);
