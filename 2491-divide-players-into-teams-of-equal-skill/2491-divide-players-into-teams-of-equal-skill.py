class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans = 0
        teams = []
        left = 0
        right = len(skill)-1
        target = skill[left] + skill[right]
        while left < right:
            if target != (skill[left]+skill[right]):
                return -1
            else:
                ans += (skill[left]*skill[right])   
            left += 1
            right -= 1
       
        return ans
            