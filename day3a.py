import argparse


def get_data(data_path):
    with open(data_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def to_int(lst):
    return int(''.join([str(x) for x in lst]), 2)

def main(data_path):
    data = get_data(data_path)
    width = len(data[0])
    height = len(data)
    gamma = []
    for i in range(width):
        gamma.append(1 if (sum([int(row[i]) for row in data]) * 2 > height) else 0)
    epsilon = [1 if x == 0 else 0 for x in gamma]
    return to_int(gamma) * to_int(epsilon)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 3, Problem 1')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 3
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

