#!/usr/local/bin/ruby
require "cgi"
require "./cgi-utils.rb"

cgi = CGI.new("html5")

color = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon",
         "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]
num = rand(color.length)
helloString = "<H1>Hello World from Ruby @ " + Time.now.to_s + "</H1>"

cgi.out {
  cgi.html("PRETTY" => " ") {
    html_head(color[num]) + helloString + "</BODY>"
  }
}
