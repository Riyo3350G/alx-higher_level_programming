#!/usr/bin/node

const list = require('./100-data.js').list;

const mapList = list.map((v, i) => v * i);
console.log(list);
console.log(mapList);
