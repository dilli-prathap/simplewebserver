# EX01 Developing a Simple Webserver
## Date:31-10-24

## AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
'''
from http.server import HTTPServer,BaseHTTPRequestHandler

content="""
<html>
    <head>
        <title>Specifications</title>
        </head>
        <body>
            <caption>LAPTOP SPECIFICATIONS</caption>
            <TABLE border="2" cellpadding="2">
                <tr>
                    <th>SYSTEM CONFIGURATION</th>
                    <th>DESCRIPTIONS</th>
                </tr>
                <TR>
                    <TD>RAM</TD>
                    <TD>16GB</TD>
                </TR>
                <TR>
                    <TD>PROCESSOR</TD>
                    <TD>13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</TD>
                </TR>
                <TR>
                    <TD>PEN & touch</TD>
                    <TD>No pen or touch input is available for this display</TD>
                </TR>
                <TR>
                    <TD>WINDOWS EDITION</TD>
                    <TD>Windows 11 Home Single Language</TD>
                </TR>
            </TABLE>
        </body>
</html>
"""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
'''

## OUTPUT:
![alt text](<Screenshot 2024-11-01 150805-2.png>)

![alt text](<Screenshot 2024-11-01 150849.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
