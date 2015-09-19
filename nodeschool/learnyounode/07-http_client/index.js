/*
HTTP CLIENT
 Exercise 7 of 13

Write a program that performs an HTTP GET request to a URL provided to you as the first command-line argument. Write the String contents of each "data" event from the response to a new line on the console (stdout).
*/

var http = require('http'),
    url = process.argv[2];

// create http get request to url
var request = http.get(url, function onGet(response){
  // convert to string
  response.setEncoding('utf8');
  // whenever a chunk of data comes in, console.log it
  response.on('data', console.log);
  // catch any errors from response
  response.on('error', console.error);
});

// catch any errors on request
request.on('error', console.error);
