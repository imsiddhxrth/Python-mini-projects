import random
print("Welcome to the Raffle!")
names = []
count = int(input("How many people are entering? "))
for i in range(count):
    if count < 3:
        quit("Sorry, you need at least 3 people to enter the raffle.")
    else:
        print("Kindly enter your name (or type 'done' to finish): ")
        names.append(input(": ").lower())
prize = []
for i in range(3):
    prize.append(input("Enter 3 prizes: "))
tickets = {name: random.randint(1, 100) for name in names}
print(tickets)
print(input("The raffle is now closed. The winners are being picked...(press enter to continue): "))
random.shuffle(prize)
for i in range(3):
    winners = random.choice(names)
    names.remove(winners)
    print(f'{winners} Your lottery ticket number is {tickets[winners]}')
    if i == 2:
        print (f'{winners} You have won {prize[i]} the Grand prize!')
    elif i == 1:
        print (f'{winners} You have won {prize[i]} the Second prize!')
    else:        print (f'{winners} You have won {prize[i]} the Third prize!')