#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const title = JSON.parse(body).title;
    console.log(title);
  }
});
