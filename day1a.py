import argparse


def get_data(data_path):
    with open(data_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def main(data_path):
    data = get_data(data_path)
    count = 0
    for x in range(1, 10):
        print(data[x] > data[x-1])
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
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

