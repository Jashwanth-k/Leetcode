# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def DFS(root):
            if root is None:
                return None,True

            left,onel = DFS(root.left)
            right,oner = DFS(root.right)

            if onel and oner and root.val == 0:
                return None,True
            root.left = None if onel else left
            root.right = None if oner else right
            return root,False
        return DFS(root)[0]