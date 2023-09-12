#!/usr/bin/node

const dict = require('./101-data.js');

const result = {};
const entries = dict.dict;

for (const key in entries) {
  const occurrence = entries[key];

  if (result[occurrence] === undefined) {
    result[occurrence] = [key];
  } else {
    result[occurrence].push(key);
  }
}

console.log(result);
