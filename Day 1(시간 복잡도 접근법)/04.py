# [필수] N번째 피보나치 수 구하기 1

def fibo(n):
	if n == 1: return 1
	elif n == 2: return 1
	else:
		a = 1
		b = 1
		for i in range (3, n+1):
			tmp = a + b
			a = b
			b = tmp
	return b

num = int(input())
print(fibo(num))