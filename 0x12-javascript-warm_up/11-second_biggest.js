#!/usr/bin/node

const args = process.argv;
const argv = args.slice(2).map((el, _idx) => Number(el));
let largest, seclargest;
largest = argv[0];
seclargest = 0;
for (let i = 0; i < argv.length; i++) {
  if (argv[i] >= largest && argv.length > 1) {
    if (argv[i] !== largest) {
      seclargest = largest;
    }
    largest = argv[i];
    for (let j = 0; j < argv.length; j++) {
      if (argv[j] > seclargest && argv[j] !==
          argv[i]) {
        seclargest = argv[j];
      }
    }
  }
}
console.log(seclargest);
