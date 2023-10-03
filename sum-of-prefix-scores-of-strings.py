class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count += 1
         
        
    def search(self, word: str) -> int:
        ans = 0
        curr = self.root
        for char in word:
            curr = curr.children[char]
            ans += curr.count

        return ans
  
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        op = Trie()
        for word in words:
            op.insert(word)
        ans = []
        for word in words:
            ans.append(op.search(word))
        return ans