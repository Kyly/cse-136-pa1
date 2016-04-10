#!/usr/bin/node

var out = process.stdout;
var html = require('./cgi.js').html;
var now = require('moment')(new Date()).format('MM/DD/YYYY HH:mm:ss');
var colorIndex = Math.floor(Math.random() * 17);
var colors = ['aqua','black','blue','fuchsia','gray','green','lime','maroon','navy',
           'olive', 'purple', 'red', 'silver', 'teal', 'white', 'yellow'];

out.write(html.contentType);
out.write(html.head);
out.write( '<body style="background-color:' + colors[colorIndex] + ';">\n' );
out.write( '<h1>Hello World from JavaScript @ ' + now + '<h1>\n') ;
out.write(html.footer);


