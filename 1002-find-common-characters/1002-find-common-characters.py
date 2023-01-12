class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        output = []
        ResultDict = [0] * 26
        offset = ord('a')
        for char in words[0]:
            asciii = ord(char)
            ResultDict[asciii - offset] += 1
             
        for i in range(1,len(words)):
            temp = [0] * 26
            for char in words[i]:
                asciii = ord(char)
                temp[asciii - offset] += 1
            
            for j in range(26):
                if ResultDict[j] == temp[j] and ResultDict[j] < temp[j]:
                    continue
                elif ResultDict[j]  > temp[j]:
                    ResultDict[j] = temp[j]
                 
        for i in range(len(ResultDict)):
            for j in range(ResultDict[i]):
                output.append(chr(ord('a')+i))
                    
        return output  