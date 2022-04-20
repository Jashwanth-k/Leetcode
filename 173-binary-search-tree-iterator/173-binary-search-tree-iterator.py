# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.root = root
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        return

    def next(self) -> int:
        node = self.stack.pop()
        r = node.right
        while r:
            self.stack.append(r)
            r = r.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()