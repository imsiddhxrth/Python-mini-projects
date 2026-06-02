print('====== Ghostwire ======')
def create_keys():
    keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=~`[]{}|;:,.<>?'
    values = keys[-1] + keys[0:-1]
    dict_encode = dict(zip(keys, values))
    dict_decode = dict(zip(values, keys))
    msg = input('Enter the message: ')
    mode = input('Enter the mode (encode/decode): ')
    if mode == 'encode':
        result = ''.join([dict_encode[char] for char in msg])
    elif mode == 'decode':
        result = ''.join([dict_decode[char] for char in msg])
    else:
        result = 'Invalid mode'
    return result
print(create_keys())