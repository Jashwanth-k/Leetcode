# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.head = self.tail = Node(0)
        while iterator.hasNext():
            newNode = Node(iterator.next())
            self.tail.next = newNode
            self.tail = self.tail.next
            
        self.head = self.head.next
        return 
            
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.head.val

    def next(self):
        """
        :rtype: int
        """
        value = self.head.val
        self.head = self.head.next
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.head else False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].