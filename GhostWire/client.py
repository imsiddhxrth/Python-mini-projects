import json
import socket
import threading
from getpass import getpass


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))
print('Connected to GhostWire!')

def encrypt(msg):
    keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=~`[]{}|;:,.<>?'
    values = keys[-1] + keys[0:-1]
    dict_encode = dict(zip(keys, values))
    msg = msg.replace(' ', '_')
    return ''.join([dict_encode.get(char, char) for char in msg])

def decrypt(msg):
    keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=~`[]{}|;:,.<>?'
    values = keys[-1] + keys[0:-1]
    dict_decode = dict(zip(values, keys))
    return ''.join([dict_decode.get(char, char) for char in msg]).replace('_', ' ')

def send_messages():
    while True:
        recipient = input('Send to (or exit): ')
        if recipient.lower() == 'exit':
            break
        message = input('Message: ')
        encrypted_message = encrypt(message)
        client.send(f'MSG:{recipient}:{encrypted_message}'.encode())

def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg.startswith('FROM:'):
                _, sender, message = msg.split(':', 2)
                decrypted_message = decrypt(message)
                print(f'\nMessage from {sender}: {decrypted_message}')
            elif msg.startswith('BROADCAST:'):
                message = msg.split(':', 1)[1]
                print(f'BROADCAST FROM ADMIN: {message}')
            elif msg.startswith('PRIVATE_FROM:'):
                _, sender, message = msg.split(':', 2)
                print(f'{sender}: {message}')
            else:
                print(f'\n{msg}')
        except:
            print('Connection lost.')
            break

def admin_commands():
    while True:
        print('\nAdmin Commands:')
        print('1. List Online Users')
        print('2. Broadcast Message')
        print('3. Send Private Message')
        print('4. Kick User')
        print('5. View Logs')
        print('6. Exit')
        cmd = input('> ')
        if cmd == '1' or cmd.lower() == 'list online users':
            client.send('ADMIN_CMD:LIST_USERS'.encode())
            response = client.recv(1024).decode()
            users = response.split(':')[1].split(',')
            print('Online users:', users)
        elif cmd == '2' or cmd.lower() == 'broadcast message':
            message = input('Enter broadcast message (or exit): ')
            if message.lower() == 'exit':
                continue
            client.send(f'ADMIN_CMD:BROADCAST:{message}'.encode())
            response = client.recv(1024).decode()
            print('Broadcast sent!')
        elif cmd == '3' or cmd.lower() == 'send private message':
            recipient = input('Enter badge number (or exit): ')
            if recipient.lower() == 'exit':
                continue
            message = input('Message: ')
            client.send(f'ADMIN_CMD:PRIVATE_MSG:{recipient}:{message}'.encode())
            response = client.recv(1024).decode()
            print(response)
        elif cmd == '4' or cmd.lower() == 'kick user':
            target = input('Enter badge number to kick (or exit): ')
            if target.lower() == 'exit':
                continue
            client.send(f'ADMIN_CMD:KICK:{target}'.encode())
            response = client.recv(1024).decode()
            print(response)
        elif cmd == '5' or cmd.lower() == 'view logs':
            client.send('ADMIN_CMD:VIEW_LOGS'.encode())
            response = client.recv(8192).decode()
            logs = json.loads(response.split(':', 1)[1])
            for log in logs:
                print(f"{log['timestamp']} | {log['badge_number']} | {log['action']}")
        elif cmd == '6' or cmd.lower() == 'exit':
            break

start_menu = {
    '1': 'Login',
    '2': 'Register',
    '3': 'Admin Login',
    '4': 'Exit'
}
Start_menu = input('Welcome to GhostWire! Please select an option:\n1. Login\n2. Register\n3. Admin Login\n4. Exit\n> ')
if Start_menu == '2' or Start_menu == 'register':
    name = input('Enter your name: ')
    password = input('Enter a password: ')
    client.send(f'REGISTER:{name}:{password}'.encode())
    response = client.recv(1024).decode()
    if response.startswith('REGISTER_SUCCESS'):
        badge_number = response.split(':')[1]
        print(f'Registration successful! Your badge number is {badge_number}')
    else:
        print('Registration failed. Please try again.')
        client.close()
        exit()
elif Start_menu == '1' or Start_menu == 'login':
    badge_number = input('Enter badge number: ')
    password = getpass('Enter password: ')
    client.send(f'LOGIN:{badge_number}:{password}'.encode())
    response = client.recv(1024).decode()
    if response.startswith('AUTH_SUCCESS'):
        role = response.split(':')[1]
        print(f'Login successful! Role: {role}')
        threading.Thread(target=receive_messages, daemon=True).start()
        sending_thread = threading.Thread(target=send_messages)
        sending_thread.start()
        sending_thread.join()
    else:
        print('Login failed. Please check your credentials.')
elif Start_menu == '3' or Start_menu == 'admin login':
    admin_id = input('Enter admin ID: ')
    key = getpass('Enter admin key: ')
    client.send(f'ADMIN_LOGIN:{admin_id}:{key}'.encode())
    response = client.recv(1024).decode()
    if response == 'ADMIN_AUTH_SUCCESS':
        print('Admin login successful!')
        admin_commands()
    else:
        print('Admin login failed.')
elif Start_menu == '4' or Start_menu == 'exit':
    print('Exiting...')
else:
    print('Invalid option. Please try again.')
    client.close()
    exit()
client.close()