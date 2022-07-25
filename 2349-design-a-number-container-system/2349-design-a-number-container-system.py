from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.d = collections.defaultdict(SortedList)
        self.used = {}
        return

    def change(self, index: int, number: int) -> None:
        self.d[number].add(index)
        if index in self.used:
            prevNbr = self.used[index]
            self.d[prevNbr].discard(index)
            if len(self.d[prevNbr]) == 0:
                self.d.pop(prevNbr)
        self.used[index] = number
        return

    def find(self, number: int) -> int:
        if number in self.d:
            return self.d[number][0]
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)