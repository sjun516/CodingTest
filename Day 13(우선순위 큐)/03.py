# [필수] 통행료

import heapq

N, M = map(int, input().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
	u, v, cost = map(int, input().split())
	edge[u].append((cost, v))
	edge[v].append((cost, u))
	
def dijkstra(start):
	heap = []
	visited = [0 for _ in range(N+1)]
	dist = [0 for _ in range(N+1)]
	
	for u in edge[start]:
		heapq.heappush(heap, (u[0], u[1]))
	visited[start] = 1
		
	while(visited[N] != 1):
		cost, v = heapq.heappop(heap)
		if(visited[v] == 1):
			continue
		visited[v] = 1
		dist[v] = cost
		
		for u in edge[v]:
			heapq.heappush(heap, (u[0] + dist[v], u[1]))
	
	print(dist[N])
	
dijkstra(1)
	
