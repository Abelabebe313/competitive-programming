# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
tupl = tuple(map(lambda a: int(a),input().split(" ")))

print(hash(tupl))
