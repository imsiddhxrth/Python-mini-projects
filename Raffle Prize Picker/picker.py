import random
print("Welcome to the Lottery!")
names = []
count = int(input("How many people are entering?: "))
for i in range(count):
    if count < 3:
        quit("Sorry, you need at least 3 people to enter the lottery.")
    else:
        print("Kindly enter your name (or type 'done' to finish): ")
        names.append(input(": ").lower())
tickets = {}
for name in names:
    ticket_count = int(input(f"Hey {name}, how many tickets do you want?: "))
    while ticket_count < 1:
        print("Sorry, you need to buy at least 1 ticket.")
        ticket_count = int(input(f"Hey {name}, how many tickets do you want?: "))
    tickets[name] = []
    for _ in range(ticket_count):
        while True:
            try:
                number = int(input(f"Hey {name}, choose a number between 1-99: "))
                if number < 1 or number > 99:
                    print("Please choose a number between 1 and 99!")
                    continue
            except ValueError:
                print("Please enter a valid number!")
                continue
            all_tickets = [t for lst in tickets.values() for t in lst]
            if number in all_tickets:
                print("Already taken! Please choose another number.")
            else:
                tickets[name].append(number)
                break
ticket_price = 100
prize = ticket_price * sum(len(t) for t in tickets.values())
prize1 = prize * 0.5
prize2 = prize * 0.3
prize3 = prize * 0.2
prize = [prize1, prize2, prize3]
all_tickets = [t for lst in tickets.values() for t in lst]
winning_number = random.choice(all_tickets)
print(input("The lottery is now closed. The winners are being picked...(press enter to continue): "))
for i in range(3):
    all_tickets = [t for lst in tickets.values() for t in lst]
    winning_number = random.choice(all_tickets)
    print(f'🎱 Winning number: {winning_number}')
    for name, numbers in tickets.items():
        if winning_number in numbers:
            winner = name
            break
    del tickets[winner]
    if i == 0:
        print(f'{winner} won Grand Prize of ${prize1:.2f}')
    elif i == 1:
        print(f'{winner} won Second Prize of ${prize2:.2f}')
    else:
        print(f'{winner} won Third Prize of ${prize3:.2f}')