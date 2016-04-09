var _ = require('lodash');

function ProcessHeader() {
    this.server = [];
    this.http = [];
}

ProcessHeader.prototype.parseHeader = function (env) {

    var http = this.http;
    var server = this.server;

    if (!env) return;

    var keys = Object.keys(env).sort();

    keys.forEach(function(key) {

        var value = env[key];

        if (!value) return;

        if (key.startsWith('HTTP_') || key.startsWith('REQUEST_')) {
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

module.exports = new ProcessHeader();
