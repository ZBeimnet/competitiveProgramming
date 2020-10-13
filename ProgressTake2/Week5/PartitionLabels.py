"""
end_pos = [...]
partitions = [9, 7, 8]
curr_length = 8
start, end =
S = "ababcbaca defegde hijhklij"
                          |   |
"""
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        end_pos = [-1] * 26
        
        for i, char in enumerate(S):
            end_pos[ord(char) - ord('a')] = i
        
#         partitions = []
#         curr_length = -1
#         start, end = 0, 0
        
#         while end < len(S):
#             if curr_length == -1:
#                 if end == end_pos[ord(S[start]) - ord('a')]:
#                     partitions.append(1)
#                     start += 1
#                     end += 1
#                 else:
#                     end = end_pos[ord(S[start]) - ord('a')]
#                     curr_length = end - start + 1
#                     start += 1
#             else:
#                 if start == end or end == len(S) - 1:
#                     partitions.append(curr_length)
#                     curr_length = -1
#                     start += 1
#                     end += 1
#                 elif end_pos[ord(S[start]) - ord('a')] > end:
#                     curr_length += (end_pos[ord(S[start]) - ord('a')] - end)
#                     end = end_pos[ord(S[start]) - ord('a')]
#                     start += 1
#                 else:
#                     start += 1
		
		# way cleaner and to the point than my solution (Leetcode's solution)
        partitions = []
	start, end = 0, 0

        for i, char in enumerate(S):
            end = max(end, end_pos[ord(char) - ord('a')])
            if i == end:
                partitions.append(i - start + 1)
                start = i + 1
       
        return partitions

       
