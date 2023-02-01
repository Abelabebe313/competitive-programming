class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ''
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(word1) or ptr2 < len(word2):
            if ptr1 < len(word1) and ptr2 < len(word2):
                if word1[ptr1:] >= word2[ptr2:]:
                    merge += word1[ptr1]
                    ptr1 += 1
                elif word1[ptr1:] < word2[ptr2:]:
                    merge += word2[ptr2]
                    ptr2 += 1
    
            elif ptr1 < len(word1):
                merge += word1[ptr1]
                ptr1 += 1
            elif ptr2 < len(word2):
                merge += word2[ptr2]
                ptr2 += 1
        return merge
                
        