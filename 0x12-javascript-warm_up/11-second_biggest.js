#!/usr/bin/node

const argv = process.argv;
let largest, seclargest;
if (isNaN(Number(argv[2])) || argv.length === 3) {
  console.log(0);
} else {
  largest = argv[2];
  for (let i = 2; i < argv.length; i++) {
    if (argv[i] > largest) {
      seclargest = largest;
      largest = argv[i];
    }
  }
  console.log(seclargest);
}
