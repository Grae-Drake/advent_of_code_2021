import argparse
import math


def get_data(data_path):
    with open(data_path) as file:
        data = file.read().rstrip()
        data = data[data.index('x=') + 2:].split(', y=')
        result = []
        for x in data:
            pair = x.split('..')
            result.append([int(n) for n in pair])
        return result


def triangle(n):
    return n * (n + 1) / 2


def triangle_height(n):
    return (-1 + math.sqrt(1 + 8 * n)) / 2


def in_xrange(step, initial_velocity, x_left, x_right):
    distance = triangle(initial_velocity) - triangle(max(initial_velocity - step, 0))
    return distance >= x_left and distance <= x_right


def in_yrange(step, initial_velocity, y_top, y_bottom):
    if initial_velocity < 0:
        distance = triangle(-initial_velocity - 1 + step) - triangle(-initial_velocity - 1)
    else:
        apex = triangle(initial_velocity)
        distance = triangle(step - initial_velocity - 1) - apex
    return -distance >= y_bottom and -distance <= y_top


def main(data_path):
    x_range, y_range = get_data(data_path)
    x_left, x_right = x_range
    y_bottom, y_top = y_range
    max_step = y_bottom * -2

    velocities = set()
    for step in range(1, max_step + 1):
        
        start_x_velocities = []
        for start_x_velocity in range(math.ceil(triangle_height(x_left)), x_right + 1):
            if in_xrange(step, start_x_velocity, x_left, x_right):
                start_x_velocities.append(start_x_velocity)

        start_y_velocities = []
        for start_y_velocity in range(y_bottom, -y_bottom):
            if in_yrange(step, start_y_velocity, y_top, y_bottom):
                start_y_velocities.append(start_y_velocity)
        
        for x in start_x_velocities:
            for y in start_y_velocities:
                velocities.add((x, y))

    return(len(velocities))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 17')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 17
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
