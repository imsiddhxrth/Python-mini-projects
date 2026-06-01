import random
print("Welcome to the Lottery Simulator!")
print("START MENU")
start_menu = input("Choose a mode (MANUAL MODE / SIMULATION MODE): ").upper()

if start_menu == "SIMULATION MODE":
    print("You have selected Simulation Mode.")
    print("Welcome to the Simulation Lottery Simulator!")
    print("In this mode, we will simulate a lottery with 1000 tickets sold.")
    names = [f'Player{i}' for i in range(1, 1001)]
    tickets = {name: [random.randint(1, 99) for _ in range(random.randint(1, 10))] for name in names}
    ticket_price = 100
    revenue = ticket_price * sum(len(t) for t in tickets.values())
    company_revenue = revenue * 0.3
    prize_pool = revenue * 0.7
    prize1 = prize_pool * 0.5
    prize2 = prize_pool * 0.3
    prize3 = prize_pool * 0.2
    prize = [prize1, prize2, prize3]
    total_tickets_sold = sum(len(t) for t in tickets.values())
    print(input("The lottery is now closed. The winners are being picked...(press enter to continue): "))
    winners = []
    for i in range(3):
        all_tickets = [t for lst in tickets.values() for t in lst]
        winning_number = random.choice(all_tickets)
        for name, numbers in tickets.items():
            if winning_number in numbers:
                winner = name
                break
        winners.append(winner)
        del tickets[winner]
        if i == 0:
            print(f'{winner} won Grand Prize of ${prize1:.2f}')
        elif i == 1:
            print(f'{winner} won Second Prize of ${prize2:.2f}')
        else:
            print(f'{winner} won Third Prize of ${prize3:.2f}')
    print("🏢 LOTTERY SIMULATOR - Results")
    print("----------------------------------")
    print(f"🎟️ Tickets Sold: {total_tickets_sold}")
    print(f"💰 Revenue: ${revenue:.2f}")
    print(f"🏆 Prize Pool: ${prize_pool:.2f}")
    print(f"📊 Company Profit: ${company_revenue:.2f}")
    print(f"🥇 Winner 1 - Grand Prize: {winners[0]} wins ${prize1:.2f}")
    print(f"🥈 Winner 2 - Second Prize: {winners[1]} wins ${prize2:.2f}")
    print(f"🥉 Winner 3 - Third Prize: {winners[2]} wins ${prize3:.2f}")

elif start_menu == "MANUAL MODE":
    print("You have selected Manual Mode.")
    print("Welcome to the Manual Lottery Simulator!")
    print("Each ticket costs $100. The more tickets you buy, the higher your chances of winning!")
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
    revenue = ticket_price * sum(len(t) for t in tickets.values())
    company_revenue = revenue * 0.3
    prize_pool = revenue * 0.7
    prize1 = prize_pool * 0.5
    prize2 = prize_pool * 0.3
    prize3 = prize_pool * 0.2
    prize = [prize1, prize2, prize3]
    total_tickets_sold = sum(len(t) for t in tickets.values())
    print(input("The lottery is now closed. The winners are being picked...(press enter to continue): "))
    winners = []
    for i in range(3):
        all_tickets = [t for lst in tickets.values() for t in lst]
        winning_number = random.choice(all_tickets)
        for name, numbers in tickets.items():
            if winning_number in numbers:
                winner = name
                break
        winners.append(winner)
        del tickets[winner]
        if i == 0:
            print(f'{winner} won Grand Prize of ${prize1:.2f}')
        elif i == 1:
            print(f'{winner} won Second Prize of ${prize2:.2f}')
        else:
            print(f'{winner} won Third Prize of ${prize3:.2f}')
    print("🏢 LOTTERY SIMULATOR - Results")
    print("----------------------------------")
    print(f"🎟️ Tickets Sold: {total_tickets_sold}")
    print(f"💰 Revenue: ${revenue:.2f}")
    print(f"🏆 Prize Pool: ${prize_pool:.2f}")
    print(f"📊 Company Profit: ${company_revenue:.2f}")
    print(f"🥇 Winner 1 - Grand Prize: {winners[0]} wins ${prize1:.2f}")
    print(f"🥈 Winner 2 - Second Prize: {winners[1]} wins ${prize2:.2f}")
    print(f"🥉 Winner 3 - Third Prize: {winners[2]} wins ${prize3:.2f}")

else:
    print("Invalid mode selected. Please restart the program and choose either MANUAL MODE or SIMULATION MODE.")