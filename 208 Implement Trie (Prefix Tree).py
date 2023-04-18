class TrieNode:
    #initializes one node
    def __init__(self):
        self.children = {}      #should have max of 26 children for 26 letters
        self.word = False       #if word is complete or not. True when it is a finished word

class Trie:
    #initializes the trie object
    def __init__(self):
        self.root = TrieNode()

    #inserts the word into the trie
    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word = True

    #returns true if the word is in the trie (i.e. was inserted before) and false otherwise
    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        if node.word == False:
            return False
        return True

    #returns true if there is a previously inserted word that has the prefix
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)