#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: nodescript {movie_id}');
}

const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(movieUrl, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const charactersList = JSON.parse(body).characters;

  printCharacter(charactersList, 0);
});

function printCharacter (charactersList, index) {
  if (index >= charactersList.length) {
    return;
  }

  request(charactersList[index], function (error, response, body) {
    if (error) {
      return console.log(error);
    }
    const character = JSON.parse(body).name;
    console.log(character);
    printCharacter(charactersList, index + 1);
  });
}
