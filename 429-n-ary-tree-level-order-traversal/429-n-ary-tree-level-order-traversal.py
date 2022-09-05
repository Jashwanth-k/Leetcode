"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        q = deque([root])
        res = []
        while len(q) != 0:
            curlevel = []
            for _ in range(len(q)):
                nd = q.popleft()
                curlevel.append(nd.val)
                for child in nd.children:
                    q.append(child)
            res.append(curlevel)
        return res