#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

html = """
<html>
    <head>
        <title>Hello my world</title>
    </head>
    <body>
        <h2>Hello Word! This is my first CGI program - dude</h2>
"""

tab = "<table><tr><th>ID</th><th>SQUARE</th><th>CUBE</th></tr>"

for  i in range(0,50):
    tab += "<tr><td>%d</td><td>%d</td><td>%d</td></tr>"%(i,i**2,i**3)

tab += "</table>"

html += tab
html += "</body></html>"

print(html)