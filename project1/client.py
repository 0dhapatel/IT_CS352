import socket
import sys
import threading
import time

def client_to_ts(hn, tshn): # giving hostname to ts
    try:
        ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
    
    #ts port number
    tspn=int(sys.argv[3])
    #ts hostname
    tsh=socket.gethostbyname(tshn)
    
    ts.close()

def client_to_rs(hn): # giving hostname to rs
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
    
    #rs port number
    rspn=int(sys.argv[2])
    #rs hostname
    rsh=socket.gethostbyname(sys.argv[1])
    
    rs.close()
    

if __name__=='__main__':
    # save from file PROJI-HNS.txt to data structure
    
    #connect to rs machine
    client_to_rs(gh) #given hostname
