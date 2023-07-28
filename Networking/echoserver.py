import socket
host = '127.0.0.1'
port = 7777 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    conn, address = s.accept()
    with conn:
        print(f"new client joined from {address}")
        while True:
            data = conn.recv(1024)
            if not data:
                break;
            print(f"received {data} from client" )
            conn.sendall(data)