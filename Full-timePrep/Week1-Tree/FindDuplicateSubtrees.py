from typing import List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time -> O(N), space -> O(N)
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        subtrees, subtree_ids = defaultdict(list), {}
        curr_id = [0]
        self.dfs(root, subtrees, subtree_ids, curr_id)
        return [root[0] for root in subtrees.values() if len(root) > 1]
    
    def dfs(self, node, subtrees, subtree_ids, curr_id):
        if not node:
            return None
        
        left_id = self.dfs(node.left, subtrees, subtree_ids, curr_id)
        right_id = self.dfs(node.right, subtrees, subtree_ids, curr_id)
        subtree = (node.val, left_id, right_id)
        subtrees[subtree].append(node)
        subtree_id = subtree_ids.get(subtree, curr_id[0])
        
        if subtree_id == curr_id[0]:
            subtree_ids[subtree] = subtree_id
            curr_id[0] += 1
        
        return subtree_id
        

# time -> O(N^2), space -> O(N^2)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        subtrees, duplicates = set(), {}
        self.dfs(root, subtrees, duplicates)
        return list(duplicates.values())
     
    def dfs(self, node, subtrees, duplicates):
        if not node:
            return ""
        
        left_st = self.dfs(node.left, subtrees, duplicates)
        right_st = self.dfs(node.right, subtrees, duplicates)
        st_string = f"({node.val}L{left_st}R{right_st})"
        
        if st_string in subtrees and st_string not in duplicates:
            duplicates[st_string] = node
        elif st_string not in subtrees:
            subtrees.add(st_string)
        
        return st_string
            