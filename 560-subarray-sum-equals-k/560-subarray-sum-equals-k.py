class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d = {0 : 1}
        tSum = 0
        count = 0
        for num in nums:
            tSum += num
            
            if tSum-k in d:
                count += d[tSum-k]
            
            if tSum in d:
                d[tSum] += 1
            else:
                d[tSum] = 1
        return count