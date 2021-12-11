import argparse


def get_data(data_path):
    with open(data_path) as file:
        return [line.rstrip() for line in file.readlines()]


def main(data_path):
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    complement = {')': '(', ']': '[', '}': '{', '>': '<'}
    openers = '([{<'
    
    result = 0
    data = get_data(data_path)
    for line in data:
        stack = []
        for char in line:
            if char in openers:
                stack.append(char)
            elif complement[char] == stack[-1]:
                stack.pop()
            else:
                result += scores[char]
                break
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 10')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 10
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
