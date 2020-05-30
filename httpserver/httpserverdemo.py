# coding: utf-8
"""
# Created by xudazhou at 2019/9/18
"""
import SimpleHTTPServer
import SocketServer
import logging
import urlparse
import subprocess
import os


class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_HEAD(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_HEAD(self)

    def do_GET(self):
        querypath = urlparse.urlparse(self.path)
        logging.info(querypath.path)
        logging.info(querypath.query)

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write("hello http server".encode())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(name)s %(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    p = subprocess.Popen(["D:\ProgramDev\Python27\python.exe", "D:\_python\TestPython27\subprocessdemo\hello3.py", str(os.getpid())])

    httpd = SocketServer.TCPServer(("", 9999), MyHandler)
    logging.info("Start Server ...")
    httpd.serve_forever()
    # 这会执行到这一句
    logging.info("------------------------- main end -------------------------------")
