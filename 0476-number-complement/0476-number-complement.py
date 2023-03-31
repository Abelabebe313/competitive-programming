class Solution:
    def findComplement(self, num: int) -> int:
    
        for i in range(len(bin(num))-2):
            num = num ^ (1<<i)
        return num
        