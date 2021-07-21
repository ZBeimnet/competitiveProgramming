from collections import deque
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = [x for x in dominoes]
        queue = deque([i for i in range(len(dominoes)) if dominoes[i] != '.'])
        
        while queue:
            size = len(queue)
            visited = set()
            for _ in range(size):
                idx = queue.popleft()
                if dominoes[idx] == 'L' and idx - 1 >= 0:
                    if dominoes[idx-1] == '.':
                        dominoes[idx-1] = 'L'
                        queue.append(idx - 1)
                        visited.add(idx - 1)
                    elif idx - 1 in visited and dominoes[idx-1] == 'R':
                        dominoes[idx-1] = '.'
                elif dominoes[idx] == 'R' and idx + 1 < len(dominoes):
                    if dominoes[idx+1] == '.':
                        dominoes[idx+1] = 'R'
                        queue.append(idx + 1)
                        visited.add(idx + 1)
                    elif idx + 1 in visited and dominoes[idx+1] == 'L':
                        dominoes[idx+1] = '.'
                        
        return "".join(dominoes)