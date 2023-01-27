class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        length = n + m - 1
        while nums2:
            if not m:
                nums1[m:length+1] = nums2[:length+1]
                break
            if nums1[m-1] < nums2[-1]:
                nums1[length] = nums2.pop()
            else:
                nums1[length] = nums1[m-1]
                m -= 1
            length -= 1
                
        