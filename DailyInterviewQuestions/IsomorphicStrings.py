class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.generate_code(s) == self.generate_code(t)
    
    
    def generate_code(self, string):
        char_map = {}
        code = []
        count = 0
        
        for char in string:
            if char not in char_map:
                char_map[char] = count
                count += 1
            code.append(str(char_map[char]))
        
        return "".join(code)