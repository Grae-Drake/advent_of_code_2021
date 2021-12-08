import argparse
from os import stat
import statistics

def get_data(data_path):
    with open(data_path) as file:
        return [int(x) for x in file.read().split(',')]


def triangle(n):
    return (n * (n + 1)) / 2


def main(data_path):
    data = get_data(data_path)
    mean = round(statistics.mean(data))
    distances = []
    for x in data:
        distances.append(sum([triangle(abs(y - x)) for y in data]))
    return min(distances)
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 7')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 7
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

