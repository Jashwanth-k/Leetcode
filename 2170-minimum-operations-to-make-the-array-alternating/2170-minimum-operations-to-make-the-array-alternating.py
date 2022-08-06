class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def helper(d):
            max1,max2 = [0,-1],[0,-1]
            for i in d:
                cur = d[i]
                if cur > max1[1]:
                    max2 = max1
                    max1 = [i, cur]
                elif cur > max2[1]:
                    max2 = [i, cur]
            return max1,max2

        n = len(nums)
        even,odd = defaultdict(int),defaultdict(int)
        for i in range(n):
            if i % 2 == 0:
                even[nums[i]] += 1 
            else:
                odd[nums[i]] += 1
        even[-1] = odd[-1] = 0
        me1,me2 = helper(even)
        mo1,mo2 = helper(odd)

        res = 1e6
        for ele1,freq1 in [me1,me2]:
            for ele2,freq2 in [mo1,mo2]:
                if ele1 != ele2:
                    res = min(res,n - freq1-freq2)
        return res