# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def DFS(self,cloned,target):
        if cloned == None:
            return 
        
        if cloned.val == target.val:
            return cloned
        
        return self.DFS(cloned.left,target) or self.DFS(cloned.right,target)
        
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.DFS(cloned,target)