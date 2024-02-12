#!/usr/bin/node

const lines = {
  first_line: 'C is fun',
  second_line: 'Python is cool',
  third_line: 'JavaScript is amazing'
};
for (const line in lines) {
  console.log(lines[line]);
}
