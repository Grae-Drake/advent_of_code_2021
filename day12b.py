import argparse
import itertools


def get_data(data_path):
    with open(data_path) as file:
        return [item.rstrip().split('-') for item in file.readlines()]


class Node():
    def __init__(self, name):
        self.name = name
        self.connected = []
        self.lower = name.islower()

    def __repr__(self):
        return 'Node(' + self.name + ')'


def initialize_graph(name_list):
    return {name: Node(name) for name in name_list}


def go(node, visited, backtracked):
    result = 0
    visited = visited.copy()
    visited.add(node)
    if node.name == 'end':
        result += 1
    else:
        for next_node in node.connected:
            if not next_node.lower or next_node not in visited:
                result += go(next_node, visited, backtracked)
            elif next_node.name != 'start' and not backtracked:
                result += go(next_node, visited, True)

    return result


def main(data_path):
    # Parse data and initialize unconnected notes in a graph.
    data = get_data(data_path)
    graph = initialize_graph(list(itertools.chain(*data)))
    
    # Connect up the nodes.
    for a, b in data:
        graph[a].connected.append(graph[b])
        graph[b].connected.append(graph[a])
    
    # Explore the graph and count paths.
    path_count = 0
    for next_node in graph['start'].connected:
        path_count += go(next_node, set([graph['start']]), False)
    return path_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 12')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test1 data (default: use real data)')
    args = parser.parse_args()
    day = 12
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
