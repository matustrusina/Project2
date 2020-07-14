import scripts1, statistics

def game():
    ch = '1'
    while ch == '1':
        scripts1.beginning()
        scripts1.generator()
        scripts1.guesser()
        scripts1.winner()

        print('Would you like to see some statistics?')
        choice = input('yes/no: ')
        if choice == 'yes':
            statistics.stat_printer()

        print('Would you like to play again?')
        ch = input('If you do, type "1", if not, type "2": ')
    print('Hope to see you next time!')

if __name__ == '__main__':
    game()