class MapSum:

    def __init__(self):
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val

    def sum(self, prefix: str) -> int:
        count,l = 0,len(prefix)
        for key in self.d:
            if l > len(key):
                continue
            else:
                if key[0:l] == prefix:
                    count += self.d[key]
        return count
            
            

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)