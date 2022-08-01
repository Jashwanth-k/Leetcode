class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        imp = [0]*n
        pq = []
        for i,j in requests:
            imp[i] += 1
            if j + 1 < n: imp[j+1] -= 1
        for i in range(1,n):
            imp[i] += imp[i-1]
        for i in range(n):
            pq.append((imp[i],i))
        
        permute = [0]*n
        pq.sort(reverse=True)
        nums.sort(reverse=True)
        i = 0
        for val,idx in pq:
            permute[idx] = nums[i]
            i += 1
        for i in range(1,n):
            permute[i] += permute[i-1]
        res = 0
        for i,j in requests:
            if i == 0:
                val = permute[j]
            else:
                val = permute[j] - permute[i-1]
            res = (res + val) % (10**9 + 7)
        return res