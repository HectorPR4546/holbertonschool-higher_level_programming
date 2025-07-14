#!/usr/bin/node

function factorial(n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  if (n < 0) {
    return 1; // Factorial of negative numbers is not defined in this context, return 1 as per problem statement for NaN
  }
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);

console.log(factorial(num));
