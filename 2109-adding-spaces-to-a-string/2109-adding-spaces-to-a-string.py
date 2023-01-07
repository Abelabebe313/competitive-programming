class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space = set(spaces)
        answer = ''
        for i in range(len(s)):
            if i in space:
                answer += ' ' + s[i]
            else:
                answer += s[i]    
        
        return answer