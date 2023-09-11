#!/usr/bin/node

const args = process.argv;
const x = args[2];
let i = 0;
if (x === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
