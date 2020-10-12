"""
run bfs starting from '0000' to target, our state -> (current_lock , turns), e.g. ("0000", 0)
at each step:
    # we check if we've reached our target
    # we will generate our possible next moves 
    # we proceed to the ones that are not in the deadends and 
      the ones we haven't seen before
"""
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)         
        if "0000" in deadends:
            return -1
        
        queue = deque([("0000", 0)]) # current, turns
        visited = {"0000"}
        
        while queue:
            lock, turn = queue.popleft()
            
            if lock == target:
                return turn
            
            for move in self.generateNextMoves(lock):
                if move not in deadends and move not in visited:
                    queue.append((move, turn + 1))
                    visited.add(move)
        
        return -1
    
    
    def generateNextMoves(self, lock):
        moves = []
        
        for i in range(len(lock)):
            lock_copy1 = list(lock)
            lock_copy2 = list(lock)
            
            if lock[i] == "0":
                lock_copy1[i] = "1"
                lock_copy2[i] = "9"
            elif lock[i] == "9":
                lock_copy1[i] = "0"
                lock_copy2[i] = "8"
            else:
                lock_copy1[i] = str(int(lock_copy1[i]) + 1)
                lock_copy2[i] = str(int(lock_copy2[i]) - 1)
            
            moves.append("".join(lock_copy1))
            moves.append("".join(lock_copy2))
        
        return moves
