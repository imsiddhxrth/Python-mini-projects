import socket
import threading

def handle_client(conn, addr):
    print(f'New connection from {addr}')
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f'Received from {addr}: {msg}')
        except:
            break
    conn.close()
    print(f'Connection closed from {addr}')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5000))
server.listen()
print('GhostWire Server listening on port 5000...')

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f'Active connections: {threading.active_count() - 1}')