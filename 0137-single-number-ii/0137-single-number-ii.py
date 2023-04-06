class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbers = defaultdict(int)
        ans = 0
        negative = 0
        
        for num in nums:
            i = 0
            while num:
                if num<0:
                    negative+=1
                    num = -num
                if num % 2:
                    numbers[i] += 1
                num >>= 1
                i+=1
        for key,val in numbers.items():
            ans |= (val % 3)<<key
            
        if negative % 3 == 0:
            return ans
        
        return -ans
        
                
        
        