# 바닥 도배

a, b = map(int, input().split())

for i in range (3, a+b):
	j = (a+b)//i
	if(i*j == a+b and a == 2*(i+j)-4):
		if(j >= i):
			print(j, i)
			break
	