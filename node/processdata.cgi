#!C:\Program Files\nodejs\node.exe

var sys=require("sys");

sys.puts("Content-type: text/html\n");

sys.puts("<!DOCTYPE html> <html> <head> <meta charset='UTF-8'><title>We code in our underpants</title>\n");
sys.puts("</head>\n");
sys.puts("<body bgcolor=\"white\">\n");

var variable = "";
var value = "";
var i = 0;
var l = new Array(10);

for(var key in form.keys()){
	variable = key.toString();
	l[0] = 	form.getvalue(variable).toString();
	i ++;
}

var username = l[0];
var password = l[1];
var magicnumber = l[2];

while(magicnumber != 0){
	sys.puts("<h1>Hello " + str(username) +" with a password of " + str(password) + " !</h1>\n");
	magicnumber = magicnumber -1;

sys.puts("</body>\n");
sys.puts("</html>\n");