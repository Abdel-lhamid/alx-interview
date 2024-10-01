#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (process.argv.length > 2){
	const movieId = process.argv[2];
	request(url, (error, response, body) => {
		if (error) {
			console.error('Error:', error);
		} else if (response.statusCode === 200) {
			const film = JSON.parse(body);
			const characters = film.characters;

			characters.forEach((characterUrl) => {
				request(characterUrl, (error, response, body) => {
					if (!error && response.statusCode === 200) {
						const character = JSON.parse(body);
						console.log(character.name);
					}
				});
			});
		} else {
			console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
		}
	})
};

