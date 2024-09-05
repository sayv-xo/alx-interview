#!/usr/bin/node
const request = require('request');

const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(movieUrl, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  if (response && response.statusCode !== 200) {
    return;
  }
  const charactersList = JSON.parse(body).characters;

  for (const character of charactersList) {
    printCharacter(character);
  }
});

function printCharacter (character) {
  request(character, function (error, response, body) {
    if (error) {
      return console.log(error);
    }
    if (response && response.statusCode !== 200) {
      return;
    }
    console.log(JSON.parse(body).name);
  });
}
