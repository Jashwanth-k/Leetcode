# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_isBST(root):
            if root is None:
                return True,float('inf'),float('-inf')

            rootleft,leftmin,leftmax = check_isBST(root.left)
            rootright,rightmin,rightmax = check_isBST(root.right)
            isTreeBST = True

            overallMax = max(leftmax,rightmax,root.val)
            overallMin = min(leftmin,rightmin,root.val)

            if rootleft == False or rootright == False:
                isTreeBST = False

            if leftmax >= root.val or root.val >= rightmin:
                isTreeBST = False
            return isTreeBST,overallMin,overallMax
        return check_isBST(root)[0]