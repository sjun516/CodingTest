# [필수] 이분 그래프

V, E = map(int, input().split())
edge = [[] for _ in range(V+1)]
for _ in range(E):
	u, v = map(int, input().split())
	edge[u].append(v)
	edge[v].append(u)

def dfs(i, num):
	global result
	
	if(color[i] == num):
		return
	if(color[i] == 3-num):
		result = 0
		return
	color[i] = num

	for u in edge[i]:
		dfs(u, 3-num)
		
color = [0 for _ in range(V+1)]
result = 1
dfs(1, 1)
if(result == 0):
	print("NO")
else:
	print("YES")