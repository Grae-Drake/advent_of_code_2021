import argparse


def get_data(data_path):
    with open(data_path) as file:
        result = []
        for line in file.readlines():
            result.append([int(n) for n in line.rstrip()])
        return result


def energize(matrix, top_left, bottom_right):
    i_tl, j_tl = top_left
    i_tl = max(i_tl, 0)
    j_tl = max(j_tl, 0)
    
    i_br, j_br = bottom_right
    i_br = min(i_br, len(matrix) - 1)
    j_br = min(j_br, len(matrix[0]) - 1)

    to_energize = []
    for i in range(i_tl, i_br + 1):
        for j in range(j_tl, j_br + 1):
            to_energize.append(matrix[i][j])
    
    for point in to_energize:
        if not point['flashed']:
            point['energy'] += 1


def flash(matrix, point):
    i = point['i']
    j = point['j']
    point['energy'] = 0
    point['flashed'] = True
    flash_count = 1
    energize(matrix, (i - 1, j - 1), (i + 1, j + 1))
    for i_new in range(max(i - 1, 0), min(i + 2, len(matrix))):
        for j_new in range(max(j - 1, 0), min(j + 2, len(matrix[0]))):
            point_new = matrix[i_new][j_new]
            if point_new['energy'] > 9:
                flash_count += flash(matrix, point_new)
    return flash_count


def step(matrix):

    # Track flashes per step.
    flash_count = 0

    # Reset flash flags.
    for row in matrix:
        for point in row:
            point['flashed'] = False
    
    # Energize the whole matrix.
    energize(matrix, (0, 0), (len(matrix) - 1, len(matrix[0]) - 1))

    # Initial flashes.
    for row in matrix:
        for point in row:
            if point['energy'] > 9:
                flash_count += flash(matrix, point)

    print(flash_count)
    return flash_count


def main(data_path):
    matrix = get_data(data_path)
    
    # Refactor matrix to track which cells flash.
    for i, row in enumerate(matrix):
        for j, n in enumerate(row):
            matrix[i][j] = {
                'energy': n,
                'flashed': False,
                'i': i,
                'j': j
                }
    
    steps = 0
    while True: 
        steps += 1
        flash_count = step(matrix)
        if flash_count == 100:
            return steps


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 11')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 11
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
