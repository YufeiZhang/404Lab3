#!/usr/bin/env python

from __future__ import print_function

import sys, os, cgi

print("Blah!", file=sys.stderr)  # this is printed on terminal


''' This is the HTMP version '''
print("Content-type: text/html")# this is the header of a webpage
print("")

print("<HTML><BODY><FORM method='POST'> <INPUT name='x'>")
print("<br><br>Hello, this is the cgi script<br><br>") # this is what we print on web
print("I am process %i<br><br>" % os.getpid())


print(os.environ)

print("<br><br>")
form = cgi.FieldStorage()
print(form.getvalue('x'))

print("</FORM></BODY></HTML>")


''' This is the plain version '''
'''
print("Content-type: text/plain")# this is the header of a webpage
print("")

print("Hello, this is the cgi script\n") # this is what we print on web
print("I am process %i\n" % os.getpid())

print(os.environ)

print("")
form = cgi.FieldStorage()
print(form.getvalue('x'))
'''