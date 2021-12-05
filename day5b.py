import argparse
from collections import defaultdict


def get_data(data_path):
    with open(data_path) as file:
        result = []
        for line in file.readlines():
            sides = line.split(" -> ")
            result.append([[int(n) for n in side.split(',')] for side in sides])
        return result


def orientation(line):
    if line[0][0] == line[1][0]:
        return 'vertical'
    elif line[0][1] == line[1][1]:
        return 'horizontal'
    else:
        return 'diagonal'


def get_line_points(line):
    if orientation(line) == 'vertical':
        i = line[0][0]
        j_s = [line[0][1], line[1][1]]
        return [(i, j) for j in range(min(j_s), max(j_s) + 1)]
    elif orientation(line) == 'horizontal':
        j = line[0][1]
        i_s = [line[0][0], line[1][0]]
        return [(i, j) for i in range(min(i_s), max(i_s) + 1)]
    elif orientation(line) == 'diagonal':
        i_step = 1 if line[0][0] < line[1][0] else -1
        j_step = 1 if line[0][1] < line[1][1] else -1
        i_range = range(line[0][0], line[1][0] + i_step, i_step)
        j_range = range(line[0][1], line[1][1] + j_step, j_step)
        return [(x) for x in zip(i_range, j_range)]


def main(data_path):
    lines = get_data(data_path)
    coordinates = defaultdict(int)
    for line in lines:
        line_points = get_line_points(line)
        for line_point in line_points:
            coordinates[line_point] += 1
    return len([x for x in coordinates.values() if x > 1])
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 5, Problem 1')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 5
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

