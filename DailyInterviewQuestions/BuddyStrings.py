class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or set(A) != set(B):
            return False
        elif A == B:
            return len(A) != len(set(A))
        else:
            diffCount = 0
            diffChar = []
            for i, char in enumerate(A):
                if A[i] != B[i]:
                    diffCount += 1
                    diffChar.append((A[i], B[i]))
                if diffCount > 2:
                    return False
            return diffChar[0][0] == diffChar[1][1] and diffChar[0][1] == diffChar[1][0]