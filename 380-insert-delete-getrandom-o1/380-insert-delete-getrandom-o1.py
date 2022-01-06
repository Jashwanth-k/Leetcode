import random
class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.a = []
        
    def insert(self, val: int) -> bool:
        if val in self.a:
            return False
        
        self.d[val] = len(self.a)
        self.a.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.a:
            return False
        
        lastEl = self.a[-1]
        idxEltoRemove = self.d[val]
        
        self.a[idxEltoRemove] = lastEl
        self.d[lastEl] = idxEltoRemove
        
        self.a.pop()
        self.d.pop(val)
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.a)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()