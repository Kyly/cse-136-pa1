#!/usr/bin/env python

import os
env_vars = os.environ.data

print "Content-Type: text/html"
print

print "<!DOCTYPE html> <html> <head> <meta charset='UTF-8'><title>We code in our underpants</title>"
print "<style>" 
print "table, th, td { border: 1px solid black; border-collapse: collapse; }"
print "th, td { padding: 5px; }"
print "</style>"

print "</head> <body style='background-color:" + "white" + "'>"
sorted_env_vars = sorted(env_vars.items())

print "<h1>ENVIRONMENT VARIABLES</h1> <br><br>"

# Browser Vars
print "<h2>BROWSER VARIABLES</h2>"
print "<table>"
print "<tr><th>ENVIRONMENT VARIABLE NAME</th><th>VALUE</th></tr>"
for var in sorted_env_vars:
    if "HTTP" in var[0]:
        print "<tr><td>" + var[0] + "</td><td>" + var[1] + "</td></tr>"
print "</table>"
print "<br><br>"

# Server Vars
print "<h2>SERVER VARIABLES</h2>"
print "<table>"
print "<tr><th>ENVIRONMENT VARIABLE NAME</th><th>VALUE</th></tr>"
for var in sorted_env_vars:
    if "HTTP" not in var[0]:
        print "<tr><td>" + var[0] + "</td><td>" + var[1] + "</td></tr>"

print "</table>"
print "<br><br>"
print "</body>"
print "</html>"
