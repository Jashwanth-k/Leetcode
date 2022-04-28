class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = collections.deque()
        visited = set()
        visited.add((0,0,k))
        q.append((0,0,0,k))
        m,n = len(grid),len(grid[0])
        
        while q:
            r,c,ct,k = q.popleft()
            if r == m-1 and c == n-1:
                return ct
            
            paths = [[r,c+1],[r,c-1],[r+1,c],[r-1,c]]
            for i,j in paths:
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 1 and k > 0 and (i,j,k-1) not in visited:
                        q.append((i,j,ct+1,k-1))
                        visited.add((i,j,k-1))
                    elif grid[i][j] == 0 and (i,j,k) not in visited:
                        q.append((i,j,ct+1,k))
                        visited.add((i,j,k))
        return -1