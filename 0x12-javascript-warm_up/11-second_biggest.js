#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const int_list = process.argv.slice(2).map(Number).sort((a, b) => b - a);
  console.log(int_list[1]);
}
