# [필수] 키 순서

N, M = map(int, input().split())
tedge = [[] for _ in range(N + 1)]
sedge = [[] for _ in range(N + 1)]
for _ in range(M):
	u, v = map(int, input().split())
	tedge[u].append(v)
	sedge[v].append(u)

def dfs(edge, i):
	if(chk[i] == 1):
		return 0
	chk[i] = 1
	
	cnt = 1
	for u in edge[i]:
		cnt += dfs(edge, u)
	return cnt
	
chk = [0 for _ in range(N + 1)]
cnt = 0
for i in range(1, N+1):
	chk = [0 for _ in range(N + 1)]
	tcnt = dfs(tedge, i) - 1
	chk = [0 for _ in range(N + 1)]
	scnt = dfs(sedge, i) - 1
	
	if(tcnt + scnt == N - 1):
		cnt += 1

print(cnt)