class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        newlist = []
        for i in range(len(intervals)):
            newlist.append([intervals[i][0],intervals[i][1],i])
        newlist.sort()
        ans = []
        
        def checker(target):
            left = -1
            right = len(newlist)
            result = 10**6
            
            while left + 1 < right:
                mid = left + (right - left)//2
                
                if newlist[mid][0] >= target:
                    right = mid
                    result = min(result,newlist[mid][2])
                    # return result
                else:
                    left = mid
            if result == 10**6:
                return -1
            return result
            
        
        for i in range(len(intervals)):
            ans.append(checker(intervals[i][1]))
            
        return ans