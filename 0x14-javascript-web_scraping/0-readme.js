#!/usr/bin/node

// script that reads and prints the content of a file
const fs = require('fs');

const filename = process.argv.slice(2)[0];
fs.readFile(filename, 'utf-8', (e, output) => {
  if (e) {
    console.log(e);
  } else {
    console.log(output.toString());
  }
});
