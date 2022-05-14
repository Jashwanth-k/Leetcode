# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def DFS(root,height):
            if root is None:
                return 
            
            if len(nums) == height:
                nums.append(root.val)
            else:
                nums[height] = max(nums[height],root.val)
            
            DFS(root.left,height+1)
            DFS(root.right,height+1)
            
        nums = []
        DFS(root,0)
        return nums