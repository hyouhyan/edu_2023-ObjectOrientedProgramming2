#!/usr/bin/env python
# coding:utf-8

import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html; charset=utf-8\n\n")
print("<html><h1>Hello, Python CGI!!</h1>")

form = cgi.FieldStorage() # リクエストパラメータの取得

print("<ol>")

for key in form:
    value = form[key].value
    print('<li>%s: %s</li>' % (key, value))

print("</ol>")
print("</html>")