from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        root = TrieNode()
        
        # add all words into the trie
        for word in words:
            self.add_word(root, word)
        
        # for every board[i][j] in root, check if we can construct a word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    trie_node = root.children[board[i][j]]
                    self.dfs((i, j), board, trie_node, [board[i][j]], visited, result, neighbours)
        
        return list(result)
    
    def dfs(self, point, board, trie_node, path, visited, result, neighbours):
        if trie_node.is_end:
            result.add("".join(path))
            
        visited.add(point)
        for x, y in neighbours:
            row = point[0] + x
            col = point[1] + y
            if 0 <= row < len(board) and \
                0 <= col < len(board[0]) and \
                 (row, col) not in visited and \
                  board[row][col] in trie_node.children:
                new_trie_node = trie_node.children[board[row][col]]
                self.dfs((row, col), board, new_trie_node, path + [board[row][col]], visited, result, neighbours)
        visited.remove(point)
        
    def add_word(self, root, word):
        current = root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True