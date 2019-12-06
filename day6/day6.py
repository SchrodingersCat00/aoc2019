class Node:
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

def read_file_lines():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines


def part1(lines):
    node_dict = {}
    for line in lines:
        parent, child = line.strip().split(')')
        if parent not in node_dict:
            parent_node = Node()
            node_dict[parent] = parent_node
        else:
            parent_node = node_dict[parent]
        if child not in node_dict:
            node_dict[child] = Node(parent_node)
        else:
            node_dict[child].parent = parent_node

    count = 0
    for node in node_dict.values():
        while node.parent is not None:
            node = node.parent
            count += 1

    return count


def part2(lines):
    node_dict = {}
    for line in lines:
        parent, child = line.strip().split(')')
        if parent not in node_dict:
            parent_node = Node()
            node_dict[parent] = parent_node
        else:
            parent_node = node_dict[parent]
        if child not in node_dict:
            node_dict[child] = Node(parent_node)
        else:
            node_dict[child].parent = parent_node

    path = set()
    node = node_dict['YOU']
    while node.parent is not None:
        path.add(node)
        node = node.parent

    san_count = 0
    total = 0
    node = node_dict['SAN']
    while node not in path:
        node = node.parent
        total += 1

    while node is not None:
        node = node.parent
        san_count += 1
        total += 1

    return len(path) + total - 2*san_count - 1


def main():
    lines = read_file_lines()
    print(part2(lines))

if __name__ == '__main__':
    main()
