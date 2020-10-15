"""
"aab" a -> 0, b -> 0
"aba"
-----
"aaabcab" a -> 0, b -> 0, c -> 0
"ababaca"
-------
"aaaabc" a -> 1 , b -> 0, c -> 0
"abaca" -> ""

step1: count every character with a format -> [[count, char], ...]
step2: heapify our count (max heap)
step3: while len(count) > 0
        # if top of heap is d/t from our prev char
            # pop -> add to reorganized_str -> count-- -> push 
        # else
            # if count of 2nd max > 0:
                # pop 2 elements -> add the 2nd to reorganized_str -> count of 2nd --
                  -> push both 
            # else:
                # return ""

time-complexity -> O(N*log26) = O(N), where N is len(S)
space-complexity -> O(N)
"""
import heapq 
class Solution:
    def reorganizeString(self, S: str) -> str:
        char_count = [[0, chr(ord('a') + i)] for i in range(26)]
        reorganized_arr = ["#"]
        
        for char in S:
            char_count[ord(char) - ord('a')][0] -= 1
        
        heapq.heapify(char_count)
        
        for _ in range(len(S)):
            if char_count[0][1] != reorganized_arr[-1] and char_count[0][0] < 0:
                curr_char = heapq.heappop(char_count)
                reorganized_arr.append(curr_char[1])
                curr_char[0] += 1
                heapq.heappush(char_count, curr_char)
            else:
                if char_count[1][0] == 0 and char_count[2][0] == 0:
                    return ""
                else:
                    char1 = heapq.heappop(char_count)
                    char2 = heapq.heappop(char_count)
                    reorganized_arr.append(char2[1])
                    char2[0] += 1
                    heapq.heappush(char_count, char2)
                    heapq.heappush(char_count, char1)
        
        return "".join(reorganized_arr[1:])
