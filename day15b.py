import argparse
from math import inf as infinity
import sys


sys.setrecursionlimit(10000)

def get_data(data_path):
    with open(data_path) as file:
        result = []
        for line in file.readlines():
            result.append([int(x) for x in line.rstrip()])
        return result


def parents(matrix, node):
    result = []
    if node.i > 0:
        result.append(matrix[node.i - 1][node.j])
    if node.j > 0:
        result.append(matrix[node.i][node.j - 1])
    return result


def children(matrix, node):
    result = []
    if node.i < len(matrix) - 1:
        result.append(matrix[node.i + 1][node.j])
    if node.j < len(matrix[0]) - 1:
        result.append(matrix[node.i][node.j + 1])
    return result


class Node():
    def __init__(self, risk, i, j):
        self.risk = risk
        self.sum = infinity
        self.i = i
        self.j = j
        self.children = []
        self.parents = []
        self.visited = False


def get_matrix(data, tiles):
    
    side = len(data) * tiles
    matrix = [[0 for x in range(side)] for y in range(side)]
    
    for i, row in enumerate(data):
        for j, n in enumerate(row):
            for i_tile in range(tiles):
                for j_tile in range(tiles):
                    i_m = i + i_tile * (len(data))
                    j_m = j + j_tile * (len(data))
                    risk = (n - 1 + i_tile + j_tile) % 9 + 1
                    matrix[i_m][j_m] = Node(risk, i_m, j_m)
    
    matrix[0][0].risk = 0
    matrix[0][0].sum = 0
    matrix[0][0].visited = True
    
    for row in matrix:
        for node in row:
            node.children = children(matrix, node)
            node.parents = parents(matrix, node)
            node.neighbors = node.children + node.parents
    
    return matrix


def visit(node):
    
    # Normal case propagating forwards.
    if not node.visited:
        if all(parent.visited for parent in node.parents):
            node.sum = min(parent.sum for parent in node.parents) + node.risk
            node.visited = True
            
            # Check whether to backpropagate.
            for neighbor in node.neighbors:
                if neighbor.visited and neighbor.sum > node.sum + neighbor.risk:
                    visit(neighbor)

            # Continue propagating through children.
            for child in node.children:
                if all(parent.visited for parent in child.parents):
                    visit(child)
    
    # Visit during backpropagation.
    else:
        node.sum = min(neighbor.sum for neighbor in node.neighbors if neighbor.visited) + node.risk
        for neighbor in node.neighbors:
            if neighbor.visited and neighbor.sum > node.sum + neighbor.risk:
                    visit(neighbor)


def main(data_path):
    # Load data.
    data = get_data(data_path)
    
    # Create matrix.
    matrix = get_matrix(data, 5)
    side = len(matrix)

    # Propigate.
    for child in matrix[0][0].children:
        visit(child)
    
    return matrix[side - 1][side - 1].sum


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 15')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 15
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
