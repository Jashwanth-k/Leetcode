# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def DFS(root):
            if root is None:
                return 
            
            DFS(root.right)
            root.val = root.val + self.prev
            self.prev = root.val
            DFS(root.left)
        
        self.prev = 0
        DFS(root)
        return root