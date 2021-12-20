import argparse
import math


def get_data(data_path):
    with open(data_path) as file:
        return [line.rstrip() for line in file.readlines()]


class Node():
    def __init__(self, value, children, left_neighbor, right_neighbor, parent, depth, graph):
        self.value = value
        self.children = children
        self.left_neighbor = left_neighbor
        self.right_neighbor = right_neighbor
        self.parent = parent
        self.depth = depth
        self.graph = graph


class Graph():
    def __init__(self, root, head, tail, reduced):
        self.root = root
        self.head = head
        self.tail = tail
        self.reduced = reduced


def bury(node):
    '''Recursively increment the depth for each node in a subgraph.'''
    node.depth += 1
    for child in node.children:
        bury(child)


def update_graph(node, graph):
    '''Recursively update the graph property for each node in a subgraph.'''
    node.graph = graph
    for child in node.children:
        update_graph(child, graph)


def split(node):
    '''Replace a large value with a pair.'''

    # Create new child nodes.
    depth = node.depth + 1
    left_child = Node(int(math.floor(node.value / 2)), None, None, None, node, depth, node.graph)
    right_child = Node(int(math.ceil(node.value / 2)), None, None, None, node, depth, node.graph)
    
    # Update neighbor pointers.
    left_child.right_neighbor = right_child
    left_child.left_neighbor = node.left_neighbor
    right_child.left_neighbor = left_child
    right_child.right_neighbor = node.right_neighbor
    if left_child.left_neighbor is not None:
        left_child.left_neighbor.right_neighbor = left_child
    if right_child.right_neighbor is not None:
        right_child.right_neighbor.left_neighbor = right_child
    
    # Update exploded node properties.
    node.children = [left_child, right_child]
    node.value = None
    node.left_neighbor = None
    node.right_neighbor = None

    # Update graph properties.
    node.graph.reduced = False
    if left_child.left_neighbor is None:
        node.graph.head = left_child
    if right_child.right_neighbor is None:
        node.graph.tail = right_child


def explode(node):
    '''Replace each deep pair with 0, propigate the pair values left and right.'''
        
    # Shift all references to the children of the exploding node.
    node.left_neighbor = node.children[0].left_neighbor
    node.left_neighbor.right_neighbor = node
    node.right_neighbor = node.children[1].right_neighbor
    node.rightneighbor.left_neighbor = node
    
    # Propagate the exploded values left and right.
    node.left_neighbor.value += node.children[0].value
    node.right_neighbor.value += node.children[1].value

    # Remove children
    node.children = None
    node.value = 0


def reduce(graph):
    while not graph.reduced:
        graph.reduced = True
        
        # Explode all deep nodes.
        node = graph.head
        while node is not None:
            if node.depth > 4:
                explode(node)
                graph.reduced = False
            node = node.right_neighbor


        # Split first large node, then restart loop.
        node = graph.head
        while node is not None:
            if node.value > 9:
                split(node)
                graph.reduced = False
                break
            else:
                node = node.right_neighbor


def add(graph1, graph2):
    root = Node(graph1.root, graph2.root, None, None, None, -1)
    bury(root)
    graph1.tail.right_neighbor = graph2.head
    graph2.head.left_neighbor = graph1.tail
    graph = Graph(root, graph1.head, graph2.tail, False)
    while not graph.reduced:
        reduce(graph)
    return graph


def magnitude(node):
    left = node.left_child if isinstance(node.left_child, int) else magnitude(node.left_child)
    right = node.right_child if isinstance(node.right_child, int) else magnitude(node.left_child)
    return 3 * left + 2 * right


def main(data_path):
    # ADD two numbers
    #   - Create a parent, first number is left child, second is right child.
    #   - REDUCE the number. Repeatedly do the FIRST of:
    #     - EXPLODE the leftmost 4-nested pair.
    #     _ SPLIT the leftmost number of 10 or higher.
    #     
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Day 18')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='use test data (default: use real data)')
    args = parser.parse_args()
    day = 18
    data_path = 'data/day' + str(day) + ('_test' if args.test else '') + '.txt'
    print(main(data_path))
