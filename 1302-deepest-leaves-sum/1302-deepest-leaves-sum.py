# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findHeight(self,root):
        if root is None:
            return 0
        
        return 1 + max(self.findHeight(root.left),self.findHeight(root.right))
        
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def DFS(root,h):
            if root is None:
                return 
            
            if h == 0:
                self.ans += root.val
            DFS(root.left,h-1)
            DFS(root.right,h-1)
                
        self.ans = 0
        h = self.findHeight(root)-1
        DFS(root,h)
        return self.ans