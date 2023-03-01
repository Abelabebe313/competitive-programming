class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        def recurstion(left,right):
            if left >= right:
                return
            s[left],s[right] = s[right], s[left]
            
            return recurstion(left+1,right-1)
        
        return recurstion(left,right)