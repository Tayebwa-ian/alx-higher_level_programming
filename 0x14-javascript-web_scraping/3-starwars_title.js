#!/usr/bin/node

// fetch and use data from Star wars API
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const resource = url + process.argv.slice(2)[0];
request.get(resource, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    console.log(`${content.title}`);
  }
});
