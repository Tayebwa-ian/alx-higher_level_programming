#!/usr/bin/node

const argv = process.argv;
if (isNaN(Number(argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= Number(argv[2]); i++) {
    let ch = '';
    for (let j = 1; j <= Number(argv[2]); j++) {
      ch += 'X';
    }
    console.log(ch);
  }
}
