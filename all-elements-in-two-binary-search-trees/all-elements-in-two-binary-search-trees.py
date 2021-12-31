# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createList(self,root,l):
        if root is None:
            return
        
        self.createList(root.left,l)
        l.append(root.val)
        self.createList(root.right,l)
        return l
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        list1 = self.createList(root1,[])
        list2 = self.createList(root2,[])
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1 == None and list2 == None:
            return []
        print(list1,list2)

        finalList = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                finalList.append(list1[i])
                i += 1
            elif list1[i] > list2[j]:
                finalList.append(list2[j])
                j += 1
            else:
                finalList.append(list1[i])
                finalList.append(list2[j])
                i += 1
                j += 1
                
        return finalList + list1[i:] + list2[j:]