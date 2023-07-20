# [필수] 직접 만든 큐

queue = []
num = int(input())
for i in range(num):
	n = input()

	if("push" in n):
		push, num = n.split()
		queue.append(int(num))
	if("pop" == n):
		if(len(queue) == 0):
			print(-1)
		else:
			print(queue.pop(0))
	if("size" == n):
		print(len(queue))
	if("empty" == n):
		if(len(queue) == 0):
			print(1)
		else:
			print(0)
	if("front" == n):
		if(len(queue) == 0):
			print(-1)
		else:
			print(queue[0])
	if("back" == n):
		if(len(queue) == 0):
			print(-1)
		else:
			print(queue[-1])
	
