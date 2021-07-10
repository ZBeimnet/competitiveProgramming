class Solution:
    def numDecodings(self, s: str) -> int:
        mod = int(math.pow(10, 9)) + 7
        return self.dfs(s, 0, s[0], {}, mod) 
    
    def dfs(self, s, idx, curr_el, cache, mod):
        if (idx, curr_el) in cache:
            return cache[(idx, curr_el)]
        if idx == len(s):
            return 1
        if curr_el == '0':
            return 0
        
        decode_count = 0
        
        if curr_el == '*':
            for i in range(1, 10):
                decode_count += self.dfs(s, idx, str(i), cache, mod) % mod
        else:
            next_el = s[idx + 1] if idx + 1 < len(s) else -1
            decode_count += self.dfs(s, idx + 1, next_el, cache, mod) % mod
            if idx + 1 < len(s):
                next_el = s[idx + 2] if idx + 2 < len(s) else -1
                if s[idx + 1] == '*' and curr_el == '1':
                    decode_count += 9 * self.dfs(s, idx + 2, next_el, cache, mod) % mod
                elif s[idx + 1] == '*' and curr_el == '2':
                    decode_count += 6 * self.dfs(s, idx + 2, next_el, cache, mod) % mod
                elif s[idx + 1] != '*' and int(curr_el + s[idx + 1]) <= 26:
                    decode_count += self.dfs(s, idx + 2, next_el, cache, mod) % mod
        
        decode_count %= mod
        cache[(idx, curr_el)] = decode_count
        return decode_count
                    
                
