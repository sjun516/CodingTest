# N번째 피보나치 수 구하기 3

def fibo(n):
	if n == 1: return 1
	elif n == 2: return 2
	elif n == 3: return 4
	else:
		a = 1
		b = 2
		c = 4
		for i in range (4, n+1):
			tmp = c + 2*b - a
			a = b % 1000000007
			b = c % 1000000007
			c = tmp % 1000000007
	return c 

num = int(input())
print(fibo(num))