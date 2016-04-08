#!/usr/bin/env nodejs
var now = require('moment')(new Date()).format('MM/DD/YYYY HH:mm:ss');
var colorIndex = Math.floor(Math.random() * 17);
var colors = ['aqua','black','blue','fuchsia','gray','green','lime','maroon','navy',
           'olive', 'purple', 'red', 'silver', 'teal', 'white', 'yellow'];

var head =  'Content-Type: text/html\r\n\n' +
            '<!DOCTYPE html> <html> <head> <meta charset="UTF-8"><title>We code in our underpants</title>\n' +
            '</head><body style="background-color:' + colors[colorIndex] + ';">\n';
var footer = '</body>\n</html>';


process.stdout.write( head );
process.stdout.write( '<h1>Hello World from JavaScript @ ' + now + '<h1>\n') ;
process.stdout.write( footer );


