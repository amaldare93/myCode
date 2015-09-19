/*
You will be given text on process.stdin. Buffer the text and reverse it using
the `concat-stream` module before writing it to stdout.
*/

var concat = require('concat-stream');

process.stdin
  .pipe(concat(function(buffer){
    var stream = buffer.toString().split('').reverse().join('');
    console.log(stream);
  }));
