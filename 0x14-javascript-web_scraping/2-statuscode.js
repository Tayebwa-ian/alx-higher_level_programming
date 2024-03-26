#!/usr/bin/node

// Make an HTTP request with request module
const request = require('request');

const url = process.argv.slice(2)[0];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
