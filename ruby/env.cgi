#!/usr/local/bin/ruby
require "cgi"
cgi = CGI.new("html5")
cgi.out {
  cgi.html({"PRETTY" => " "}) {
    envBrowserVars = {}
    envServerVars = {}
    envServerVarsString = ""
    envBrowserVarsString = ""
    ENV.each {|key, value| 
      print key + " "
      if key.match('^HTTP|^REQUEST')
        envBrowserVars[key] = value
      else
        envServerVars[key] = value
      end
    }
    envServerVars.each {|var, value|
      envServerVarsString.concat("<TR><TD>"+var+"</TD><TD>"+value+"</TD></TR>")
    }
    envBrowserVars.each {|var, value|
      envBrowserVarsString.concat("<TR><TD>"+var+"</TD><TD>"+value+"</TD></TR>")
    }
    "<HEAD><META charset='UTF-8'><TITLE>We code in our underpants</TITLE></HEAD>"+
    "<BODY><H1>Server</H1><TABLE><TR><TH>Name</TH><TH>Value</TH></TR>"+envServerVarsString+
    "</TABLE><H1>Client</H1><TABLE><TR><TH>Name</TH><TH>Value</TH></TR>"+
    envBrowserVarsString
  }
}
