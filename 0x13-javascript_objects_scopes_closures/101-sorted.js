#!/usr/bin/node


const data = require('./101-data.js');

const result = {};
const entries = data.dict;

for (const key in entries) {
  const occurrence = entries[key];

  if (result[occurrence] === undefined) {
    result[occurrence] = [key];
  } else {
    result[occurrence].push(key);
  }
}

console.log(result);
