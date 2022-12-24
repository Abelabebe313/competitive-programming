class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)
        while i < len(arr):
            if arr[i] == 0:
                arr[i+1:] = [0] + arr[i+1:-1]
                i += 2
            else:
                i += 1
        arr[:]=arr[:n]
        