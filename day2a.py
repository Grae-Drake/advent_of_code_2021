import argparse


def get_data(data_path):
    with open(data_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def update_position(position, command):
    result = position.copy()
    direction, distance = command.split(' ')
    distance = int(distance)
    if direction == 'forward':
        result[0] += distance
    elif direction == 'down':
        result[1] += distance
    elif direction == 'up':
        result[1] -= distance
    return result


def main(data_path):
    position = [0, 0]
    data = get_data(data_path)
    for command in data:
        position = update_position(position, command)
    return position[0] * position[1]



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 2, Problem 1')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 2
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

