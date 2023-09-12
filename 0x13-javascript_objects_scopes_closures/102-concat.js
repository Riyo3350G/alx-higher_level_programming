#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const distFile = process.argv[4];

const contentA = fs.readFileSync(fileA);
const contentB = fs.readFileSync(fileB);
fs.writeFile(distFile, contentA + contentB, 'utf-8', (err) => {
  if (err) {
    throw err;
  }
});
