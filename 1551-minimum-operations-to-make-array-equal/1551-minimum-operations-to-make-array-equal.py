class Solution:
    def minOperations(self, n: int) -> int:
        oper = 0
        nbr = n-1
        for i in range(n//2):
            oper += nbr
            nbr -= 2
        return oper