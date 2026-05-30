import random
print("Welcome to the Raffle!")
names = []
count = int(input("How many people are entering?: "))
for i in range(count):
    if count < 3:
        quit("Sorry, you need at least 3 people to enter the lottery.")
    else:
        print("Kindly enter your name (or type 'done' to finish): ")
        names.append(input(": ").lower())
ticket_counts = {}
for name in names:
    ticket_counts[name] = int(input(f"Hey {name}, how many tickets do you want to buy?: "))
    if ticket_counts[name] <= 0:
        quit("Sorry, you can't buy zero or negative tickets.")
ticket_price = 100
prize = sum(ticket_counts.values()) * ticket_price
prize1 = prize * 0.5
prize2 = prize * 0.3
prize3 = prize * 0.2
prize = [prize1, prize2, prize3]
tickets = {name: [random.randint(1, 100) for _ in range(ticket_counts[name])] for name in names}
print(tickets)
print(input("The lottery is now closed. The winners are being picked...(press enter to continue): "))
for i in range(3):
    winners = random.choice(names)
    names.remove(winners)
    if i == 0:
        print (f'{winners} You have won {prize[0]} the Grand prize(Your ticket number is {random.choice(tickets[winners])}!)')
    elif i == 1:
        print (f'{winners} You have won {prize[1]} the Second prize(Your ticket number is {random.choice(tickets[winners])}!)')
    else:        print (f'{winners} You have won {prize[2]} the Third prize(Your ticket number is {random.choice(tickets[winners])}!)')