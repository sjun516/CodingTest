# 등수 찾기

N, M, X = map(int, input().split())
tedge = [[] for _ in range(N+1)]
sedge = [[] for _ in range(N+1)]
for _ in range(M):
	u, v = map(int, input().split())
	tedge[v].append(u)
	sedge[u].append(v)

def dfs(edge, i):
	if(chk[i] == 1):
		return 0
	chk[i] = 1
	cnt = 1
	for u in edge[i]:
		cnt += dfs(edge, u)
	return cnt
	
chk = [0 for _ in range(N+1)]
ucnt = dfs(tedge, X) - 1
chk = [0 for _ in range(N+1)]
vcnt = dfs(sedge, X) - 1
print(ucnt+1, N - vcnt)