# 하노이의 탑

K = int(input())

def hanoi(K, start, mid, end):
	cnt = 0
	
	if(K == 1):
		arr.append((start, end))
		return 1
	else:
		# n - 1개 미드로 이동
		cnt += hanoi(K-1, start, end, mid)
		arr.append((start, end))
		cnt += 1
		cnt += hanoi(K-1, mid, start, end)
		
		return cnt
	
arr = []	
cnt = 0	
print(hanoi(K, 1, 2, 3))
for a, b in arr:
	print(a, b)