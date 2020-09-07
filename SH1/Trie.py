
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = self.get_node()

    @staticmethod
    def get_node():
        return TrieNode()

    @staticmethod
    def char_to_index(ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        current = self.root
        for char in word:
            index = self.char_to_index(char)
            if not current.children[index]:
                current.children[index] = self.get_node()
            current = current.children[index]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            index = self.char_to_index(char)
            if not current.children[index]:
                return False
            current = current.children[index]
        return current and current.is_end_of_word

    def delete(self, word):
        current = self.root
        for char in word:
            index = self.char_to_index(char)
            if not current.children[index]:
                return -1
            current = current.children[index]
        if not current:
            return -1
        else:
            current.is_end_of_word = False


dictionary = Trie()
dictionary.insert("beimnet")
dictionary.insert("beizd")
print(dictionary.search("beimnet"))
print(dictionary.search("beizd"))
dictionary.delete("beimnet")
print(dictionary.search("beimnet"))
