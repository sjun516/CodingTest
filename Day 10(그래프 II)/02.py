# 우유 공장

N = int(input())
edge = [[] for _ in range(N+1)]
for _ in range(N-1):
	u, v = map(int, input().split())
	edge[v].append(u)

def dfs(num):
	if(chk[num] == 1):
		return
	chk[num] = 1
	for u in edge[num]:
		dfs(u)

result = 0
for i in range(1, N+1):
	cnt = 0
	chk = [0 for _ in range(N+1)]
	dfs(i)
	for j in range(1, N+1):
		if(chk[j] == 0):
			cnt = 1
			break
	if(cnt == 0):
		result = 1
		print(i)
		break
if(result == 0):
	print(-1)
