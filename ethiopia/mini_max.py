class EthiopiaAdversarialSearch:
    def __init__(self, graph, utilities, adversary_positions):
        self.graph = graph  
        self.utilities = utilities 
        self.adversary_positions = adversary_positions 

    def minimax(self, node, depth, maximizing_player):
      
        if depth == 0 or node not in self.graph or not self.graph[node]:
            return self.utilities.get(node, 0)  
        
        if maximizing_player:
            max_eval = float('-inf')
            for child in self.graph[node]:
                if child in self.adversary_positions:
                    continue  
                eval = self.minimax(child, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        
        else: 
            min_eval = float('inf')
            for child in self.graph[node]:
                eval = self.minimax(child, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self, start):
        best_val = float('-inf')
        best_move = None

        for move in self.graph[start]:
            # Skip initial moves blocked by adversaries
            if move in self.adversary_positions:
                continue
            # Evaluate move with depth=3 (agent -> adversary -> agent -> adversary)
            move_val = self.minimax(move, depth=3, maximizing_player=False)
            if move_val > best_val:
                best_val = move_val
                best_move = move

        return best_move, best_val