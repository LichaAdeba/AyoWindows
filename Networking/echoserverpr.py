import socket 

host = "127.0.0.1"
port = 2369

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    conn, address= s.accept()
    with conn: 
        print(F"NEW CLIENT JOINED FROM {address} ")
        while True:
            data = conn.recv(1024)
            if not data:
                break;
            print(f"received data {data} from client")
            conn.sendall(data)