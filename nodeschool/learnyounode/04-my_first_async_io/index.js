/*
MY FIRST ASYNC I/O!
 Exercise 4 of 13

Write a program that uses a single asynchronous filesystem operation to read a file and print the number of newlines it contains to the console (stdout), similar to running cat file | wc -l.

The full path to the file to read will be provided as the first command-line argument.
*/

var fs = require('fs'),
    file = process.argv[2];

// async read file and handle results in callback function
fs.readFile(file, 'utf8', function callback (err, data){

  if(!err){

    // split string by newline, and count
    var lines = data.split('\n').length - 1;

    console.log(lines);
  }
});
