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

    digit_segments = [
        'abcefg',
        'cf',
        'acdeg',
        'acdfg',
        'bcdf',
        'abdfg',
        'abdefg',
        'acf',
        'abcdefg',
        'abcdfg'
    ]

    # Iterate over each pattern
    for i, pattern in enumerate(patterns):
        
        # Initialize containers
        real = {}
        two_three_five = []
        zero_six_nine = []
        
        # Initial easy pattern assignment
        for scrambled in pattern.split(' '):
            if len(scrambled) == 2:
                one = scrambled
            elif len(scrambled) == 4:
                four = scrambled
            elif len(scrambled) == 3:
                seven = scrambled
            elif len(scrambled) == 7:
                eight = scrambled
            elif len(scrambled) == 5:
                two_three_five.append(scrambled)
            else:
                zero_six_nine.append(scrambled)
        
        # Start deducing
        # We can figure out 9 because it wholly overlaps 4.
        # We can diff 9 against 8 to map e.
        for scrambled in zero_six_nine:
            if len(set(four).intersection(scrambled)) == 4:
                nine = scrambled
                for x in eight:
                    if x not in nine:
                        real['e'] = x
                zero_six_nine.remove(scrambled)
        
        # Knowing e, we can deduce 2, 3, and 5.
        for scrambled in two_three_five:
            if real['e'] in scrambled:
                two = scrambled
                two_three_five.remove(scrambled)
        for scrambled in two_three_five:
            if len(set(two).intersection(scrambled)) == 3:
                five = scrambled
            else:
                three = scrambled
        for scrambled in zero_six_nine:
            # need six and zero. Six has 1 overlap with one, zero has 2.
            if len(set(one).intersection(scrambled)) == 2:
                zero = scrambled
            else:
                six = scrambled

            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 8')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 8
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

