import argparse


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


def main(data_path):
    x_range, y_range = get_data(data_path)
    y_bottom = y_range[0]
    return triangle(-y_bottom - 1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 17')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 17
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
