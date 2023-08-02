from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

def bidirectional_search(graph, start, goal):
    forward_queue = deque([(start, [start])])
    backward_queue = deque([(goal, [goal])])

    forward_visited = set([start])
    backward_visited = set([goal])

    forward_paths = {start: [start]}
    backward_paths = {goal: [goal]}

    while forward_queue and backward_queue:
        current_node, path = forward_queue.popleft()
        for neighbor in graph.graph[current_node]:
            if neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_queue.append((neighbor, path + [neighbor]))
                forward_paths[neighbor] = path + [neighbor]
                if neighbor in backward_visited:
                    return forward_paths[neighbor] + backward_paths[neighbor][::-1]

        current_node, path = backward_queue.popleft()
        for neighbor in graph.graph[current_node]:
            if neighbor not in backward_visited:
                backward_visited.add(neighbor)
                backward_queue.append((neighbor, path + [neighbor]))
                backward_paths[neighbor] = path + [neighbor]
                if neighbor in forward_visited:
                    return forward_paths[neighbor] + backward_paths[neighbor][::-1]

    return None  

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(7, 8)

    start_node = 1
    goal_node = 8

    path = bidirectional_search(graph, start_node, goal_node)

    print('🟥')
    if path:
        print("Path found:", path)
    else:
        print(f"No path found between {start_node} and {goal_node}")
