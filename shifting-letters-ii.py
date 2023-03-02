class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        lineSweep = [0] * (len(s)+1)
        
        for start, end, direction in shifts: 
            if direction:
                lineSweep[start] += 1
                lineSweep[end+1] -= 1
            else:
                lineSweep[start] -= 1
                lineSweep[end+1] += 1
        print(lineSweep)        
        total = 0
        result = ''
        for i,char in enumerate(s):
            total += lineSweep[i]
            result += chr((((ord(char) + total) - 97) % 26) + 97) 
            
                
        return result