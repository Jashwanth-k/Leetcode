class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        n = len(grid)
        visited = set()
        if grid[0][0] == 0:
            q.append((0,0,1))
            visited.add((0,0))
            
        while q:
            i,j,ct = q.popleft()
            if i == j == n-1:
                return ct
            
            paths = [[i,j+1],[i,j-1],[i+1,j],[i-1,j],[i+1,j+1],[i-1,j+1],[i-1,j-1],[i+1,j-1]]
            for r,c in paths:
                if 0 <= r < n and 0 <= c < n and grid[r][c] == 0 and (r,c) not in visited:
                    q.append((r,c,ct+1))
                    visited.add((r,c))
        return -1