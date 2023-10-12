class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        moves = {
            0:[4,6],
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[0,3,9],
            5:[],
            6:[0,1,7],
            7:[2,6],
            8:[1,3],
            9:[2,4]
        }
        first = [2, 2, 2, 2, 3, 0, 3, 2, 2, 2]
        dp = [[0 for _ in range(10)] for i in range(n-1)]
        for i in range(n-1):
            for j in range(10):
                if i == 0:
                    dp[i][j] = first[j]
                else: 
                    for k in moves[j]:
                        dp[i][j] += dp[i-1][k]
        
        ans = sum(dp[-1])
        return ans % (10**9 + 7)