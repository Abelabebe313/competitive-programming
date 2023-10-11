class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        hash = 0
        curr = 0

        if len(haystack) < n:
            return -1
        for i in range(n):
            hash += (ord(needle[i]) - 97) * pow(26,n-i-1)
            curr += ((ord(haystack[i]) - 97) * pow(26,n-i-1))
        left = 0
        right = n

        while right < len(haystack):
            if hash == curr:
                return left
            curr -= ((ord(haystack[left]) - 97) * pow(26,n-1))
            curr = curr * 26
            curr += ((ord(haystack[right]) - 97))

            left += 1
            right += 1
        if hash == curr:
            return left
        return -1