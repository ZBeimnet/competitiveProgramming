class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # initializing possible next moves from a current point
        left, right, up, down = {1, 6, 4}, {1, 5, 3}, {2, 3, 4}, {2, 5, 6}
        left_dir, right_dir, up_dir, down_dir = (0, -1), (0, 1), (-1, 0), (1, 0)
        
        # building the adjancency list
        adj_list = {
            1: [[left_dir, left],[right_dir, right]],
            2: [[up_dir, up],[down_dir, down]],
            3: [[left_dir, left],[down_dir, down]],
            4: [[right_dir, right],[down_dir, down]],
            5: [[left_dir, left],[up_dir, up]],
            6: [[right_dir, right],[up_dir, up]]
        }
        
        # initializing stack and visited set
        end = (len(grid) - 1, len(grid[0]) - 1)
        stack = [(0, 0)]
        visited = set()
        
        while stack:
            x, y = stack.pop()
            
            # visiting a point
            visited.add((x, y))
            
            # checking if we reached the end
            if (x, y) == end:
                return True
            
            # exploring neighbours 
            for neighbour in adj_list[grid[x][y]]:
                new_x = x + neighbour[0][0]
                new_y = y + neighbour[0][1]
                if 0 <= new_x < len(grid) and \
                    0 <= new_y < len(grid[0]) and \
                     (new_x, new_y) not in visited and \
                      grid[new_x][new_y] in neighbour[1]:
                    stack.append((new_x, new_y))
        
        return False
