import argparse


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
    return all([True if (matrix[i][j] < x) else False for x in adjacent])


def main(data_path):
    matrix = get_data(data_path)
    low_points = []
    for i, row in enumerate(matrix):
        for j, n in enumerate(row):
            if is_low(matrix, i, j):
                low_points.append(n)

    print(low_points)
    return len(low_points) + sum(low_points)
            
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 9')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 9
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

