customer_name = input('Kindly enter your name: ')
num_of_passes = int(input('Kindly enter your the number of passes you need: '))
tokens_per_pass = 10
price_per_pass = 20
tokens_required_per_game = 2
#calculation 
total_tokens = num_of_passes*tokens_per_pass
total_cost = num_of_passes*price_per_pass
games_available = total_tokens // tokens_required_per_game
#reciept
print('ARCADE DAY PASS')
print(f'Welcome to Arcade {customer_name}')
print(f'No. of passes: {num_of_passes}')
print(f'Total tokens: {total_tokens}')
print(f'Bill:${total_cost}')
print(f'Games available: {games_available}')