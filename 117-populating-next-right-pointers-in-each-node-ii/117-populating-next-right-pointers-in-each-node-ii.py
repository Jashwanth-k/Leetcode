"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return 
        q = collections.deque()
        q.append(root)
        q.append(None)
        prev = None
        
        while len(q) != 0:
            curr = q.popleft()
            if prev: prev.next = curr
            prev = curr
            
            if not curr:
                if len(q) == 0: break
                q.append(None)
                continue
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root