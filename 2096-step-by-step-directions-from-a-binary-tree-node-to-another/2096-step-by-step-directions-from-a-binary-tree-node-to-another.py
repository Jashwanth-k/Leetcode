# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(root):
            if root == None:
                return
            
            left = lca(root.left)
            right = lca(root.right)
            
            if (root.val == startValue or root.val == destValue) and (left or right):
                self.rootlca = root
                return
            if left and right:
                self.rootlca = root
                return
            if left or right:
                return True
            if root.val == startValue or root.val == destValue:
                return True
                
        self.rootlca = None
        lca(root)
        def DFS(root,path1,path2):
            if root == None:
                return
            
            if root.val == startValue:
                if self.flag:
                    self.res = path1 + self.res
                else:
                    self.res += path1
                
            if root.val == destValue:
                self.res += path2
                self.flag = True
            
            path1.append("U")
            path2.append("L")
            DFS(root.left,path1,path2)
            path2.pop()
            path2.append("R")
            DFS(root.right,path1,path2)
            path2.pop()
            path1.pop()
            
        self.res = []
        self.flag = False
        DFS(self.rootlca,[],[])
        return "".join(self.res)