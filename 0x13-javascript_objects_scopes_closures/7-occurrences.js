#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurCounter = 0;

  for (let idx = 0; idx < list.length; idx++) {
    if (list[idx] === searchElement) {
      occurCounter++;
    }
  }

  return occurCounter;
};
