operators = input('Select an Operator +,-,/,*,f: ')
if operators == 'f':
    num1 = int(input('Enter First Number: '))
    print(f'{num1*9/5} temp in F')

else:
    num1 = int(input('Enter First Number: '))
    num2 = int(input('Enter Second Number: '))

if operators == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
elif operators == '-':
    print(f'{num1} - {num2} = {num1 - num2}')
elif operators == '/':
    print(f'{num1} / {num2} = {num1 / num2}')
elif operators == '*':
    print(f'{num1} * {num2} = {num1 * num2}')
