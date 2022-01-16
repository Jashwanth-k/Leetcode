# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self,root,val):
        if root is None:
            newNode = TreeNode(val)
            return newNode
        
        if root.val > val:
            root.left = self.insert(root.left,val)
        else:
            root.right = self.insert(root.right,val)
        return root
        
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None
        for i in preorder:
            root = self.insert(root,i)
        return root
    