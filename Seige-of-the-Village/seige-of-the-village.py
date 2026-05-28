freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

cart = {}
purse = 1000
stores = [freelancers, antiques, pet_shop]

while True:
    main_menu = input("Select a store to visit: 'freelancing shop'/'antique shop'/'pet shop': ")
    selected_store = None
    for store in stores:
        if main_menu == store['name'].lower():
            selected_store = store
            print(f'Welcome to the {selected_store["name"]}! items for sale are: ')
            break
    else:
        print('Sorry, that store is not available. Please select a valid store.')
    for item in selected_store:
        if item == 'name':
            continue
        print(item, ':', selected_store[item])
    while True:
        choice = input('What would you like to buy?(you can exit the store by typing "exit"): ')
        if choice in selected_store:
            cart[choice] = selected_store[choice]
            del selected_store[choice]
            print(f'You have added {choice} to your cart.')
            break
        elif choice == 'exit':
            print(f'You have left the {selected_store["name"]}.')
            break
        else:
            print('Sorry, that item is not available')
    visit_again = input("Visit another store? (yes/no): ")
    if visit_again == 'no':
        break
print(f'Your cart contains: {list(cart.keys())} ')
total_cost = sum(cart.values())
print(f'Total cost of your purchases is: {total_cost} gold pieces.')
confirm = input('Confirm your purchase? (yes/no): ')
if confirm == 'yes':
    purse -= total_cost
    print(f'purchase confirmed! You have bought: {list(cart.keys())}')
    print(f'You have {purse} gold pieces left.')