class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.d = []
        self.idx = 0
        prev = 0
        for i in range(0,len(encoding)-1,2):
            freq,val = encoding[i],encoding[i+1]
            if freq == 0: continue
            pairs = [val,prev+1,prev+freq]
            self.d.append(pairs)
            prev = pairs[2]

    def next(self, n: int) -> int:
        self.idx += n
        val = -1
        for i in range(len(self.d)):
            key,start,end = self.d[i]
            if start <= self.idx <= end:
                val = key
                self.d[i] = [key,self.idx,end]
        return val

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)