# [필수] 길 찾기

N = int(input())
arr = [[] for _ in range(N)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
	arr[i] = list(input())

if(arr[0][0] != "*"):
	dp[1][1] = 1	
for i in range(N):
	for j in range(N):
		if(arr[i][j] == "*" or (i == 0 and j == 0)):
			continue
		dp[i+1][j+1] = (dp[i+1][j] + dp[i][j+1]) % int(1e9 + 7)

print(dp[N][N])