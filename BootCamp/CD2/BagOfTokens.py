class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        token = sorted(tokens)
        power = P
        score = 0
        start = 0
        end = len(tokens) - 1

        while start <= end:

            if token[start] <= power:
                power -= token[start]
                score += 1
                start += 1
            elif token[start] > power and score > 0:
                power += token[end]
                score -= 1
                if start == end and token[start] <= power:
                    score += 1
                end -= 1
            else:
                break

        return score