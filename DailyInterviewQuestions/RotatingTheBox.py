class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        answer = [["." for i in range(len(box))] for j in range(len(box[0]))]
        
        for i in range(len(box)):
            stone_count = 0
            for j in range(len(box[0])):
                if box[i][j] == "#":
                    stone_count += 1
                    box[i][j] = "."
                elif box[i][j] == "*":
                    self.fill(answer, stone_count, len(box) - i - 1, j)
                    stone_count = 0
            if stone_count > 0:
                self.fill(answer, stone_count, len(box) - i - 1, len(box[0]))
        
        return answer
    
    def fill(self, answer, count, col, end):
        for i in range(end - 1, end - count - 1, -1):
            answer[i][col] = "#"
        if end < len(answer):
            answer[end][col] = "*"
        
            
