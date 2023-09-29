# [필수] 싸이클_KOI지역2012_초등부_2

N, P = map(int, input().split())

def dfs(x, n):
	if(check[x] != 0):
		print(n - check[x])
	else:
		check[x] = n
		dfs(x*N%P, n+1)
	

check = [0 for _ in range(N+1)]
dfs(N, 0)