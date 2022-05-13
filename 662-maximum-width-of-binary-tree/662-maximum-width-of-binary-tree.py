# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeft(self,root,ht,ct):
        if root is None:
            return 
        self.leftd[ht] = min(self.leftd.get(ht,float('inf')),ct)
   
        lct = self.findLeft(root.left,ht+1,ct*2)
        rct = self.findLeft(root.right,ht+1,(ct*2)+1)
    
    def findRight(self,root,ht,ct):
        if root is None:
            return 
        self.rightd[ht] = min(self.rightd.get(ht,float('inf')),ct)
            
        lct = self.findRight(root.left,ht+1,(ct*2)+1)
        rct = self.findRight(root.right,ht+1,ct*2)
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.leftd = {}
        self.rightd = {}
        self.findLeft(root,0,0)
        self.findRight(root,0,0)
        ans = 0
        for i in self.leftd:
            if i in self.rightd:
                ans = max(ans,2**i - (self.leftd[i] + self.rightd[i]))
        return ans