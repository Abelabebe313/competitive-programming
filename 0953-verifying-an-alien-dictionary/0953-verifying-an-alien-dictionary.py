class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha = {order[i]: i for i in range(len(order))}
        for i in range(1,len(words)):
            a = words[i-1]
            b = words[i]
            for j in range(len(a)):
                if j == len(b): 
                    return False
                achar, bchar = a[j], b[j]
                aix, bix = alpha[achar], alpha[bchar]
                if aix < bix:
                    break
                if aix > bix:
                    return False
        return True
                    
                   
                    
        
        