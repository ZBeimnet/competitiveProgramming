class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            minimum = S

            for i in range(1, len(S)):
                current = S[i:] + S[:i]
                if current < minimum:
                    minimum = current

            return minimum

        else:
            return "".join(sorted(S))