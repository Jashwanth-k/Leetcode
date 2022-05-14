# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def DFS(root,minim,maxim,ans):
            if root is None:
                return
            
            ans[0] = max(ans[0],abs(root.val-minim))
            ans[0] = max(ans[0],abs(root.val-maxim))
            
            minim = min(minim,root.val)
            maxim = max(maxim,root.val)
            DFS(root.left,minim,maxim,ans)
            DFS(root.right,minim,maxim,ans)
            
        ans1 = [0]
        ans2 = [0]
        DFS(root.left,root.val,root.val,ans1)
        DFS(root.right,root.val,root.val,ans2)
        return max(ans1[0],ans2[0])