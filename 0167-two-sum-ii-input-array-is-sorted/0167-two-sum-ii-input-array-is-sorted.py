class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1
        ans = []
        
        while left != right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] == target:
                ans.append(left+1)
                ans.append(right+1)
                break
        return ans
                
            