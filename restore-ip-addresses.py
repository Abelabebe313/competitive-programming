class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if int(s) not in range(255255255256):
            return []
        
        def check_valid(num):
            length = len(num)
        
            if length not in range(1,4):
                return False
        
            if str(int(num)) != num:
                return False
            if int(num) in range(256):
                return True
        ans = []
        for firstDot in range(1,4):
            num1 = s[0:firstDot]
            if check_valid(num1):
                for secDot in range(firstDot+1,firstDot+4):
                    num2 = s[firstDot:secDot]
                    if check_valid(num2):
                        for thrdDot in range(secDot+1,secDot+4):
                            num3 = s[secDot:thrdDot]
                            num4 = s[thrdDot:]
                            if check_valid(num3) and check_valid(num4):
                                ans.append(".".join((num1,num2,num3,num4)))
        return ans