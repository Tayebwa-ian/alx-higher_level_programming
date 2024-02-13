#!/usr/bin/node

const oldlist = require('./100-data.js').list;
const newlist = oldlist.map((value, idx) => value * idx);
console.log(oldlist);
console.log(newlist);
