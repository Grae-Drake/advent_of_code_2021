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
    for x in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        new_i = i + x[0]
        new_j = j + x[1]
        if in_bounds(matrix, new_i, new_j):
            adjacent.append(matrix[new_i][new_j])
    return all([True if (matrix[i][j] < x) else False for x in adjacent])


def basin(matrix, i, j):
    count = 1
    for x in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        new_i = i + x[0]
        new_j = j + x[1]
        if in_bounds(matrix, new_i, new_j):
            if matrix[new_i][new_j]['basin'] is None:
                count += basin(matrix, new_i, new_j)
    return count


def main(data_path):
    matrix = get_data(data_path)
    
    low_points = []
    for i, row in enumerate(matrix):
        for j, n in enumerate(row):
            # Revise matrix for tracking basin affiliation.
            matrix[i][j] = {
                'height': n,
                'basin': None
            }
            
            # Get a list of low points.
            if is_low(matrix, i, j):
                low_points.append((i, j))

    print(low_points)
    basins = []
    for low_point in low_points:
        basins.append(basin(matrix, low_point[0], low_point[1]))
    return max(basins)
            
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 9')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 9
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

