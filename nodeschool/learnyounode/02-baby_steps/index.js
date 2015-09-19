/*
BABY STEPS
 Exercise 2 of 13

Write a program that accepts one or more numbers as command-line arguments and prints the sum of those numbers to the console (stdout).
*/

var args = process.argv;

var sum = 0;
// loop through args (starting at 2)
for (var i = 2; i < args.length; i++){
  // sum values (converted to ints)
  sum += +args[i];
}

console.log(sum);
