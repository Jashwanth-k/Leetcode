from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.data = SortedList()
        return
    def binarySearch(self,tar):
        si = 0
        ei = len(self.data)-1
        while si <= ei:
            mid = si + (ei-si) // 2
            l,r = self.data[mid]
            if (l <= tar[0] < r) or (l < tar[1] < r) or (l >= tar[0] and r <= tar[1]):
                return True
            if tar[1] <= l:
                ei = mid-1
            else:
                si = mid+1
        return False
        
    def book(self, start: int, end: int) -> bool:
        if self.binarySearch([start,end]):
            return False
        self.data.add((start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)