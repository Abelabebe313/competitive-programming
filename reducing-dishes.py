class Solution:
    def maxSatisfaction(self, dish: List[int]) -> int:
        res = 0
        prefix = 0

        new = sorted(dish,reverse = True)
        print(new)
        for i in range(len(new)):
            prefix += new[i]
            if prefix >= 0:
                res += prefix
        return res