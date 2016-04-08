#!C:\Program Files\nodejs\node.exe

var sys=require("sys");

var date = new Date();
var hour = date.getHours();
    hour = (hour < 10 ? "0" : "") + hour;

    var min  = date.getMinutes();
    min = (min < 10 ? "0" : "") + min;

    var sec  = date.getSeconds();
    sec = (sec < 10 ? "0" : "") + sec;

    var year = date.getFullYear();

    var month = date.getMonth() + 1;
    month = (month < 10 ? "0" : "") + month;

    var day  = date.getDate();
    day = (day < 10 ? "0" : "") + day;


var colors = new Array(16);
colors[0] = "aqua";
colors[1] = "black";
colors[2] = "blue";
colors[3] = "fuchsia";
colors[4] = "gray";
colors[5] = "green";
colors[6] = "lime";
colors[7] = "maroon";
colors[8] = "navy";
colors[9] = "olive";
colors[10] = "purple";
colors[11] = "red";
colors[12] = "silver";
colors[13] = "teal";
colors[14] = "white";
colors[15] = "yellow";

var randomint = Math.floor(Math.random() * (16) + 1);
var color = colors[randomint-1].toString();

sys.puts("Content-type: text/html\n");

sys.puts("<!DOCTYPE html> <html> <head> <meta charset='UTF-8'><title>We code in our underpants</title>\n");
sys.puts("</head>\n");
sys.puts("<body bgcolor=\""+color+"\">\n");
sys.puts("Hello World from node @"+year + ":" + month + ":" + day + ":" + hour + ":" + min + ":" + sec+"<br/>\n");
sys.puts("</body>\n");
sys.puts("</html>\n");
