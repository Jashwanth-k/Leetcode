import queue
class Solution:
    def explore(self,maze,entrance,n,m):
        q = queue.Queue()
        q.put([entrance[0],entrance[1],0])
        ans = float('inf')
        while not q.empty():
            r,c,moves = q.get()
            maze[r][c] = '+'
            if moves > 0 and (r == n-1 or c == m-1 or r == 0 or c == 0):
                ans = min(ans,moves)
                continue

            if c+1 < m and maze[r][c+1] != '+':
                q.put([r,c+1,moves+1])
                maze[r][c+1] = '+'

            if c-1 >= 0 and maze[r][c-1] != '+':
                q.put([r,c-1,moves+1])
                maze[r][c-1] = '+'

            if r+1 < n and maze[r+1][c] != '+':
                q.put([r+1,c,moves+1])
                maze[r+1][c] = '+'

            if r-1 >= 0 and maze[r-1][c] != '+':
                q.put([r-1,c,moves+1])
                maze[r-1][c] = '+'
        return ans
    
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        ans = self.explore(maze,entrance,n,m)
        return -1 if ans == float('inf') else ans