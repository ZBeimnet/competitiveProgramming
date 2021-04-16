from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam = defaultdict(set)
        answer = [0] * k
        
        for u_id, time in logs:
            uam[u_id].add(time)
        
        for value in uam.values():
            answer[len(value) - 1] += 1
        
        return answer
        
