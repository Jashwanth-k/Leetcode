class Solution:
    def calculateResult(self,nums,div):
        res = 0
        for i in nums:
            res += math.ceil(i / div)
        return res
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        si = 1
        ei = max(nums)
        ans = 0
        while si <= ei:
            mid = si + (ei - si) // 2
            res = self.calculateResult(nums,mid)
            if res <= threshold:
                ans = mid
                ei = mid-1
            else:
                si = mid+1
        return ans