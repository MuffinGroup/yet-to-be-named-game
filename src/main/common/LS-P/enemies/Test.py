import socket

s = socket.socket()

s.bind(('localhost', 1234))

s.listen(5)

while True:

  c, addr = s.accept()

  print ("Got connection from"), 
  addr

c.send("Thank you for connecting")

c.close()

