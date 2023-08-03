# 최소 힙

def heap_add(num):
	global size, arr
	
	size += 1
	arr[size] = num
	idx = size
	
	while(idx > 1):
		if(arr[idx] < arr[idx//2]):
			arr[idx], arr[idx//2] = arr[idx//2], arr[idx]
		else:
			break
		idx //= 2 
	
def heap_remove():
	global size, arr
	
	if(size == 0):
		return 0
	top = arr[1]
	arr[1] = arr[size]
	size -= 1
	
	idx = 1
	while(idx*2 <= size):
		l, r = idx*2, idx*2+1
		
		if((r > size or arr[l] < arr[r]) and arr[l] < arr[idx]):
			arr[idx], arr[l] = arr[l], arr[idx]
			idx = l
		elif(r <= size and arr[r] < arr[idx]):
			arr[idx], arr[r] = arr[r], arr[idx]
			idx = r
		else:
			break
	return top

arr = [0 for _ in range(100000)]
size = 0
N = int(input())
for _ in range(N):
	num = int(input())
	if(num == 0):
		print(heap_remove())
	else:
		heap_add(num)