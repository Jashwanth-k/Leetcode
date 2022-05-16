# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        q = collections.deque()
        q.append(root)
        q.append(None)
        curr = collections.deque()
        output = []
        state = 0
        
        while len(q) != 0:
            currNode = q.popleft()
            if currNode == None:
                output.append(curr)
                state = 1 - state
                curr = collections.deque()
                if len(q) == 0:break
                q.append(None)
                continue
            
            if state == 0:
                curr.append(currNode.val)
            if state == 1:
                curr.appendleft(currNode.val)
                
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
        return output
            