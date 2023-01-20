class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxx = max(arr)
        Found = False
       
        if len(arr) >= 3:
            for i in range(len(arr)-1):
                if arr[i]==arr[i+1]:
                    return False
                    break
                elif arr[i] == maxx and arr[-1] != maxx  and arr[0] != maxx:
                    Found = True
                    continue
                elif Found == True and arr[i] == maxx:
                    print(arr[i])
                    return False
                    break
                elif arr[-1] == maxx:
                    return False
                    break
                elif arr[i] > arr[i+1] and Found == False or arr[i] < arr[i+1] and Found == True:
                    return False
                    break
                elif arr[i] < arr[i+1] and Found == False:
                    continue
                elif arr[i-1] > arr[i] and Found == True:
                    continue
        else:
            return False
        return True
            