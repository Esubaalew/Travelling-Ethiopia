from collections import deque


class EthiopiaSearch:
    """Handles Ethiopia travel route search using BFS and DFS strategies."""

    def __init__(self, graph):
        """Initialize with the state space graph.

        Args:
            graph (dict): City connections in adjacency list format
        """
        self.graph = graph

    def bfs(self, start, goal):
        """Breadth-First Search implementation for shortest path finding."""
        visited = set()
        queue = deque([[start]])

        while queue:
            path = queue.popleft()
            current = path[-1]

            if current == goal:
                return path

            if current not in visited:
                visited.add(current)
                for neighbor in self.graph.get(current, []):
                    queue.append(path + [neighbor])

        return None

    def dfs(self, start, goal):
        """Depth-First Search implementation for path finding."""
        visited = set()
        stack = [[start]]

        while stack:
            path = stack.pop()
            current = path[-1]

            if current == goal:
                return path

            if current not in visited:
                visited.add(current)

                for neighbor in (self.graph.get(current, [])):
                    stack.append(path + [neighbor])

        return None
