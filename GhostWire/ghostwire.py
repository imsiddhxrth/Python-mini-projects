print('====== Ghostwire ======')
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