class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        d = [0] * 101
        offset = 1950
        for birth, death in logs:
            birth = birth - offset
            death =  death - offset
            d[birth] += 1
            d[death] -= 1
        print(d)
        s = mx = j = 0
        for i, x in enumerate(d):
            s += x
            if mx < s:
                mx, j = s, i
        return j + offset
        