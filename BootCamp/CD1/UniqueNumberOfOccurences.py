class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in range(len(arr)):
            if arr[i] in count:
                count[arr[i]] += 1
            else:
                count[arr[i]] = 1

        occurence_count = set()
        for c in count.values():
            if c in occurence_count:
                return False
            else:
                occurence_count.add(c)

        return True

