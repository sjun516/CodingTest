# [필수] 연구활동 가는 길(S)

# 첫 줄 정점갯수
# 둘째 줄 간선의갯수

nvertex, nedge = map(int, input().split())
edge = [[] for _ in range(nvertex + 1)]
for _ in range(nedge):
    u, v, cost = map(int, input().split())
    edge[u].append((v, cost))
    edge[v].append((u, cost))

start = 1
end = nvertex
result = 0
cost = 0
chk = [0 for _ in range(nvertex + 1)]

def dfs(v):
	global result, cost
	
	if v == end:
		if result == 0 or result > cost:
			result = cost
		return

	for u in edge[v]:
		if chk[u[0]] == 0:
			chk[u[0]] = 1
			cost += u[1]
			dfs(u[0])
			
			chk[u[0]] = 0
			cost -= u[1]

chk[start] = 1
dfs(start)

if(result == 0):
	print(-1)
else:
	print(result)