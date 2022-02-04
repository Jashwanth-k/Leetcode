import numpy as np
class Solution:
    def explore(self,r,c,n,m,solution,visited,helper,path = None):
        if r >= n or c >= m or r < 0 or c < 0 or visited[r][c] == True:
            return
        
        present = solution[r][c]
        if path != None and present[helper[path]] == False:
            return
        
        if r == n-1 and c == m-1:
            return True
        
        visited[r][c] = True
        if present['R']:
            if self.explore(r,c+1,n,m,solution,visited,helper,'R'): return True
        if present['L']:
            if self.explore(r,c-1,n,m,solution,visited,helper,'L'): return True
        if present['U']:
            if self.explore(r-1,c,n,m,solution,visited,helper,'U'): return True
        if present['D']:
            if self.explore(r+1,c,n,m,solution,visited,helper,'D'): return True
        
        visited[r][c] = False
        return
    
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {1: {'L': True, 'R': True, 'U': False, 'D': False}, 2: {'L': False, 'R': False, 'U': True, 'D': True}, 3: {'L': True, 'R': False, 'U': False, 'D': True}, 4: {'L': False, 'R': True, 'U': False, 'D': True}, 5: {'L': True, 'R': False, 'U': True, 'D': False}, 6: {'L': False, 'R': True, 'U': True, 'D': False}}
        helper = {'L' : 'R' , 'R' : 'L', 'U' : 'D', 'D' : 'U'}
        
        n = len(grid)
        m = len(grid[0])
        solution = [[0 for i in range(m)] for j in range(n)]
        visited = [[False for i in range(m)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                solution[i][j] = directions[grid[i][j]]
                
        return self.explore(0,0,n,m,solution,visited,helper)
