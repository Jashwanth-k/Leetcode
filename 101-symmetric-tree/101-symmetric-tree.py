# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self,root):
        if root is None:
            return
        
        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def checkTree(self,root1,root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None and root2 != None:
            return False
        if root1 != None and root2 == None:
            return False
        
        if root1.val != root2.val:
            return False
        left = self.checkTree(root1.left,root2.left)
        right = self.checkTree(root1.right,root2.right)
        if left and right:
            return True
        return False
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        rightin = self.invertTree(root.right)
        return self.checkTree(root.left,rightin)