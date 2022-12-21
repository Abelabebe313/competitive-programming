class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x:len(x))
        first = strs[0]
        ans = ''
        if len(strs)==1:
            return first
        for i in range(len(first)):
            temp = 0
            for j in range(1,len(strs)):
                if strs[j][i] == first[i]:
                    temp += 1
                    
                if temp == len(strs)-1:
                    ans += first[i]
            if temp != len(strs)-1:
                return ans
        return ans
                    
        
        