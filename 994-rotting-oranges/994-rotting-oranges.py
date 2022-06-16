class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        minutes = 0
        fresh = 0
        
        q = collections.deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
        q.append((None,None))
                    
        while len(q) != 0:
            r,c = q.popleft()
            if r == None:
                minutes += 1
                if len(q) == 0:
                    break
                q.append((None,None))
                continue
            
            paths = [[r,c+1],[r,c-1],[r-1,c],[r+1,c]]
            for i,j in paths:
                if 0 <= i < n and 0 <= j < m and grid[i][j] == 1:
                    fresh -= 1
                    grid[i][j] = 2
                    q.append([i,j])
        return minutes-1 if fresh == 0 else -1