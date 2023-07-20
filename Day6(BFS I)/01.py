# [필수] 스택

stack = []

while(True):
	n = input()

	if("push" in n):
		push, num = n.split()
		print(num)
		stack.append(int(num))
		# print(stack)
	if("pop" == n):
		if(len(stack) == 0):
			print(-1)
		else:
			print(stack.pop())
	if("size" == n):
		print(len(stack))
	if("empty" == n):
		if(len(stack) == 0):
			print(1)
		else:
			print(0)
	if("top" == n):
		if(len(stack) == 0):
			print(-1)
		else:
			print(stack[-1])
	if("end" == n):
		break
	
