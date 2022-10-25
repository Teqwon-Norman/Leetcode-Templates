class TrieNode:
    def __init__(self):
        self.isWord = False
        self.nodes = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """
        Takes in a str and checks if it 
        exists, otherwise it inserts it.
        """
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = TrieNode()
            curr = curr.nodes[c]
        curr.isWord = True
    
    def search(self, word: str) -> bool:
        """
        Takes in a str and checks if it
        exists, returns True or False
        """
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return curr.isWord
    
    def startsWith(self, prefix: str) -> bool:
        """
        Takes in a str and checks if it
        exists in the Trie, returns True or False
        """
        curr = self.root
        for c in prefix:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return True


