import queue
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return
        q = queue.Queue()
        q.put(root)
        q.put(None)
        prev = None
        
        while not q.empty():
            curr = q.get()
            if prev != None:
                prev.next = curr
            prev = curr
            
            if curr == None:
                if not q.empty():
                    q.put(None)
            else:
                if curr.left != None:
                    q.put(curr.left)
                if curr.right != None:
                    q.put(curr.right)
                
        return root