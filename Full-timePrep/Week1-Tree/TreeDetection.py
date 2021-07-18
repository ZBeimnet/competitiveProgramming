class Solution:
    def solve(self, left, right):
        root = -1
        left_set = set(left)
        right_set = set(right)
        
        for i in range(len(left)):
            if i not in left_set and i not in right_set:
                root = i
                break
        if root == -1:
            return False
        
        stack = [root]
        visited = {root}

        while stack:
            node = stack.pop()
            for child in [left[node], right[node]]:
                if child in visited:
                    return False
                if child != -1:
                    stack.append(child)
                    visited.add(child)
        
        return len(left) == len(visited)
