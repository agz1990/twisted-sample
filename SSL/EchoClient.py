'''
Created on 

@author: jigc
'''

from twisted.internet import ssl, reactor
from twisted.internet.protocol import ClientFactory, Protocol

class EchoClient(Protocol):
    def connectionMade(self):
        print "hello, world"
        self.transport.write("hello, world")
        
    def dataReceived(self, data):
        print "Server said:" ,data
        self.transport.loseConnection()
        
class EchoClientFactory(ClientFactory):
    protocol = EchoClient
    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - gooodbye!"
    
    def clientConnectionLost(self, connector, reason):
        print "Connection lose - goodbye"

if __name__ == '__main__':
    factory = EchoClientFactory()
    reactor.connectSSL('127.0.0.1', 8000, factory, ssl.ClientContextFactory())
    reactor.run()
    pass