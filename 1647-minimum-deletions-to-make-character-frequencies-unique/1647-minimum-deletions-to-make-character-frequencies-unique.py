class Solution:
    def minDeletions(self, s: str) -> int:
        def binary_search(nums,target):
            si = 0
            ei = len(nums)-1
            while si <= ei:
                mid = si + (ei-si) // 2
                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    si = mid+1
                else:
                    ei = mid-1
            return ei
        
        d = {}
        maxim = 0
        for i in s:
            d[i] = d.get(i,0) + 1
            
        freq = {}
        for i in d:
            freq[d[i]] = freq.get(d[i],-1) + 1
            if freq[d[i]] > 0:
                maxim = max(maxim,d[i])
        
        helper = []
        for j in range(1,maxim+1):
            if j not in freq:
                helper.append(j)
        
        ans = 0
        for slen in freq:
            curr = freq[slen]
            while curr != 0:
                idx = binary_search(helper,slen)
                ans += slen - helper.pop(idx) if idx >= 0 else slen - 0
                curr -= 1
        return ans