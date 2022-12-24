class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for i in arr:
            if i == 0 and count[i]>1:
                return True
            elif i != 0 and count[i*2]:
                return True
        return False
                