#!/usr/bin/node

const argv = process.argv.map((el, _idx) => Number(el));
let largest, seclargest;
largest = argv[2];
seclargest = 0;
for (let i = 2; i < argv.length; i++) {
    if (argv[i] >= largest) {
	seclargest = largest;
	largest = argv[i];
	for (let j = 2; j < argv.length; j++) {
	    if (argv[j] > seclargest && argv[j] != argv[i]) {
		seclargest = argv[j];
	    }
	}
    }
}
console.log(seclargest);
