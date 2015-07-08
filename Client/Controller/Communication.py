import socket
from threading import Thread

class Connection(Thread):
	def __init__(self, s = None):
		super(Connection, self).__init__()
		self.s = s
		
	def send(self, message):
		self.s.send(message)

	def disconnect(self):
		self.s.close()
		
	def run(self):
		self.s = socket.socket()
		self.s.connect(('192.168.0.98', 9999))

def accept():
	thr1 = Connection()
	thr1.start()
	print "Client thread done"
	return thr1

if __name__ == '__main__':
		accept()