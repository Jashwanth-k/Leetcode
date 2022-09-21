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
            if left or right or root.val == startValue or root.val == destValue:
                return True
                
        self.rootlca = None
        lca(root)
        def DFS(root,path):
            if root == None:
                return
            
            if root.val == startValue:
                self.start = "U"*len(path)
            if root.val == destValue:
                self.dest = path[:]
            
            path.append("L")
            DFS(root.left,path)
            path[-1] = "R"
            DFS(root.right,path)
            path.pop()
            
        self.start = []
        self.dest = []
        DFS(self.rootlca,[])
        return self.start + "".join(self.dest)