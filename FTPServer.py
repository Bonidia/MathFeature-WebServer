import os
import sys
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
path = os.path.dirname(os.path.abspath(__file__))

def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user test
    authorizer.add_user('mathfeature', '&l#t$L^Ex9BWHYGpZR', path + '/tmp/')
    # authorizer.add_user('mathfeature','&l#t$L^Ex9BWHYGpZR',
    #                     path + '/tmp/',perm='elradfmwMT')
    # authorizer.add_anonymous(os.getcwd())
    # ftp://mathfeature:%26l%23t%24L%5EEx9BWHYGpZR@localhost:2121/foutput

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "MathFeature"

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    # handler.masquerade_address = '151.25.42.11'
    handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('', 2121)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 20
    server.max_cons_per_ip = 20

    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()
