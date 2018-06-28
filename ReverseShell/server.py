import socket
import sys

'''
FUNCTIONS USED IN SERVER:
    socket()
    bind()
    listen()
    accept()
    read()
    write()
    close()
'''

#Create a Socket
#   Connect two computers
def create_socket():
    try:
        global host
        global port
        global s

        host = ''
        port = 9999 #UNCOMMON PORT - hence why we are using it
        s = socket.socket()
    except socket.error as msg:
        print ( 'Socket creation error: ' + str(msg))

#Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print( 'Binding the Port: ' + str(port) )

        s.bind((host,port))
        s.listen(5)
        
    except socket.error as msg:
        print ( 'Socket binding error: ' + str(msg)  + '\n' + 'Retrying ...')
        bind_socket()

# Establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept() #returns a connection object and a list of ip & port
    print ( 'Connection has been established! ')
    print ( 'IP: ' + address[0] )
    print ( 'Port: ' + str(address[1]) )
    send_commands(conn)
    conn.close()

#Send commands to Client
def send_commands(conn):
    while(1):
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.clost()
            sys.exit()
        #data transers in bytes, so switch type
        if len(str.encode(cmd) ) > 0: #check if user types something in
            conn.send( str.encode(cmd) )
            client_response = str( conn.recv(1024), 'utf-8' ) #convert byte to str
            print (client_response, end ='' )

def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
            
        
    
    
