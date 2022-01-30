class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(n,k):
            if k == 1:
                return [[i] for i in range(1,n+1)]
            
            smalloutput = helper(n,k-1)
            output = []
            for sublist in smalloutput:
                idx = sublist[-1]
                for j in range(idx+1,n+1):
                    output.append(sublist + [j])
            return output
        return helper(n,k)