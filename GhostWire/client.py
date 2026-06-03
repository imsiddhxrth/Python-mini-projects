import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))
print('Connected to GhostWire!')

while True:
    msg = input('Enter message: ')
    if msg.lower() == 'exit':
        break
    client.send(msg.encode())

client.close()