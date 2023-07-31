# [필수] 포탈

from collections import deque

def bfs(X, Y):
	queue = deque([X, 0])
	visited = set()
	visited.add(X)
	
	while(queue):
		x = queue.popleft()
		d = queue.popleft()
		
		if(x == Y):
			return d
		
		if(0 <= x+1 <= 200000 and x+1 not in visited):
			queue.append(x+1)
			queue.append(d+1)
			visited.add(x+1)
		if(0 <= x-1 <= 200000 and x-1 not in visited):
			queue.append(x-1)
			queue.append(d+1)
			visited.add(x-1)
		if(0 <= 2*x <= 200000 and 2*x not in visited):
			queue.append(2*x)
			queue.append(d+1)
			visited.add(2*x)
		
X, Y = map(int, input().split())	
print(bfs(X, Y))