#!/usr/bin/node

// script writes to a file
const fs = require('fs');

const filename = process.argv.slice(2)[0];
const input = process.argv.slice(2)[1];
fs.writeFile(filename, input, (e) => {
  if (e) {
    console.log(e);
  }
});
