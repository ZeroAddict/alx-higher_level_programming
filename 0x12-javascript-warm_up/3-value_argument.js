#!/usr/bin/node
// prints the first valid arg passed to it

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
