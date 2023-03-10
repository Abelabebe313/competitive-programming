class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def btc(num,path):
            if len(path)==k:
                ans.append(path)
                return
            for i in range(num+1,n+1):
                btc(i,path+[i])
        # def backtrack(cur_num,path):
        #     if cur_num > n + 1:
        #         return
        #     if len(path)==k:
        #         ans.append(path[::])
        #         return
            
        #     path.append(cur_num)
        #     backtrack(cur_num + 1, path)
        #     path.pop()
        #     backtrack(cur_num + 1, path)
        # backtrack(1, [])
        btc(0,[])
        return ans