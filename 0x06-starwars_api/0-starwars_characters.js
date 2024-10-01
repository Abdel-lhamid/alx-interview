#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (process.argv.length > 2){
	const movieId = process.argv[2];
	request(url, (error, response, body) => {
		if (error) {
			console.log(err);
		}
		const charactersURL = JSON.parse(body).characters;
		const charactersName = charactersURL.map(
			url => new Promise((resolve, reject) => {
				request(url, (promiseErr, __, charactersReqBody) => {
					if (promiseErr) {
						reject(promiseErr);
					}
					resolve(JSON.parse(charactersReqBody).name);
				});
			}));

		Promise.all(charactersName)
			.then(names => console.log(names.join('\n')))
			.catch(allErr => console.log(allErr));
	});
}
