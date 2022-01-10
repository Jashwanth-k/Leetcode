import queue
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        d = {}
        for i in edges:
            d[i[0]] = d.get(i[0],[]) + [i[1]]
            d[i[1]] = d.get(i[1],[]) + [i[0]]

        q = queue.Queue()
        visited = [False] * n
        q.put(start)
        while not q.empty():
            curr = q.get()
            if curr == end:
                return True
            while curr in d and d[curr] != []:
                ans = d[curr].pop(0)
                if visited[ans] == False: q.put(ans)
                visited[ans] = True

        return False