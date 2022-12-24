class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        ptr = 0
        while ptr <= len(nums)-1:
            if nums[ptr] == val:
                nums.pop(ptr)
                continue
            ptr += 1
                
        return len(nums)