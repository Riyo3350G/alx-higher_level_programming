#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    const charIndex = 0;

    function fetchChar (charIndex) {
      if (charIndex < characters.length) {
        request(characters[charIndex], function (err, response, body) {
          if (err) {
            console.log(err);
          } else {
            const name = JSON.parse(body).name;
            console.log(name);
            fetchChar(charIndex + 1); // Fetch the next character
          }
        });
      }
    }

    fetchChar(charIndex);
  }
});
