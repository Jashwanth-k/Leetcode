# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def DFS(root,h,s):
            if root is None:
                return
            
            if h not in s:
                self.nums.append(root.val)
                s.add(h)
                
            DFS(root.right,h+1,s)
            DFS(root.left,h+1,s)
            
        s = set()
        self.nums = []
        DFS(root,0,s)
        return self.nums
        