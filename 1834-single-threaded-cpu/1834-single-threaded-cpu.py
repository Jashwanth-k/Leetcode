from heapq import heappush,heappop
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            tasks[i].append(i)
        tasks.sort()
        
        pq = []
        res = []
        idx = 0
        time = tasks[0][0]
        while idx < n:
            while idx < n and time >= tasks[idx][0]:
                heappush(pq,(tasks[idx][1],tasks[idx][2]))
                idx += 1
            if pq:
                resPro,resIdx = heappop(pq)
                res.append(resIdx)
                time += resPro
            if idx < n and not pq and time < tasks[idx][0]:
                time = tasks[idx][0]
        while pq:
            res.append(heappop(pq)[1]) 
        return res