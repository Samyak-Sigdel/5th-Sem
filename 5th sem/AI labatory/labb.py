graph_a = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

print(graph_a)

from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)



def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited
graph_a_set = {key: set(value) for key, value in graph_a.items()}

# For graph_a
print("\nBFS")
bfs(graph_a_set, 'A')


print("\nDFS")
dfs(graph_a_set, 'A')

