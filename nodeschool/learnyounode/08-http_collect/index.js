/*
HTTP COLLECT
Exercise 8 of 13

Write a program that performs an HTTP GET request to a URL provided to you as the first command-line argument. Collect all data from the server (not just the first "data" event) and then write two lines to the console (stdout).

The first line you write should just be an integer representing the number of characters received from the server. The second line should contain the complete String of characters sent by the server.
*/

var http = require('http'),
    url = process.argv[2];

// create http get request to url
var request = http.get(url, function onGet(response){
  var collection = [];

  // convert to string
  response.setEncoding('utf8');

  // whenever a chunk of data comes in, console.log it
  response.on('data', function onData(data){
    collection.push(data);
  });

  // when completed, output # and string of chars
  response.on('end', function onEnd(){
    collection = collection.join('');
    console.log(collection.length);
    console.log(collection);
  });


  // catch any errors from response
  response.on('error', console.error);
});

// catch any errors on request
request.on('error', console.error);
