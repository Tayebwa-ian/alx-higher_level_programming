#!/usr/bin/node

// Make an HTTP request with request module
const request = require('request');

const url = process.argv.slice(2)[0];
request
  .get(url)
  .on('response', (response) => {
    console.log(`code: ${response.statusCode}`);
  });
