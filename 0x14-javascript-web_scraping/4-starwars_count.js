#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';
let count = 0;

request(apiUrl, function (err, response, body) {
    if (err) {
        console.log(err);
    } else {
        const results = JSON.parse(body);
        console.log(results);
    }
    });