from Controller import Communication
from View import cliente 

def main():
	thr2 = cliente.GUI()
	thr2.start()
	print "GUI thread done"

if __name__ == '__main__':
		main()
