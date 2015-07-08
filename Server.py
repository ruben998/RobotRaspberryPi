#!/usr/bin/env python

## Imports ## 
import socket
import thread
import MovesServer



def menu(opcio):
    if opcio == 'frwd':
        moves.forward()
    elif opcio == 'back':
        moves.back()
    elif opcio == 'left':
        moves.left()
    elif opcio == 'rght':
        moves.right()
    elif opcio== 'stop':
	   moves.stop()
    elif opcio == 'clse':
        moves.stop()
    else:
        moves.stop()

def handler(clientsocket, clientaddr):
    while True:
	data = clientsocket.recv(1024)
	if not data:
	    break
	else:
	    menu(data)
    clientsocket.close()

def main():
    moves = MovesServer()

    stop() 

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
    s.bind(("", 9999))
     
    s.listen(1)
    while True:
    	sc, addr = s.accept()
    	thread.start_new_thread(handler,(sc,addr))
main()
