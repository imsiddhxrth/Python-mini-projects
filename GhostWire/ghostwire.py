import json
from getpass import getpass
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def saved_messages(badge_number):
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

def save_message(badge_number, encrypted, decrypted, sender=None):
    try:
        with open('messages.json', 'r') as f:
            messages = json.load(f)
    except FileNotFoundError:
        messages = {}
    if badge_number not in messages:
        messages[badge_number] = []
    messages[badge_number].append({
        "from": sender,
        "encrypted": encrypted,
        "decrypted": decrypted,
        "timestamp": get_current_time()
    })
    with open('messages.json', 'w') as f:
        json.dump(messages, f)

def send_message(sender_badge, recipient_badge=None):
    users = load_users()
    if recipient_badge is None:
        recipient_badge = input('Enter recipient badge number: ')
    if recipient_badge not in users:
        print('Recipient not found!')
        return
    msg = input('Enter the message to send: ')
    encrypted = encrypt(msg)
    save_message(recipient_badge, encrypted, msg, sender_badge)
    print('Message sent!')
    log_action(sender_badge, f'Sent message to {recipient_badge}')

def view_inbox(badge_number):
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
        if msg['from'] is None:
            continue
        print(f"\n--- Message {i+1} ---")
        print(f"From: {msg['from']}")
        print(f"Time: {msg['timestamp']}")
        print(f"Encrypted: {msg['encrypted']}")
        print(f"Decrypted: {msg['decrypted']}")
        reply_choice = input('Reply? (yes/no): ').lower()
        if reply_choice == 'yes':
            send_message(badge_number, msg['from'])

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
    log_action(badge_number, 'Registered')

def login():
    users = load_users()
    badge_number = input('Enter badge number: ')
    password = getpass('Enter password: ')
    user = users.get(badge_number)
    if user and user['password'] == password:
        print('Login successful')
        log_action(badge_number, 'Logged in')
        return badge_number
    else:
        print('Invalid badge number or password')
        return None
    
def admin_login():
    try:
        with open('admins.json', 'r') as f:
            admins = json.load(f)
    except FileNotFoundError:
        print('No admin accounts found!')
        return None
    admin_id = input('Enter Admin ID: ')
    key = getpass('Enter Admin Key: ')
    admin = admins.get(admin_id)
    if admin and admin['key'] == key:
        print('Admin login successful!')
        return admin_id
    else:
        print('Invalid Admin ID or Key!')
        return None

def remove_user():
    users = load_users()
    badge_number = input('Enter badge number to remove: ')
    if badge_number in users:
        del users[badge_number]
        save_users(users)
        print('User removed successfully!')
        log_action(badge_number, 'User removed')
    else:
        print('User not found!')

def view_all_messages():
    try:
        with open('messages.json', 'r') as f:
            messages = json.load(f)
    except FileNotFoundError:
        print('No messages found!')
        return
    for badge_number, msgs in messages.items():
        print(f"\n--- Messages for {badge_number} ---")
        for i, msg in enumerate(msgs):
            print(f"\nMessage {i+1}:")
            print(f"From: {msg.get('from', 'N/A')}")
            print(f"Time: {msg['timestamp']}")
            print(f"Encrypted: {msg['encrypted']}")
            print(f"Decrypted: {msg['decrypted']}")

def delete_messages():
    try:
        with open('messages.json', 'r') as f:
            messages = json.load(f)
    except FileNotFoundError:
        print('No messages found!')
        return
    badge_number = input('Enter badge number to delete messages for: ')
    if badge_number in messages:
        del messages[badge_number]
        with open('messages.json', 'w') as f:
            json.dump(messages, f)
        print('Messages deleted successfully!')
    else:
        print('User not found!')

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

def view_logs():
    try:
        with open('logs.json', 'r') as f:
            logs = json.load(f)
    except FileNotFoundError:
        print('No logs found!')
        return
    for log in logs:
        print(f"Time: {log['timestamp']} | {log['badge_number']} | {log['action']}")



admin_menu = {
    '1': 'Add User',
    '2': 'Remove User',
    '3': 'View All Messages',
    '4': 'Delete Messages',
    '5': 'View Logs',
    '6': 'Exit'
}

start_menu = {
    '1': 'Login',
    '2': 'Register',
    '3': 'Admin Login',
    '4': 'Exit'
}

menu = {
    '1': 'Encode',
    '2': 'Decode',
    '3': 'Inbox',
    '4': 'Exit'
}

inbox_menu = {
    '1': 'Recent Messages',
    '2': 'Send Message',
    '3': 'Saved Messages',
    '4': 'Back'
}

def process_message(mode):
    msg = input('Enter the message (or type exit to go back): ')
    if msg.lower() == 'exit':
        return 'exit', None
    original_msg = msg
    if mode == 'encode':
        result = encrypt(msg)
    elif mode == 'decode':
        result = decrypt(msg)
    else:
        result = 'Invalid mode'
    return original_msg, result

print('====== Ghostwire ======')
while True:
    is_admin = False
    badge_number = None

    # Start menu
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
        elif choice == '3' or choice == 'Admin Login':
            admin_id = admin_login()
            if admin_id:
                is_admin = True
                break
        elif choice == '4' or choice == 'Exit':
            exit()
        else:
            print('Invalid choice')

    # Admin menu
    if is_admin:
        while True:
            for key, value in admin_menu.items():
                print(f"{key}. {value}")
            choice = input('Enter your choice: ').title()
            if choice == '1' or choice == 'Add User':
                register()
            elif choice == '2' or choice == 'Remove User':
                remove_user()
            elif choice == '3' or choice == 'View All Messages':
                view_all_messages()
            elif choice == '4' or choice == 'Delete Messages':
                delete_messages()
            elif choice == '5' or choice == 'View Logs':
                view_logs()
            elif choice == '6' or choice == 'Exit':
                break
            else:
                print('Invalid choice')

    # User menu
    else:
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
            elif choice == '3' or choice == 'Inbox':
                while True:
                    for key, value in inbox_menu.items():
                        print(f"{key}. {value}")
                    choice = input('Enter your choice: ').title()
                    if choice == '1' or choice == 'Recent Messages':
                        view_inbox(badge_number)
                    elif choice == '2' or choice == 'Send Message':
                        send_message(badge_number)
                    elif choice == '3' or choice == 'Saved Messages':
                        saved_messages(badge_number)
                    elif choice == '4' or choice == 'Back':
                        break
                    else:
                        print('Invalid choice')
            elif choice == '4' or choice == 'Exit':
                break
            else:
                print('Invalid choice')