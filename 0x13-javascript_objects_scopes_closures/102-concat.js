#!/usr/bin/node

const fs = require('fs');
/* retrieving filenames from the command line */
const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];
const tA = fs.readFileSync(file1, 'utf8');
const tB = fs.readFileSync(file2, 'utf-8');
fs.writeFileSync(file3, tA + tB);
