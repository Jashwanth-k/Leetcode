# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def BST(root):
            if root is None:
                return 0
            
            BST(root.right)
            total[0] += root.val
            root.val = total[0]
            BST(root.left)
            
        total = [0]
        BST(root)
        return root
            