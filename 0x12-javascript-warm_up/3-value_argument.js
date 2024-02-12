#!/usr/bin/node

const argv = process.argv;
let len = 0;
argv.forEach((val, index) => len++);
if (len < 3) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
