#!/usr/bin/node

const argv = process.argv;
let len = 0;
argv.forEach((val, index) => len++);
if (len < 3) {
  console.log('Missing number of occurrences');
} else if (isNaN(Number(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(argv[2]); i++) {
    console.log('C is fun');
  }
}
