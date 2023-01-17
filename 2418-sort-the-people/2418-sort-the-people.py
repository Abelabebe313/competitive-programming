class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # insertion
        for i in range(1,len(heights)):
            unsorted = heights[i]
            while heights[i-1] < heights[i] and i > 0:
                heights[i],heights[i-1] = heights[i-1],heights[i]
                names[i],names[i-1] = names[i-1],names[i]
                i -= 1
                
        return names
    
        # selection
#         for i in range(len(heights)):
#             minn = i
#             for j in range(i+1,len(heights)):
#                 if heights[minn] < heights[j]:
#                     minn = j
                    
#             heights[i],heights[minn] = heights[minn],heights[i]
#             names[i],names[minn] = names[minn],names[i]
#         return names
                
                
                # bubble
        # swap = 0
        # sort = False
        # nameDict = {}
        # while not sort:
        #     sort = True
        #     for i in range(len(heights)-1):
        #         if heights[i] < heights[i+1]:
        #             sort = False
        #             heights[i],heights[i+1] = heights[i+1],heights[i]
        #             names[i],names[i+1] = names[i+1],names[i]
        #             swap +=1
        # return names