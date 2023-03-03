class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        lastIdx = defaultdict()

        for idx in range(len(s)):
            lastIdx[s[idx]] = idx 
        print(lastIdx)
        for idx in range(len(s)):
            if not stack or s[idx] >= stack[-1] and s[idx] not in stack:
                stack.append(s[idx])
            else:
                while stack and stack[-1] > s[idx]:
                    if lastIdx[stack[-1]] > idx and s[idx] not in stack:
                        stack.pop() 
                    else:
                        break
                if s[idx] not in stack:
                    stack.append(s[idx])
        return ''.join(stack)