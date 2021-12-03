import argparse
import sys


def get_data(data_path):
    with open(data_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def to_int(lst):
    return int(''.join([str(x) for x in lst]), 2)


def most_common_bit(data, i):
    digit_sum = sum([int(row[i]) for row in data])
    if digit_sum > len(data) / 2:
        return 1
    elif digit_sum < len(data) / 2:
        return 0
    else:
        return -1


def oxygen(data, i=0):
    if len(data) == 1:
        return to_int(data[0])
    else:
        most_common = most_common_bit(data, i)
        most_common = 0 if most_common == 0 else 1
        new_data = [row for row in data if row[i] == str(most_common)]
        return oxygen(new_data, i + 1)


def carbon_dioxide(data, i=0):
    if len(data) == 1:
        return to_int(data[0])
    else:
        most_common = most_common_bit(data, i)
        least_common = 1 if most_common == 0 else 0
        data = [row for row in data if row[i] == str(least_common)]
        return carbon_dioxide(data, i + 1)


def main(data_path):
    sys.setrecursionlimit(2000)
    data = get_data(data_path)
    return oxygen(data) * carbon_dioxide(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 3, Problem 1')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 3
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

