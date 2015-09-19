/*
Instead of transforming every line as in the previous "TRANSFORM" example,
for this challenge, convert even-numbered lines to upper-case and odd-numbered
lines to lower-case. Consider the first line to be odd-numbered. For example
given this input:

    One
    Two
    Three
    Four

Your program should output:

    one
    TWO
    three
    FOUR
*/

var through = require('through2'),
    split = require('split');

// create through stream with write and end functions
var lineCount = 0;
var transform = through(function (buffer, _, next) {
  var line = buffer.toString();
  if (lineCount % 2 === 1) {
    this.push(line.toUpperCase() + '\n');
  } else {
    this.push(line.toLowerCase() + '\n');
  }
  lineCount++;
  next();
});

process.stdin
  .pipe(split())
  .pipe(transform)
  .pipe(process.stdout);
