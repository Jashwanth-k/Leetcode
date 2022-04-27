class MedianFinder:
    def binarySearch(self,target):
        si = 0
        ei = self.length - 1
        while si <= ei:
            mid = si + (ei-si) // 2
            if target == self.nums[mid]:
                return mid
            if target > self.nums[mid]:
                si = mid + 1
            else:
                ei = mid - 1
        return si

    def __init__(self):
        self.nums = []
        self.length = 0

    def addNum(self, num: int) -> None:
        idx = self.binarySearch(num)
        self.nums.insert(idx,num)
        self.length += 1
        return

    def findMedian(self) -> float:
        mid = (self.length-1) // 2
        if self.length % 2 == 0:
            ans = (self.nums[mid] + self.nums[mid+1]) / 2
        else:
            ans = self.nums[mid]
        return ans

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()