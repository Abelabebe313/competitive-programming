class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = []
        def kthLargest(lists,k):
            if not lists:
                return
            pivot = random.choice(lists)
            
            left = [num for num in lists if num > pivot]
            mid = [num for num in lists if num == pivot]
            right = [num for num in lists if num < pivot]
            
            L = len(left)
            M = len(mid)
            
            if k <= L:
                return kthLargest(left,k)
            elif k > L + M:
                return kthLargest(right, k - L - M)
            else:
                return mid[0]
        
        return kthLargest(nums,k) 
            