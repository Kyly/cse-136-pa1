#!/usr/bin/node

var out = process.stdout;
var cgi = require('./cgi.js');
var headers = cgi.header.parseHeader(process.env);
var html = cgi.html;

function printTable(arr) {
    out.write('<table><tr><th>Name</th><th>Value</th></tr>');
    arr.forEach(function(el) {
        out.write(`<tr>\n\t<td>${el[0]}</td>\n\t<td>${el[1]}</td>\n</tr>`);
    });
    out.write('</table>');
}

out.write(html.contentType);
out.write(html.head);
out.write(html.body);
out.write('<h1>Server</h1>');
printTable(headers.server);
out.write('<h1>Client</h1>');
printTable(headers.http);
out.write(html.footer);
