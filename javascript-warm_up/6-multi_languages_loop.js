#!/usr/bin/node

const languages = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

let output = '';
for (const lang of languages) {
  output += lang + '\n';
}

console.log(output.trimEnd());
