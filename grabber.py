from utils import timefunc

import socket

class Grabber:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))

    def read(self, length=1024):
        return self.socket.recv(length)

    def close(self):
        self.socket.close()

def main():
    grabber = Grabber('your local ip', 22)      # create the grabber
    print(grabber.read())                   # read the grabber
    grabber.close()                     # close the grabber




if __name__ == '__main__':
    main()
    
