class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        rotation_point = self.find_rotation_point(nums)
        start, end = 0, rotation_point - 1

        # checking in which bucket target is found
        if target < nums[0]:
            start, end = rotation_point, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    def find_rotation_point(self, nums):
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        return start if start else len(nums)