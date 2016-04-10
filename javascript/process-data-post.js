#!/usr/bin/node

var cgi = require('./cgi.js');
var out = process.stdout;
var html = cgi.html, queryParser = cgi.query;

var inputStream = process.stdin
    , data = '';

process.stdin.resume();

inputStream.on('data', (chunk) => {
    data += chunk;
});

inputStream.on('end', () => {
    var queryVar = queryParser.parseQueryString(data);
    out.write(html.contentType);
    out.write(html.head);
    out.write(html.body);

    for (var i = 0; i < queryVar.magicnumber; ++i) {
        out.write(`<h1>Hello ${queryVar.username} with a password of ${queryVar.userpassword}!</h1>`);
    }

    out.write(html.footer);
});