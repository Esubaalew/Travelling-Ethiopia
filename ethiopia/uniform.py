import heapq


def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = {}
    
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        
        if node == goal:
            return cost, path + [node]
        
        if node in visited and visited[node] <= cost:
            continue
            
        visited[node] = cost
        
        for neighbor, edge_cost in graph[node].items():
            new_cost = cost + edge_cost
            new_path = path + [node]
            if neighbor not in visited or new_cost < visited.get(neighbor, float('inf')):
                heapq.heappush(priority_queue, (new_cost, neighbor, new_path))
    
    return float("inf"), []
