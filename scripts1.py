import random
import time

def beginning():
    global separator
    separator = 51 * '_'

    print(separator)
    print('Welcome to our table! Today we play "Bulls & Cows".')
    print(separator)
    print('''I am going to generate a random 4-digit number.
You will guess this number. Digits do not 
repeat. If a digit in your number is correct, 
but its position is wrong, I will give you "Cows".
If a digit in your number is correct on its correct
position, I will give you "Bulls".
Please note, this number may begin with "0"''')
    print(separator)
    print('If you understand, please press enter. If you do not, read it again please...')
    input()
    print('Good luck!')
    print(separator)

def generator():
    global number
    number = []

    print('Generating number...')
    while len(number) != 4:
        k = random.randint(0, 9)
        if str(k) not in number:
            number.append(str(k))

    number = ''.join(number)

    time.sleep(1)
    for i in range(3):
        print('.')
        time.sleep(1)

    print('GOT IT!')
    print(separator)

def guesser():
    global move
    global t1
    global t2
    move = 1
    while move:
        bulls = 0
        cows = 0
        t1 = int(time.time())

        guess = input(f'Type a number. Guess number {move}: ')

        for i in guess:
            if i in number and number.index(i) != guess.index(i):
                cows += 1
            elif i in number and number.index(i) == guess.index(i):
                bulls += 1

        if number == guess:
            t2 = int(time.time())
            break

        print(f'|Bulls: {bulls} | Cows: {cows}|')
        move += 1

def winner():
    print(separator)
    print('You won!')
    print(separator)
    print(f'You guessed the right number in {move} guesses!')
    print(f'It took you {t2 - t1} seconds.')
    print(separator)