"""
g = [1,2,3], s = [1,1] , s[j] >= g[i]
     |            |
     sort both g and s

     if s[j] >= g[i]:
        max += 1
        i += 1
        j += 1
    else:
        j += 1

time-complexity -> O(X), where x is the minimum of g and s
space-complexity -> O(1)

"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        max_children = 0
        child_ptr = cookie_ptr = 0

        g.sort()
        s.sort()

        while child_ptr < len(g) and cookie_ptr < len(s):
            if s[cookie_ptr] >= g[child_ptr]:
                max_children += 1
                child_ptr += 1
                cookie_ptr += 1
            else:
                cookie_ptr += 1

        return max_children