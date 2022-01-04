class MapSum:

    def __init__(self):
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val
        # print(self.d)

    def sum(self, prefix: str) -> int:
        count = 0
        for key in self.d.keys():
            prelen = 0
            for i in range(len(prefix)):
                if len(prefix) > len(key) or prefix[i] != key[i]:
                    break
                else:
                    prelen += 1
            if prelen == len(prefix):
                count += self.d[key]
        return count
            
            

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)