class Solution:
    def numberOfWays(self, s: str) -> int:
        count = Counter(s)
        zeros,ones = count["0"],count["1"]
        lzero = lone = res = 0
        for i in s:
            if i == "1":
                res += lzero * zeros
                lone += 1
                ones -= 1
            else:
                res += lone * ones
                lzero += 1
                zeros -= 1
        return res