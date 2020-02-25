import socket
import sys
import threading
import time
import sys

def rs():
    try:
        rss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    server_binding = ('', int(sys.argv[1]))
    ss.bind(server_binding)
    
    rss.close()

if __name__ == "__main__":
