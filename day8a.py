import argparse
from os import stat
import statistics

def get_data(data_path):
    with open(data_path) as file:
        patterns = []
        outputs = []
        for line in file.readlines():
            pattern, output = line.rstrip().split(' | ')
            patterns.append(pattern)
            outputs.append(output)
        return (patterns, outputs)


def main(data_path):
    patterns, outputs = get_data(data_path)
    result = 0
    for output in outputs:
        for digit in output.split(' '):
            if len(digit) in [2, 4, 3, 7]:
                result += 1
    return result
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 8')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 8
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

