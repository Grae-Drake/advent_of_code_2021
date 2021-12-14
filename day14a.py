import argparse
from collections import defaultdict


def get_data(data_path):
    with open(data_path) as file:
        seed, raw_rules = file.read().split('\n\n')
        seed = seed.rstrip()
        rules = {}
        for raw_rule in raw_rules.rstrip().split('\n'):
            x, y = raw_rule.split(' -> ')
            rules[x] = y
        
        return (seed, rules)


def pairs(seed):
    return [''.join(pair) for pair in zip(seed[:-1], seed[1:])]


def main(data_path):
        seed, rules = get_data(data_path)
        for x in range(10):
            daughters = []
            for pair in pairs(seed):
                daughters.append(rules[pair])
            new_seed = seed[0]
            for i, char in enumerate(seed[1:]):
                new_seed += daughters[i] + char
            seed = new_seed
        
        element_counts = defaultdict(int)
        for element in seed:
            element_counts[element] += 1

        return max(element_counts.values()) - min(element_counts.values())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 14')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 14
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
