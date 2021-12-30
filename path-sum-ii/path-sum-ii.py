# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def pathSum_K(root,k,output,l = []):
            if root is None:
                return

            l.append(root.val)
            left = pathSum_K(root.left,k-root.val,output,l)
            right = pathSum_K(root.right,k-root.val,output,l)

            if left == None and right == None:
                if k == root.val:
                    output.append(l[:])
            l.pop()
            return root
        
        output = []
        pathSum_K(root,targetSum,output)
        return output
        