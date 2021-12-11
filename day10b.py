import argparse


def get_data(data_path):
    with open(data_path) as file:
        return [line.rstrip() for line in file.readlines()]


def string_score(string):
    char_scores = {')': 1, ']': 2, '}': 3, '>': 4}
    result = 0
    for char in string:
        result *= 5
        result += char_scores[char]
    return result


def main(data_path):
    opening_complement = {')': '(', ']': '[', '}': '{', '>': '<'}
    closing_complement = {'(': ')', '[': ']', '{': '}', '<': '>'}
    openers = '([{<'
    
    result = 0
    data = get_data(data_path)
    filtered = []
    for line in data:
        stack = []
        syntax_error = False
        for char in line:
            if char in openers:
                stack.append(char)
            elif opening_complement[char] == stack[-1]:
                stack.pop()
            else:
                syntax_error = True
        if not syntax_error:
            filtered.append(stack)
    
    completion_strings = []
    for line in filtered:
        completion_string = ''
        for char in line[::-1]:
            completion_string += closing_complement[char]
        completion_strings.append(completion_string)
    
    completion_strings.sort(key=string_score)
    return string_score(completion_strings[len(completion_strings) // 2])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 10')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 10
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
