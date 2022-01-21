class PQnode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority

class Solution:
    def __init__(self):
        self.pq = []
        
    def __percolateUp(self):
        childIdx = len(self.pq) - 1
        while childIdx > 0:
            parentIdx = (childIdx - 1)//2
            if self.pq[childIdx].priority > self.pq[parentIdx].priority:
                self.pq[childIdx],self.pq[parentIdx] = self.pq[parentIdx],self.pq[childIdx]
                childIdx = parentIdx
            else:
                break

    def __percolateDown(self):
        parentIdx = 0
        n = len(self.pq)
        
        while parentIdx < n:
            LCidx = 2*(parentIdx) + 1
            RCidx = 2*(parentIdx) + 2
            minIdx = parentIdx

            if LCidx < n and self.pq[LCidx].priority > self.pq[minIdx].priority:
                minIdx = LCidx
            if RCidx < n and self.pq[RCidx].priority > self.pq[minIdx].priority:
                minIdx = RCidx
            if minIdx == parentIdx:
                break

            self.pq[parentIdx],self.pq[minIdx] = self.pq[minIdx],self.pq[parentIdx]
            parentIdx = minIdx
    
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        
        for i in d:
            node = PQnode(i,d[i])
            self.pq.append(node)
            self.__percolateUp()
            
        ans = ''
        while len(self.pq):
            root = self.pq[0]
            self.pq[0] = self.pq[len(self.pq)-1]
            self.pq.pop()
            self.__percolateDown()
            ans += root.value * root.priority
        return ans
            
            