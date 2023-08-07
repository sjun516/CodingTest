# 마라톤

N = int(input())
dic = {}
for _ in range(N):
	num = input()
	if(num in dic):
		dic[num] += 1
	else:
		dic[num] = 1
    
for _ in range(N-1):
	num = input()
	if(num in dic):
		if(dic[num] == 1):
			del dic[num]
		else:
			dic[num] -= 1

for num in dic:
	print(num)