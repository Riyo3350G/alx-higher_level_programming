// JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (response) {
  $('DIV#character').text(response.name);
});
