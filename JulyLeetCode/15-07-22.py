class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        max_area_of_island = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] ==1:
            
                    curr_max_area_of_island = self.bfs(r, c, grid)
                    max_area_of_island = max(max_area_of_island, curr_max_area_of_island)

        return max_area_of_island
    
    
    def dfs(self, row, col, grid):
        
        if row <0 or col<0  or row>= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        
        grid[row][col] = 0
        # seen.add((row, col))
        
        return 1 + self.dfs(row+1, col, grid) + self.dfs(row-1, col, grid)+self.dfs(row, col+1, grid)+self.dfs(row, col-1, grid)
            
        
        
    def bfs(self, row, col, grid):
        
        from collections import deque
        
        directions =[(1, 0), (-1, 0), (0, 1),(0, -1)]
        
        queue = deque([(row, col)])
        
        count =0 
        while queue:
            
            r, c  = queue.popleft()
            
            count +=1
            
            grid[r][c] = 0
            
            for i, j in directions:
                dir_r = i+r
                dir_c = j +c
                
                if 0<=dir_r<=len(grid)-1 and 0<=dir_c<=len(grid[0])-1 and grid[dir_r][dir_c] ==1:
                    
                    grid[dir_r][dir_c] = 0
                    queue.append((dir_r, dir_c))
                    
        return count
                    
                    
                    
            
            
        
        
        
        
        
        
        
        
        