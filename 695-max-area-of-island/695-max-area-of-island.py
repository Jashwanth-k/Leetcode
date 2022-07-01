class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def BFS(r,c):
            q = collections.deque()
            q.append([r,c])
            visited.add((r,c))
            totalOnes = 0
            while len(q) != 0:
                r,c = q.popleft()
                totalOnes += 1
                paths = [[r,c+1],[r,c-1],[r+1,c],[r-1,c]]
                for i,j in paths:
                    if (0 <= i < m and 0 <= j < n) and (grid[i][j] == 1) and (i,j) not in visited:
                        visited.add((i,j))
                        q.append([i,j])
            return totalOnes
        
        m,n = len(grid),len(grid[0])
        visited = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or (i,j) in visited: continue
                ans = max(ans,BFS(i,j))
        return ans