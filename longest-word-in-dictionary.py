class TrieNode:
    def __init__(self, key):
        self.children = defaultdict(TrieNode)
        self.key = key
        self.is_end_of_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode("*")
        self.root.is_end_of_word = True

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char] 
        node.is_end_of_word = True

    def longestWord(self, words: List[str]) -> str:
        # words.sort()
        for word in words:
            self.addWord(word)

        def backtrack(cur):
            # base case
            if not cur.is_end_of_word:
                return ""
            if cur.is_end_of_word and len(cur.children) == 0:
                return cur.key

            lex = ""

            for c in cur.children.values():
                if c.is_end_of_word:
                    res = backtrack(c)
                    if res == "":
                        continue
                    if lex == "":
                        lex = res
                    elif len(lex) < len(res):
                        lex = res
                    elif len(lex) == len(res) and lex > res:
                        lex = res

            if cur.key == "*":
                return lex
            return cur.key + lex
        return backtrack(self.root)