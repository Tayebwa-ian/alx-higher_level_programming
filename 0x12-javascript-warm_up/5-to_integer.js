#!/usr/bin/node

const argv = process.argv;
let len = 0;
argv.forEach((val, index) => len++);
if (len < 3) {
  console.log('Not a number');
} else if (isNaN(Number(argv[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Number(argv[2])}`);
}
