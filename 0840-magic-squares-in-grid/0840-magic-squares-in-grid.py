class Solution:    
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def magic(a,b,c,d,e,f,g,h,i):
            s1 = set([a,b,c,d,e,f,g,h,i])
            s2 = set([1,2,3,4,5,6,7,8,9])
            if(s1 == s2 and (a+b+c)==15 and (d+e+f)==15 and (g+h+i)==15 and 
               (a+d+g)==15 and (b+e+h)==15 and (c+f+i)==15 and 
               (a+e+i)==15 and (c+e+g)==15):
                return True
            else:
                return False
        output = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if magic(grid[i][j],grid[i][j+1],grid[i][j+2],
                        grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],
                        grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]) == True:
                    output +=1
        return output
                   
                   
           
                    
                
              
                        