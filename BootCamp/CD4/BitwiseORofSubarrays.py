class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        result = {A[0]}
        current = {A[0]}

        for i in range(1, len(A)):
            tmp = {A[i]}
            for num in current:
                tmp.add(A[i] | num)

            current = tmp
            for num in current:
                result.add(num)

        return len(result)







