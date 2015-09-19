/*
In this challenge, write an http server that uses a through stream to write back
the request stream as upper-cased response data for POST requests.
*/

var http = require('http'),
  through = require('through2');

var server = http.createServer(function (req, res) {
  req.pipe(res);
});

server.listen(process.argv[2]);
