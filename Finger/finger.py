'''
Created on 

@author: jigc
'''

from twisted.internet import protocol, reactor, defer
from twisted.protocols.basic import LineReceiver


class FingerProtocol(LineReceiver):
    def lineReceived(self, line):
            d = self.factory.getUser(line)
            
            def onError(err):
                return 'Internal error in server'
            
            d.addErrback(onError)
            
            def writeResponse(message):
                self.transport.write(message + '\r\n')
                self.transport.loseConnection()
            
            d.addCallback(writeResponse)
            

class FingerFactory(protocol.Factory):
    protocol = FingerProtocol
    
    def __init__(self, **kwargs):
        self.users = kwargs
        
    def getUser(self, user):
        return defer.succeed(self.users.get(user, "No such user"))



if __name__ == '__main__':
    reactor.listenTCP(1079, FingerFactory(moshez='happy and well'))
    reactor.run()