class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode) 
        self.num = 0
        # self.is_end_of_word = False
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.Hash = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        node = self.root
        if key not in self.Hash:
            for c in key:
                if c not in node.children:
                    node.children[c] = TrieNode()
                
                node = node.children[c]
                node.num += val 
        else:
            print(self.Hash)
            for c in key:
                if c not in node.children:
                    node.children[c] = TrieNode()
                
                node = node.children[c]
                node.num =  node.num - self.Hash[key] + val 
        self.Hash[key] = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            node = node.children[c]
            # print(node.num)
        return node.num        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)