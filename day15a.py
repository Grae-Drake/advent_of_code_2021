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
    matrix = get_data(data_path)
    matrix[0][0] = 0
    side = len(matrix)
    i = 0
    j = 0
    while i < len(matrix) -1 or j < len(matrix[0]) - 1:

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
