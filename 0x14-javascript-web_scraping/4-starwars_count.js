#!/usr/bin/node

// fetch and use data from Star wars API
const request = require('request');

const url = process.argv.slice(2)[0];
request(url, (err, response, body) => {
  if (err) {
    console.log('An error occured. Status code: ' + response.statusCode);
  } else {
    const content = JSON.parse(body);
    const films = content.results;
    let count = 0;
    for (const i in films) {
      // collection of all film characters
      const cast = films[i].characters;
      for (const j in cast) {
        const id = cast[j].split('/')[5];
        if (id === '18') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
