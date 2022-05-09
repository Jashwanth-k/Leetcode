# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return False
        
        leftR = self.lowestCommonAncestor(root.left,p,q)
        rightR = self.lowestCommonAncestor(root.right,p,q)
        
        if type(leftR) != bool: return leftR
        if type(rightR) != bool: return rightR
      
        if leftR and rightR:
            return root
        if (root.val == p.val or root.val == q.val) and (leftR or rightR):
            return root
        if root.val == p.val or root.val == q.val:
            return True
        return leftR or rightR