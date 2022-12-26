class Solution:
    def interpret(self, command: str) -> str:
        result = []
        for i in range(len(command)):
            if command[i] == 'G':
                result.append('G')
            elif command[i] == '(':
                result.append(command[i])
            elif command[i] == 'a':
                result.append(command[i])
            elif command[i] == 'l':
                result.append(command[i])
                    
            elif command[i] == ')':
                if result[-1] == '(':
                    result.pop(-1)
                    result.append('o')
                else:
                    for i in range(3):
                        result.pop(-1)
                    result.append('al')
            
        return ''.join(result)
                
                