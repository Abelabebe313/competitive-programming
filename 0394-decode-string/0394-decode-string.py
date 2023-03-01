class Solution:
    def decodeString(self, s: str) -> str:
        # output = []
        # def decoder(k,string):
        #     if k == 1:
        #         return 
        #     k -= 1
        #     output.append(string)
        #     return decoder(k,string)
        
        stack = []
        if s.isdigit():
            return "" 
        else:
            for i in range(len(s)):
                if s[i] == ']':
                    temp = ''
                    while stack[-1].isalpha():
                        temp = stack.pop() + temp
                    stack.pop()
                    k = ''
                    while stack and stack[-1].isdigit():
                        k = stack[-1] + k
                        stack.pop()
                    temp = int(k) * temp
                    stack.append(temp)

                else:             
                    stack.append(s[i])

            return ''.join(stack)