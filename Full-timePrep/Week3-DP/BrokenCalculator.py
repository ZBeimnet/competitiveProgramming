class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ans = 0
        
        while Y > X:
            ans += 1
            if Y % 2: 
                Y += 1
            else: 
                Y //= 2

        return ans + X - Y