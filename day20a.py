import argparse


def get_data(data_path):
    with open(data_path) as file:
        algo, image = file.read().split('\n\n')
        algo = algo.rstrip()
        image = image.rstrip()
        image = image.split('\n')
        return algo, image


def process_algo(algo_string):
    return ''.join(['1' if char == '#' else '0' for char in algo_string])


def process_image(image_strings):
    result = []
    for str in image_strings:
        row = []
        for char in str:
            row.append('1' if char == '#' else '0')
        result.append(row)
    return result


def window_sum(image, i, j, default):
    result = []

    for i_n in (i - 1, i, i + 1):
        for j_n in (j - 1, j , j + 1):
            if i_n >= 0 and j_n >= 0 and i_n < len(image) and j_n < len(image[0]):
                result.append(image[i_n][j_n])
            else:
                result.append(default)
    return int(''.join(result), 2)


def image_sum(image):
    result = 0
    for row in image:
        for char in row:
            result += int(char)
    return result


def enhance(image, algo, default):
    result = []
    for i in range(len(image) + 2):
        row = []
        for j in range(len(image[0]) + 2):
            w_sum = window_sum(image, i - 1, j - 1, default)
            row.append(algo[w_sum])
        result.append(row)
    return result


def main(data_path):
    algo_string, image_strings = get_data(data_path)
    algo = process_algo(algo_string)
    image = process_image(image_strings)
    defaults = ['0', '1']
    step = 0
    for x in range(50):
        image = enhance(image, algo, defaults[step % 2])
        step += 1
    return image_sum(image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 20')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 20
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
