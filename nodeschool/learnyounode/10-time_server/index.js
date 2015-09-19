/*
TIME SERVER
 Exercise 10 of 13

Write a TCP time server!

Your server should listen to TCP connections on the port provided by the first argument to your program. For each connection you must write the current date & 24 hour time in the format:

    "YYYY-MM-DD hh:mm"

followed by a newline character. Month, day, hour and minute must be zero-filled to 2 integers. For example:

    "2013-07-06 17:42"
*/

var net = require('net'),
    port = process.argv[2];

// start server
var server = net.createServer(function(socket){

  // write current date & time
  var date = new Date(),
      year = date.getFullYear(),
      month = ('0' + (date.getMonth() + 1)).slice(-2),
      day = ('0' + date.getDate()).slice(-2),
      hour = ('0' + date.getHours()).slice(-2),
      min = ('0' + date.getMinutes()).slice(-2),
      data = year + '-' + month + '-' + day + ' ' + hour + ':' + min;

  // write data
  socket.end(data);
  console.log(); // endline
});
server.listen(port);
