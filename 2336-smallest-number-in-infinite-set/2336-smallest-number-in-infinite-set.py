from heapq import heappush,heappop

class SmallestInfiniteSet:
    def __init__(self):
        self.freq = 1
        self.pq = []
        self.present = set()
        return

    def popSmallest(self) -> int:
        if self.pq:
            res = heappop(self.pq)
            self.present.remove(res)
            return res
        res = self.freq
        self.freq += 1
        return res

    def addBack(self, num: int) -> None:
        if num < self.freq and num not in self.present:
            heappush(self.pq,num)
            self.present.add(num)
        return
            
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)