# 수 정렬하기

def merge_sort(arr, l, r):
	if(r - l == 1):
		return
	m = (l+r) // 2
	merge_sort(arr, l, m)
	merge_sort(arr, m, r)
	
	lp = l
	rp = m
	tmp = []
	for i in range(l, r):
		if(rp == r or (lp < m and arr[lp] < arr[rp])):
			tmp.append(arr[lp])
			lp += 1
		else:
			tmp.append(arr[rp])
			rp += 1
			
	for i in range(0, r-l):
		arr[i+l] = tmp[i]
		

N = int(input())
arr = []
for i in range(N):
	arr.append(int(input()))
merge_sort(arr, 0, len(arr))
for i in range(N):
	print(arr[i])
