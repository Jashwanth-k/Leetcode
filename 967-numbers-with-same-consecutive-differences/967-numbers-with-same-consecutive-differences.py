class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [str(i) for i in range(1,10)]
                    
        smalloutput = self.numsSameConsecDiff(n-1,k)
        output = set()
        for i in smalloutput:
            sub = int(i[-1]) - k
            add = int(i[-1]) + k
            if sub >= 0:
                output.add(i + str(sub))
            if add < 10:
                output.add(i + str(add))
        return output
