class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def helper(a,b):
            if b == 0:
                return 1
            if b == 1:
                return a
            
            if b % 2 == 0:
                return helper(a*a % mod, b // 2) % mod
            return a * helper(a, b - 1) % mod
    
        mod = 1337
        power = 0
        for i in b:
            power = power * 10 + i
        return helper(a,power)