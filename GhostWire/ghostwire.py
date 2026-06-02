import json
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
    password = input('Enter password: ')
    user = users.get(badge_number)
    if user and user['password'] == password:
        print('Login successful')
        return True
    else:
        print('Invalid badge number or password')
        return False

start_menu = {
    '1': 'Login',
    '2': 'Register',
    '3': 'Exit'
}

menu = {
    '1': 'Encode',
    '2': 'Decode',
    '3': 'Exit'
}

def process_message(mode):
    keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=~`[]{}|;:,.<>?'
    values = keys[-1] + keys[0:-1]
    dict_encode = dict(zip(keys, values))
    dict_decode = dict(zip(values, keys))
    msg = input('Enter the message (or type exit to go back): ')
    if msg.lower() == 'exit':
        return 'exit'
    if mode == 'encode':
        msg = msg.replace(' ', '_')
        result = ''.join([dict_encode.get(char, char) for char in msg if char != ' '])
        result = result.replace(' ', '_')
    elif mode == 'decode':
        result = ''.join([dict_decode.get(char, char) for char in msg])
        result = result.replace('_', ' ')
    else:
        result = 'Invalid mode'
    return result
    
print('====== Ghostwire ======')
while True:    
    while True:
        for key, value in start_menu.items():
            print(f"{key}. {value}")
        choice = input('Enter your choice: ').title()
        if choice == '1' or choice == 'Login':
            if login():
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
                result = process_message('encode')
                if result == 'exit':
                    break
                print(result)
        elif choice == '2' or choice == 'Decode':
            while True:
                result = process_message('decode')
                if result == 'exit':
                    break
                print(result)
        elif choice == '3' or choice == 'Exit':
            break
        else:
            print('Invalid choice')