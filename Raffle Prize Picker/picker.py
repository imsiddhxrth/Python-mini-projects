import random
print("Welcome to the Raffle!")
name = []
count = int(input("How many people are entering? "))
for i in range(count):
    if count < 3:
        quit("Sorry, you need at least 3 people to enter the raffle.")
    else:
        print("Kindly enter your name (or type 'done' to finish): ")
        name.append(input(": ").lower())
prize = []
for i in range(3):
    prize.append(input("Enter 3 prizes: "))

for i in range(3):
    winner = random.choice(name)
    name.remove(winner)
    if i == 2:
        print (f'{winner} You have won {prize[i]} the Grand prize!')
    elif i == 1:
        print (f'{winner} You have won {prize[i]} the Second prize!')
    else:        print (f'{winner} You have won {prize[i]} the Third prize!')