/*
Convert data from `process.stdin` to upper-case data on `process.stdout`
using the `through2` module.
*/

var through = require('through2');

// create through stream with write and end functions
var stream = through(function write(buffer, encoding, next) {
  this.push(buffer.toString().toUpperCase());
  next();
});

process.stdin.pipe(stream).pipe(process.stdout);
