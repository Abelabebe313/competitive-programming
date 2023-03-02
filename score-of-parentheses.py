class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count = 0
        for i in s:
            if i == '(':
               stack.append(count)
               count = 0
            else:
                if count:
                    count += stack.pop() + count
                else:
                    count += stack.pop() + 1
        return count