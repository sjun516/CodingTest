# 분할정복으로 별 찍기

N = int(input())
arr = [[" " for _ in range(N)] for _ in range(N)]

def star(x, y, l):
	if(l == 1):
		arr[x][y] = "*"
		return
		
	for i in range(x, x+l, l//3):
		for j in range(y, y+l, l//3):
			if(i == x+l//3 and j == y+l//3):
				continue
			star(i, j, l//3)
	
star(0, 0, N)

for a in arr:
	for b in a:
		print(b, end = "")
	print()