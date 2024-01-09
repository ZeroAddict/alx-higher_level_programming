#!/usr/bin/node
// executes n times a function.

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
