class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern = self.generate_pattern(pattern)
        output = []
        
        for word in words:
            if self.generate_pattern(word) == pattern:
                output.append(word)
        
        return output
    
    def generate_pattern(self, word):
        pattern = []
        pattern_dict = {}
        curr_num = 1
        
        for char in word:
            if char in pattern_dict:
                pattern.append(pattern_dict[char])
            else:
                pattern_dict[char] = curr_num
                pattern.append(curr_num)
                curr_num += 1
        
        return pattern
        
