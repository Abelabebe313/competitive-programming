class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)-1
        ans = 0
        while left <= right:
            mid = (left+right)//2
            
            if citations[mid] > len(citations[mid:]):
                right = mid - 1
            elif citations[mid] < len(citations[mid:]):
                left = mid + 1
            else:
                return citations[mid]
        return len(citations) - left