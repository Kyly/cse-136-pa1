#!/usr/bin/env node

var now = Date.now();
var colorIndex = Math.floor(Math.random() * 17);
var colors = ['aqua','black','blue','fuchsia','gray','green','lime','maroon','navy',
           'olive', 'purple', 'red', 'silver', 'teal', 'white', 'yellow'];

var response = 'Content-Type: text/html\r\n\n' +
 '<!DOCTYPE html> <html> <head> <meta charset="UTF-8"><title>We code in our underpants</title>\n' +
 '</head> <body style="background-color:' + colors[colorIndex] + ';"">\n' +
 '<h1>Hello World from JavaScript @ ' + now + '<h1>\n' +
 '</body>\n' +
 '</html>';

process.stdout.write( response );
