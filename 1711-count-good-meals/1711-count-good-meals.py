class Solution:    
    def countPairs(self, deliciousness: List[int]) -> int:
        d = {}
        powers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152]
        ans = 0
        for i in deliciousness:
            for val in powers:
                if (val - i) in d:
                    ans = (ans + d[val - i]) % (10**9 + 7)
            d[i] = d.get(i,0) + 1
        return ans