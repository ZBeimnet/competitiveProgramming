class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr: return []

        new_arr = [(arr[i], i) for i in range(len(arr))]
        output = [0] * len(new_arr)
        current_rank = 1

        new_arr.sort()

        output[new_arr[0][1]] = current_rank
        for i in range(1, len(new_arr)):
            if new_arr[i][0] > new_arr[i - 1][0]:
                current_rank += 1
                output[new_arr[i][1]] = current_rank
            else:
                output[new_arr[i][1]] = current_rank

        return output
