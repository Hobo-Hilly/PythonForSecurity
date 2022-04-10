




# Justin, if you are reading this awesome! Thank you :) ok so here is what the contents of sniffer.py are on my local machine at home. It says I have an error in nettype.py. I have left the contents of nettype.py in here as well. Any tips would be greatly appreciated. Thank you!

┌──(kali㉿kali)-[~/myrepo]
└─$ cat nettypes.py 
import socket
from struct import unpack

def mac_addr(bytestring):
    return ":".join('{:02x}'.format(piece) for piece in bytestring).upper()


class EthernetFrame:
    length = 14 
    def __init__(self, data):
        unpacked_data = unpack('!6s6sH', data[0:self.length])
        self.protocol = socket.ntohs(unpacked_data([2])
        self.destination = mac_addr(data[0:6])
        self.source = mac_addr(data[6:12])
        self.leftover_data = data[self.length:

    def __str__(self):
    return """ 
        Source:         {source}
        Destination:    {destination}
        Protocol:       {protocol}
    """.format(**self.__dict__)



--------------------------------------------------------------------
SNIFFER.PY


┌──(kali㉿kali)-[~/myrepo]
└─$ cat sniffer.py 

import socket
from capture import PCAPFile
from nettypes import EthernetFrame


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    #pcap = PCAPFile('packets.pcap')
    while True:
        raw_data, addr = conn.recvfrom(65535)
        ethframe = EthernetFrame(raw_data)
        print(ethframe)
        #pcap.write(raw_data)
    #pcap.close()


if __name__ == '__main__':
    main()




-----------------------------------------------------------
Result after running command



┌──(kali㉿kali)-[~/myrepo]
└─$ python3 sniffer.py       
Traceback (most recent call last):
  File "/home/kali/myrepo/sniffer.py", line 4, in <module>
    from nettypes import EthernetFrame
  File "/home/kali/myrepo/nettypes.py", line 13
    self.destination = mac_addr(data[0:6])
    ^
SyntaxError: invalid syntax
