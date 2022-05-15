# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        q.append(None)
        curr = 0
        while len(q) != 0:
            curNode = q.popleft()
            if curNode == None:
                if len(q) == 0:
                    break
                q.append(None)
                curr = 0
                continue
                
            curr += curNode.val
            if curNode.left:
                q.append(curNode.left)
            if curNode.right:
                q.append(curNode.right)
        return curr
        