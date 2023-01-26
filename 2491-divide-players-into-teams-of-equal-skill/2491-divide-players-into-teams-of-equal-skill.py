class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans = 0
        teams = []
        left = 0
        right = len(skill)-1
        while left < right:
            teams.append((skill[left],skill[right]))
            left += 1
            right -= 1
        target = teams[0][0] + teams[0][1]
        for i in range(len(teams)):
            if sum(teams[i]) != target:
                return -1
            else:
                ans += (teams[i][0]*teams[i][1])
            
        return ans
            