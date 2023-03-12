class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = defaultdict(int)
        prefix = [] 
        ans = 0
        
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            prefix.append(temp)

        for num in prefix:
            if num == goal:
                ans += 1
            if (num - goal) in seen:
                ans += seen[num - goal]

            seen[num] += 1
        

        return ans