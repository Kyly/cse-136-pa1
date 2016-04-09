#!/usr/bin/env node
var out = process.stdout;
var headers = require('./processHeader.js').parseHeader(process.env);
var head =  'Content-Type: text/html\r\n\n' +
    '<!DOCTYPE html> <html> <head> <meta charset="UTF-8"><title>We code in our underpants</title>\n' +
    '</head><body>\n';
var footer = '</body>\n</html>\n';

function printTable(arr) {
    out.write('<table><tr><th>Name</th><th>Value</th></tr>');
    arr.forEach(function(el) {
        out.write('<tr>');
        out.write('<td>' + el[0] + '</td><td>' + el[1] + '</td>');
        out.write('</tr>');
    });
    out.write('</table>');

}

out.write( head );
out.write('<h1>Server</h1>');
printTable(headers.server);
out.write('<h1>Client</h1>');
printTable(headers.http);
out.write( footer );
