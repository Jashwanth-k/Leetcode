# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def buildGraph(root,par):
            if root is None:
                return
            
            d[root.val][0] = par
            if root.left: d[root.val][1] = root.left.val
            if root.right: d[root.val][2] = root.right.val
            buildGraph(root.left,root.val)
            buildGraph(root.right,root.val)
        
        d = defaultdict(lambda : [-1,-1,-1])
        buildGraph(root,-1)
        infected = set([start])
        
        q = deque([[start,0]])
        res = 0
        while len(q) != 0:
            cur,time = q.popleft()
            res = max(res,time)
            for sib in d[cur]:
                if sib != -1 and sib not in infected:
                    q.append([sib,time+1])
                    infected.add(sib)
        return res