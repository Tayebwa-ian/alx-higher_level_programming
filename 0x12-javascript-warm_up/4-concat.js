#!/usr/bin/node

const argv = process.argv;
let len = 0;
argv.forEach((val, index) => len++);
if (len < 3) {
  console.log('undefined is undefined');
} else if (len === 3) {
  console.log(`${argv[2]} is undefined`);
} else {
  console.log(`${argv[2]} is ${argv[3]}`);
}
