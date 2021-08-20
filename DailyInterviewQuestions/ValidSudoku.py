from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_map = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    ids = (3, 6, 9)
                    row_id = next((x for x in ids if i < x))
                    col_id = next((x for x in ids if j < x))
                    if board[i][j] in hash_map[f"r-{i}"] or \
                        board[i][j] in hash_map[f"c-{j}"] or \
                         board[i][j] in hash_map[(row_id, col_id)]:
                        return False
                    hash_map[f"r-{i}"].add(board[i][j])
                    hash_map[f"c-{j}"].add(board[i][j])
                    hash_map[(row_id, col_id)].add(board[i][j])
        
        return True
                
