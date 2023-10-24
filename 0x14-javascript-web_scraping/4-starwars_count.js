#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';
let count = 0;

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.endsWith(characterId + '/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
