import argparse
from os import defpath


def get_data(data_path):
    with open(data_path) as file:
        result = []
        for row in file.readlines():
            row = row.rstrip()
            result.append([int(x) for x in row])
    return result

    
def in_bounds(matrix, i, j):
    return i >= 0 and \
           j >= 0 and \
           i < len(matrix) and \
           j < len(matrix[0])


def is_low(matrix, i, j):
    adjacent = []
    for i_offset, j_offset in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if in_bounds(matrix, i + i_offset, j + j_offset):
            adjacent.append(matrix[i + i_offset][j + j_offset])
    
    for point in adjacent:
        if point['depth'] <= matrix[i][j]['depth']:
            return False
    return True


def basin_count(matrix, point):
    result = 1
    point['basin'] = True
    for i_offset, j_offset in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        new_i = point['i'] + i_offset
        new_j = point['j'] + j_offset
        if in_bounds(matrix, new_i, new_j):
            if not matrix[new_i][new_j]['basin']:
                result += basin_count(matrix, matrix[new_i][new_j])
    return result


def main(data_path):
    matrix = get_data(data_path)
    
    # Refactor each point in the matrix to track its basin.
    for i, row in enumerate(matrix):
        for j, n in enumerate(row):
            matrix[i][j] = {
                'depth': n,
                'basin': True if n == 9 else False,
                'i': i,
                'j': j}

    # Identify the low points. Each will have a basin.
    low_points = []
    for i, row in enumerate(matrix):
        for j, point in enumerate(row):
            if is_low(matrix, i, j):
                low_points.append(point)

    basin_counts = [basin_count(matrix, point) for point in low_points]
    biggest = sorted(basin_counts)[-3:]
    result = 1
    for n in biggest:
        result *= n
    return result
            
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 9')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 9
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

