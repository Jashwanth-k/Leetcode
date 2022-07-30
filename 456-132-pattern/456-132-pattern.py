class Solution:        
    def find132pattern(self, nums: List[int]) -> bool:
        prefix,n = [],len(nums)
        minim = 1e10
        for i in nums:
            minim = min(minim,i)
            prefix.append(minim)
        
        st = []
        prevGtr = [-1]*n
        for i in range(n):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            if st:
                prevGtr[i] = st[-1]
            st.append(i)    
            
        for i in range(n):
            mid = prevGtr[i]
            if mid == -1 or mid == 0: continue
            end = nums[i]
            if end > prefix[mid-1]:
                return True
        return False