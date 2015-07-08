#!/usr/bin/env python
 
import socket
import RPi.GPIO as GPIO
import time
import thread

def adelante():
    stop()
    GPIO.output(11, True)
    GPIO.output(13, True)

def atras():
    stop()
    GPIO.output(15, True)
    GPIO.output(7, True)

def derecha():
    stop()
    GPIO.output(7, True)
    GPIO.output(13, True)

def izquierda():
    stop()
    GPIO.output(11, True)
    GPIO.output(15, True)

def stop():
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)

def menu(opcio):
    if opcio == 'w':
        adelante()
        return 0
    elif opcio == 's':
        atras()
        return 0
    elif opcio == 'a':
        izquierda()
        return 0
    elif opcio == 'd':
        derecha()
        return 0
    elif opcio == 'close':
        stop()
        return -1
    else:
        stop()
        return 0

def handler(clientsocket, clientaddr):
    while True:
	data = clientsocket.recv(1024)
	if not data:
	    break
	else:
	    menu(data)
    clientsocket.close()

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

    stop() 

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
    s.bind(("", 9999))
     
    s.listen(1)
    while True:
	sc, addr = s.accept()
	thread.start_new_thread(handler,(sc,addr))
main()
