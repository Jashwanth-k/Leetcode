class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        def BFS(grid,n,m):
            q = collections.deque()
            visited = set()
            if grid[0][0] == "(":
                q.append((1,0,0,0))
                visited.add((1,0,0,0))

            while len(q) != 0:
                leftc,rightc,i,j = q.popleft()
                if i == n - 1 and j == m - 1 and leftc == rightc:
                    return True

                paths = [[i, j + 1], [i + 1, j]]
                for r, c in paths:
                    if r < n and c < m:
                        nextCell = grid[r][c]
                        newl,newr = leftc,rightc
                        if nextCell == ")":
                            newr += 1
                        else:
                            newl += 1
                        if newl >= newr and (newl, newr, r, c) not in visited:
                            q.append((newl, newr, r, c))
                            visited.add((newl, newr, r, c))
            return False
        
        n,m = len(grid),len(grid[0])
        return BFS(grid,n,m)
                