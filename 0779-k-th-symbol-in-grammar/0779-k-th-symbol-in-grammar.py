class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def recurtion(n,k):
            if n == 1:
                return 0
            mid = (2 **(n-1))//2
            if k <= mid:
                return recurtion(n-1,k)
            else:
                temp = recurtion(n-1,k-mid)
                if temp == 1:
                    return 0
                else:
                    return 1
        return recurtion(n,k)
        