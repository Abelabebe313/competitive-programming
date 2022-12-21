class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack = []
        for i in str(x):
            stack.append(i)
        for i in str(x):
            j = stack.pop()
            if i != j:
                print(i,j)
                return False
        return True