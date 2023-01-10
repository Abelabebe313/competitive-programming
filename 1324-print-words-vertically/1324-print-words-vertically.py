class Solution:
    def printVertically(self, s: str) -> List[str]:
        llist = s.split()
        vertical = []
        max_str = max(llist, key=len)
                
        for i in range(len(max_str)):
            temp = ''
            for j in range(len(llist)):
                if len(llist[j]) > i:
                    temp += llist[j][i] 
                else:
                    temp += ' '
                
            k = len(temp)-1
            while temp[k] == " ":
                temp = temp[:-1]
                k -= 1
                    
            vertical.append(temp)
        return vertical