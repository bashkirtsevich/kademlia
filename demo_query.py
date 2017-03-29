from twisted.internet import reactor
from twisted.python import log
from network import Server
from utils import from_hex_to_byte
import sys

log.startLogging(sys.stdout)


def done(result):
    print "Found peers:", result
    reactor.stop()


def bootstrapDone(found, server, info_hash):
    if len(found) == 0:
        print "Could not connect to the bootstrap server."
        reactor.stop()
    else:
        print "Bootstrap completed"

        server.get_peers(info_hash).addCallback(done)


info_hash = from_hex_to_byte('f7bf674bd41c5a7affc8a61479d8968063fc609d')

server = Server(id=from_hex_to_byte('b481586aac12255d290fc575656dd31d67f765b8'))
server.listen(12346)
server.bootstrap([('67.215.246.10', 6881)]).addCallback(bootstrapDone, server, info_hash)

reactor.run()
