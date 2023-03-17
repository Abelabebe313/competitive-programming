class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True)
        mini = float('inf')
        path = [0] * k
        def bk(idx):
            nonlocal mini
            if idx >= len(cookies):
                mini = min(mini,max(path))
                return
            if mini < max(path):
                return
            for i in range(k):
                path[i] += cookies[idx]
                bk(idx+1)
                path[i] -= cookies[idx]
        
        bk(0)
        return mini