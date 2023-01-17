class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        swap = 0
        sort = False
        nameDict = {}
        while not sort:
            sort = True
            for i in range(len(heights)-1):
                if heights[i] < heights[i+1]:
                    sort = False
                    heights[i],heights[i+1] = heights[i+1],heights[i]
                    names[i],names[i+1] = names[i+1],names[i]
                    swap +=1
        return names