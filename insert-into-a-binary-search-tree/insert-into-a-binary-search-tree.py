# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert_helper(self,root,node):
        if root is None:
            root = node
            return root

        if root.val > node.val:
            root.left = self.insert_helper(root.left,node)
        else:
            root.right = self.insert_helper(root.right,node)
        return root
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        return self.insert_helper(root,newNode)