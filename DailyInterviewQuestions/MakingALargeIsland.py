class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        point_to_island = {}
        island_size = {}
        island_id = 1
        max_size = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in point_to_island:
                    size = self.dfs(i, j, grid, point_to_island, island_id, neighbours)
                    island_size[island_id] = size
                    max_size = max(max_size, size)
                    island_id += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    neighbour_islands = set()
                    combined_size = 0
                    for new_row, new_col in self.is_inbound(i, j, grid, neighbours):
                        curr_island_id = point_to_island[(new_row, new_col)]
                        neighbour_islands.add(curr_island_id)
                    for island_id in neighbour_islands:
                        combined_size += island_size[island_id]
                    max_size = max(max_size, combined_size + 1)
        
        return max_size
    
    def dfs(self, row, col, grid, point_to_island, island_id, neighbours):
        point_to_island[(row, col)] = island_id
        count = 0
        for new_row, new_col in self.is_inbound(row, col, grid, neighbours):
            if (new_row, new_col) not in point_to_island:
                count += self.dfs(new_row, new_col, grid, point_to_island, island_id, neighbours)
        return count + 1        
    
    def is_inbound(self, row, col, grid, neighbours):
        for x, y in neighbours:
            new_row = row + x
            new_col = col + y
            if 0 <= new_row < len(grid) and \
                0 <= new_col < len(grid[0]) and \
                 grid[new_row][new_col] == 1:
                yield (new_row, new_col)
                            
                            
        
