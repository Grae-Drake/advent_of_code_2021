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

    # Iterate over each pattern.
    for i, pattern in enumerate(patterns):
        
        # Initialize containers.
        real = [None for x in range(10)]
        e = None
        two_three_five = []
        zero_six_nine = []
        
        # Initial easy pattern assignment.
        for scrambled in pattern.split(' '):
            if len(scrambled) == 2:
                real[1] = set(scrambled)
            elif len(scrambled) == 4:
                real[4] = set(scrambled)
            elif len(scrambled) == 3:
                real[7] = set(scrambled)
            elif len(scrambled) == 7:
                real[8] = set(scrambled)
            elif len(scrambled) == 5:
                two_three_five.append(scrambled)
            else:
                zero_six_nine.append(scrambled)
        
        for scrambled in zero_six_nine:
            if len(set(real[4]).intersection(scrambled)) == 4:
                real[9] = set(scrambled)
                for x in real[8]:
                    if x not in real[9]:
                        e = x
                zero_six_nine.remove(scrambled)

        for scrambled in two_three_five:
            if e in scrambled:
                real[2] = set(scrambled)
                two_three_five.remove(scrambled)
        for scrambled in two_three_five:
            if len(set(real[2]).intersection(scrambled)) == 3:
                real[5] = set(scrambled)
            else:
                real[3] = set(scrambled)
        
        for scrambled in zero_six_nine:
            if len(set(real[1]).intersection(scrambled)) == 2:
                real[0] = set(scrambled)
            else:
                real[6] = set(scrambled)

        unscrambled = [str(real.index(set(digit))) for digit in outputs[i].split(' ')]
        result += int(''.join(unscrambled))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 8')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 8
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

