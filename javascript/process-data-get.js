#!/usr/bin/node

var cgi = require('./cgi.js');
var out = process.stdout, html = cgi.html, queryParser = cgi.query;

var qStr     = process.env.QUERY_STRING;
var queryVars = {};

if (qStr)
{
    queryVars = queryParser.parseQueryString(qStr);
}

out.write(html.contentType);
out.write(html.head);
out.write(html.body);

for (var i = 0; i < queryVars.magicnumber; ++i)
{
    out.write(`<h1>Hello ${queryVars.username} with a password of ${queryVars.userpassword}!</h1>`);
}

out.write(html.footer);