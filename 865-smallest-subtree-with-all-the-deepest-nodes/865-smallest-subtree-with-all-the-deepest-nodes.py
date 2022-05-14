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
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        h = self.findHeight(root) - 1
        def DFS(root,h):
            if root is None:
                return False
            if h == 0:
                self.ans = root
                return True
            
            left = DFS(root.left,h-1)
            right = DFS(root.right,h-1)
            
            if left and right:
                self.ans = root
                return True
            if left or right:
                return True
            return False
            
        self.ans = None
        DFS(root,h)
        return self.ans
            