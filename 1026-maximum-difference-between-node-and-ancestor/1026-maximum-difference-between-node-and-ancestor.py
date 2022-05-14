# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def DFS(root,minim,maxim):
            if root is None:
                return
            
            self.ans = max(self.ans,abs(root.val-minim))
            self.ans = max(self.ans,abs(root.val-maxim))
            
            minim = min(minim,root.val)
            maxim = max(maxim,root.val)
            DFS(root.left,minim,maxim)
            DFS(root.right,minim,maxim)
            
        self.ans = 0
        DFS(root,root.val,root.val)
        return self.ans
