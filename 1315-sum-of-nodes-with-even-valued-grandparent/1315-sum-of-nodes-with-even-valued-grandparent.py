# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def checkChildren(root,c):
            if root is None:
                return c
            if root.left:
                c += root.left.val
            if root.right:
                c += root.right.val
            # print(c)
            return c
        
        def DFS(root,count):
            if root is None:
                return count
            
            if root.val % 2 == 0:
                count += checkChildren(root.left,0)
                count += checkChildren(root.right,0)
            count = DFS(root.left,count)
            count = DFS(root.right,count)
            return count
            
        return DFS(root,0)
                
            