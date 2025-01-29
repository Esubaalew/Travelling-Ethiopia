import heapq


class AStarSearch:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def a_star(self, start, goal):
        open_list = []
        closed_list = set()
        came_from = {}

        # Initialize the start node
        # (f, g, node)
        heapq.heappush(open_list, (0 + self.heuristic[start], 0, start))

        g_scores = {start: 0}
        f_scores = {start: self.heuristic[start]}

        while open_list:
            _, current_g, current = heapq.heappop(open_list)

            # If goal is reached, reconstruct the path
            if current == goal:
                return self.reconstruct_path(came_from, current)

            closed_list.add(current)

            for neighbor, cost in self.graph.get(current, {}).items():
                if neighbor in closed_list:
                    continue

                tentative_g_score = current_g + cost

                if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                    came_from[neighbor] = current
                    g_scores[neighbor] = tentative_g_score
                    f_scores[neighbor] = tentative_g_score + \
                        self.heuristic[neighbor]
                    heapq.heappush(
                        open_list, (f_scores[neighbor], tentative_g_score, neighbor))

        return None  # No path found

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]
