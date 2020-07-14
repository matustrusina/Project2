import csv
import time

def stat_writer(move, time_stats):
    to_insert = [move, time_stats]
    with open('stats.csv', 'a', newline='') as file:
        f_writer = csv.writer(file)
        f_writer.writerow(to_insert)


def stat_reader():
    with open('stats.csv', 'r') as file:
        f_reader = csv.reader(file)
        to_read = list(f_reader)

    avg_moves = 0
    avg_time = 0

    for indx, value in enumerate(to_read):
        avg_moves += int(to_read[indx][0])
        avg_time += int(to_read[indx][1])

    avg_moves /= len(to_read)
    avg_moves = round(avg_moves, 2)
    avg_time /= len(to_read)
    avg_time = round(avg_time, 2)

    data = [avg_moves, avg_time]

    return data

def stat_printer():
    separator = 51 * '_'

    with open('stats.csv', 'r') as file:
        f_reader = csv.reader(file)
        to_read = list(f_reader)

    print(separator)
    print('|Num. of moves|Time elapsed|')
    print(separator)

    for j in to_read:
        time.sleep(0.2)
        print(f'|{j[0]: ^13}|{j[1]: ^12}|')
        print(separator)

    time.sleep(1)
    print(f'Average number of moves: {stat_reader()[0]}')
    time.sleep(1)
    print(f'Average time elapsed: {stat_reader()[1]}')
    print(separator)
    time.sleep(1)
