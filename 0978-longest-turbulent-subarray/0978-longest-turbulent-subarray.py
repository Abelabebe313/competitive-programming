class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        size = 1
        great = False
        equal = False
        for r in range(1,len(arr)):
            if arr[r] < arr[r-1]:
                if great or equal:
                    size += 1
                else:
                    ans = max(ans, size)
                    size = 2
                great = False
                equal = False
            elif arr[r] > arr[r-1]:
                if not great or equal:
                    size += 1
                else:
                    ans = max(ans, size)
                    size = 2
                great = True
                equal = False
            elif arr[r] == arr[r-1]:
                ans = max(ans, size)
                size = 1
                equal = True
        return max(ans, size)