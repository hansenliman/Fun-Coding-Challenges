"""
Design a data structure that supports adding new words and
finding if a string matches any previously added string.

Implement the WordDictionary class:

 - WordDictionary() Initializes the object.
 
 - void addWord(word) Adds word to the data structure, it can be matched later.
 
 - bool search(word) Returns true if there is any string in the data structure that matches
   word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:

WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

"""

import collections

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class WordDictionary():
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.isWord = True
    
    def searchWord(self, word):
        return self.dfs(self.root,word)

    def dfs(self,root,word):

        # Case if word is empty
        if word == "":
            if root.isWord == True:
                return True
            return False

        # Case when we encounter a '.'
        if word[0] == '.':
            for w in root.children:
                if self.dfs(root.children[w],word[1:]):
                    return True
            return False

        # Case when we're still searching
        if word[0] not in root.children:
            return False
        else:
            return self.dfs(root.children[word[0]],word[1:])

