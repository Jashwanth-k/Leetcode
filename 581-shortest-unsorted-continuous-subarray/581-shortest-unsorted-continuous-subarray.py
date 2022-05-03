class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        leftStack = []
        n = len(nums)
        ln = 0
        left = float('inf')
        for i in nums:
            if not leftStack or leftStack[-1] <= i:
                leftStack.append(i)
                ln += 1
            else:
                while leftStack and leftStack[-1] > i:
                    leftStack.pop()
                    ln -= 1
                leftStack.append(i)
                ln += 1
                left = min(ln,left)
        
        rightStack = []
        rn = 0
        right = float('inf')
        for i in nums[::-1]:
            if not rightStack or rightStack[-1] >= i:
                rightStack.append(i)
                rn += 1
            else:
                while rightStack and rightStack[-1] < i:
                    rightStack.pop()
                    rn -= 1
                rightStack.append(i)
                rn += 1
                right = min(rn,right)
        
        ridx = n - right
        lidx = left-1
        return ridx - lidx + 1 if left != float('inf') else 0
            
                
                