class TrieNode:
    def __init__(self, letter=None):
        # initialize TrieNode
        # it should have link to the downstream neighbirs
        # also a signal that checks whether current node is end of
        # a word
        self.neighbors = {} # this allows us to access both the letter and its node instance 
        self.last_letter = False
    
    
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        head = self.trie # get a pointer to the root of the trie
        for letter in word:
            # if we already dont have it in the neighbors add it
            if letter not in head.neighbors:
                head.neighbors[letter] = TrieNode(letter)
            # traverse to the correct neighbor
            head = head.neighbors[letter]
        head.last_letter = True # last letter of the word is marked so that search method knows whether it reached the end
            
                    
                    
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        head = self.trie
        for letter in word:
            if letter not in head.neighbors: 
                return False
            head = head.neighbors[letter]
        # if traversed the whole word fully, check if you get to end of a word
        return head.last_letter

                

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        head = self.trie
        for letter in prefix:
            if letter not in head.neighbors: 
                return False
            head = head.neighbors[letter]
        # if traversed the whole word fully, return true
        return True
