import argparse


def get_data(data_path):
    with open(data_path) as file:
        result = []
        for line in file.readlines():
            result.append([int(x) for x in line.rstrip()])
        return result


def get_parents(i, j):
    result = []
    if i > 0:
        result.append([i - 1, j])
    if j > 0:
        result.append([i, j - 1])
    return result


def main(data_path):
    # Load data.
    data = get_data(data_path)
    
    # Initilaze empty matrix.
    side = len(data) * 5
    matrix = [[0 for x in range(side)] for y in range(side)]

    # Populate risk levels in each matrix.
    for i, row in enumerate(data):
        for j, n in enumerate(row):
            for i_tile in range(5):
                for j_tile in range(5):
                    i_m = i + i_tile * (side / 5)
                    j_m = j + j_tile * (side / 5)
                    matrix[i_m][j_m] = (n - 1 + i_tile + j_tile) % 9 + 1
    matrix[0][0] = 0

    # Pathfind.
    i = 0
    j = 0
    while i < side -1 or j < side - 1:

        # Figure out which cell to evaluate next.
        # First, check whether we've hit an edge.
        if i == 0 and j < side - 1:
            i = min(j + 1, side - 1)
            j = 0
        elif i == 0 and j == side - 1:
            i = side - 1
            j = 1
        elif j == side - 1:
            j = i + 1
            i = side - 1
        else:
            i -= 1
            j += 1

        # Update each cell with the lowest cost to reach it.
        parents_coordinates = get_parents(i, j)
        parents = [matrix[x[0]][x[1]] for x in parents_coordinates]
        matrix[i][j] = matrix[i][j] + min(parents)
    
    return matrix[side - 1][side - 1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 15')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 15
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
