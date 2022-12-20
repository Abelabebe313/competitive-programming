k = int(input())
rooms = list(map(int, input().split(" ")))

dics = {}

for key in rooms:
    if key in dics:
        dics[key] += 1
    else:
        dics[key] = 1

for key in dics:
    if dics[key] == 1:
        print(key)
        break
