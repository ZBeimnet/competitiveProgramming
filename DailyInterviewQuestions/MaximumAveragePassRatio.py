import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        ratio_sum = 0
        max_heap = []
        
        for i in range(len(classes)):
            passed, total = classes[i]
            initial_ratio = (passed / total)
            ratio_diff = ((passed + 1) / (total + 1)) - initial_ratio
            classes[i][0] += 1
            classes[i][1] += 1
            ratio_sum += initial_ratio
            heapq.heappush(max_heap, (-ratio_diff, i))
        
        for _ in range(extraStudents):
            ratio_diff, index = heapq.heappop(max_heap)
            passed, total = classes[index]
            current_ratio = passed / total
            new_ratio_diff = ((passed + 1) / (total + 1)) - current_ratio
            classes[index][0] += 1
            classes[index][1] += 1
            ratio_sum += -ratio_diff
            heapq.heappush(max_heap, (-new_ratio_diff, index))
        
        return ratio_sum / len(classes)
            
