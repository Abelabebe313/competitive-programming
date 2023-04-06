from collections import defaultdict
n = int(input())
source = []
sink = []
vrtx = defaultdict(list)
value_list = []

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(len(row)):
        if row[j] == 1:
            vrtx[i+1].append(j+1)
        
    value_list.extend(vrtx[i+1])

for key,val in vrtx.items():
    if key and not val and key not in value_list:
        source.append(key)
        sink.append(key)
    elif key and val and key not in value_list:
        source.append(key)
    elif key and not val and key in value_list:
        sink.append(key)

print(len(source),*source)
print(len(sink),*sink)




