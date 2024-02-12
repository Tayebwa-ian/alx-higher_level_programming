#!/usr/bin/node

function add (a, b) {
  if (isNaN(Number(a)) || isNaN(Number(b))) {
    console.log('NaN');
  } else {
    const result = Number(a) + Number(b);
    console.log(result);
  }
}
const argv = process.argv;
add(argv[2], argv[3]);
