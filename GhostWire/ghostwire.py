import json
from getpass import getpass
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M")
    
def save_message(badge_number, encrypted, decrypted):
    try:
        with open('messages.json', 'r') as f:
            messages = json.load(f)
    except FileNotFoundError:
        messages = {}
    if badge_number not in messages:
        messages[badge_number] = []
    messages[badge_number].append({
        "encrypted": encrypted,
        "decrypted": decrypted,
        "timestamp": get_current_time()
    })
    with open('messages.json', 'w') as f:
        json.dump(messages, f)

def view_messages(badge_number):
    try:
        with open('messages.json', 'r') as f:
            messages = json.load(f)
    except FileNotFoundError:
        print('No messages found!')
        return
    if badge_number not in messages:
        print('No messages found!')
        return
    for i, msg in enumerate(messages[badge_number]):
        print(f"\n--- Message {i+1} ---")
        print(f"Time: {msg['timestamp']}")
        print(f"Encrypted: {msg['encrypted']}")
        print(f"Decrypted: {msg['decrypted']}")
        print('-------------------')


def load_users():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f)

def register():
    users = load_users()
    badge_number = f"EMP-{str(len(users) + 1).zfill(3)}"
    name = input('Enter name: ')
    password = input('Enter password: ')
    users[badge_number] = {"name": name, "password": password}
    save_users(users)
    print(f"Your badge number is: {badge_number}")
    print('Registration successful')

def login():
    users = load_users()
    badge_number = input('Enter badge number: ')
    password = getpass('Enter password: ')
    user = users.get(badge_number)
    if user and user['password'] == password:
        print('Login successful')
        return badge_number
    else:
        print('Invalid badge number or password')
        return None

start_menu = {
    '1': 'Login',
    '2': 'Register',
    '3': 'Exit'
}

menu = {
    '1': 'Encode',
    '2': 'Decode',
    '3': 'View Messages',
    '4': 'Exit'
}

def process_message(mode):
    keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=~`[]{}|;:,.<>?'
    values = keys[-1] + keys[0:-1]
    dict_encode = dict(zip(keys, values))
    dict_decode = dict(zip(values, keys))
    msg = input('Enter the message (or type exit to go back): ')
    if msg.lower() == 'exit':
        return 'exit'
    original_msg = msg
    if mode == 'encode':
        msg = msg.replace(' ', '_')
        result = ''.join([dict_encode.get(char, char) for char in msg if char != ' '])
        result = result.replace(' ', '_')
    elif mode == 'decode':
        result = ''.join([dict_decode.get(char, char) for char in msg])
        result = result.replace('_', ' ')
    else:
        result = 'Invalid mode'
    return original_msg, result

print('====== Ghostwire ======')
while True:    
    while True:
        for key, value in start_menu.items():
            print(f"{key}. {value}")
        choice = input('Enter your choice: ').title()
        if choice == '1' or choice == 'Login':
            badge_number = login()
            if badge_number:
                break
        elif choice == '2' or choice == 'Register':
            register()
        elif choice == '3' or choice == 'Exit':
            exit()
        else:
             print('Invalid choice')

    while True:
        for key, value in menu.items():
            print(f"{key}. {value}")
        choice = input('Enter your choice: ').title()
        if choice == '1' or choice == 'Encode':
            while True:
                original, result = process_message('encode')
                if original == 'exit':
                    break
                print(result)
                save = input('Save this message? (yes/no): ').lower()
                if save == 'yes':
                    save_message(badge_number, result, original)
                    print('Message saved!')
        elif choice == '2' or choice == 'Decode':
            while True:
                original, result = process_message('decode')
                if original == 'exit':
                    break
                print(result)
                save = input('Save this message? (yes/no): ').lower()
                if save == 'yes':
                    save_message(badge_number, result, original)
                    print('Message saved!')
        elif choice == '3' or choice == 'View Messages':
            view_messages(badge_number)
        elif choice == '4' or choice == 'Exit':
            break
        else:
            print('Invalid choice')