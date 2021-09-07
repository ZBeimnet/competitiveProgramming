def build_prefix(pattern):
    prefix = [0] * len(pattern)
    i, j = 0, 1
    
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            prefix[j] = i + 1
            i += 1
            j += 1
        else:
            if i == 0:
                j += 1
            else:
                i = prefix[i-1]
    
    return prefix


def match_string(string, pattern):
    prefix = build_prefix(pattern)
    p_idx = s_idx = 0
    
    while s_idx < len(string) and p_idx < len(pattern):
        if string[s_idx] == pattern[p_idx]:
            p_idx += 1
            s_idx += 1
        else:
            if p_idx == 0:
                s_idx += 1
            else:
                p_idx = prefix[p_idx-1]
    
    return p_idx == len(pattern)

print(match_string("abcdadbcdadbcadb", "adbcadb"))
