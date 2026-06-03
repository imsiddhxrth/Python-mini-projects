import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5000))
server.listen()
print('GhostWire Server listening')

conn, addr = server.accept()
print(f'Connected by {addr}')

msg = conn.recv(1024).decode()
print(f'Received: {msg}')
conn.close()