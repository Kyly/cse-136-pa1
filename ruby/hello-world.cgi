#!/usr/bin/ruby
color = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]
num = rand(color.length)
print "Content Type: text/html\n\n"
print "<!DOCTYPE html>\n<html><body style='background-color:"+color[num]+"'>\n"
print "<p>Hello World from Ruby @ " + Time.now.to_s + "</p>"
print "</body>\n</html>"
