import socket 
class ThreadEchoClient(object):
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
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    def host(self):
        self.host= input('enter host: ')
        self.port = input('enter port: ')
    def client(self):
        s.connect(('%s, %s')(self.host.getHost(), self.port.getPort()))
        s.sendall((b'How is this wonderful day'))
    data = s.recv(1024)
    print(f"received {data} from server")
    self.host()
    self.cient()
