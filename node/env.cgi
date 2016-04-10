#!C:\Program Files\nodejs\node.exe

var sys=require("sys");
sys.puts("Content-type: text/html\n");
var argstr="";
for(var i in process.env){
  argstr+=i+": " + process.env[i] + "<br/>\n";
}
sys.puts("Environment Variables<br/>\n");
sys.puts(argstr +"<br/>\n");