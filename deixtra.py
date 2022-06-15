infinity = float('inf')

graph = {}
graph['start'] = {
    'a': 5,
    'b': 2
}
graph['a'] = {
    'c': 2,
    'd': 4
}
graph['b'] = {
    'a': 8,
    'c': 4
}
graph['c'] = {
    'fin': 1
}
graph['d'] = {
    'c': 6,
    'fin': 3,
}

graph['fin'] = {}

costs = {
    'a': 5,
    'b': 2,
    'c': infinity,
    'd': infinity,
    'fin': infinity
}

parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

processed = []


def find_lowest_cost_node(nodes):
    nodes = [node for node in nodes.items() if node not in processed]
    if not nodes:
        return None
    min_node = min(nodes, key=lambda x: x[1])
    processed.append(min_node)
    return min_node[0]


def deixtra():
    node = find_lowest_cost_node(costs)
    while node is not None:
        neighbors = graph[node]
        for neighbor in neighbors:
            cost_to_neighbor_node = costs[node] + neighbors[neighbor]
            if cost_to_neighbor_node < costs[neighbor]:
                parents[neighbor] = node
                costs[neighbor] = cost_to_neighbor_node
        node = find_lowest_cost_node(costs)
    return print_path()

def print_path():
    path = ['fin']
    while parents[path[-1]] != 'start':
        path.append(parents[path[-1]])
    path.append(parents[path[-1]])
    path.reverse()
    return ' -> '.join(path)

print(deixtra())


