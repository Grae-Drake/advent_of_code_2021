import argparse
from collections import defaultdict


def get_data(data_path):
    with open(data_path) as file:
        result = []
        for line in file.readlines():
            sides = line.split(" -> ")
            result.append([[int(n) for n in side.split(',')] for side in sides])
        return result


def step_direction(a, b):
    diff = b - a
    return 1 if diff > 0 else -1 if diff < 0 else 0


def coordinate_range(start, stop, step, length):
    return [start + step * x for x in range(length)]


def get_line_points(line):
    length = max(abs(line[0][0] - line[1][0]), abs(line[0][1] - line[1][1])) + 1
    i_step = step_direction(line[0][0], line[1][0])
    j_step = step_direction(line[0][1], line[1][1])
    i_range = coordinate_range(line[0][0], line[1][0], i_step, length)
    j_range = coordinate_range(line[0][1], line[1][1], j_step, length)
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
