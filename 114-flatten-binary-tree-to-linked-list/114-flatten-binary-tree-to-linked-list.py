# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def DFS(root):
            if root is None:
                return
            
            leftR = DFS(root.left)
            rightR = DFS(root.right)
            
            root.left = None
            if leftR:
                root.right = leftR
                if rightR:
                    while leftR.right:
                        leftR = leftR.right
                    leftR.right = rightR
            return root
        DFS(root)