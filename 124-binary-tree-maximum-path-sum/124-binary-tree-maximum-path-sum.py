# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def DFS(root):
            if root is None:
                return 0
        
            left = DFS(root.left)
            right = DFS(root.right)
            
            curr = max(left + root.val, right + root.val)
            self.ans = max(self.ans,curr,left + right + root.val)
            return max(curr,0)
            
        self.ans = float("-inf")
        DFS(root)
        return self.ans