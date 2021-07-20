# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nested_list = nestedList
        self.nested_list_gen = self.find_next_int(nestedList)
        self.next_int = None
    
    def next(self) -> int:
        return self.next_int
    
    def hasNext(self) -> bool:
        try:
            self.next_int = next(self.nested_list_gen)
        except StopIteration:
            return False
        else:
            return True
    
    def find_next_int(self, nested_list):
        for el in nested_list:
            if el.isInteger():
                yield el.getInteger()
            else:
                yield from self.find_next_int(el.getList())
    
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())