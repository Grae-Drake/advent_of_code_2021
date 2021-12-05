import argparse
import sys


def get_data(data_path):
    with open(data_path) as file:
        numbers = [int(x) for x in file.readline().rstrip().split(',')]
        file.readline()
        boards = [[[
            int(n) for n in row.split()]
            for row in board.split('\n')]
            for board in file.read().split('\n\n')]
        return (numbers, boards)


class Board:
    def __init__(self, raw_board):
        self.raw = raw_board
        self.height = len(self.raw)
        self.width = len(self.raw[0])
        
        self.row_matches = [0 for x in range(self.height)]
        self.column_matches = [0 for x in range(self.width)]
        
        self.sum = sum([sum(row) for row in self.raw])
        self.winner = False
        self.positions = {}
        for i, row in enumerate(self.raw):
            for j, n in enumerate(row):
                self.positions[n] = (i, j)

    
    def handle_draw(self, n):
        if n in self.positions:
            i, j = self.positions[n]
            self.row_matches[i] += 1
            self.column_matches[j] += 1
            self.raw[i][j] = 0
            self.sum -= n
            if self.row_matches[i] == self.width or self.column_matches[j] == self.height:
                self.winner = True


def main(data_path):
    numbers, raw_boards = get_data(data_path)
    boards = [Board(raw_board) for raw_board in raw_boards]
    wincount = 0
    for n in numbers:
        for board in boards:
            if not board.winner:
                board.handle_draw(n)
                if board.winner:
                    wincount += 1
                    if wincount == len(boards):
                        return board.sum * n


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 4, Problem 1')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 4
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))

