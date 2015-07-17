'''
Created on 

@author: jigc
'''

from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol

class EchoServer(DatagramProtocol):
    def datagramReceived(self, datagram, (host,port)):
        print "received %r from %s:%d" % (datagram, host, port)
        self.transport.write(datagram, (host,port))
        

if __name__ == '__main__':
    reactor.listenUDP(9999, EchoServer())
    reactor.run()
    pass