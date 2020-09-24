"""
start from root
    5
4       8
state -> (node, [path], path_sum)
leaf node -> no right and left child
-------------
step1: run dfs on the root node, states of the dfs --> (node, [path], path_sum)
step2: checking if current node is a leaf node. condition for being a leaf node --> no right and left child
    if step2: * check if path_sum is equal with sum, if true add the path to the result array
"""
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        all_paths = []
        stack = [(root, [], 0)]
        
        while stack:
            node, path, path_sum = stack.pop()
            path_sum += node.val
            path.append(node.val)
            
            if not node.left and not node.right and path_sum == sum:
                all_paths.append(path)
            
            if node.left:
                stack.append((node.left, path[:], path_sum))
            if node.right:
                stack.append((node.right, path[:], path_sum))
                
        return all_paths
        
