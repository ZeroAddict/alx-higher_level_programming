#!/usr/bin/node
// prints the two arguments passed to it, in the following format: “ is ”
//uses isNaN & parseInt((process.argv[]))

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
