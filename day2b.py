import argparse


def get_data(data_path):
    with open(data_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def update_state(state, command):
    result = state.copy()
    direction, distance = command.split(' ')
    distance = int(distance)
    if direction == 'forward':
        result['h'] += distance
        result['d'] += distance * result['a']
    elif direction == 'down':
        result['a'] += distance
    elif direction == 'up':
        result['a'] -= distance
    return result


def main(data_path):
    state = {
        'h': 0,
        'd': 0,
        'a': 0
    }
    data = get_data(data_path)
    for command in data:
        state = update_state(state, command)
    return state['h'] * state['d']



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 2, Problem 1')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 2
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

