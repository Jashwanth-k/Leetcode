# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,l):
        if root is None:
            return 
        self.inorder(root.left,l)
        l.append(root.val)
        self.inorder(root.right,l)
        return l
    
    def createRoot(self,a):
        stack = []
        
        for i in a:
            n = TreeNode(i)
            while stack and stack[-1].val < i:
                n.left = stack.pop()
                
            if stack:
                stack[-1].right = n
            stack.append(n)
        return stack[0]
        
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        a = self.inorder(root,[])
        a.append(val)
        return self.createRoot(a)