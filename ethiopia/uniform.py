import heapq


def uniform_cost_search(graph, start, goal):
    """Uniform Cost Search implementation."""

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


def customized_ucs(graph, start, goals):
    """Uniform Cost Search with multiple goals."""

    goals = set(goals)

    priority_queue = [(0, start, set(), [])]
    visited = {}  # Tracks {(node, frozenset(visited_goals)): min_cost}

    while priority_queue:
        cost, node, visited_goals, path = heapq.heappop(priority_queue)

        # Update visited goals
        if node in goals and node not in visited_goals:
            new_visited = visited_goals | {node}
        else:
            new_visited = visited_goals

        # Termination check
        if new_visited == goals:
            return cost, path + [node]

        # State pruning
        state_key = (node, frozenset(new_visited))
        if state_key in visited and visited[state_key] <= cost:
            continue
        visited[state_key] = cost

        # Expand neighbors
        for neighbor, edge_cost in graph[node].items():
            new_cost = cost + edge_cost
            new_path = path + [node]
            heapq.heappush(
                priority_queue,
                (new_cost, neighbor, new_visited.copy(), new_path)
            )

    return float("inf"), []
