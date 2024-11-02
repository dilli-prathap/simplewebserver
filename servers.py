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