/*
Exercise 9 of 13

This problem is the same as the previous problem (HTTP COLLECT) in that you need to use http.get(). However, this time you will be provided with three URLs as the first three command-line arguments.

You must collect the complete content provided to you by each of the URLs and print it to the console (stdout). You don't need to print out the length, just the data as a String; one line per URL. The catch is that you must print them out in the same order as the URLs are provided to you as command-line arguments.
*/

var http = require('http');

var responses = [],
    index = 0;



(function httpGet(index){
  if (index < 3){

    http.get(process.argv[2 + index], function onGet(response){
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
        responses.push(collection);
        index += 1;
        httpGet(index);
      });
    });

  } else {
    // print results
    for (var line in responses) {
      console.log(responses[line]);
    }
  }
})(index);
