guess_count = 1
while guess_count <= 10:
    guess = int(input('make a guess: '))
    guess_count +=1
    secret_num = 7
    if guess == secret_num:
        print('YOU WIN!!')
        break
    elif guess > 7:
        print('GO LOW')
    elif guess < 7:
        print('GO HIGH')
    else:
        print('YOU LOOSE!!!')