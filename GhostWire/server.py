import socket
import threading
import json
from datetime import datetime

connected_clients = {}

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def load_users():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f)

def log_action(badge_number, action):
    try:
        with open('logs.json', 'r') as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []
    logs.append({
        "badge_number": badge_number,
        "action": action,
        "timestamp": get_current_time()
    })
    with open('logs.json', 'w') as f:
        json.dump(logs, f)

def handle_client(conn, addr):
    print(f'New connection from {addr}')
    try:
        credentials = conn.recv(1024).decode()
        action, data = credentials.split(':', 1)
        
        if action == 'LOGIN':
            badge_number, password = data.split(':')
            users = load_users()
            user = users.get(badge_number)
            if user and user['password'] == password:
                conn.send(f'AUTH_SUCCESS:{user["role"]}'.encode())
                connected_clients[badge_number] = conn
                log_action(badge_number, 'Logged in')
                print(f'{badge_number} logged in')
            else:
                conn.send('AUTH_FAIL'.encode())
                log_action(badge_number, 'Failed login attempt')
                conn.close()
                return

        elif action == 'REGISTER':
            name, password = data.split(':')
            users = load_users()
            badge_number = f"EMP-{str(len(users) + 1).zfill(3)}"
            users[badge_number] = {"name": name, "password": password, "role": "Employee"}
            save_users(users)
            conn.send(f'REGISTER_SUCCESS:{badge_number}'.encode())
            log_action(badge_number, 'Registered')
            print(f'New user registered: {badge_number}')

    except Exception as e:
        print(f'Error: {e}')
        conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5000))
server.listen()
print('GhostWire Server listening on port 5000...')

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()