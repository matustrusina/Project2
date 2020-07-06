from scripts1 import beginning, generator, guesser, winner

def game():
    ch = '1'
    while ch == '1':
        beginning()
        generator()
        guesser()
        winner()
        print('Would you like to play again?')
        ch = input('If you do, type "1", if not, type "2": ')
    print('Hope to see you next time!')





game()