class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.index = 0
        self.is_end = False


class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        temp = self.root
        for i,word in enumerate(words):
            self.insert(word,i)
    def insert(self, word: str,i : int) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.index = i
        curr.is_end = True

    def f(self, pref: str, suff: str) -> int:
        ind = -1
        temp = self.root
        for i in pref:
            if i not in temp.children:
                return -1
            temp = temp.children[i]
        def dfs(node,w):
            nonlocal ind
            if node.is_end:
                if w[len(w) - len(suff):] == suff:
                    ind = max(ind,node.index)
            for i in node.children:
                dfs(node.children[i],w + i)

        dfs(temp,pref)
        return ind

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)