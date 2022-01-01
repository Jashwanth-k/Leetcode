# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createList(self,root,li):
        if root is None:
            return li
        
        self.createList(root.left,li)
        li.append(root.val)
        self.createList(root.right,li)
        return li
    
    def createTree(self,l):
        if len(l) == 0:
            return 
        
        mid = (len(l)-1) // 2
        root = TreeNode(l[mid])
        root.left = self.createTree(l[:mid])
        root.right = self.createTree(l[mid+1:])
        return root
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        treeList = self.createList(root,[])
        return self.createTree(treeList)