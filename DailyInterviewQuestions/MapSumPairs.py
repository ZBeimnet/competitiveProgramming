class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, val):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.val += val
    
    def sum_prefix_val(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.val

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        self.map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        val_diff = val - self.map[key]
        self.map[key] = val
        self.trie.insert(key, val_diff)

    def sum(self, prefix: str) -> int:
        return self.trie.sum_prefix_val(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
