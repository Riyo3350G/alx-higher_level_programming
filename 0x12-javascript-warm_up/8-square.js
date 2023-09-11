#!/usr/bin/node

const args = process.argv;
const size = args[2];
let i = 0;

if (size === undefined || isNaN(size)) {
  console.log('Missing size');
} else {
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
}
