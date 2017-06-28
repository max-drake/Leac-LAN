import socket
from threading import Thread
import time


class SimpleClient:
    # change localhost to ip address for server
    def __init__(self, host="192.186.0.123", port=12345):  
        self.host = host
        self.port = port
        self.message_received = "NONE"

    def get_message(self, timeout=None):
        self.s = socket.socket()         # Create a socket object
        if timeout != None:
            self.s.settimeout(timeout)
        try:
            self.s.connect((self.host, self.port))
        except:
            print "could not connect to %s:%s. Is broadcaster running?" % \
                    (self.host, self.port)
            return
        self.message_received = self.s.recv(1024)
        self.s.close                     # Close the socket when done
        return self.message_received


class SimpleServer:
    def __init__(self, port=12345, threading=False):
        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(("", port))
        self.s.listen(5)
        self.msg = "Not Ready"
        self.stop_broadcast = False
        self.threading = threading

        if self.threading:
            self.t = Thread(target=self.threaded_broadcast)
            self.t.start()

    def update_broadcast(self, msg):
        print "UPDATING msg from", self.msg, "to", msg
        self.msg = msg

    def threaded_broadcast(self):
        while not self.stop_broadcast:
            c, addr = self.s.accept()
            c.send(self.msg)
            c.close()
        print "done send"

    def broadcast(self, msg):
        c, addr = self.s.accept()
        c.send(msg)
        c.close()


if __name__ == "__main__":

    server_type = raw_input("For Broadcaster input B for Listener  input L\n")
    if server_type == "B":
        broadcaster = SimpleServer()
        while True:
            msg = raw_input("Enter text you want to broadcast: ")
            broadcaster.broadcast(msg)
    else:
        listener = SimpleClient()
        while True:
            msg = listener.get_message()
            if msg == None:
                time.sleep(1)
            else:
                print"listening message is: %s " % msg
