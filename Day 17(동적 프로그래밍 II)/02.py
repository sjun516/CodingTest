# [필수] 욕심많은 윌리

# 입력 단계
N, W = map(int, input().split())
w = []
v = []
for _ in range(N):
	a, b = map(int, input().split())
	w.append(a)
	v.append(b)

# dp[n][k] : n번째 물건을 무게k까지 가치 최댓값
# max (dp[n-1][k] , dp[n-1][k-w[n]] + v[n])
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
for i in range(1, N+1):
	for j in range(1, W+1):
		dp[i][j] = dp[i-1][j]
		if(j-w[i-1] >= 0):
			dp[i][j] = max(dp[i][j], dp[i-1][j-w[i-1]] + v[i-1])	
print(dp[N][W])			