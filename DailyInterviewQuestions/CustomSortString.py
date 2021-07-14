class Solution:
    def customSortString(self, order: str, str: str) -> str:
        order_rank, rank_to_char_map = self.generate_rank(order)
        ordered_count = [0] * len(order_rank)
        unordered_elements = []
        result = []
        
        for char in str:
            if char in order_rank:
                ordered_count[order_rank[char]] += 1
            else:
                unordered_elements.append(char)
        
        for i, count in enumerate(ordered_count):
            if count > 0:
                result.append(rank_to_char_map[i] * count)
        
        result.extend(unordered_elements)
        return "".join(result)
    
    
    def generate_rank(self, order):
        rank = 0
        order_rank = {}
        rank_to_char_map = {}
        
        for char in order:
            order_rank[char] = rank
            rank_to_char_map[rank] = char
            rank += 1
        
        return (order_rank, rank_to_char_map)
        
        