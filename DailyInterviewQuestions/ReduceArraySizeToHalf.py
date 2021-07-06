from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_count = Counter(arr)
        set_size = 0
        removed_elements = 0
        
        for count in sorted(arr_count.values(), reverse=True):
            removed_elements += count
            set_size += 1
            if removed_elements >= len(arr) / 2:
                return set_size
        