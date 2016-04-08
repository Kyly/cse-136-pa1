#!/usr/bin/env python

import datetime
import random


now = datetime.datetime.now()

rand_int = random.randint(1,17)
colors = { 1:"aqua", 2:"black", 3:"blue", 4:"fuchsia", 5:"gray", 6:"green", 7:"lime", 8:"maroon", 9:"navy",
           10:"olive", 11:"purple", 12:"red", 13:"silver", 14:"teal", 15:"white", 16:"yellow"}
 
color = ""
if rand_int == 1:
	color = "aqua"
if rand_int == 2:
	color = "black"
if rand_int == 3:
	color = "blue"
if rand_int == 4:
	color = "fuchsia"
if rand_int == 5:
	color = "gray"
if rand_int == 6:
	color = "green"
if rand_int == 7:
	color = "lime"
if rand_int == 8:
	color = "maroon"
if rand_int == 9:
	color = "navy"
if rand_int == 10:
	color = "olive"
if rand_int == 11:
	color = "purple"
if rand_int == 12:
	color = "red"
if rand_int == 13:
	color = "silver"
if rand_int == 14:
	color = "teal"
if rand_int == 15:
	color = "white"
if rand_int == 16:
	color = "yellow"


print "Content-Type: text/html"
print
print "<!DOCTYPE html> <html> <head> <meta charset='UTF-8'><title>We code in our underpants</title>"
print "</head> <body style='background-color:" + str(color) + "'>"
print "<h1>Hello World from Python @ " + str(now) + "<h1>"
print "</body>"
print "</html>"
