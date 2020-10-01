class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_map = defaultdict(list)
        bulls = set()
        result = ["0", "A", "0", "B"]
        
        # build a map for digits in secret (key -> digit, value -> [pos, ""])
        for i, digit in enumerate(secret):
            secret_map[digit].append([i, ""])
        
        # go over digits in guess if we can find bulls
        for i, digit in enumerate(guess):
            if digit in secret_map:
                for j, secret_digit in enumerate(secret_map[digit]):
                    if i == secret_digit[0]:
                        secret_map[digit][j][1] = "bull"
                        result[0] = str(int(result[0]) + 1)
                        bulls.add(i)
        
        # go over digits in guess if we can find cows
        for i, digit in enumerate(guess):
            if i not in bulls and digit in secret_map:
                for j, secret_digit in enumerate(secret_map[digit]):
                    if not secret_digit[1]:
                        secret_map[digit][j][1] = "cow"
                        result[2] = str(int(result[2]) + 1)
                        break
        
        return "".join(result)
