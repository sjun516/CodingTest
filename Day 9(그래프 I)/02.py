# [필수] 바이러스_KOI지역2004_초등부_3

# 첫째 줄 정점 수
# 둘째 줄 간선 수
from collections import deque

nvertex = int(input())
nedge = int(input())
edge = [[] for _ in range(nvertex + 1)]
for _ in range(nedge):
	u, v = map(int, input().split())
	edge[u].append(v)
	edge[v].append(u)

# dfs
chk = [0 for _ in range(nvertex+1)]
cnt = 0
def dfs(v):
	global cnt
	if(chk[v] == 1):
		return
	chk[v] = 1
	if(v != 1):
		cnt += 1
	
	for u in edge[v]:
		dfs(u)
dfs(1)
print(cnt)

# bfs
chk = [0 for _ in range(nvertex+1)]
queue = deque([1])
cnt = 0

while(queue):
	v = queue.popleft()
	if(chk[v] == 1):
		continue
	chk[v] = 1
	if(v != 1):
		cnt += 1
	
	for u in edge[v]:
		queue.append(u)

print(cnt)
