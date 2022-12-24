class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1.split()
        word2.split()
        
        length1 = len(word1)
        length2 = len(word2)
        
        merged = ''
        for i in range(min(length1,length2)):
            merged += word1[i]
            merged += word2[i]
        
        if length1 > length2:
            merged += word1[length2:]
        else:
            merged += word2[length1:]
        
        return merged
            