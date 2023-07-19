# [필수] N-QUEEN

def dfs(x):
	global cnt
	
	if (x == num):
		cnt += 1
		return

	for i in range(num):
		if (arr[x][i] > 0):
			continue
			
		for j in range(num):
			if (x + j >= num):
				break
			if (i - j >= 0):
				arr[x+j][i-j] += 1
			arr[x+j][i] += 1
			if (i + j < num):
				arr[x+j][i+j] += 1
		dfs(x+1)
		
		for j in range(num):
			if (x + j >= num):
				break
			if (i - j >= 0):
				arr[x+j][i-j] -= 1
			arr[x+j][i] -= 1
			if (i + j < num):
				arr[x+j][i+j] -= 1
		
	

num = int(input())
arr = [[0 for j in range(num)] for i in range(num)]
cnt = 0
dfs(0)
print(cnt)

