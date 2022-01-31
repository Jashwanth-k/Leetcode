class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(left,right,ans,s):
            if left == 0 and right == 0:
                ans.append(s)
                return
            
            if left > 0:
                helper(left-1,right,ans,s + '(')
            if right > left:
                helper(left,right-1,ans,s + ')')
                
        ans = []
        helper(n,n,ans,'')
        return ans