import sys
sys.setrecursionlimit(100000)
class TrieNode:
    def __init__(self):
        self.children = {} 
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    def countSubsequences(self, s):

        def dfs(node, index):
            stack = []
            count = 0
            stack.append((node, index))

            while len(stack):
                
                root, idx = stack.pop()
                
                if idx >= len(s):
                    return True
                
                if root.is_end_of_word:
                    return False 

                for key, val in root.children.items():
                    if key == s[idx]:
                        stack.append((val, idx+1))
                    else:
                        stack.append((val, idx))

            return False

        node = self.root
        return dfs(node, 0)


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        trie.addWord(s)
        count = 0
        memo = {}
        for word in words:
            if word in memo:
                if memo[word]:
                    count+=1
                continue

            memo[word] = trie.countSubsequences(word)
            if memo[word]:
                count += 1

        return count