# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightMin(self,root):
        if root is None:
            return float('-inf')
        
        if root.left == None:
            return root.val
        return self.rightMin(root.left)
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return 
        
        if root.val == key:
            if root.left == root.right:
                return root.left
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            else:
                ans = self.rightMin(root.right)
                root = self.deleteNode(root,ans)
                root.val = ans
                return root

        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)
        return root