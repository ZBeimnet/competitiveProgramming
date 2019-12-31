# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l <= r:
            mid = (l + r) // 2

            if not isBadVersion(mid - 1) and not isBadVersion(mid):
                l = mid + 1
            elif isBadVersion(mid - 1) and isBadVersion(mid):
                r = mid - 1
            else:
                return mid

