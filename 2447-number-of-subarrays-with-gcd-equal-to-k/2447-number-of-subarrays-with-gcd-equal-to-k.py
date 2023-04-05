class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def find_gcd(a,b):
            if b==0:
                return a
            return find_gcd(b,a%b)
        
        count_gcd = 0
        curr_gcd = 0
        for i in range(len(nums)):
            curr_gcd = nums[i]
            if curr_gcd == k:
                count_gcd+=1
            for j in range(i+1,len(nums)):
                curr_gcd = find_gcd(curr_gcd,nums[j])
                if curr_gcd == k:
                    count_gcd += 1
                
        return count_gcd