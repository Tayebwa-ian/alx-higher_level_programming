#!/usr/bin/node

function factorial (m) {
  if (m === 0) {
    return (0);
  } else if (m === 1) {
    return (1);
  }
  return (m * factorial(m - 1));
}
const argv = process.argv;
if (isNaN(Number(argv[2]))) {
  console.log(1);
} else {
  console.log(factorial(Number(argv[2])));
}
