class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        N = len(requests)
        achieved = 0
        transfer = [0] * n

        def bt(i,count):
            nonlocal achieved
            if i == N:
                if all(x == 0 for x in transfer):
                    achieved = max(achieved,count)
                return

            bt(i+1, count)

            f , t = requests[i]
            transfer[f] -= 1
            transfer[t] += 1

            bt(i+1, count + 1)
            transfer[t] -= 1
            transfer[f] += 1

        bt(0,0)
        return achieved