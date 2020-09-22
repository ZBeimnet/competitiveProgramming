class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        stack = [(self.root, 0)]
        while stack:
            node, index = stack.pop()
            if index == len(word):
                if node.is_end_of_word:
                    return True
                else:
                    continue
            trie_index = ord(word[index]) - ord('a')
            if word[index] == ".":
                for child in node.children:
                    if child:
                        stack.append((child, index + 1))
            elif node.children[trie_index]:
                stack.append((node.children[trie_index], index + 1))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)