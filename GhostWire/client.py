import socket
import threading
from getpass import getpass


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))
print('Connected to GhostWire!')

def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg.startswith('FROM:'):
                _, sender, message = msg.split(':', 2)
                print(f'\nMessage from {sender}: {message}')
            else:
                print(f'\n{msg}')
        except:
            print('Connection lost.')
            break
def send_messages():
    while True:
        recipient = input('Send to (or exit): ')
        if recipient.lower() == 'exit':
            break
        message = input('Message: ')
        client.send(f'MSG:{recipient}:{message}'.encode())
start_menu = {
    '1': 'Login',
    '2': 'Register',
    '3': 'Exit'
}
Start_menu = input('Welcome to GhostWire! Please select an option:\n1. Login\n2. Register\n3. Exit\n> ')
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
elif Start_menu == '3' or Start_menu == 'exit':
    print('Exiting...')
else:
    print('Invalid option. Please try again.')
    client.close()
    exit()
client.close()