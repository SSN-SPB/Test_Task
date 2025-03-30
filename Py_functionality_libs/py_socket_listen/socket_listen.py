#!/usr/bin/env python3

import socket
import threading
host = 'localhost'
port = 50000
connectionSevered=0

class client(threading.Thread):
    def __init__(self, conn):
        super(client, self).__init__()
        self.conn = conn
        self.data = ""
    def run(self):
        while True:
            self.data = self.data + self.conn.recv(1024)
            if self.data.endswith(u"\r\n"):
                print self.data
                self.data = ""

    def send_msg(self,msg):
        self.conn.send(msg)

    def close(self):
        self.conn.close()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(5)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

print '[+] Listening for connections on port: {0}'.format(port)

