class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        d = Counter([i for i in nums if i % 2 == 0])
        tsum = 0
        for i,j in d.items(): tsum += i*j
        res = []
        for val,idx in queries:
            if d[nums[idx]] != 0:
                tsum -= nums[idx]
                d[nums[idx]] -= 1
            csum = nums[idx] + val
            if csum % 2 == 0:
                tsum += csum
                d[csum] += 1
            nums[idx] = nums[idx] + val
            res.append(tsum)
        return res