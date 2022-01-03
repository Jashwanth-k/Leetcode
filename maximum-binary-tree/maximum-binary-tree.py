# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        
        for i in nums:
            n = TreeNode(i)
            while stack and stack[-1].val < i:
                n.left = stack.pop()
                
            if stack:
                stack[-1].right = n
            stack.append(n)
        return stack[0]