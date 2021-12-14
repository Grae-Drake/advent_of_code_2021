import argparse


def get_data(data_path):
    with open(data_path) as file:
        raw_points, raw_folds = file.read().split('\n\n')
        points = []
        for point in raw_points.rstrip().split('\n'):
            x, y = point.split(',')
            points.append((int(x), int(y)))

        folds = []
        for fold in raw_folds.rstrip().split('\n'):
            axis, intercept = fold.split('=')
            intercept = int(intercept)
            axis = 'x' if 'x' in axis else 'y'
            folds.append({'axis': axis, 'intercept': intercept})
        
        return (points, folds)


def main(data_path):
    points, folds = get_data(data_path)
    for fold in folds:
        axis = fold['axis']
        intercept = fold['intercept']
        result = set()
        for point in points:
            x = point[0]
            y = point[1]
            if axis == 'x' and x > intercept:
                x = intercept * 2 - x
            if axis == 'y' and y > intercept:
                y = intercept * 2 - y
            result.add((x, y))
        points = result
    
    width = max([point[0] for point in points]) + 1
    depth = max([point[1] for point in points]) + 1

    row = [' '] * width
    matrix = []
    for _ in range(depth):
        matrix.append(row.copy())
    for x, y in points:
        matrix[y][x] = "#"
    print(points)
    for row in matrix:
        print(''.join(row))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 13')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 13
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
