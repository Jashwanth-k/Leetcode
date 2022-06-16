class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def countRotten():
            rotten = []
            for i in range(n):
                for j in range(m):
                    if (i,j) not in used and grid[i][j] == 2:
                        rotten.append([i,j])
            return rotten
        
        n,m = len(grid),len(grid[0])
        minutes = 0
        used = set()
        rotten = countRotten()

        while rotten:
            flag = False
            for i,j in rotten:
                used.add((i,j))
                paths = [[i,j+1],[i,j-1],[i+1,j],[i-1,j]]
                for r,c in paths:
                    if 0 <= r < n and 0 <= c < m and grid[r][c] == 1: 
                        grid[r][c] = 2
                        flag = True
            if flag:
                minutes += 1
            rotten = countRotten()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return minutes
                    