#!/usr/bin/env python
 
#importamos el modulo para trabajar con sockets
import socket
from threading import Thread
from Tkinter import *
import select


class Connection(Thread):
	def __init__(self):
		super(Connection, self).__init__()
		self.s = None
		
	def send(self, message):
		self.s.send(message)

	def disconnect(self):
		self.s.close()
		print "Adios"

	def run(self):
		self.s = socket.socket()
		self.s.connect(('192.168.0.98', 9999))		


class GUI(Thread):
	def __init__(self):
		super(GUI, self).__init__()
		self.thr1 = Connection()
		self.thr1.start()
		print "Client thread done"
		self.root = None

	def adelante(self, event):
		self.thr1.send('w')

	def atras(self, event):
		self.thr1.send('s')

	def izquierda(self, event):
		self.thr1.send('a')

	def derecha(self, event):
		self.thr1.send('d')

	def exit(self, event):
		self.thr1.send('close')
		self.thr1.disconnect()
		self.root.quit()

	def run(self):
		self.root = Tk()
		button1 = Button(None, text='adelante')
		button1.bind("<Button-1>", self.adelante)
		button1.pack()

		button2 = Button(None, text='atras')
		button2.bind("<Button-1>", self.atras)
		button2.pack()

		button3 = Button(None, text='izquierda')
		button3.bind("<Button-1>", self.izquierda)
		button3.pack()

		button4 = Button(None, text='derecha')
		button4.bind("<Button-1>", self.derecha)
		button4.pack()

		button5 = Button(None, text='salir')
		button5.bind("<Button-1>", self.exit)
		button5.pack()

		self.root.mainloop()


def main():

	thr2 = GUI()
	thr2.start()
	print "GUI thread done"

if __name__ == '__main__':
		main()



