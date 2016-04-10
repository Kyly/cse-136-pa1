var _ = require('lodash');

var header = {
    server: [],
    http: []
};

var html = {
    contentType: 'Content-Type: text/html\r\n\n',
    head: '<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset="UTF-8">\n\t<title>We code in our underpants</title>\n</head>\n',
    body: '<body>',
    footer: '</body>\n</html>\n'
};

header.parseHeader = (env) => {

    var http   = header.http;
    var server = header.server;

    if (!env)
    {
        return;
    }

    var keys = Object.keys(env).sort();

    keys.forEach(function (key) {

        var value = env[key];

        if (!value)
        {
            return;
        }

        if (key.startsWith('HTTP_') || key.startsWith('REQUEST_') || key.startsWith('QUERY_'))
        {
            http.push([key, value]);
            return;
        }

        server.push([key, value]);
    });

    return {
        server: server,
        http: http
    };
};

var query = {};

query.parseQueryString = (qStr) => {
    var elements = qStr.split('&');
    var queryVars = elements.reduce((prev, curr) => {
        var s = curr.split('='); 

        prev[s[0]] = s[1];

        return prev;
    }, {});
    
    return queryVars;
};

query.getQueryStringObject = function (env) {

    header.parseHeader(env);
    var qStr = _.find(header.http, function(arr) {
        return arr[0] === 'QUERY_STRING';
    });

    if (!qStr) return;

    return parse.parseQueryString(qStr);
};

module.exports = {
    header: header,
    html: html,
    query: query
};
