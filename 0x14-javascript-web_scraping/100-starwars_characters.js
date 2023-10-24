#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
    }
  }
});
