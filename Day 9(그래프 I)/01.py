# [필수] DFS와 BFS

from collections import deque
arr = list(map(int, input().split()))

# 간선 초기화
edge = [[] for _ in range(arr[0]+1)]
for i in range(arr[1]):
	u, v = map(int, input().split())
	edge[u].append(v)
	edge[v].append(u)
# 인접리스트 정렬
for i in range(arr[0]+1):
	edge[i].sort()
	
# dfs
chk = [0 for _ in range(arr[0]+1)]
def dfs(v):
	if(chk[v] == 1):
		return
	chk[v] = 1
	print(v, end=" ")
	
	for u in edge[v]:
		dfs(u)
dfs(arr[2])
print()

# bfs
chk = [0 for _ in range(arr[0]+1)]
queue = deque([arr[2]])

while(queue):
	v = queue.popleft()
	if(chk[v] == 1):
		continue
	chk[v] = 1
	print(v, end=" ")
	
	for u in edge[v]:
		queue.append(u)
print()	
	



	

