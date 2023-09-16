#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  // Initialize a count variable to keep track of occurrences
  let count = 0;

  // Loop through the list
  for (let i = 0; i < list.length; i++) {
    // Check if the current element is equal to the search element
    if (list[i] === searchElement) {
      // If they are equal, increment the count
      count++;
    }
  }

  // Return the count of occurrences
  return count;
