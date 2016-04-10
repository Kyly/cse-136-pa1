#!/usr/local/bin/ruby
require "cgi"
cgi = CGI.new("html5")
cgi.out {
  cgi.html({"PRETTY" => " "}) {
    envServerVarsString = ""
    envBrowserVarsString = ""
    ENV.each {|key, value| 
      if key.match('^HTTP|^REQUEST')
        envBrowserVarsString.concat("<TR><TD>"+key+"</TD><TD>"+value+"</TD></TR>")
      else
        envServerVarsString.concat("<TR><TD>"+key+"</TD><TD>"+value+"</TD></TR>")
      end
    }
    "<HEAD><META charset='UTF-8'><TITLE>We code in our underpants</TITLE></HEAD>"+
    "<BODY><H1>Server</H1><TABLE><TR><TH>Name</TH><TH>Value</TH></TR>"+envServerVarsString+
    "</TABLE><H1>Client</H1><TABLE><TR><TH>Name</TH><TH>Value</TH></TR>"+envBrowserVarsString+
    "</TABLE></BODY>"
  }
}
