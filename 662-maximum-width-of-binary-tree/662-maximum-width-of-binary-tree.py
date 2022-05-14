# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def BFS(root):
            q = collections.deque()
            q.append((root,1))
            q.append((None,None))
            prev = None
            while len(q) != 0:
                curr,idx = q.popleft()
                if prev == None or idx == None:
                    prev = idx
                if curr == None:
                    if len(q) == 0:
                        break
                    q.append((None,None))
                    continue
                
                if prev:
                    self.ans = max(self.ans,idx - prev + 1)
                    
                if curr.left:
                    q.append((curr.left,2*idx))
                if curr.right:
                    q.append((curr.right,2*idx+1))
                    
        self.ans = 1
        BFS(root)
        return self.ans