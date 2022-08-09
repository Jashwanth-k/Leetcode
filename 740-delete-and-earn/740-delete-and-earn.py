class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = Counter()
        for i in nums:
            d[i] += 1
        nums = sorted(d.keys())
        n = len(nums)
        nums.append(-1)
        p1 = p2 = 0
        
        for i in range(n-1,-1,-1):            
            inclu = nums[i] * d[nums[i]]
            inclu += p2 if nums[i+1] == nums[i]+1 else p1
            exclu = p1
            curr = max(inclu,exclu)
            p2 = p1
            p1 = curr
        return max(p1,p2)