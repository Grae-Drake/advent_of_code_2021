import argparse


def get_data(data_path):
    with open(data_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def main(data_path):
    data = [int(x) for x in get_data(data_path)]
    a = sum(data[0:3])
    b = sum(data[1:4])
    count = 1 if b > a else 0
    for i in range(2, len(data) - 3):
        a = b
        b = a - data[i] + data[i + 3]
        if b > a:
            count += 1    
    return count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 1, Problem 1')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 1
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

