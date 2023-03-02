class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        ans = []
        path = path.split('/')
        for i in path:
            if i == '':
                continue
            stack.append(i)
        
        for pathh in stack:
            if pathh == '..' and len(ans)>0:
                ans.pop()
                continue
            elif pathh == '.' or pathh == '..':
                continue
            ans.append('/' + pathh)
        
        if len(ans) > 0:
            return ''.join(ans)
        return '/'
    
    
#         for i in range(len(path)):
#             temp = ""
#             stack.append(path[i])
#             if path[i] == '/':
#                 flag = not flag
#             # if path[i] == '.':
#             #     dot += 1
                
#             if not flag:
#                 letters = Counter(stack)
#                 if letters['.'] == 2:
#                     stack.pop()
#                     while stack:
#                         stack.pop()
#                     ans = "/"
#                     ans += '/'
#                 elif letters['.'] != 2:
#                     stack.pop()
#                     while not flag and stack:
#                         temp = stack.pop() + temp
#                     ans = ans + temp 
#         return ans