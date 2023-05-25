class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)
        for bill in bills:
            if bill == 5:
                count[bill] += 1
            elif bill == 10:
                if count[5] == 0:
                    return False
                count[bill] += 1
                count[5] -= 1
            else:
                if count[10] > 0 and count[5] > 0:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False
        return True