import heapq

# Graph definition
graph = {
    'A': {'B': 22, 'D': 30, 'E': 25},
    'B': {'A': 22, 'C': 20, 'D': 11},
    'C': {'B': 20},
    'D': {'A': 30, 'B': 11, 'F': 10},
    'E': {'A': 25, 'F': 25, 'G': 40},
    'F': {'D': 10, 'E': 25, 'G': 12},
    'G': {'E': 40, 'F': 12, 'H': 6},
    'H': {'G': 6}
}

# Heuristic values
heuristic = {
    'A': 46, 'B': 39, 'C': 41, 'D': 29, 'E': 38, 'F': 17, 'G': 6, 'H': 0
}

def a_star_search(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start))
    
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None

# Perform A* search from 'A' to 'H'
path = a_star_search(graph, 'A', 'H', heuristic)
print(path)
