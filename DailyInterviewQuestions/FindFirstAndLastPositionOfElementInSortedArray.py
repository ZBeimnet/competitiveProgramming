class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        random_target_pos = self.findTarget(nums, target)

        if random_target_pos == -1:
            return [-1, -1]
        elif len(nums) == 1:
            return [0, 0]

        return [self.findTargetEnd(nums, target, random_target_pos, True),
                self.findTargetEnd(nums, target, random_target_pos)]

    def findTarget(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def findTargetEnd(self, nums, target, target_pos, find_left_end=False):
        left, right = target_pos, len(nums) - 1
        if find_left_end:
            left, right = 0, target_pos

        # to handle this condition [8,8,8,8,8,8,8,8], target=8
        if not find_left_end and nums[right] == target:
            return right

        while left < right:
            mid = (left + right) // 2
            if find_left_end:
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1

        return (right - 1, left)[find_left_end]


