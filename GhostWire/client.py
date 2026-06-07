import json
import os
import queue
import socket
import threading
from getpass import getpass

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

users_queue = queue.Queue()
current_chat = None

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg.startswith('FROM:'):
                _, sender, message = msg.split(':', 2)
                print(f'[{sender}]: {decrypt(message)}')
            elif msg.startswith('BROADCAST:'):
                message = msg.split(':', 1)[1]
                print(f'\n*** BROADCAST: {message} ***')
            elif msg.startswith('PRIVATE_FROM:'):
                _, sender, message = msg.split(':', 2)
                print(f'\n[{sender}]: {message}')
            elif msg.startswith('USERS:'):
                users_queue.put(msg)
            elif msg == 'KICKED':
                print('\nYou have been kicked by admin!')
                client.close()
                exit()
            else:
                print(f'\n{msg}')
        except:
            print('Connection lost.')
            break

def admin_commands():
    while True:
        clear()
        print('================================')
        print('       GHOSTWIRE - ADMIN        ')
        print('================================')
        print('1. List Online Users')
        print('2. Broadcast Message')
        print('3. Send Private Message')
        print('4. Kick User')
        print('5. View Logs')
        print('6. Exit')
        print('--------------------------------')
        cmd = input('> ')
        if cmd == '1' or cmd.lower() == 'list online users':
            client.send('ADMIN_CMD:LIST_USERS'.encode())
            response = client.recv(1024).decode()
            users = response.split(':')[1].split(',')
            print('\nOnline users:')
            for u in users:
                parts = u.split('|')
                print(f'  {parts[0]}  |  {parts[1] if len(parts) > 1 else "Unknown"}')
            input('\nPress Enter to continue...')
        elif cmd == '2' or cmd.lower() == 'broadcast message':
            message = input('Broadcast message (or /back): ')
            if message == '/back':
                continue
            client.send(f'ADMIN_CMD:BROADCAST:{message}'.encode())
            response = client.recv(1024).decode()
            print('Broadcast sent!')
            input('Press Enter to continue...')
        elif cmd == '3' or cmd.lower() == 'send private message':
            recipient = input('Badge number (or /back): ')
            if recipient == '/back':
                continue
            message = input('Message: ')
            client.send(f'ADMIN_CMD:PRIVATE_MSG:{recipient}:{message}'.encode())
            response = client.recv(1024).decode()
            print(response)
            input('Press Enter to continue...')
        elif cmd == '4' or cmd.lower() == 'kick user':
            target = input('Badge number to kick (or /back): ')
            if target == '/back':
                continue
            client.send(f'ADMIN_CMD:KICK:{target}'.encode())
            response = client.recv(1024).decode()
            print(response)
            input('Press Enter to continue...')
        elif cmd == '5' or cmd.lower() == 'view logs':
            client.send('ADMIN_CMD:VIEW_LOGS'.encode())
            response = client.recv(8192).decode()
            logs = json.loads(response.split(':', 1)[1])
            print('\n--- Logs ---')
            for log in logs:
                print(f"{log['timestamp']} | {log['badge_number']} | {log['action']}")
            input('\nPress Enter to continue...')
        elif cmd == '6' or cmd.lower() == 'exit':
            break

clear()
print('================================')
print('         GHOSTWIRE              ')
print('================================')
print('1. Login')
print('2. Register')
print('3. Admin Login')
print('4. Exit')
print('--------------------------------')
Start_menu = input('> ')

if Start_menu == '2' or Start_menu == 'register':
    name = input('Enter your name: ')
    password = getpass('Enter a password: ')
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
        threading.Thread(target=receive_messages, daemon=True).start()

        while True:
            clear()
            client.send('GET_USERS'.encode())
            try:
                users_response = users_queue.get(timeout=5)
            except queue.Empty:
                print('Could not fetch users, retrying...')
                continue
            raw_users = users_response.split(':')[1].split(',')
            users = []
            for u in raw_users:
                parts = u.split('|')
                if parts[0] and parts[0] != badge_number:
                    users.append({'badge': parts[0], 'role': parts[1] if len(parts) > 1 else 'Unknown'})

            print('================================')
            print(f'   GHOSTWIRE  |  {badge_number}  |  {role}')
            print('================================')
            if not users:
                print('No users online.')
            for i, user in enumerate(users):
                print(f'[{i+1}] {user["badge"]}  |  {user["role"]}')
            print('--------------------------------')
            print('/exit to disconnect')

            choice = input('Select user: ')
            if choice == '/exit':
                break
            selected = choice.upper()
            selected_user = next((u for u in users if u['badge'] == selected), None)
            if not selected_user:
                print('User not found!')
                input('Press Enter to continue...')
                continue

            clear()
            print('================================')
            print(f'     Chat with {selected}')
            print('================================')
            print('/back = return | /exit = disconnect')
            print('--------------------------------')
            while True:
                message = input('> ')
                if message == '/exit':
                    client.close()
                    exit()
                if message == '/back':
                    break
                encrypted = encrypt(message)
                client.send(f'MSG:{selected}:{encrypted}'.encode())
    else:
        print('Login failed. Please check your credentials.')

elif Start_menu == '3' or Start_menu == 'admin login':
    admin_id = input('Enter admin ID: ')
    key = getpass('Enter admin key: ')
    client.send(f'ADMIN_LOGIN:{admin_id}:{key}'.encode())
    response = client.recv(1024).decode()
    if response == 'ADMIN_AUTH_SUCCESS':
        admin_commands()
    else:
        print('Admin login failed.')

elif Start_menu == '4' or Start_menu == 'exit':
    print('Exiting...')

else:
    print('Invalid option.')
    client.close()
    exit()

client.close()