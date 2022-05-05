class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.d = {}
        self.nbr = 0
        count = 0
        for i in range(0,len(encoding)-1,2):
            freq,val = encoding[i],encoding[i+1]
            if freq == 0: continue
            self.d[count + freq] = val
            count += freq
        self.bs = list(self.d.keys())
        self.len = len(self.bs)

    def next(self, n: int) -> int:
        self.nbr += n
        si = 0
        ei = self.len - 1
        while si <= ei:
            mid = si + (ei - si) // 2
            if self.nbr == self.bs[mid]:
                return self.d[self.bs[mid]]
            if self.nbr > self.bs[mid]:
                si = mid + 1
            else:
                ei = mid - 1
                
        if si >= self.len:  return -1
        return self.d[self.bs[si]]

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)