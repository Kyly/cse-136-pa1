#!/usr/bin/env python

import os

print "Content-Type: text/html"
print

print "Content-Type: text/html"
print
print "<!DOCTYPE html> <html> <head> <meta charset='UTF-8'><title>We code in our underpants</title>"
print "</head> <body style='background-color:" + "white" + "'>"
for key in os.environ.keys():
    print "<h3>%30s %s </h3>\n" % (key,os.environ[key])
print "</body>"
print "</html>"
