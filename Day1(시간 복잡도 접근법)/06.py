# N번째 피보나치 수 구하기 2

def fibo(n):
	if n == 1: return 1
	elif n == 2: return 1
	else:
		a = 1
		b = 1
		for i in range (3, n+1):
			tmp = a + b
			a = b % 1000000007
			b = tmp % 1000000007
	return b

num = int(input())
print(fibo(num))