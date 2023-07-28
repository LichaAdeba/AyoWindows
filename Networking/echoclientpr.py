import socket

host= "127.0.0.1"
port = 2369

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host,port))
    s.sendall(b"how are you today, kind sir")
    data = s.recv(1024)
print(f"received {data} from server")