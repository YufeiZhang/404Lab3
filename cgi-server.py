#!/usr/bin/env python

# Copyright by Nick Zarczynski.
# I probabaly do not have permitin to post this on github 
# but I am going to using it in the lab

# https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/
# Retrieved date: Jan/19/2016
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/"]
 
httpd = server(server_address, handler)
httpd.serve_forever()