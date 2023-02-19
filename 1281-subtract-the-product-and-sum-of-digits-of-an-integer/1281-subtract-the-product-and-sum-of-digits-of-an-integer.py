class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = list(map(int, str(n)))
        add = 0
        prod = 1
        for num in res:
            prod *= num
            add += num
        return prod - add