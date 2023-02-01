t = int(input())
 
 
for _ in range(t):
    
	n = int(input())
	nums = list(map(int,input().split()))
 
	res = 0
	maxNum = float('-inf')
	flag = "p"
	if nums[0] > 0:
		flag = "p"
		#maxNum = 0
	else:
		flag = "n"
		#maxNum = float('-inf')
	
	for i in range(n):
		if nums[i] > 0:
			if flag == "p":
				maxNum =  max(maxNum,nums[i])
			else:
				res += maxNum
				maxNum = float('-inf')
				maxNum = max(maxNum,nums[i])
				flag = 'p'
		else:
			if flag == "n":
				maxNum =  max(maxNum,nums[i])
			else:
				res += maxNum
				maxNum = float('-inf')
				maxNum = max(maxNum,nums[i])
				flag = "n"
		#print("found max",maxNum,res,flag)
	
	res += maxNum
	print(res)
