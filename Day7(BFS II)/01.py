# 미로탐험

from collections import deque

N, M = map(int, input().split())
arr = []
dist = [[0 for _ in range(M)] for _ in range(N)]
queue = deque([0, 0, 1])

for _ in range(N):
	row = list(map(int, input()))
	arr.append(row)

def bfs(N, M):
	dx = [1, -1, 0 ,0]
	dy = [0, 0, 1, -1]
	
	while(queue):
		x = queue.popleft()
		y = queue.popleft()
		d = queue.popleft()
		
		if(x < 0 or x >= N or y < 0 or y >= M or arr[x][y] == 0 or dist[x][y] > 0):
			continue
			
		dist[x][y] = d
		
		for i in range(4):
			queue.append(x + dx[i])
			queue.append(y + dy[i])
			queue.append(d + 1)
		
	if(dist[N-1][M-1] == 0):
		print(-1)
	else:
		print(dist[N-1][M-1])

bfs(N,M)