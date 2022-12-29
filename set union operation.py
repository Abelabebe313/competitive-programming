# Enter your code here. Read input from STDIN. Print output to STDOUT
def setUnion():
    English = []
    French = []
    
    n = int(input())
    English = list(map(lambda a: int(a),input().split(" ")))
    m = int(input())
    French = list(map(lambda a: int(a), input().split(" ")))
    
    for i in range(len(French)):
        if French[i] not in English:
            English.append(French[i])
    print(len(English))
    
setUnion()
    
