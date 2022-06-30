# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def DFS(root,prev):
            if root is None:
                return 0
            if (root,prev) in dp:
                return dp[root,prev]
            
            pick = 0
            if prev:
                pick = root.val + DFS(root.left,False) + DFS(root.right,False)
            unpick = DFS(root.left,True) + DFS(root.right,True)
            dp[root,prev] = max(pick,unpick)
            return dp[root,prev]
        
        dp = {}
        return DFS(root,True)