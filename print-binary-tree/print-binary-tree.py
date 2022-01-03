# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findHeight(self,root):
        if root is None:
            return 0
        
        lh = self.findHeight(root.left)
        rh = self.findHeight(root.right)
        return 1 + max(lh,rh)
    
    def addValues(self,root,res,r,si,ei):
        if root is None:
            return
        
        c = si + (ei-si) // 2
        res[r][c] += str(root.val)
        
        self.addValues(root.left,res,r+1,si,c-1)
        self.addValues(root.right,res,r+1,c+1,ei)
        return res
    
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.findHeight(root) - 1
        m = height + 1
        n = 2**(height+1) - 1
        res = [["" for i in range(n)] for j in range(m)]
        return self.addValues(root,res,0,0,n-1)