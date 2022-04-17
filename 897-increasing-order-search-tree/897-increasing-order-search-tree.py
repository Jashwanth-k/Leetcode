# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,nums):
        if root is None:
            return 
        
        self.preorder(root.left,nums)
        nums.append(root.val)
        self.preorder(root.right,nums)
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nums = []
        self.preorder(root,nums)
        newRoot = TreeNode(nums[0])
        prev = newRoot
        for i in nums[1:]:
            prev.right = TreeNode(i)
            prev = prev.right
        return newRoot