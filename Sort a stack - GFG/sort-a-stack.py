class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, stack):
        def helper(st,val):
            if len(st) == 0:
                st.append(val)
                return
            elif st[-1] < val:
                st.append(val)
                return
            cur = st.pop()
            helper(st,val)
            st.append(cur)

        def sortStackHelper(st):
            if len(st) == 0:
                return
            cur = st.pop()
            sortStackHelper(st)
            if len(st) == 0 or st[-1] < cur:
                st.append(cur)
            else:
                helper(st,cur)
    
        sortStackHelper(stack)

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends