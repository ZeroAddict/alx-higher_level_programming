#!/usr/bin/node
// prints the addition of 2 integers and uses parseInt

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]));
