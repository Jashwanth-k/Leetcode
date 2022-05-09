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
                return None,None
            
            leftR,leftT = DFS(root.left)
            rightR,rightT = DFS(root.right)
            
            if rightT:
                tail = rightT
            elif leftT:
                tail = leftT
            else:
                tail = root
                
            root.left = None
            if leftR:
                root.right = leftR
                if rightR:
                    leftT.right = rightR
                    tail = rightT
            return root,tail
        DFS(root)