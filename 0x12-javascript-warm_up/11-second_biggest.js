#!/usr/bin/node

const argv = process.argv;
let largest, seclargest;
largest = argv[2];
seclargest = 0;
for (let i = 2; i < argv.length; i++) {
  if (argv[i] > largest) {
    seclargest = largest;
    largest = argv[i];
  } else if (argv[i] > seclargest) {
    seclargest = argv[i];
  }
}
console.log(seclargest);
