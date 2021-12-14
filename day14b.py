import argparse
from collections import defaultdict


def get_data(data_path):
    with open(data_path) as file:
        seed, raw_rules = file.read().split('\n\n')
        seed = seed.rstrip()
        rules = {}
        for raw_rule in raw_rules.rstrip().split('\n'):
            x, y = raw_rule.split(' -> ')
            rules[x] = (x[0] + y, y + x[1])
        
        return (seed, rules)


def pairs(seed):
    return [''.join(pair) for pair in zip(seed[:-1], seed[1:])]


def main(data_path):
        
        # Initialize.
        seed, rules = get_data(data_path)
        pair_counts = defaultdict(int)
        for pair in pairs(seed):
            pair_counts[pair] += 1
        
        # Iterate over n generations.
        for x in range(40):
            new_pair_counts = defaultdict(int)
            for parent in pair_counts:
                daughters = rules[parent]
                for daughter in daughters:
                    new_pair_counts[daughter] += pair_counts[parent]
            pair_counts = new_pair_counts
        
        # Count up the elements of each pair.
        element_counts = defaultdict(int)
        for pair, count in pair_counts.items():
            for element in pair:
                element_counts[element] += count
        
        # Every element is counted twice, EXCEPT for the elements at the start
        # and end of the seed.
        element_counts[seed[0]] += 1
        element_counts[seed[-1]] += 1
        for key, value in element_counts.items():
            element_counts[key] = value / 2

        return max(element_counts.values()) - min(element_counts.values())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 14')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 14
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
