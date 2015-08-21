var fs = require('fs'),
    path = require('path');

function lsfilter(dir, ext, callback){
  fs.readdir(dir, function readdir_CB(err, list){
    // catch any errors from readdir
    if (err)
      return callback(err);

    // filter through list by ext name
    list = list.filter(function filter_CB(file){
      return path.extname(file) == '.' + ext;
    });

    // call callback function with list and null error 
    callback(err, list);
  });
}

module.exports = lsfilter;
