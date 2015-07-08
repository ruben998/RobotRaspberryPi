#!/usr/bin/env python
 
from threading import Thread
from Tkinter import *
from Controller import Communication

class GUI(Thread, Frame):
	def __init__(self, root = None):
		super(GUI, self).__init__()
		self.comm = Communication.accept()
		self.root = root

	def forward(self, event):
		self.comm.send('frwd')

	def back(self, event):
		self.comm.send('back')

	def left(self, event):
		self.comm.send('left')

	def right(self, event):
		self.comm.send('rght')

	def stop(self, event):
		self.comm.send('stop')

	def exit(self, event):
		self.comm.send('clse')
		self.comm.disconnect()
		self.root.quit()

	def run(self):
		self.root = Tk()
		forwardBtn  = Button(None, text='adelante')
		forwardBtn.bind("<Button-1>", self.forward)
		forwardBtn.pack()

		backBtn = Button(None, text='atras')
		backBtn.bind("<Button-1>", self.back)
		backBtn.pack()

		leftBtn = Button(None, text='izquierda')
		leftBtn.bind("<Button-1>", self.left)
		leftBtn.pack()

		rightBtn = Button(None, text='derecha')
		rightBtn.bind("<Button-1>", self.right)
		rightBtn.pack()

		stopBtn = Button(None, text = 'pausa')
		stopBtn.bind("<Button-1>", self.stop)
		stopBtn.pack()

		exitBtn = Button(None, text='salir')
		exitBtn.bind("<Button-1>", self.exit)
		exitBtn.pack()

		self.root.mainloop()



