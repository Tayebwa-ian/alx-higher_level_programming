#!/usr/bin/node

const olddict = require('./101-data.js').dict;
const newdict = {};
for (const key in olddict) {
  if (newdict[`${olddict[key]}`]) {
    newdict[`${olddict[key]}`].push(key);
  } else {
    newdict[`${olddict[key]}`] = [key];
  }
}
console.log(newdict);
