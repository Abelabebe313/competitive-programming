class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        t = list(zip(ages,scores))

        t.sort(reverse=True)

        ans = 0

        dp = [0]*(len(t) + 1)

        result = 0

        ans = 0
        for i in range(len(t)):

            dp[i] = t[i][1]

            for j in range(i):

                if t[j][1] >= t[i][1]:

                    dp[i] = max(dp[i], dp[j] + t[i][1])
            
            result = max(result, dp[i])

        
        return result