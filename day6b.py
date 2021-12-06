import argparse
from collections import defaultdict


def get_data(data_path):
    with open(data_path) as file:
        return [int(x) for x in file.read().split(',')]


def main(data_path):
    data = get_data(data_path)
    counts = defaultdict(int)
    for n in data:
        counts[n] += 1

    for x in range(256):
        memo = counts[0]
        for n in range(1, 9):
            counts[n - 1] = counts[n]
        counts[8] = memo
        counts[6] += memo
    
    return sum(counts.values())
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 6, Problem 1')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 6
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

