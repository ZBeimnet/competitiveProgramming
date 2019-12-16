# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:

        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        # find the maximum index
        max_index = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[max_index]:
                max_index = i

        root = TreeNode(nums[max_index])
        left_subtree = nums[:max_index]
        right_subtree = nums[max_index + 1:]

        root.left = self.constructMaximumBinaryTree(left_subtree)
        root.right = self.constructMaximumBinaryTree(right_subtree)

        return root

tree = Solution()
tree.constructMaximumBinaryTree([3,2,1,6,0,5])

