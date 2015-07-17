'''
Created on 

@author: jigc
'''

from twisted.internet import  reactor
from twisted.internet.protocol import DatagramProtocol

class EchoClient(DatagramProtocol):
    def startProtocol(self):
        host = "127.0.0.1"
        port = 1234
        
        self.transport.connect(host,port)
        print "now we can only sent to host %s port %d" % (host,port)
        self.transport.write("hello")
        
    def datagramReceived(self, datagram, (host,port)):
        print "received %r from %s:%d" % (datagram, host, port)
        
    def connectionRefused(self):
        print "No one listening"

if __name__ == '__main__':
    reactor.listenUDP(0, EchoClient())
    reactor.run()
    pass