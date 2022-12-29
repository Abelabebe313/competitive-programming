# Enter your code here. Read input from STDIN. Print output to STDOUT
def setDifference():
    English = []
    French = []
    ans = 0
    NumEng = int(input())
    English = list(map(lambda a: int(a), input().split(" ")))
    NumFrc = int(input())
    French = list(map(lambda a: int(a), input().split(" ")))
    
    for i in range(len(English)):
        if English[i] not in French:
            ans += 1
            
    print(ans)
        
setDifference()
        
