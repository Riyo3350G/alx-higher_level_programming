#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
