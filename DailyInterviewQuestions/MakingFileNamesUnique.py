class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        unique_names = {}
        result = []
        
        for name in names:
            if name not in unique_names:
                unique_names[name] = 1
                result.append(name)
            else:
                curr_k = unique_names[name]
                valid_k = self.find_valid_k(unique_names, name, curr_k)
                new_name = f"{name}({valid_k})"
                result.append(new_name)
                unique_names[name] = valid_k + 1
                unique_names[new_name] = 1
        
        return result
    
    def find_valid_k(self, unique_names, name, curr_k):
        while f"{name}({curr_k})" in unique_names:
            curr_k += 1
        return curr_k
