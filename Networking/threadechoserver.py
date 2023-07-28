import socket 
from threading import Thread
class ThreadEchoServer(Thread):
    def __init__(self, host, port):
        self.host = host 
        self.port = port 
    def setHost(self,host):
        self.host = host
    def getHost(self, host):
        return self. host
    def setPort(self, port):
        self.port = port 
    def getPort(self, port):
        return self.port
    def start(self):
        self.host= input('enter host: ' )
        self.port = input('enter port: ' )        
  
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    def Help():
        s.bind('(%s), %s '%(self.host.getHost(), self.port.getPort()))
    def start(self):
        self.Help()
    s.listen()
    conn, address= s.accept()
    with conn:
        print(f"new client joined from {address}")
        while True:
            data = conn.recv(1024)
            if not data:
                break;
            print(f"received {data} from client" )
            conn.sendall(data)
 #   def server(self):
  #      s.bind(('%s, %s')(self.host.getHost(), self.port.getPort()))
   # s.listen()
   # conn, address = s.accept()
    #with conn: 
     #   print(f'new client joined from {address}')
      #  while True:
       #     data = coonn.recv(1024)
        #    if not data:
         #       break;
          #  print(f'receive{data}from client')
            #conn.sendall(data)
