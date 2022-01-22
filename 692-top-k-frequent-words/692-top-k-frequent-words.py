class PQnode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def __percolateDown(a,idx,n):
            parentIdx = idx
            while parentIdx < n:
                LCidx = (2*parentIdx) + 1
                RCidx = (2*parentIdx) + 2
                minIdx = parentIdx

                if LCidx < n and a[LCidx].priority > a[minIdx].priority:
                    minIdx = LCidx
                if RCidx < n and a[RCidx].priority > a[minIdx].priority:
                    minIdx = RCidx
                    
                if LCidx < n and a[LCidx].priority == a[minIdx].priority:
                    if a[LCidx].value < a[minIdx].value:
                        minIdx = LCidx
                    
                if RCidx < n and a[RCidx].priority == a[minIdx].priority:
                    if a[RCidx].value < a[minIdx].value:
                        minIdx = RCidx

                if parentIdx == minIdx:
                    break
                a[parentIdx],a[minIdx] = a[minIdx],a[parentIdx]
                parentIdx = minIdx
        
        self.pq = []
        d = {}
        for i in words:
            d[i] = d.get(i,0) + 1
        
        for i in d:
            node = PQnode(i,d[i])
            self.pq.append(node)
            
        n = len(self.pq)
        for i in range(n//2-1,-1,-1):
            __percolateDown(self.pq,i,n)
            
        output = []
        for i in range(k):
            output.append(self.pq[0].value)
            self.pq[0] = self.pq[len(self.pq)-1]
            self.pq.pop()
            __percolateDown(self.pq,0,len(self.pq))
        return output
        