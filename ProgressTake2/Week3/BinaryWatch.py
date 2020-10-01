"""
number of LEDs on = number of 1's in binary representation of hours and minutes
"""
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        
        for hour in range(12):
            for minute in range(60):
                if (bin(hour) + bin(minute)).count("1") == num:
                    if minute < 10:
                        result.append(f"{hour}:0{minute}")
                    else:
                        result.append(f"{hour}:{minute}")
        
        return result
